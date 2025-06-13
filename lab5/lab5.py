import math
import matplotlib.pyplot as plt
import random
from typing import Tuple, List
from sklearn.cluster import AffinityPropagation, SpectralClustering, HDBSCAN
from functools import lru_cache
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider


def random_sign():
    return random.random() * 2 - 1


class Generator:
    @staticmethod
    @lru_cache
    def first(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        R = 0.9 * min(area) / 2
        r = R / 3
        delta = R / 20
        o1 = lambda x: math.sqrt(abs(R ** 2 - x**2))
        o2 = lambda x: math.sqrt(abs(r ** 2 - x**2))
        dots = []
        def f(x):
            return 1 if x >= 0 else -1
        for _ in range(n//2):
            x = random_sign() * R
            dots.append((x, o1(x) * f(random_sign()) + delta * random_sign()))
            x = random_sign() * r
            dots.append((x, o2(x) * f(random_sign()) + delta * random_sign()))
        return tuple(dots)

    @staticmethod
    @lru_cache
    def second(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        w, h = map(lambda x: x / 2, area)
        accuracyH = h / 10
        accuracyw = w / 15
        v1 = (-w / 3, h * 0.9)
        v2 = (w / 3, -h * 0.9)
        b1 = 2 * v1[1] / (v2[0] ** 2 / v1[0] - v2[0])
        c1 = v1[1] - (b1/2) * v1[0]
        a1 = -b1 / (2 * v1[0])
        D1 = b1**2 - 4 * a1 * (c1 + v1[1] / 2)
        xk1 =(-b1 + math.sqrt(D1)) / (2 * a1)
        b2 = 2 * v2[1] / (v1[0] ** 2 / v2[0] - v1[0])
        c2 = v2[1] - (b2/2) * v2[0]
        a2 = -b2 / (2 * v2[0])
        D2 = b2**2 - 4 * a2 * (c2 + v2[1] / 2)
        xk2 =(-b2 + math.sqrt(D2)) / (2 * a2)
        f1 = lambda x: a1 * x ** 2 + b1 * x + c1
        f2 = lambda x: a2 * x ** 2 + b2 * x + c2
        dots = []
        for _ in range(n//2):
            x = random_sign() * abs(v1[0] - xk1) - w/3
            dots.append((x + random_sign() * accuracyw, f1(x) + random_sign() * accuracyH))
            x = random_sign() * abs(v2[0] - xk2) + w/3
            dots.append((x + random_sign() * accuracyw, f2(x) + random_sign() * accuracyH))
        return tuple(dots)


    @staticmethod
    @lru_cache
    def third(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        measurement = min(area)
        r1 = 0.37 * measurement
        c1 = (0, 0.04*measurement)  # (0.5*measurement, 0.54*measurement)
        r2 = 0.27 * measurement
        c2 = (-0.4*measurement, 0.33 * measurement)  # (0.04*measurement, 0.83 * measurement)
        r3 = 0.2 * measurement
        c3 = (0.4 * measurement, 0.17 * measurement)  # (0.95 * measurement, 0.67 * measurement)
        dots = []

        def generate_dots(r, center, n):
            dots = []
            for i in range(n):
                 x = random_sign() *  r + center[0]
                 y = random_sign() *\
                    math.sqrt((r ** 2) - (x -  center[0]) ** 2) + center[1]
                 dots.append((x, y))
            return dots

        for i in range(3):
            dots.extend(eval(f"generate_dots(r{i+1}, c{i+1}, n//3)"))
        return tuple(dots)


    @staticmethod
    @lru_cache
    def forth(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        area = tuple(0.8*pos for pos in area)
        delta = min(area) / 20
        that_corner1 = (-0.5 * area[0], -0.25 * area[1])
        that_corner2 = (0, area[1] / 4)
        that_corner3 = (-0.5 * area[0], 0.18*area[1])
        func1 = lambda x: that_corner1[1] + (that_corner1[0] - x)
        func2 = lambda x: that_corner2[1] + (that_corner2[0] - x)
        func3 = lambda x: that_corner3[1] + (that_corner3[0] - x)
        dots = []
        for _ in range(n//3):
            x = random_sign() * area[0] * 0.5
            dots.append((x, func1(x) + delta * random_sign()))
        for _ in range(n//3):
            x = random_sign() * area[0] * 0.7
            dots.append((x, func2(x) + delta * random_sign()))
        for _ in range(n//3):
            x = random_sign() * area[0] * 0.5
            dots.append((x, func3(x) + delta * random_sign()))
        return tuple(dots)

    @staticmethod
    @lru_cache
    def fifth(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        measurement = min(area)
        r = 0.37 * measurement * 0.8
        c1 = (0, -0.2*measurement)  # (0.5*measurement, 0.54*measurement)
        c2 = (-0.35*measurement, 0.33 * measurement)  # (0.04*measurement, 0.83 * measurement)
        c3 = (0.3 * measurement, 0.17 * measurement)  # (0.95 * measurement, 0.67 * measurement)
        dots = []

        def generate_dots(r, center, n):
            dots = []
            for i in range(n):
                x = random_sign() * r + center[0]
                y = random_sign() * \
                    math.sqrt((r ** 2) - (x - center[0]) ** 2) + center[1]
                dots.append((x, y))
            return dots

        for i in range(3):
            dots.extend(eval(f"generate_dots(r, c{i + 1}, n//3)"))
        return tuple(dots)

    @staticmethod
    @lru_cache
    def sixth(area: Tuple[int, int], n) -> Tuple[Tuple[float, float]]:
        return tuple((random_sign() * area[0]/2, random_sign() * area[1]/2) for _ in range(n))


def standardization(lst: List[int]) -> List[int]:
    """Делает метки кластеров неотрицательными"""
    mi = min(lst)
    return [el - mi for el in lst] if mi < 0 else lst


class App:
    def __init__(self):
        self.area = (10, 10)
        self.n = 500
        self.clustering_methods = {
            1: ("Affinity Propagation", self.affinity_propagation),
            2: ("Spectral Clustering", self.spectral_clustering),
            3: ("HDBSCAN", self.HDBSCAN)
        }
        self.generation_methods = {
            1: ("Two Circles", Generator.first, 2),
            2: ("Two Parabolas", Generator.second, 2),
            3: ("Three Circles", Generator.third, 3),
            4: ("Three Lines", Generator.forth, 3),
            5: ("Three Circles'", Generator.fifth, 3),
            6: ("Random Points", Generator.sixth, 3)
        }
        self._setup_plots()

    def _setup_plots(self):
        # Настройка сетки графиков: 6 строк (генерации) x 3 столбца (кластеризации)
        fig = plt.figure(figsize=(15, 20))
        gs = gridspec.GridSpec(
            nrows=6,
            ncols=3,
            figure=fig,
            wspace=0.3,
            hspace=0.4
        )

        # Заполнение таблицы
        for gen_num, (gen_name, gen_func, n) in self.generation_methods.items():
            dots = gen_func(self.area, self.n)

            for cluster_num, (cluster_name, cluster_func) in self.clustering_methods.items():
                ax = fig.add_subplot(gs[gen_num - 1, cluster_num - 1])

                # Применение кластеризации
                labels = cluster_func(dots, n)
                unique_clusters = len(set(labels))

                # Отрисовка точек
                scatter = ax.scatter(
                    [dot[0] for dot in dots],
                    [dot[1] for dot in dots],
                    c=labels,
                    cmap='viridis',
                    s=10
                )

                # Настройка заголовка и подписей
                if gen_num == 1:
                    ax.set_title(cluster_name, pad=10)
                if cluster_num == 1:
                    ax.set_ylabel(gen_name, rotation=0, labelpad=40, ha='right')

                ax.set_xticks([])
                ax.set_yticks([])
                ax.set_xlim(-self.area[0] / 2, self.area[0] / 2)
                ax.set_ylim(-self.area[1] / 2, self.area[1] / 2)


        plt.suptitle("Clustering Results for Different Generations and Methods", y=0.99, fontsize=14)
        plt.show()

    @staticmethod
    @lru_cache
    def affinity_propagation(dots: Tuple[Tuple[float, float]], n) -> List[int]:
        model = AffinityPropagation(preference=-50, random_state=42).fit(dots)
        return standardization(model.labels_)

    def spectral_clustering(self, dots: Tuple[Tuple[float, float]], n) -> List[int]:
        model = SpectralClustering(n_clusters=n).fit_predict(dots)
        return standardization(model.tolist())

    @staticmethod
    @lru_cache
    def HDBSCAN(dots: Tuple[Tuple[float, float]], n) -> List[int]:
        min_size = max(5, int(len(dots) * 0.05))
        model = HDBSCAN(min_cluster_size=min_size).fit(dots)
        return standardization(model.labels_.tolist())


if __name__ == "__main__":
    App()
