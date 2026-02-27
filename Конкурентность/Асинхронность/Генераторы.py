from time import time
import socket


# def gen_filename():
#     while True:
#         patter = 'file-{}.jpeg'
#         t = int(time() * 1000)
#         yield patter.format(str(t))
#
# g = gen_filename()
# print(next(g))
#
# def geb():
#     yield [1, 2, 3, 4, 5]
#     print('какаято работа между генераторами')
#     yield (1, 2, 3, 4, 5)
# a = geb()
# print(a)
# print(next(a))
# print(next(a))
# #print(next(a))
# """
# Round Robin (карусель)
# объекты в очереди после выполнения работы возврщаются в конец очереди
# """
#
# def gen1(n:str):
#     for i in n:
#         yield i
#
# def gen2(n:int):
#     for i in range(n):
#         yield i
#
# g1 = gen1('Илья')
# g2 = gen2(4)
# tasks = [g1, g2]
#
# while tasks:
#     task = tasks.pop(0)
#
#     try:
#         i = next(task)
#         print(i)
#         tasks.append(task)
#
#     except StopIteration:
#         print('Итератор закончился')


def server():
    # Создаем TCP сокет (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Опция REUSEADDR позволяет переиспользовать порт после перезапуска
    # 1 = True/включить опцию
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Привязываем сокет к адресу localhost и порту 5001
    server_socket.bind(('localhost', 5001))

    # Переводим сокет в режим прослушивания (макс. очередь соединений - стандарт)
    server_socket.listen()

    while True:  # Бесконечный цикл работы сервера
        # Говорим планировщику: "Хочу прочитать из server_socket"
        # Возвращаем управление планировщику до появления соединения
        yield ('read', server_socket)

        # Когда есть входящее соединение, планировщик вернет управление сюда
        # accept() принимает соединение и возвращает (клиентский сокет, адрес клиента)
        client_socket, addr = server_socket.accept()

        print("Соединение ", addr)

        # Создаем генератор для работы с конкретным клиентом
        client_gen = client(client_socket)

        # Запускаем клиентский генератор
        try:
            while True:
                # Получаем следующую команду от клиентского генератора
                # и передаем её планировщику
                yield next(client_gen)
        except StopIteration:
            # Клиентский генератор закончил работу
            pass


def client(client_socket):  # Принимаем сокет конкретного клиента
    while True:  # Цикл обработки одного клиента
        # Говорим планировщику: "Хочу прочитать данные от клиента"
        yield ('read', client_socket)

        # Пытаемся прочитать до 4094 байт от клиента
        request = client_socket.recv(4094)

        if not request:  # Если данных нет - клиент закрыл соединение
            break
        else:
            response = 'Hello world\n'.encode()  # Готовим ответ
            # Говорим планировщику: "Хочу записать данные клиенту"
            yield ('write', client_socket)
            client_socket.send(response)  # Отправляем ответ

    client_socket.close()  # Закрываем соединение с клиентом


import select  # Для мониторинга готовности сокетов


def scheduler(generators):
    # Словари для хранения генераторов, ожидающих чтения/записи
    # Ключ - сокет, значение - генератор
    read_wait = {}
    write_wait = {}

    # Главный цикл планировщика - работает пока есть активные генераторы
    while generators:
        # Убираем завершенные генераторы
        # generators - список активных генераторов, готовых к работе
        generators = [g for g in generators if g]

        # Проходим по всем активным генераторам
        for gen in generators[:]:  # [:] создает копию, чтобы можно было изменять оригинал
            try:
                # Запрашиваем у генератора следующую команду
                # Каждый генератор должен yield ('read', сокет) или ('write', сокет)
                cmd, sock = next(gen)

                # Распределяем генераторы по словарям ожидания
                if cmd == 'read':
                    read_wait[sock] = gen  # Генератор ждет чтения
                elif cmd == 'write':
                    write_wait[sock] = gen  # Генератор ждет записи

            except StopIteration:
                # Генератор завершил работу (дошел до конца или выполнил return)
                # Удаляем его из списка активных
                generators.remove(gen)

        # Ждем события на сокетах
        if read_wait or write_wait:  # Если есть хоть один ожидающий генератор
            # select возвращает списки сокетов, готовых к операциям
            readable, writable, _ = select.select(
                list(read_wait.keys()),  # Сокеты, которые мы хотим читать
                list(write_wait.keys()),  # Сокеты, в которые мы хотим писать
                []  # Игнорируем исключительные ситуации
            )

            # Для каждого готового к чтению сокета
            for sock in readable:
                # Достаем генератор из словаря ожидания
                gen = read_wait.pop(sock)
                # Добавляем его обратно в активные (он теперь может работать)
                generators.append(gen)

            # Для каждого готового к записи сокета
            for sock in writable:
                # Достаем генератор из словаря ожидания
                gen = write_wait.pop(sock)
                # Добавляем его обратно в активные
                generators.append(gen)


# Запуск сервера
if __name__ == '__main__':
    # Создаем генератор сервера
    server_gen = server()
    # Запускаем планировщик с одним серверным генератором
    scheduler([server_gen])


