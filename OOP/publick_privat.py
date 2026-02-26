"""
Публичные, приватные, защищенные атрибуты и методы в пайтон не дают защиты а лишь обозначают информацию для других людей
protected _ prvate __
для более защищёного кода есть метод accessify
"""


class Banc_acc:
    def __init__(self, name, balans, passport):
        self.__name = name  # Приватный атрибут
        self.__balans = balans  # Приватный атрибут
        self.__pasport = passport  # Приватный атрибут

    def print_privat(self):
        """Публичный метод, который может обращаться к приватным атрибутам"""
        return f'{self.__name}, {self.__balans}, {self.__pasport}'


# Создаем экземпляр
acc_ilya = Banc_acc('Ilya', 250000, 1814252728)

# 1. Прямой доступ к приватным атрибутам НЕ работает
# print(acc_ilya.__name)  # AttributeError
# print(acc_ilya.__balans)  # AttributeError
# print(acc_ilya.__pasport)  # AttributeError

# 2. Доступ через публичный метод работает
print(acc_ilya.print_privat())  # Ilya, 250000, 1814252728

# 3. Доступ через name mangling работает (но так делать НЕ нужно!)
print(acc_ilya._Banc_acc__name)  # Ilya
print(acc_ilya._Banc_acc__balans)  # 250000
print(acc_ilya._Banc_acc__pasport)  # 1814252728

"""
property, getter-методы, setter-методы
"""

class Banc_acc:
    def __init__(self, name, balans, passport):
        self.__name = name  # Приватный атрибут
        self.__balans = balans  # Приватный атрибут
        self.__pasport = passport  # Приватный атрибут

    def public_print(self):
        """метод предоставления данных для экземпляра класса через вызов приватной функции"""
        return f'{self.__print_privat()}'

    def __print_privat(self):
        """метод, который обращается к приватным атрибутам"""
        return f'{self.__name}, {self.__balans}, {self.__pasport}'

    def get_balans(self):
        """вывод баланса"""
        return f'{self.__balans}'
    def set_balans(self, new_balans):
        """изменение баланса"""
        if not isinstance(new_balans, int):
            raise ValueError('Новый баланс должен быть целым числом')
        self.__balans = new_balans
        return f'баланс равен {self.__balans}'

new_peopl = Banc_acc('Jorik', 100, 1415181910)
print(new_peopl.get_balans())

class Banc_acc:
    def __init__(self, name, balans, passport):
        self.__name = name  # Приватный атрибут
        self.__balans = balans  # Приватный атрибут
        self.__pasport = passport  # Приватный атрибут

    def public_print(self):
        """метод предоставления данных для экземпляра класса через вызов приватной функции"""
        return f'{self.__print_privat()}'

    def __print_privat(self):
        """метод, который обращается к приватным атрибутам"""
        return f'{self.__name}, {self.__balans}, {self.__pasport}'

    def get_balans(self):
        """вывод баланса"""
        return f'{self.__balans}'
    def set_balans(self, new_balans):
        """изменение баланса"""
        if not isinstance(new_balans, int):
            raise ValueError('Новый баланс должен быть целым числом')
        self.__balans = new_balans
        return f'баланс равен {self.__balans}'
    def del_balans(self):
        del self.__balans

    balance = property(fget=get_balans, fset=set_balans, fdel=del_balans)

a = Banc_acc('Ilya', 250000, 1814252728)
c = Banc_acc('Jorik', 100, 1415181910)

a.balance = 400
print(a.balance)
print(c.balance)
del a.balance
try:
    print(a.balance)
except Exception as e:
    print(f'была ошибка {e}')

print(f'вывел {c.balance}')


class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
    @property
    def sise(self):
        print('сработал геттер')
        return self.__side

    @sise.setter
    def sise(self, new_side):
        self.__side = new_side
        print('сработал сеттер')
        self.__area = None
        return f'размер стороны куба изменён на {self.__side}'


    @property
    def area(self):
        if self.__area is None:
            area = self.__side**2
            return f'площадь куба = {area}'

a = Square(5)

a.sise = 6
a.sise
print(a.area)
print(a.sise)



