"""
                               Лабораторная работа №7
                                    III Уровень
                               Сазонов Данила Сергеевич
"""


from typing import List, Callable, Any, Dict, Union


def descriptions(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        addition = ""
        if "addition" in kwargs:
            addition = kwargs["addition"]
            del kwargs["addition"]
        print(f'\n{func.__name__} {addition}\n')
        print("Исходные данные\n")
        for el in args:
            if isinstance(el, list) and isinstance(el[0], list):
                print("\n".join(map(repr, el)), end="\n"*3)
            else:
                print(el)
        result = func(*args, **kwargs)
        print("\nРезультат\n")
        print(result)
        print(f'\n{func.__name__} finished!\n')
        return result
    return wrapper


class Lab:
    @staticmethod
    @descriptions
    def task6_2(names: List[str], all_scores: List[int]) -> str:
        """
        Задание 6 из 2 уровня.

        Протокол соревнований по прыжкам в воду содержит список
        фамилий спортсменов и баллы, выставленные 5 судьями по
        результатам 2 прыжков. Получить итоговый протокол, содержащий
        фамилии и результаты, в порядке занятых спортсменами мест по
        результатам 2 прыжков.
        """
        class SportsMan:
            def __init__(self, name, scores):
                self.name = name
                self.score = sum(scores) / len(scores)
            def __lt__(self, other):
                return self.score < other.score
            def __str__(self):
                return f"{self.name} - {self.score}"
        sportsmans = [SportsMan(name, all_scores[i*5: i*5+5]) for i, name in enumerate(names)]
        return "\n".join(map(str, sorted(sportsmans, reverse=True)))


    @staticmethod
    @descriptions
    def task6_3(ans: List[str]) -> str:
        """
        Задание 6 из 3 уровня.

        Японская радиокомпания провела опрос радиослушателей по
        трем вопросам:
            а) какое животное вы связываете с Японией и японцами?
            б) какая черта характера присуща японцам больше всего?
            в) какой неодушевленный предмет или понятие вы связываете с Японией?
        Большинство опрошенных прислали ответы на все или часть вопросов.
        Составить программу получения первых пяти наиболее часто встречающихся ответов
        по каждому вопросу и доли (%) каждого такого ответа. Предусмотреть необходимость
        сжатия столбца ответов в случае отсутствия ответов на некоторые вопросы.
        """

        class Answer:
            def __init__(self, animal, personality, object):
                self.animal = animal
                self.personality = personality
                self.object = object
                self.__str__ = self.__repr__
            def __repr__(self):
                return f"({self.animal}, {self.personality}, {self.object})"


        class Counter:
            def __init__(self, objects: List[Any]):
                self._value = {object: objects.count(object) for object in set(objects)}
                del self._value[""]
                self._value = list(self._value.items())
                self._value.sort(reverse=True, key=lambda el: el[1])

            def __repr__(self):
                su = sum([el[1] for el in self._value])
                value = [[el[0], el[1] * 100 // su] for el in self._value]
                return "\n".join(map(lambda el: f"{el[0]} - {el[1]}%", value[:5]))


        anwers = [Answer(*ans[i*3:i*3+3]) for i in range(len(ans) // 3)]
        animal = Counter([answer.animal for answer in anwers])
        personality = Counter([answer.personality for answer in anwers])
        object = Counter([answer.object for answer in anwers])
        return "\n\n".join(map(Counter.__repr__, (animal, personality, object)))




    @staticmethod
    @descriptions
    def task4(participants: Dict[str, int]) -> int:
        """
        Лыжные гонки проводятся отдельно для двух групп участников.
        Результаты соревнований заданы в виде фамилий участников и
        их результатов в каждой группе. Расположить результаты
        соревнований в каждой группе в порядке занятых мест.
        Объединить результаты обеих групп с сохранением
        упорядоченности и вывести в виде таблицы с заголовком.
        """
        class Group:
            def __init__(self, participants: List[Union[str, int]]):
                self.participants = participants
                self.participants.sort(key=lambda participant: participant[1])

            def __repr__(self):
                ma = len(max(self.participants, key=lambda el: len(el[0]))[0]) + 2
                res = f"{"Фамилия": ^{ma}}| Результат\n"
                for participant in participants:
                    res += f"{participant[0]: ^{ma}}| {participant[1]}\n"
                return res

            def __add__(self, other):
                res = Group([])
                res.participants = self.participants + other.participants
                return res
        participants = list(participants.items())
        group1 = Group(participants[:len(participants)//2])
        group2 = Group(participants[len(participants)//2:])
        return group2 + group1



if __name__ == "__main__":
    from random import seed, randint
    seed(1016)
    print(*[randint(1, end) for end in (9, 6, 6)])
    Lab.task6_2(
        [
            "Oleg",
            "Peter",
            "Ilya",
            "Maks"
        ],
        [
            4, 5, 5, 4, 5,
            2, 3, 4, 3, 3,
            1, 2, 1, 1, 2,
            3, 4, 4, 4, 3
        ]
    )
    Lab.task6_3([
        "Японский макака",
        "Усидчивость",
        "Чайная церемония",
        "Карп",
        "Вежливость",
        "",
        "Ушак",
        "Терпение",
        "Сакэ",
        "",
        "Скромность",
        "Бонсай",
        "Церемониальный тигр",
        "Стремление к гармонии",
        "Сакэ",
        "",
        "",
        "Чайная церемония",
        "Карп",
        "Вежливость",
        "Сакэ",
        "",
        "Терпение",
        "Сакэ",
        "",
        "Скромность",
        "Бонсай",
        "Церемониальный тигр",
        "",
        "Самурайский меч",
        "Японский макака",
        "Усидчивость",
        "Чайная церемония",
        "Карп",
        "Вежливость",
        "",
        "Ушак",
        "Терпение",
        "Сакэ",
        "",
        "Скромность",
        "Бонсай",
        "Церемониальный тигр",
        "Стремление к гармонии",
        "Сакэ"
    ])
    Lab.task4({
        "Иванов": 15.25,
        "Петров": 22.47,
        "Сидоров": 35.68,
        "Смирнов": 40.15,
        "Кузнецов": 27.83,
        "Попов": 18.92,
        "Лебедев": 44.76,
        "Зайцев": 31.54,
        "Федоров": 29.01,
        "Морозов": 12.34,
        "Васильев": 38.90
    })
