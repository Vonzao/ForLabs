"""
                    `           Лабораторная работа №2
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Tuple, Callable, Any
import math
from icecream import ic


def descripions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        print(f'\n{func.__name__}\n')
        result = func(*args, **kwargs)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @descripions
    @staticmethod
    def task14(M: List[float]):
        """
        Заданный массив преобразовать таким образом, чтобы все его элементы принадлежали отрезку [-1, 1].
        Предусмотреть возможность обратного преобразования.
        """
        """
        Чтобы вернуть обратно нужно взять наименьшое значение при логорифмировании и оставить целую часть.
        Тогда разделив все числа массива на 10**l, числа вернут исходный вид 
        """
        l = math.log10(max(abs(x) for x in M))//1
        if l < 0: print(M); return
        M = [x / 10 ** l for x in M]
        print(M)

        """
        # Для возврата
        l = math.log10(min(abs(x) for x in M))//1
        if l < 0: print(M); return
        l = l if l>=0 else l+1
        print([x / 10 ** l for x in M])"""


if __name__ == "__main__":
    Lab.task14([1, -100, 2, 7, 8])