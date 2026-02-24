from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, name, colories):
        self.name = name # название продукта
        self.colories = colories # колорийность (в нашем случае содержание энергии)

    @property
    @abstractmethod
    def eat_the_product(self):
        pass

    @property
    @abstractmethod
    def influence_on_mood(self):
        pass

    def __str__(self):
        return f'{self.name} имеет {self.colories} коллорий'


class Fish(Food):
    def __init__(self, name, colories, condition):
        super().__init__(name, colories)
        self.condition = condition # состояние еды (если плохое можно получить дебаф)

    def eat_the_product(self):
        return self.colories

    def influence_on_mood(self):
        return 10 # базово 10 для всех (но может в дальнейшем увеличится или уменшится исходя из вкусовых предпочтений котика)

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.energy = 50 # энергия
        self.mood = 50  # настроение базовое 50
        self.is_alive = True  # жив \ мёртв
        self.wool = True  # предпологаем что обычно с шерстьюю (если иначе изменим в самом коте или дочернем классе)
        self.food_preferences = {}  # словарь для предпочтений в еде



    def meow(self):
        return f'{self.name} мяукнул.'

    def eat(self):
        return
