"""
                                Контрольная работа №2
                               Сазонов Данила Сергеевич
"""


from typing import List, Callable, Any, Tuple
Self = Tuple


def descriptions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        addition = ""
        if "addition" in kwargs:
            addition = kwargs["addition"]
            del kwargs["addition"]
        print(f'\n{func.__name__} {addition}\n')
        print("Исходные данные")
        for el in args:
            print("\n".join(map(list.__repr__, el)), end="\n"*3)
        result = func(*args, **kwargs)
        print("Результат")
        print(result)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descriptions
    def task29(matrix: List[List[int]]) -> str:
        """
        Задание 29 из 1 уровня. Лабораторная работа №4

        В матрице В размером 5 х 7 удалить столбец, расположенный
        после столбца, содержащего минимальный по модулю элемент во 2-й строке
        """
        mi = min(matrix[1], key=abs)
        ind = matrix[1].index(mi) if mi in matrix[1] else matrix[1].index(-mi)
        ind = (ind + 1) % 7
        for line in matrix:
            line.pop(ind)
        return "\n".join(map(list.__repr__, matrix))


    @staticmethod
    @descriptions
    def task12(A: List[List[int]], B: List[List[int]]) -> str:
        """
        Задание 12 из 2 уровня. Лабораторная работа №5

        Заданы две матрицы одинакового размером.
        Столбец первой матрицы, содержащий максимальный
        элемент матрицы, поменять местами со столбцом второй
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
        return "\n".join(map(list.__repr__, A)) + "\n" * 2 + "\n".join(map(list.__repr__, B))

    @staticmethod
    @descriptions
    def task3(results: List[List[str]]) -> str:
        """
        Задание 3 из 3 уровня. Лабораторная работа №6

        В соревнованиях участвуют три команды по 6 человек.
        Результаты соревнований представлены в виде мест
        участников каждой команды (1-18). Определить
        команду-победителя, вычислив количество баллов,
        набранное каждой командой. Участнику, занявшему
        1-е место, начисляется 5 баллов,
        2-е 4,
        3-e 3,
        4-e 2,
        5-e 1,
        остальным 0 баллов.
        При равенстве баллов победителем считается команда,
        за которую выступает участник, занявший 1-е место.

        >>>

        Для удобства проверки лучше убрать комментарий в строчке
        # print(*teams, sep="\n")
        возле return
        """


        class Team:
            def __init__(self, name):
                self._name = name
                self._squad_list = []

            def add_member(self, sportsman):
                self._squad_list.append(sportsman)

            def __gt__(self, other: Self):
                if self._squad_list[0]._score == 5 and sum(self) == sum(other):
                    return True
                return sum(self) > sum(other)

            def __iter__(self):
                return self._squad_list.__iter__()

            def __str__(self):
                return f"{self._name}({self._squad_list})"

            def __repr__(self):
                return str(self._name)


        class SportsMan:

            _score = {place+1: 5-place if place < 5 else 0 for place in range(18)}

            def __init__(self, place: int, name: str, team: Team):
                self._score = self._score[place]
                self.name = name
                team.add_member(self)

            def __radd__(self, other: int):
                return other + self._score

            def __repr__(self):
                return str(f"{self.name}: {self._score}")


        teams = {name: Team(name) for name in set(map(lambda el: el[1], results))}
        for ind, sportsman in enumerate(results):
            SportsMan(ind+1, sportsman[0], teams[sportsman[1]])
        teams = list(teams.values())
        # Здесь нужно убрать комментарий, тогда покажет все команды, их участников и баллы участников
        # print(*teams, sep="\n")
        return max(teams).__repr__()


if __name__ == "__main__":

    from random import seed, randint
    seed(3116)
    print(*[randint(1, end) for end in (33, 28, 6)])

    matrix = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    Lab.task29(matrix)


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



    Lab.task3([
        ['Наумова Тамара Кирилловна', 'Стальные Ястребы'],
        ['Семенов Мефодий Гавриилович', 'Северные Соколы'],
        ['Стрелкова Галина Тарасовна', 'Северные Соколы'],
        ['Никитин Степан Эдгарович', 'Стальные Ястребы'],
        ['Степанов Потап Тарасович', 'Сибирские Олени'],
        ['Куприян Егорович Стрелков', 'Сибирские Олени'],
        ['Валерий Анисимович Денисов', 'Стальные Ястребы'],
        ['Бобылева Евпраксия Игоревна', 'Сибирские Олени'],
        ['Селезнев Емельян Гордеевич', 'Сибирские Олени'],
        ['Андрон Ильич Елисеев', 'Стальные Ястребы'],
        ['Лариса Юльевна Ермакова', 'Северные Соколы'],
        ['Ольга Михайловна Кошелева', 'Сибирские Олени'],
        ['Бурова Алевтина Ждановна', 'Стальные Ястребы'],
        ['Ерофей Харитонович Панов', 'Северные Соколы'],
        ['Эммануил Вячеславович Давыдов', 'Северные Соколы'],
        ['Дементьев Ратмир Харлампьевич', 'Стальные Ястребы'],
        ['Галина Александровна Орехова', 'Северные Соколы'],
        ['Андреев Дорофей Жоресович', 'Сибирские Олени']
    ]) ])
