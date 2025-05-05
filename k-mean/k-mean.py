import matplotlib.pyplot as plt
from typing import Tuple, Self, List, Any, Iterable
import random
import math
import numpy as np
from matplotlib.widgets import Slider
from itertools import permutations


class Cluster:
    center: Tuple[float, float]
    x: List[float]
    y: List[float]

    def __init__(self):
        self.r: float = random.random() * random.randint(1,10)
        self.x = []
        self.y = []

    def distance(self, other: Self):
        return math.sqrt((self.center[0] - other.center[0])**2 + (self.center[1] - other.center[1])**2)

    def generate_dots(self, n):
        for i in range(n):
            self.x.append((random.random() * 2 - 1) * self.r + self.center[0])
            self.y.append(
                (random.random() * 2 - 1) *
                math.sqrt((self.r**2) - (self.x[i] - self.center[0])**2)
                + self.center[1]
            )


def generate_clusters(k: int, n: int) -> Tuple[Cluster]:
    clusters = []
    for i in range(k):
        clusters.append(Cluster())
        clusters[i].center = (
        random.random() * random.randint(-10 * k, 10 * k), random.random() * random.randint(-10 * k, 10 * k))
        if i>0:
            while any(clusters[i].distance(cluster) < (clusters[i].r + cluster.r) for cluster in clusters[:i]):
                clusters[i].center = (random.random() * random.randint(-10 * k, 10 * k), random.random() * random.randint(-10 * k, 10 * k))
        clusters[i].generate_dots(n)
    return tuple(clusters)


def list_sum(M: Iterable[List[Any]]) -> List[Any]:
    M = list(M); list(M[0].extend(x) for x in M[1:])
    return M[0]


class App:
    def __init__(self):
        self.k = 3
        self.n_cluster = 20
        self.n = -1  # Переменная для ползунка
        self.centroids = []
        self.history = []
        self.fig, self.ax = plt.subplots()
        self.fig.subplots_adjust(bottom=0.25)

        clusters = generate_clusters(self.k, self.n_cluster)
        for cluster in clusters:
            plt.plot(cluster.x, cluster.y, marker="o", color="b", ls="")
            x = np.linspace(cluster.center[0] - cluster.r, cluster.center[0] + cluster.r, 100)
            func1 = np.sqrt(cluster.r ** 2 - (x - cluster.center[0]) ** 2) + cluster.center[1]
            func2 = -np.sqrt(cluster.r ** 2 - (x - cluster.center[0]) ** 2) + cluster.center[1]
            plt.plot(x, func1, color="b")
            plt.plot(x, func2, color="b")

        print(f"Вариант {16 % 3 - 1}")

        self.x, self.y = list_sum(cluster.x for cluster in clusters), list_sum(cluster.y for cluster in clusters)
        self.true_labels = [i for i in range(len(clusters)) for _ in range(self.n_cluster)]
        self.k_mean(self.x, self.y, self.k)

        axfreq = self.fig.add_axes([0.25, 0.1, 0.65, 0.03])
        slider = Slider(
            ax=axfreq,
            label='Поколение',
            valmin=1,
            valmax=len(self.centroids),
            valinit=len(self.history),
        )
        slider.on_changed(self.update)
        self.cluster_points = []
        self.centroid_markers = []
        self.update(len(self.history))
        plt.show()

    def accuracy(self, labels):
        unique_pred = list(set(labels))
        unique_true = list(set(self.true_labels))

        n_clusters = len(unique_pred)

        pred_to_idx = {v: i for i, v in enumerate(unique_pred)}
        true_to_idx = {v: i for i, v in enumerate(unique_true)}

        norm_pred = [pred_to_idx[p] for p in labels]
        norm_true = [true_to_idx[t] for t in self.true_labels]

        best_accuracy = 0
        for perm in permutations(range(n_clusters)):
            perm_pred = [perm[p] for p in norm_pred]
            correct = sum(1 for p, t in zip(perm_pred, norm_true) if p == t)
            current_accuracy = correct / len(labels)

            if current_accuracy > best_accuracy:
                best_accuracy = current_accuracy
                if best_accuracy == 1:
                    break

        return best_accuracy

    def update(self, val):
        centroids, labels = self.history[max(0, round(val-1))]
        colors = ["r", "g", "y"]
        if hasattr(self, 'cluster_points'):
            for artist in self.cluster_points:
                artist.remove()
        if hasattr(self, 'centroid_markers'):
            for artist in self.centroid_markers:
                artist.remove()

        self.cluster_points = []
        self.centroid_markers = []

        for i in range(len(labels)):
            p, = self.ax.plot(self.x[i], self.y[i], marker="o", color=colors[labels[i]], ls="")
            self.cluster_points.append(p)

        for i, (cx, cy) in enumerate(centroids):
            if i < len(colors):
                c, = self.ax.plot(cx, cy, marker="X", color=colors[i], markersize=10, ls="")
                self.centroid_markers.append(c)
        self.fig.canvas.draw_idle()
        print(f"Accuracy: {self.accuracy(labels)}")

    def k_mean(self, x: List[float], y: List[float], k: int):
        points = list(zip(x, y))
        centroids = random.sample(points, k)
        d_x, d_y = float("inf"), float("inf")

        while d_x + d_y:
            clusters = [[] for _ in range(k)]
            self.history.append([centroids, []])
            for point in points:
                distances = [math.sqrt((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2) for c in centroids]
                closest = distances.index(min(distances))
                clusters[closest].append(point)
                self.history[-1][1].append(closest)
            new_centroids = []
            for cluster in clusters:
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append((avg_x, avg_y))

            self.centroids.append(new_centroids)
            if all(cn == c for cn, c in zip(new_centroids, centroids)):
                d_x, d_y = 0, 0
            centroids = new_centroids

        cluster_labels = []
        for point in points:
            distances = [math.sqrt((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2) for c in centroids]
            closest = distances.index(min(distances))
            cluster_labels.append(closest)


if __name__ == "__main__":
    App()
