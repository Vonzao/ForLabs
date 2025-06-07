
"""
                    `           Лабораторная работа №1
                                    III Уровень
                               Сазонов Данила Сергеевич
"""
import math
from typing import Callable, Any


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
    def task1():

        import math
        from functools import lru_cache


        @lru_cache(None)
        def fac(x):
            if x <= 1:
                return 1
            return x * fac(x-1)


        for x in range(1, 11):
            x /= 10
            y = math.cos(x)
            s = 0
            i = 0
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = (-1) ** i * (x ** (2*i)) / fac(2*i)
                s += arg
                i += 1
            print(f"y: {y}; s: {s}")

    @staticmethod
    @descriptions
    def task2():

        import math


        for x in range(1, 9):
            x /= 10
            y = (x * math.sin(math.pi / 4)) / (1 - 2*x*math.cos(math.pi / 4) + x**2)
            s = 0
            i = 1
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = x ** i * math.sin(i * math.pi / 4)
                s += arg
                i += 1
            print(f"y: {y}; s: {s}")

    @staticmethod
    @descriptions
    def task3():

        import math


        for x in range(1, 11):
            x /= 10
            y = math.e ** math.cos(x) * math.cos(math.sin(x))
            s = 0
            i = 1
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = math.cos(i * x) / math.factorial(i)
                s += arg
                i += 1
            print(f"y: {y}; s: {s + 1}")

    @staticmethod
    @descriptions
    def task4():

        import math


        for x in range(1, 11):
            x /= 10
            y = (1+2*x**2) * math.e ** (x**2)
            s = 0
            i = 0
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = ((2*i + 1) * x ** (2*i)) / math.factorial(i)
                s += arg
                i += 1
            print(f"y: {y}; s: {s}")

    @staticmethod
    @descriptions
    def task5():

        import math

        for x in range(5, 26):
            x = x / 25 * math.pi
            y = (x**2 - math.pi**2 / 3) / 4
            s = 0
            i = 1
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = ((-1) ** i) * math.cos(i*x) / i**2
                s += arg
                i += 1
            print(f"y: {y}; s: {s}")


if __name__ == "__main__":
    Lab.task1()
    Lab.task2()
    Lab.task3()
    Lab.task4()
    Lab.task5()
