"""
более легковесные в сравнение с процессами
используют общее адрессное пространство
в Однин момент времени используется один ПОТОК


Расходы со стороны ОС
необходимо синхронизировать потоки
увеличение сложности программы
возможный ГОЛОД потока при долгом отсутствии ресурсов

Используются в
I/O боунд задачах

"""

import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from time import sleep
import threading
import os
from datetime import datetime


CNT = 0
"""
Тип задачи	                        Что использовать	                        Почему
CPU-bound (вычисления)	        ProcessPoolExecutor или multiprocessing	   Обходим GIL, используем все ядра
I/O-bound (сеть, диск)	        ThreadPoolExecutor или threading	       Мало накладных расходов, эффективно при ожидании
Смешанные	Комбинировать	Например, пул процессов для вычислений, пул потоков для I/O
"""
def new_funck():
    "имитация I/O bound"
    print(f'Это поток {threading.get_ident()} из процесса PID: {os.getpid()}')
    time.sleep(1)

def heavy_funk():
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1
    print(f'Это поток {threading.get_ident()} из процесса PID: {os.getpid()}')
    return cnt
start = datetime.now()
new_funck()
new_funck()
new_funck()
"""создаём потоки"""
thred = Thread(target=new_funck)
thred2 = Thread(target=new_funck)
thred3 = Thread(target=new_funck)
"""запускаем через старт"""
thred.start()
thred2.start()
thred3.start()
"""ждём их реализации"""
thred.join()
thred2.join()
thred3.join()
a = heavy_funk()
print(a) # 2 секунды работы
""" работа с вычислениясми"""
with ThreadPoolExecutor(max_workers=3) as thread: # пул потоков
    [thread.submit(heavy_funk) for _ in range(3)] # 7 секунда работы так как каждый поток попеременно работал с вычислениями



print(f'Время работы процесса: {datetime.now() - start}')


