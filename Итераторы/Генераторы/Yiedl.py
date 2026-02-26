"""
a = yield 1
И так объект yield возвращает generator object в котором находится информация
при передачи его в next() мы запускаем получение объекта из generator object в нашем случае 1
"""
from datetime import datetime
import sys


def func(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res

def new_fn():
    yield 1

print(func)
print(new_fn)
print(func(1))
print(new_fn()) # <generator object new_fn at 0x0000028D9CB79F30> в самом generator object находится

def yield_fn(b):
    """ """
    cnt = 0
    while cnt < b:
        yield cnt
        cnt += 1


c = yield_fn(10)
print("!!!!!")
print(c) # тут сейчас находится generator object который содержит в себе элемент первого прохода а именно 0
print(next(c)) # тут просим next получить обхект который содержится в generator object
print(next(c))

start = datetime.now()
print('start fun')
# d = yield_fn(100_000_000)
l = func(100_000_000)
print(f'размер объекта равен {sys.getsizeof(l)}')
print(f'завершение кода {datetime.now()}. Время работы функции {datetime.now() - start}')
