import random
from sklearn.neighbors import KNeighborsClassifier
from icecream import ic
import matplotlib.pyplot as plt
from typing import Tuple, List


def generate_dots(n: int, area: Tuple[int, int, int, int]) -> List[Tuple[float, float]]:
    return [
        (
            random.uniform(*area[:2]),
            random.uniform(*area[2:])
        )
        for _ in range(n)
     ]


def computeAccuracy(y_predicted, y_test):
    return sum(t==p for t, p in zip(y_test, y_predicted)) / len(y_test)


if __name__ == "__main__":
    #########
    # Пункт 1
    x1 = 1, 12
    y1 = 2, 7
    x2 = 8, 20
    y2 = 4, 10

    p = 0.8
    amount = 125  # Общее кол-во точек
    points_count_test = round((1-p) * amount)
    points_count1 = (amount - points_count_test) // 2
    points_count2 = round((amount - points_count_test) / 2)

    # Пункт 2
    x, y = generate_dots(amount//2, x1+y1) + generate_dots(round(amount/2), x2+y2), [_//(amount//2) for _ in range(amount)]
    xy = list(dict(zip(x, y)).items())
    random.shuffle(xy)
    x, y = zip(*xy)
    # x_train, y_train
    x_train = x[:points_count1 + points_count2]
    y_train = y[:points_count1 + points_count2]
    # x_test
    x_test = x[points_count1 + points_count2:]
    y_test = y[points_count1 + points_count2:]
    #########

    # Пункт 3
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x_train, y_train)
    predicted = list(map(int, neigh.predict(x_test)))

    # Отрисовка областей для кластеров
    plt.plot([x1[0], x1[0], x1[1], x1[1], x1[0]], [y1[0], y1[1], y1[1], y1[0], y1[0]])
    plt.plot([x2[0], x2[0], x2[1], x2[1], x2[0]], [y2[0], y2[1], y2[1], y2[0], y2[0]])

    # Отрисовка точек
    pos1 = list(filter(lambda el: y_train[x_train.index(el)] == 0, x_train))
    pos2 = list(filter(lambda el: y_train[x_train.index(el)], x_train))
    plt.plot([x[0] for x in pos1], [x[1] for x in pos1], marker="o", color="b", ls="")
    plt.plot([x[0] for x in pos2], [x[1] for x in pos2], marker="p", color="#FFA500", ls="")
    colors = ["#800080", "r"]
    markers = ["o", "p"]

    for ind, pos in enumerate(x_test):
        plt.plot([pos[0]], [pos[1]], marker=markers[predicted[ind]], color=colors[predicted[ind]], ls="")

    # Пункт 4
    print(f"computeAccuracy: {computeAccuracy(predicted, y_test)}")
    # Tuple[startX, maxX, startY, maxY]
    plt.axis((0, 21, 0, 11))
    plt.show()
