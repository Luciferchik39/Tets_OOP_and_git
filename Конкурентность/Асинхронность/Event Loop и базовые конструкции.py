"""
Event Loop — это менеджер, который постоянно крутится в бесконечном цикле и отвечает на два главных вопроса:
"Какие задачи готовы к выполнению?"
"Какие задачи ждут каких-то событий?"


"""

# Упрощенная схема работы event loop
# while True:
    # 1. Берем задачу из очереди готовых к выполнению
    # task = get_next_task()
    #
    # # 2. Выполняем задачу до первого await
    # result = task.run()

    # 3. Если задача завершилась - убираем
    # 4. Если задача наткнулась на await - отправляем спать
    # 5. Возвращаемся к шагу 1

"=====================    1. async def - Объявление корутины"
# Обычная функция
def regular_function():
    return "обычный результат"

# Асинхронная функция (корутина)
async def async_function():
    return "асинхронный результат"

# В чем разница?
regular_function()  # → сразу возвращает строку
async_function()    # → возвращает объект корутины, НЕ результат!
# <coroutine object async_function at 0x...>

"=====================     await - Ожидание результата"


async def example():
    # Правильно:
    result = await async_function()
    print(result)  # "асинхронный результат"

    # Ошибка! Нельзя await без async
    # result = await regular_function()  # TypeError!

    # Ошибка! Нельзя использовать await вне async функции
    # await asyncio.sleep(1)

"=====================    asyncio.run() - Запуск главной корутины"
import asyncio


async def main():
    await asyncio.sleep(1)
    return "Готово!"

# ЕДИНСТВЕННЫЙ правильный способ запуска:
result = asyncio.run(main())
print(result)  # "Готово!"

# Чего НЕЛЬЗЯ делать:
# asyncio.run(main())  # Нельзя запустить дважды в одном потоке!
# asyncio.run(main())  # RuntimeError: event loop already running

# Нельзя вызвать корутину напрямую:
# main()  # Просто создаст корутину, но не выполнит!

"=====================    asyncio.sleep() - Неблокирующая пауза"

import time


async def show_sleep_difference():
    print(f"Старт: {time.strftime('%X')}")

    # Асинхронный sleep - НЕ блокирует поток
    await asyncio.sleep(2)

    print(f"После async sleep: {time.strftime('%X')}")

    # Обычный sleep - БЛОКИРУЕТ поток!
    time.sleep(2)

    print(f"После обычного sleep: {time.strftime('%X')}")


asyncio.run(show_sleep_difference())


# Это корутина (async функция)
async def cook_pasta(name, minutes):
    """
    Функция приготовления пасты
    """
    print(f"  Начинаю варить {name} в {time.strftime('%M:%S')}")

    # await - говорим event loop'у: "я буду ждать, делай другие дела"
    await asyncio.sleep(minutes * 60)  # Неблокирующее ожидание

    print(f"  {name} готова в {time.strftime('%M:%S')}")
    return f"{name} сварилась"


async def main():
    """
    Главная корутина
    """
    print(f"Запуск приготовления в {time.strftime('%M:%S')}")

    # Создаем задачи (о них позже)
    task1 = asyncio.create_task(cook_pasta("Спагетти", .5))
    task2 = asyncio.create_task(cook_pasta("Пенне", .3))

    print("Ждем готовности...")

    # Ждем результаты
    result1 = await task1 # await не переходит к следующей строке автоматом, а приостанавливает текущую корутину(функцию)
    result2 = await task2

    print(f"Результаты: {result1}, {result2}")
    print(f"Всё готово в {time.strftime('%M:%S')}")


# Единственный правильный способ запуска
if __name__ == "__main__":
    asyncio.run(main())
