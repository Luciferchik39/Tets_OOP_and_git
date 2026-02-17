from abc import ABC, abstractmethod

class SleepMixin:
    def sleep(self):
        print(f'{self.name} заснул')


class Bowl:
    def __init__(self):
        self.food = None

    def fill(self, food):
        self.food = food


class Cat:
    def __init__(self, name, age, bowl: Bowl):
        self.name = name
        self._age = age
        self.__mood = 50 # 0 - 100
        self.bowl = bowl

    @property
    def mood(self):
        return self.__mood
    @mood.setter
    def mood(self, value):
        self.__mood = max(0, min(100, value))
    def meow(self):
        print(f'{self.name} мяу')

    def feed(self, food):
        self.__mood += food.mood_bonus

class BritishCat(Cat):
    def meow(self):
        print(f'{self.name} осуждающий взгляд')

class StreetCat(Cat):
    def meow(self):
        print(f'{self.name} громко мяукает')

class CrasyCat(Cat, SleepMixin):
    pass

"""
Создать объект от абстрактного класса нельзя
абстрактный класс обозначает базовый интерфейс семейсва этих классов
"""

class Food(ABC):
    @property
    @abstractmethod
    def mood_bonus(self):
        pass

class Fish(Food):
    @property
    def mood_bonus(self):
        return 20


class Visitor:
    def interfact_witch_cat(self, cat: Cat):
        'взаимодействуем с котиком просим помяукать'
        cat.meow()

class Child(Visitor):
    def interfact_witch_cat(self, cat: Cat):
        'взаимодействует с котом что у того настроение портистя'
        cat.mood -= 10

class Adult(Visitor):
    def interfact_witch_cat(self, cat: Cat):
        'взаимодействует с котом что у того настроение поднимается'
        cat.mood += 5

class CatCafe:
    def __init__(self):
        self.cats = []
        self.visitors = []

    def add_cat(self, cat):
        self.cats.append(cat)

    def open_day(self):
        for cat in self.cats:
            cat.meow()

    "взаимодействеи посетителей с котами через кортеж"
    def add_visitor(self, visitor, cat):
        self.visitors.append((visitor, cat))

    def visitor_action(self):
        """Все посетители взаимодействуют со своими котами"""
        for visitor, cat in self.visitors:  # распаковываем кортеж
            visitor.interfact_witch_cat(cat)  # вызываем метод и передаём кота

    "взаимодействеи посетителей с котами через словарь"
    # def add_visitor(self, visitor, cat):
    #     """Добавляет посетителя и его кота"""
    #     self.visitors.append({'visitor': visitor, 'cat': cat})  # словарь с ключами
    #
    # def visitor_action(self):
    #     """Все посетители взаимодействуют со своими котами"""
    #     for pair in self.visitors:
    #         visitor = pair['visitor']  # получаем посетителя по ключу
    #         cat = pair['cat']  # получаем кота по ключу
    #         visitor.interfact_witch_cat(cat)

cafe = CatCafe()
barsik = BritishCat('Barsik', 1, Bowl())
tom = StreetCat('Tom', 2, Bowl())
cafe.add_cat(barsik)
cafe.add_cat(tom)
cafe.open_day()

pety = Child()
olya = Adult()
print(f"\n=== НАЧАЛЬНОЕ НАСТРОЕНИЕ ===")
print(f"{barsik.name} настроение: {barsik.mood}")
print(f"{tom.name} настроение: {tom.mood}")
cafe.add_visitor(pety, barsik)
cafe.add_visitor(olya, tom)
cafe.visitor_action()
# Проверяем изменившееся настроение
print(f"\n=== НАСТРОЕНИЕ ПОСЛЕ ВЗАИМОДЕЙСТВИЯ ===")
print(f"{barsik.name} настроение: {barsik.mood}")  # должно уменьшиться (ребёнок)
print(f"{tom.name} настроение: {tom.mood}")        # должно увеличиться (взрослый)