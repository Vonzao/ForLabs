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
    def task1_12():
        """
        Лабораторная работа №1
        Вычислить при заданном х сумму s = 1+1/x + 1/x**2 + ... + 1/x**10
        """
        x = int(input("Введите число x: "))
        return sum([1/(x**n) for n in range(11)])



    @staticmethod
    @descriptions
    def task2_12():
        """
        Лабораторная работа №2
        Вводя n значений r, вычислить по выбору площадь квадрата со стороной r,
        площадь круга радиусом r или площадь равностороннего треугольника со стороной r.
        Использовать множественный выбор.
        """
        def S_tr(a: int) -> float:
            return (math.sqrt(3) * a ** 2) / 4
        def S_cir(r: int) -> float:
            return math.pi * r ** 2
        def S_sq(a: int) -> int:
            return a**2
        for _ in range(int(input("Введите число n: "))):
            r = int(input("Введите число r: "))
            typ = int(input("Введите 1 - треугольник, 2 - круг, 3 - квадрат: "))
            match typ:
                case 1:
                    print(S_tr(r))
                case 2:
                    print(S_cir(r))
                case 3:
                    print(S_sq(r))
        return ""


    @staticmethod
    @descriptions
    def task3_7(array: List[Any]) -> List[Any]:
        """
        Лабораторная работа №3
        Все отрицательные элементы переставить в конец массива с сохранением порядка их следования.
        """
        return list(filter(lambda n: n>=0, array)) + list(filter(lambda n: n<0, array))


if __name__ == "__main__":
    
    from random import seed, randint
    seed(1016)
    print("Генерация номеров заданий")
    print(*list(randint(1, n) for n in [18, 13, 14]))
    
    Lab.task1_12()
    Lab.task2_12()
    Lab.task3_7([1, -7, 3, 1, -5, -6, 2, 2, 5, 4, 1, 6])
