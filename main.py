import asyncio


async def get_user_from_db():
    pass # asyncio.sleep(5)

async def get_orders_from_api():
    pass # asyncio.sleep(5)

async def main():
    # тут мы сообщаем что будем решать задачу у которой есть простой время которого можно использовать для другой работы
    task = asyncio.create_task(get_user_from_db())
    task2 = asyncio.create_task(get_orders_from_api())

    # после должны вызвать дабы не потерять результат
    result = await task
    result2 = await task2

    return f'Результаты тасков:\n1 {result}\n{result2}'