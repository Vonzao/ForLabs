"""
                               Лабораторная работа №5
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Callable, Any


def descriptions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        addition = ""
        if "addition" in kwargs:
            addition = kwargs["addition"]
            del kwargs["addition"]
        print(f'\n{func.__name__} {addition}\n')
        result = func(*args, **kwargs)
        print(result)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descriptions
    def task12(A: List[List[int]], B: List[List[int]]) -> str:
        """
        Задание 12 из 2 уровня.

        Заданы две матрицы одинакового размером.
        Столбец первой матрицы, содержащий максимальный
        элемент матрицы, поменять ме- стами со столбцом второй
        матрицы, содержащим максимальный элемент.
        Поиск столбца, содержащего максимальный элемент
        матрицы, оформить в виде метода.
        """
        def find_max(A: List[List[int]]) -> int:
            a = [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]
            ma = max(a)
            for st in A:
                if ma in st:
                    return st.index(ma)
        max1 = find_max(A)
        max2 = find_max(B)
        for i in range(len(A)):
            A[i][max1], B[i][max2] = B[i][max2], A[i][max1]
        return "\n".join(map(list.__repr__, A)) + "\n"*2 + "\n".join(map(list.__repr__, B))

    @staticmethod
    @descriptions
    def task6(A: List[List[int]]) -> str:
        """
        Задание 6 из 3 уровня.

        Поменять местами столбец, содержащий максимальный элемент
        на главной диагонали заданной квадратной матрицы, со
        столбцом, содержащим максимальный элемент в первой строке
        матрицы. Для замены столбцов использовать метод. Для
        поиска соответствую- щих максимальных элементов
        использовать делегат.
        """
        def change_columns(A:List[List[int]], ind1: int, ind2: int) -> None:
            for i in range(len(A)):
                A[i][ind1], A[i][ind2] = A[i][ind2], A[i][ind1]
        main_diagonal = [A[i][i] for i in range(len(A))]
        ind1 = main_diagonal.index(max(main_diagonal))
        ind2 = A[0].index(max(A[0]))
        change_columns(A, ind1, ind2)
        return "\n".join(map(list.__repr__, A))

    @staticmethod
    @descriptions
    def task4(A: List[List[int]], is_upper: bool) -> int:
        """
        Задание 4 из 3 уровня.

        Вычислить сумму квадратов элементов вектора, полученного
        пересылкой в него либо верхнего, либо нижнего треугольника
        заданной квадратной матрицы (в обоих случаях включая
        главную диагональ). Для нахождения суммы использовать
        метод, для пересылки делегат.
        """
        triangle = []
        for i in range(len(A)):
            second_range = range(i, len(A)) if is_upper else range(0, i+1)
            for j in second_range:
                triangle.append(A[i][j])
        return sum(map(lambda x: x**2, triangle))


if __name__ == "__main__":
    from random import seed, randint
    seed(1016)
    print(*[randint(*diapason) for diapason in [(1, 28), (1, 7), (1, 7)]])
    matrix_A = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 9, 3, 4],
        [1, 2, 3, 4]
    ]
    matrix_B = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 9],
        [1, 2, 3, 4]
    ]
    Lab.task12(matrix_A, matrix_B)
    matrix = [
        [1, 9, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
    Lab.task6(matrix)
    matrix = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
    Lab.task4(matrix, True, addition="Верхний теругольник матрицы")
    Lab.task4(matrix, False, addition="Нижний теругольник матрицы")
