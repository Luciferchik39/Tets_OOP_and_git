import asyncio
import time
from datetime import datetime

# async def my_corutina(name, t: float):
#     start = datetime.now()
#     print(f'начало работы корутины в {start.strftime("%X")}')
#     await asyncio.sleep(t)
#     print(f'корутина с name = {name} звершила действие в {start.strftime("%X")}, а всего корутина работала {datetime.now() - start}')
#     return "Результат my_corutina"
#
# async def main():
#     print("Запуск исполняемой функции")
#
#     task = asyncio.create_task(my_corutina('Анастасия', 8))
#     task2 = asyncio.create_task(my_corutina('Илья', 4))
#     # gather сам создаст задачи и вернет список результатов
#     result = await asyncio.gather(task, task2)
#     return result
#
# if __name__ == '__main__':
#     # print(main()) косяк
#     result = asyncio.run(main())
#     print(result)





# async def main():
#     start_time = time.time()
#
#     # Создаем задачи (они уже начали выполняться в фоне!)
#     task1 = asyncio.create_task(my_coroutine("A", 6))
#     task2 = asyncio.create_task(my_coroutine("B", 2))
#
#     print("Задачи созданы, теперь ждем их...")
#
#     # Ждем завершения ВСЕХ задач
#     res1 = await task1
#     print("А вот и я, main проснулся! Проверю-ка task2")
#     res2 = await task2
#
#     print(f"Результаты: {res1}, {res2}")
#     print(f"Общее время: {time.time() - start_time:.2f} секунд")

import asyncio
from datetime import datetime


async def my_coroutine(name, sleep_time):
    print(f"{name}: начал работу в {datetime.now().strftime('%H:%M:%S')}")
    try:
        await asyncio.sleep(sleep_time)
        print(f"{name}: закончил работу в {datetime.now().strftime('%H:%M:%S')}")
        return f"Привет от {name}"
    except asyncio.CancelledError:
        print(f"{name}: меня прервали!")
        raise


async def new_main():
    start = datetime.now()
    err_list = []

    try:
        # ВАЖНО: await + return_exceptions=True
        async with asyncio.timeout(5):
            results = await asyncio.gather(  # <-- Добавил await!
                my_coroutine('Илья', 4),
                my_coroutine('Анастасия', 2),
                my_coroutine('Пупок', 7),
                return_exceptions=True  # Все исключения станут результатами
            )

            # Теперь анализируем результаты
            for i, res in enumerate(results):
                if isinstance(res, Exception):
                    print(f"Задача {i} упала или была отменена: {type(res).__name__}")
                    err_list.append(f"Ошибка в задаче {i}: {res}")
                else:
                    print(f"Задача {i} успешно выполнена: {res}")

            return results

    except asyncio.TimeoutError:
        # Сюда мы попадем ТОЛЬКО если timeout сработал ДО gather
        # Но при return_exceptions=True timeout не кинет исключение внутри gather
        print("Таймаут! Но мы уже вышли из контекста")
        return None
    finally:
        print(f'Блок try завершен, время работы {datetime.now() - start}')
        if err_list:
            print(f"Были ошибки: {err_list}")


if __name__ == '__main__':
    res = asyncio.run(new_main())
    print(f"Финальный результат: {res}")