"""
== - сравнение по ЗНАЧЕНИЮ (value equality)
is - сравнение по ПАМЯТИ (identity/object equality)
"""
import asyncio

"по ЗНАЧЕНИЮ"
# Сравниваем, равны ли значения
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True - списки содержат одинаковые элементы

c = 1000
d = 1000
print(c == d)  # True - числа равны
async def fetch_data():
    pass

# В асинхронном коде:
async def compare_results():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())

    res1 = await task1  # "данные"
    res2 = await task2  # "данные"

    print(res1 == res2)  # True - значения одинаковые


"по ПАМЯТИ"
# Проверяем, указывают ли переменные на ОДИН объект в памяти
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False - разные объекты в памяти!

# А вот здесь - один объект
x = [1, 2, 3]
y = x  # y ссылается на тот же список
print(x is y)  # True - это один и тот же объект!

async def some_fn():
    pass

# В асинхронном коде:
async def check_task_identity():
    task1 = asyncio.create_task(some_fn())
    task2 = task1  # task2 ссылается на ту же задачу

    print(task1 is task2)  # True - это один объект Task

    task3 = asyncio.create_task(some_fn())
    print(task1 is task3)  # False - разные задачи

