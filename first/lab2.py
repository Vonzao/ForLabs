"""
                    `           Лабораторная работа №2
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Tuple, Callable, Any
import math


def descriptions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        print(f'\n{func.__name__}\n')
        result = func(*args, **kwargs)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descriptions
    def task1(data: List[float]):
        """
        Определить средний рост девочек и мальчиков одного класса. В классе учится n учеников.
        """
        print(sum(data) / len(data))

    @staticmethod
    @descriptions
    def task2(r: int, center: Tuple[int, int]):
        """
        В компьютер вводятся по очереди координаты n точек.
        Определить, сколько из них попадет в круг радиусом r с центром в точке (а, б).
        """
        n = ''
        while not isinstance(n, int):
            try:
                n = abs(int(n))
            except ValueError:
                n = input("Введите количество точек: ")
        dots: List[Tuple[int, int]] = []
        for _ in range(n):
            dot: Tuple[int, int] | str = 'a'
            while not isinstance(dot, tuple):
                try:
                    dot = tuple(map(int, dot.split()))
                    if len(dot) != 2: 
                        raise ValueError
                except ValueError:
                    dot = input('Введите елочисленные координаты точки в формате "x y": ')
            dots.append(dot)

        class Vector:
            def __init__(self, start: Tuple[int, int], end: Tuple[int, int]):
                self.x = end[0] - start[0]
                self.y = end[1] - start[1]

            def __abs__(self):
                return math.sqrt(self.x ** 2 + self.y ** 2)

        g = 0
        for dot in dots:
            dot: Vector = Vector(start=center, end=dot)
            if abs(dot) < r:
                g += 1
        print(g)

    @staticmethod
    @descriptions
    def task3(students: List[float]):
        """
        Ученику 1-го класса назначается дополнительно стакан молока (200 мл), если его вес составляет меньше 30 кг.
        Определить, сколько литров молока потребуется ежедневно для одного класса, состоящего из n учеников.
        После взвешивания вес каждого ученика вводится в компьютер.
        """
        """
        Округление, чтобы избежать неточности при вычислениях с плавующей точкой 
        >>> 0.2+0.2+0.2
        0.6000000000000001
        """
        print(round(sum(0.2 for weight in students if weight < 30), 1))

    @staticmethod
    @descriptions
    def task4(r1: int, r2: int):
        """
        В компьютер вводятся по очереди координаты n точек.
        Определить, сколько из них попадет в кольцо с внутренним радиусом r1 и внешним r2.
        """
        # В задаче не задан центр кольца, поэтому приму за (0, 0)
        center = (0, 0)
        n = ''
        while not isinstance(n, int):
            try:
                n = abs(int(n))
            except ValueError:
                n = input("Введите количество точек: ")
        dots: List[Tuple[int, int]] = []
        for _ in range(n):
            dot: Tuple[int, int] | str = 'a'
            while not isinstance(dot, tuple):
                try:
                    dot = tuple(map(int, dot.split()))
                    if len(dot) != 2: 
                        raise ValueError
                except ValueError:
                    dot = input('Введите елочисленные координаты точки в формате "x y": ')
            dots.append(dot)

        class Vector:
            def __init__(self, start: Tuple[int, int], end: Tuple[int, int]):
                self.x = end[0] - start[0]
                self.y = end[1] - start[1]

            def __abs__(self):
                return math.sqrt(self.x ** 2 + self.y ** 2)

        g = 0
        for dot in dots:
            dot: Vector = Vector(start=center, end=dot)
            if r1 < abs(dot) < r2:
                g += 1
        print(g)


if __name__ == "__main__":
    # task 1
    # 165, 178, 182, 173, 159, 164, 180
    Lab.task1([165, 178, 182, 173, 159, 164, 180])

    # task 2
    # radius: 13    center: (0, 0)
    Lab.task2(13, (0, 0))

    # task 3
    # Веса студентов: 30, 25, 27, 26, 36
    Lab.task3([30, 25, 27, 26, 36])

    # task 4
    # r1: 5    r2: 13
    Lab.task4(5, 13)
