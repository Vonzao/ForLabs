import random, math
import matplotlib.pyplot as plt
from typing import List, Tuple, Self, Literal, Union


class Dot:
    def __init__(self, pos: Tuple[float, float]):
        self.pos = pos

    def __getitem__(self, item: Literal[0, 1]):
        return self.pos[item]

    def distance(self, dot: Self):
        return math.sqrt((self.pos[0] - dot.pos[0]) ** 2 + (self.pos[1] - dot.pos[1]) ** 2)

    def __repr__(self):
        return f"Dot{self.pos}"


class Cluster:
    def __init__(self, dots: List[Dot] = None):
        self.dots: List[Dot] = dots if dots else []

    def all_pos(self, axis: Literal[0, 1]):
        return [dot[axis] for dot in self.dots]

    def __repr__(self):
        return f"Cluster{self.dots}"

    def __iter__(self):
        return iter(self.dots)

    def __getitem__(self, key: Union[slice, int]) -> Union[Self, Dot]:
        if isinstance(key, slice):
            return Cluster(self.dots[key])
        else:
            return self.dots[key]

    @property
    def x(self) -> List[float]:
        return [dot[0] for dot in self]

    @property
    def y(self) -> List[float]:
        return [dot[1] for dot in self]

    @property
    def pos(self):
        return [dot.pos for dot in self]

    def append(self, dot: Dot):
        self.dots.append(dot)

    def __len__(self):
        return len(self.dots)

    def __add__(self, other: Self):
        return Cluster(self.dots + other.dots)

    def __contains__(self, item: Dot):
        return item.pos in self.pos


def generate_dots(n: int, area: Tuple[int, int, int, int]) -> List[Dot]:
    return [
        Dot((
            random.uniform(*area[:2]),
            random.uniform(*area[2:])
        ))
        for _ in range(n)
     ]


def fit(dot_to_predict: Cluster, *clusters) -> Tuple[Cluster]:
    """
    Реализация метода k ближайших соседей
    """
    result: Tuple[Cluster] = tuple(Cluster() for _ in range(len(clusters)))
    k = len(clusters) + 1
    for dot in dot_to_predict:
        distances = [
            [dot.distance(cluster_dot), ind] for ind, cluster in enumerate(clusters)
            for cluster_dot in cluster
        ]
        distances.sort(key=lambda el: el[0])
        distances = [el[1] for el in distances[:k]]
        distances = [[el, distances.count(el)] for el in set(distances)]
        prediction = max(distances, key=lambda el: el[1])[0]
        result[prediction].append(dot)
    return result


def computeAccuracy(predicted_clusters: Tuple[Cluster], cluster_test: Cluster):
    n = len(predicted_clusters)  # На сколько кластеров разбиты точки
    count = len(cluster_test)  # Сколько всего точек
    # Нужно разбить на изначальные кластеры cluster_test
    # y_test
    clusters_test = [cluster_test[count // n * i: count // n * (i+1)] for i in range(n)]
    KC = 0
    for ind, cluster in enumerate(predicted_clusters):
        for dot in cluster:
            if dot in clusters_test[ind]:
                KC += 1
    return KC / count


if __name__ == "__main__":
    #########
    # Пункт 1
    x1 = 1, 12
    y1 = 2, 7
    x2 = 8, 20
    y2 = 4, 10

    p = 0.5
    amount = 125  # Общее кол-во точек
    points_count_test = round((1-p) * amount)  # useless
    points_count1 = amount//2
    points_count2 = amount//2

    # Пункт 2
    # x_train, y_train
    cluster1 = Cluster(generate_dots(points_count1, x1+y1))
    cluster2 = Cluster(generate_dots(points_count2, x2+y2))
    # x_test
    cluster_test = cluster1[int(points_count1 * 0.8): ] + cluster2[int(points_count2 * 0.8): ]
    cluster1 = cluster1[:int(points_count1 * 0.8)]
    cluster2 = cluster2[:int(points_count2 * 0.8)]
    #########

    # Пункт 3
    predicted_clusters = fit(cluster_test, cluster1, cluster2)

    # Отрисовка областей для кластеров
    plt.plot([x1[0], x1[0], x1[1], x1[1], x1[0]], [y1[0], y1[1], y1[1], y1[0], y1[0]])
    plt.plot([x2[0], x2[0], x2[1], x2[1], x2[0]], [y2[0], y2[1], y2[1], y2[0], y2[0]])

    # Отрисовка точек
    plt.plot(cluster1.x, cluster1.y, marker="o", color="b", ls="")
    plt.plot(cluster2.x, cluster2.y, marker="p", color="#FFA500", ls="")
    colors = ["#800080", "r"]
    markers = ["o", "p"]
    for ind, cluster in enumerate(predicted_clusters):
        plt.plot(cluster.x, cluster.y, marker=markers[ind], color=colors[ind], ls="")

    # Пункт 4
    print(f"computeAccuracy: {computeAccuracy(predicted_clusters, cluster_test)}")
    # Tuple[startX, maxX, startY, maxY]
    plt.axis((0, 21, 0, 11))
    plt.show()
