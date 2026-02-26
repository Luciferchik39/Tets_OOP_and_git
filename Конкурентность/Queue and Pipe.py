from multiprocessing import Process, Queue
from queue import Empty
from time import sleep

"""
Queue — структура данных для обмена информацией между 
процессами по принципу FIFO (First In, First Out — "первым пришёл, первым ушёл") представляет из себя ОЧЕРЕДЬ.
Метод	Описание
q.put(item)	Добавляет элемент в очередь
q.get()	Извлекает и возвращает элемент из очереди (блокируется, если очередь пуста)
q.get(timeout=n)	Ждёт элемент n секунд, затем вызывает исключение queue.Empty     !!!!!! (важно иначе можем зависнуть на вечно)
q.empty()	Проверяет, пуста ли очередь (не всегда надёжно в многопроцессности)
q.qsize()	Возвращает приблизительный размер очереди
q.task_done()	Сигнализирует, что обработка элемента завершена (используется с q.join())
q.join()	Блокируется, пока не будут обработаны все элементы


queue.Queue — только для потоков (threads)
multiprocessing.Queue — для процессов (processes)
Pipe — более быстрая, но только для двух процессов
SimpleQueue — упрощённая версия Queue (без task_done и join)
"""

def worker(a:int, q:Queue):
    cnt = 0
    while cnt < 3:
        sleep(.1)
        q.put(cnt)
        cnt += 1
        print('worker, выполняется')

def worker_2(a:int, q: Queue):
    cnt = 0

    while cnt < 4:
        sleep(.1)
        cnt += 1
        value_from_queue = q.get(timeout=1)
        new_int = (cnt + 1) ** 2
        print(f'new_worker спёр из очереди: {value_from_queue} и положит туда {new_int}')
        q.put(new_int)

if __name__ == '__main__':
    q = Queue()
    arg_value = 5
    p_1 = Process(target=worker, args=(arg_value, q))
    p_2 = Process(target=worker_2, args=(2, q))
    p_1.start()
    p_2.start()
    sleep(1) # даём время дочерним процессам сработать иначе могла быть ситуация что при попытке получения информации в воркер 2 в очереди уже было пусто
    try:
        for _ in range(arg_value):
            print(q.get(timeout=1))
    except Empty as e:
        print(f'Отловили Empty q со значением {e}')
    p_2.join()
    p_1.join()


