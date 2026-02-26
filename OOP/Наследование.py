"""
================    НАСЛЕДОВАНИЕ — переиспользование и иерархия     ======================

super() — это инструмент НАСЛЕДОВАНИЯ!
super() НУЖЕН КОГДА:
✅ Вы в дочернем классе
✅ Нужно вызвать метод родителя
✅ Хотите гибкости при изменении кода
✅ Работаете с множественным наследованием
✅ Строите цепочку инициализации
super() = "родительский класс" (не важно, как он называется и сколько их)
ClassName.method(self) = "конкретный класс" (жесткая привязка)
"""

from abc import ABC, abstractmethod


# 🔧 ИНСТРУМЕНТ 1: Базовое наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


# 🔧 ИНСТРУМЕНТ 2: super() - вызов родителя
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родителя
        self.breed = breed

    def speak(self):
        return f"{super().speak()} Гав!"  # Расширение метода


# 🔧 ИНСТРУМЕНТ 3: Множественное наследование
class Flyable:
    def fly(self):
        return "Летит"


class Swimmable:
    def swim(self):
        return "Плывет"


class Duck(Flyable, Swimmable):  # Наследование от двух классов
    pass


# 🔧 ИНСТРУМЕНТ 4: Mixins (классы-примеси)
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class XMLMixin:
    def to_xml(self):
        return f"<object>{self.__dict__}</object>"


class Product(JSONMixin, XMLMixin):  # Добавляем функциональность
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 🔧 ИНСТРУМЕНТ 5: Абстрактные классы



class Shape(ABC):  # Абстрактный базовый класс
    @abstractmethod
    def area(self):  # Обязательный для реализации
        pass

    @abstractmethod
    def perimeter(self):  # Обязательный для реализации
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Обязаны реализовать!
        return 3.14 * self.radius ** 2

    def perimeter(self):  # Обязаны реализовать!
        return 2 * 3.14 * self.radius
