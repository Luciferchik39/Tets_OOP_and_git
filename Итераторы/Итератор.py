"""
Итерируемый объект и перебиратор(итератор)

Итерируемый объект - Это объект, который может предоставить итератор. У него есть метод __iter__(), который возвращает новый итератор.
Это объект, который одновременно имеет:
__iter__() - возвращает сам себя
__next__() - возвращает следующий элемент или выбрасывает StopIteration

ИТЕРИРУЕМЫЙ (Iterable)              ИТЕРАТОР (Iterator)
    |                                      |
    |-- Есть __iter__()                    |-- Есть __iter__() (возвращает себя)
    |-- НЕТ __next__()                      |-- Есть __next__()
    |-- Может создавать итераторы           |-- Можно использовать в next()
    |                                       |-- Одноразовый
    |
    |-- Примеры:                            |-- Примеры:
        list, tuple, str, dict, set, range      list_iterator,
        file objects                             generator object,
                                                  zip object,
                                                  enumerate object

"""
from collections.abc import Iterable, Iterator

def check_obj(obj, name):
    print(name)
    print(f'объект {obj}')
    print(f'объект имеет __iter__() {hasattr(obj, '__iter__')}')
    print(f'объект имеет __next__() {hasattr(obj, '__next__')}')
    print(f'объект относится к Iterable {isinstance(obj, Iterable)}')
    print(f'объект относится к Iterator {isinstance(obj, Iterator)}')

a = check_obj('Илья', 'str')
print(a)
print('=================')

tumb = ['яблоко', 'ручка', ' расчёстка', 'книга'] # перебираемы объект
a = iter(tumb) # получил итератор из списка (список создал итератор)
print(check_obj(a, 'объект iter(tumb)'))


# Итерируемый объект (фабрика)
my_list = [1, 2, 3]  # Можно создавать новые итераторы снова и снова

# Первый итератор
iter1 = iter(my_list)
print("Первый проход:", list(iter1))  # [1, 2, 3] - проработали все элементы

# iter1 теперь пуст! Но мы можем создать новый:
iter2 = iter(my_list)  # Создаем НОВЫЙ итератор из той же фабрики
print("Второй проход:", list(iter2))  # [1, 2, 3] - снова работает!
