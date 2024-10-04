"""
                    `           Лабораторная работа №3
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
        print(result)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descripions
    def task14(M: List[float]) -> List[float]:
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
        return M

        """
        # Для возврата
        l = math.log10(min(abs(x) for x in M))//1
        if l < 0: print(M); return
        l = l if l>=0 else l+1
        print([x / 10 ** l for x in M])
        """

    @staticmethod
    @descripions
    def task10(M: List[int]) -> List[int]:
        """
        В массиве, заполненном наполовину, продублировать все элементы с сохранением порядка следования.
        (Например, задан массив Х = {13, 8, ...}, получить массив Х = {13, 13, 8, 8, ...}
        """
        import itertools
        return list(itertools.chain(*[[x, x] for x in M]))
        """
        def list_sum(M: List[List[Any]]) -> List[Any]:
            list(M[0].extend(x) for x in M[1:])
            return M[0]
        return list_sum([[x,x] for x in M])
        """

    @staticmethod
    @descripions
    def task12(M: List[int]) -> List[int]:
        """
        Из массива размером 12 удалить все отрицательные элементы.
        """
        return [x for x in M if x>=0]


    @staticmethod
    @descripions
    def task13(M: List[int]) -> List[int]:
        """
        Из массива удалить повторяющиеся элементы.
        """
        # Сделано так, чтобы сохранить порядок эелементов
        return list(dict.fromkeys(M).keys())


    @staticmethod
    @descripions
    def task6(A: List[int]) -> int:
        """
        В массиве A найти максимальное количество следующих подряд упорядоченных по убыванию элементов.
        """
        g = 0
        ma = float("-inf")
        for i in range(len(A[:-1])):
            if A[i] >= A[i+1]:
                g+=1
            else:
                g+=1
                ma = max(g,ma)
                g=0
        return ma


if __name__ == "__main__":
    Lab.task14([1, -100, 7, 2, -1, 7, 8, 8])
    Lab.task10([1, -100, 7, 2, -1, 7, 8, 8])
    Lab.task12([1, -100, 7, 2, -1, 7, 8, 8])
    Lab.task13([1, -100, 7, 2, -1, 7, 8, 8])
    Lab.task6([1, -100, 7, 2, -1, 7, 8, 8])
