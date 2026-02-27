"""
Чтобы объект можно было использовать в async for, он должен реализовать:

1. __aiter__ должен вернуть объект с __anext__
2. __anext__ кидает StopAsyncIteration в конце
3. __aenter__ возвращает ресурс
4. __aexit__ принимает параметры исключений
5. async for сам вызывает __anext__ и ловит StopAsyncIteration
6. async with гарантирует вызов __aexit__ даже при ошибке
"""
import asyncio


async def my_async_gen(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i

async def main():
    a = my_async_gen(int(input()))
    async for i in a:
        if i == 4:
            continue
        print(i)


class AsyncCounter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.max_count:
            await asyncio.sleep(0.5)
            self.count += 1
            return self.count

        raise StopAsyncIteration

class DatabaseConnection:

    async def __aenter__(self):
        print('Подключаюсь к БД..')
        await asyncio.sleep(1)
        print('Подключено')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('Закрываю соединение...')
        await asyncio.sleep(1)
        print('Закрыто')

class AsyncFileReader:
    def __init__(self, filename, delay):
        self.delay = delay
        self.filename = filename
        self.list_imit = ["строка1", "строка2", "строка3"]
        self.count = -1
        self.max_count = len(self.list_imit)

    async def __aenter__(self):
        print(f'открыл фаили {self.filename}')
        await asyncio.sleep(self.delay)
        return self


    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.max_count - 1:
            await asyncio.sleep(self.delay)
            self.count += 1
            return self.list_imit[self.count]
        raise StopAsyncIteration

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываю фаили {self.filename}')
        await asyncio.sleep(1)
        print('Закрыто')

async def my_main_2():
    async with AsyncFileReader('text.txt', .5) as file:
        async for line in file:
            print(line)



async def my_main():
    async with DatabaseConnection() as conn:
        await asyncio.sleep(2)





if __name__ == '__main__':
#    asyncio.run(main())
    #asyncio.run(my_main())
    asyncio.run(my_main_2())

