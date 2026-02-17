"""
====================   АБСТРАКЦИЯ — отделение интерфейса от реализации   ==================
а также    ===== АССОЦИАЦИЯ, АГРЕГАЦИЯ, КОМПОЗИЦИЯ — отношения между объектами  ======
"""
from typing import Protocol
# 🔧 ИНСТРУМЕНТ 1: Абстрактные классы (ABC)
from abc import ABC, abstractmethod

# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def query(self, sql):
#         pass
#     @abstractmethod
#     def disconnect(self):
#         pass
#
#
# class PostgreSQL(Database):
#     def connect(self):  # Конкретная реализация
#         return "Подключение к PostgreSQL"
#     def query(self, sql):
#         return f"Выполнение {sql} в PostgreSQL"
#     def disconnect(self):
#         return "Отключение от PostgreSQL"
#
#
# # 🔧 ИНСТРУМЕНТ 2: Интерфейсы (через ABC)
# class Drawable(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
# class Movable(ABC):
#     @abstractmethod
#     def move(self, dx, dy):
#         pass
#
# class Player(Drawable, Movable):
#     def draw(self):
#         return "Рисуем игрока"
#
#     def move(self, dx, dy):
#         return f"Перемещаем на ({dx}, {dy})"
#
#
# # 🔧 ИНСТРУМЕНТ 3: Протоколы (typing.Protocol)
#
#
# class Printable(Protocol):
#     def print(self) -> str:
#         ...  # Только сигнатура!
#
# class Document:
#     def print(self):
#         return "Печать документа"
#
# class Image:
#     def print(self):
#         return "Печать изображения"
#
# def print_object(obj: Printable):  # Работает с любым, у кого есть print()
#     return obj.print()
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name  # У студента есть только имя
#
#     def __repr__(self):
#         return f"Student('{self.name}')"
#
#
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#         # ВАЖНО: Это НЕ "связь с функцией"!
#         # Это КОНТЕЙНЕР для хранения ссылок на другие объекты
#         self.students = []  # ← БУДЕТ ХРАНИТЬ ССЫЛКИ НА СТУДЕНТОВ
#
#     def add_student(self, student):
#         # ПАРАМЕТР student - это ССЫЛКА на объект класса Student
#         # Мы сохраняем эту ссылку в список
#         self.students.append(student)
#         print(f"Учитель {self.name} добавил студента {student.name}")
#
#     def list_students(self):
#         print(f"Студенты учителя {self.name}:")
#         for student in self.students:
#             print(f"  - {student.name}")
#
#
# # ========== ДЕМОНСТРАЦИЯ СВЯЗИ ==========
#
# # 1. Создаем независимые объекты
# student_anna = Student("Анна")
# student_ivan = Student("Иван")
# teacher_maria = Teacher("Мария")
#
# print("Объекты созданы, связи нет:")
# print(f"Учитель: {teacher_maria.name}")
# print(f"Студенты: {student_anna.name}, {student_ivan.name}")
# print(f"Список студентов у учителя: {teacher_maria.students}\n")
#
# # 2. Устанавливаем СВЯЗЬ между объектами
# print("Устанавливаем связь:")
# teacher_maria.add_student(student_anna)  # ← СВЯЗЬ!
# teacher_maria.add_student(student_ivan)  # ← СВЯЗЬ!
#
# # 3. Проверяем результат
# print("\nРезультат:")
# teacher_maria.list_students()
# print(f"Внутреннее устройство: {teacher_maria.students}")
"""
Абстрактный метод на примере с кредиткой и дебетовой картой
"""

class Card(ABC):
    def __init__(self, cardholder):
        self.cardholder = cardholder
        self.balans = 0

    @staticmethod
    def validate_amount(amount):
        if amount < 0:
            raise ValueError('сумма операции должны бать положительной')

    @abstractmethod
    def top_up(self, amount):
       pass

    @abstractmethod
    def spend(self, amount):
        pass

class DebitCard(Card):

    def top_up(self, amount):
        self.validate_amount(amount)
        self.balans += amount

    def spend(self, amount):
        self.validate_amount(amount)
        if amount > self.balans:
            raise ValueError('Не достаточно денег на балансе')
        self.balans -= amount

class CreditCard(Card):
    def __init__(self, cardholder, limit):
        super().__init__(cardholder)
        self.limit = limit

    def top_up(self, amount):
        self.validate_amount(amount)
        if (self.balans + amount) > 0:
            raise ValueError('На карте могут быть только кредитные средства')
        self.balans += amount

    def spend(self, amount):
        self.validate_amount(amount)
        if abs(self.balans - amount) > self.limit:
            raise ValueError('Трата выше вашего лимита не доступна')
        self.balans -= amount

    def set_limit(self, new_limit):
        self.limit = new_limit


