"""
                               Лабораторная работа №4
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Tuple, Callable, Any
import math


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
    def task6A(matrix: List[List[int]]) -> str:
        """
        Задание 6 из 3 уровня.
        Вариант А, где матрица задаётся двумерным массивом.

        В матрице размером n x n сформировать два одномерных массива:
        в один переслать по строкам верхний треугольник матрицы, включая
        элементы главной диагонали, в другой нижний треугольник.
        Вывести верхний и нижний треугольники по строкам.
        """
        upper_triangle = []
        lower_triangle = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i <= j:
                    upper_triangle.append(matrix[i][j])
                else:
                    lower_triangle.append(matrix[i][j])
        upper_triangle = map(str, upper_triangle)
        lower_triangle = map(str, lower_triangle)
        ans = ''
        nach = 0
        ma = len(matrix) - 1
        for ind, el in enumerate(upper_triangle):
            ans += f'{el} '
            if ind == nach + ma:
                ans += '\n' + "  " * (len(matrix) - ma)
                nach = ind+1
                ma -= 1
        ans += '\n'
        nach = 0
        ma = 0
        for ind, el in enumerate(lower_triangle):
            ans += f'{el} '
            if ind == nach + ma:
                ans += '\n'
                nach = ind + 1
                ma += 1
        return ans

    @staticmethod
    @descripions
    def task6B(matrix: List[int]) -> str:
        """
        Задание 6 из 3 уровня.
        Вариант В, где матрица задаётся одномерным массивом.

        В матрице размером их и сформировать два одномерных массива:
        в один переслать по строкам верхний треугольник матрицы, включая
        элементы главной диагонали, в другой нижний треугольник.
        Вывести верхний и нижний треугольники по строкам.
        """
        upper_triangle = []
        lower_triangle = []
        le = int(len(matrix) ** 0.5)
        skip = 0
        i = skip
        dob = 0
        for el in matrix:
            if dob == le - skip:
                skip += 1
                i = skip
                dob = 0
            if not i:
                upper_triangle.append(el)
                dob += 1
            else:
                lower_triangle.append(el)
                i -= 1
        upper_triangle = map(str, upper_triangle)
        lower_triangle = map(str, lower_triangle)
        ans = ''
        nach = 0
        ma = le - 1
        for ind, el in enumerate(upper_triangle):
            ans += f'{el} '
            if ind == nach + ma:
                ans += '\n' + "  " * (le - ma)
                nach = ind + 1
                ma -= 1
        ans += '\n'
        nach = 0
        ma = 0
        for ind, el in enumerate(lower_triangle):
            ans += f'{el} '
            if ind == nach + ma:
                ans += '\n'
                nach = ind + 1
                ma += 1
        return ans

    @staticmethod
    @descripions
    def task7(A: List[List[int]]) -> str:
        """
        Задание 7 из 2 уровня
        В матрице размером 6х6 найти максимальный элемент на главной диагонали.
        Заменить нулями элементы матрицы, расположенные правее главной диапнали в строках,
        расположенных выше строки, содержащей максимальный элемент на главной диагонали.
        """
        main_diagonal = [A[i][i] for i in range(6)]
        ind = main_diagonal.index(max(main_diagonal))
        for i in range(ind):
            for j in range(i + 1, 6):
                A[i][j] = 0
        return '\n'.join(map(list.__repr__, A))

    @staticmethod
    @descripions
    def task9A(M: List[List[int]]) -> str:
        """
        Задание 9 из 3 уровня
        Вариант А, где матрица задаётся двумерным массивом.

        В матрице размером 5 х 7 переставить столбцы таким образом,
        чтобы количества отрицательных элементов в столбцах
        следовали в порядке возрастания.
        """
        M = [[M[i][j] for i in range(5)] for j in range(7)]
        otrs = [(ind, len(list(filter(lambda n: n<0, st)))) for ind, st in enumerate(M)]
        otrs.sort(key=lambda tupl: tupl[1])
        M1 = [M[i] for i, n in otrs]
        M1 = [[M1[i][j] for i in range(7)] for j in range(5)]
        return '\n'.join(map(list.__repr__, M1))

    @staticmethod
    @descripions
    def task9B(M: List[int]) -> str:
        """
        Задание 9 из 3 уровня
        Вариант В, где матрица задаётся одномерным массивом.

        В матрице размером 5 х 7 переставить столбцы таким образом,
        чтобы количества отрицательных элементов в столбцах
        следовали в порядке возрастания.
        """
        otrs = [[i, 0] for i in range(7)]
        for ind, el in enumerate(M):
            if el < 0 :
                otrs[ind%7][1] += 1
        otrs.sort(key=lambda tupl: tupl[1])
        M1 = [M[ind + 7 * i] for i in range(5) for ind, _ in otrs]
        ans = ""
        for ind, el in enumerate(M1):
            ans += f"{" " * (2 if el >= 0 else 1)}{el}"
            if ind % 7 == 6:
                ans += '\n'
        return ans


if __name__ == "__main__":
    from random import seed, randint
    seed(1016)
    print(*[randint(*diapason) for diapason in [(1, 14), (1, 9), (1, 14)]])
    matrix = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
    Lab.task6A(matrix)
    matrix = [
        1, 2, 3, 4, 5,
        1, 2, 3, 4, 5,
        1, 2, 3, 4, 5,
        1, 2, 3, 4, 5,
        1, 2, 3, 4, 5
    ]
    Lab.task6B(matrix)
    matrix = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 6, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 4]
    ]
    Lab.task7(matrix)
    matrix = [
        [ 1, 2, -3, -4,  5,  6, -7],
        [-1, 2, -3,  4, -5, -6, -7],
        [ 1, 2, -3,  4,  5,  6,  7],
        [-1, 2, -3,  4, -5, -6, -7],
        [ 1, 2, -3,  4, -5, -6, -7]
    ]
    Lab.task9A(matrix)
    matrix = [
         1, 2, -3, -4,  5,  6, -7,
        -1, 2, -3,  4, -5, -6, -7,
         1, 2, -3,  4,  5,  6,  7,
        -1, 2, -3,  4, -5, -6, -7,
         1, 2, -3,  4, -5, -6, -7
    ]
    Lab.task9B(matrix)
