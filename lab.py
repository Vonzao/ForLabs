"""
                    `           Лабораторная работа №1
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


class Lab:

    @staticmethod
    def task1():

        import math
        from functools import lru_cache


        @lru_cache(None)
        def fac(x):
            if x <= 1:
                return 1
            return x * fac(x-1)


        for x in range(1, 10):
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
    def task2():

        import math


        for x in range(1, 8):
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
    def task3():

        import math


        for x in range(1, 10):
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
    def task4():

        import math


        for x in range(1, 10):
            x /= 10
            y = (1+2*x**2) * math.e ** (x**2)
            s = 0
            i = 0
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = ((2*i + 1) * x ** (2*i)) / math.factorial(i)
                s += arg
                i += 1
            print(f"y: {y}; s: {s + 1}")
