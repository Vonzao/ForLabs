"""
                               Контрольная работа №1
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Tuple, Callable, Any
import math


def descriptions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        print(f'\n{func.__name__}\n')
        result = func(*args, **kwargs)
        print(result)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descriptions
    def task7():
        """
        Лабораторная работа №1
        Из массива удалить повторяющиеся элементы.
        """

        import math

        for x in range(1, 10):
            x /= 20
            y = (1+2*x**2) * math.e ** (x**2)
            s = 0
            i = 0
            arg = float("inf")
            while abs(arg) >= 0.0001:
                arg = ((2*i + 1) * x ** (2*i)) / math.factorial(i)
                s += arg
                i += 1
            print(f"y: {y}; s: {s + 1}")

    @staticmethod
    @descriptions
    def task11():
        """
        Лабораторная работа №2
        В группе учится n студентов. Каждый сдал 4 экзамена.
        Подсчитать число неуспевающих студентов и средний балл группы.
        """
        values = [list(map(int, input(f'ВВедите оценки {i}-го ученика в формате "w x y z"').split()))
                  for i in range(int(input("ВВедите количество учеников")))]
        # Число неуспевающих - число учеников, у которых хотя бы одна двойка
        g = sum(any(value == 2 for value in values[i]) for i in range(len(values)))
        # Средний балл группы
        s = sum(map(sum, values)) / len(values)
        return f"Число неуспевающих = {g}\nСредний балл группы = {s}"

    @staticmethod
    @descriptions
    def task13(array: List[Any]) -> List[Any]:
        """
        Лабораторная работа №3
        Из массива удалить повторяющиеся элементы.
        """
        return list(dict.fromkeys(array).keys())
