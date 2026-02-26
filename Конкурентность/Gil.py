
"""
 ========================================     GIL (Global Interpreter Lock) — это глобальная блокировка интерпретатора.
 Простыми словами, это механизм, который используется в эталонной реализации Python (CPython) и гарантирует, 
 что в любой момент времени выполняется только один поток . Представьте себе узкую дверь, через которую может 
 пройти только один человек за раз. Даже если у вас есть огромный зал (многоядерный процессор) и много людей (потоков), 
 одновременно работать сможет только один.
 
 
========================================     GIL освобождается в трех случаях:
Достижение лимита "тиков" (принудительное переключение)
Блокирующая операция I/O (добровольное освобождение)
C-расширение явно освобождает GIL (например, NumPy)


========================================     Без GIL два потока, одновременно изменяющие счетчик ссылок, могут вызвать race condition. 
Счетчик может быть:
Увеличен только один раз вместо двух
Поврежден (стать некорректным)
Привести к преждевременному освобождению памяти
GIL защищает от этой проблемы, делая операции со счетчиками атомарными.

========================================     Изменения GIL в Python 3.2:
Замена счетчика тиков на таймер (5 мс)
Решена проблема "голодания" потоков
Более справедливое распределение времени CPU

========================================     GIL-дружественное программирование
Это подход, который учитывает GIL:
Для CPU-bound → multiprocessing
Для I/O-bound → threading или asyncio
Минимизация времени удержания GIL в потоках
Использование C-расширений для тяжелых вычислений

========================================     Потоки Python и нативные потоки
Каждый Python-поток (threading) — это обертка над нативным потоком ОС. Разница:
Нативных потоков может быть много, но GIL разрешает выполнять Python-код только одному
Нативные потоки все равно существуют и могут выполняться параллельно, если они не выполняют Python-код (например, системные вызовы)


========================================     Заключение
Итак, резюмируем:
GIL — это "необходимое зло" CPython, упрощающее внутреннее устройство интерпретатора и делающее его более безопасным.
Мы не вызываем его напрямую, но всегда должны помнить о его существовании при написании многопоточного кода.
Ключевое правило:
I/O-bound задачи -> используем потоки (threading).
CPU-bound задачи -> используем процессы (multiprocessing) или специализированные библиотеки (NumPy и т.д.).
Надеюсь, теперь картина стала более ясной. Если у вас появятся новые вопросы в ходе экспериментов — смело задавайте!
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import threading
import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def download_site():
    print(f"Поток {threading.current_thread().name}: Начинаю запрос")
    response = requests.get('https://google.com', verify=False)  # ⚠️ ЗДЕСЬ ПРОИСХОДИТ БЛОКИРОВКА I/O запроса до ожидания и Gil освобождается
    print(f"Поток {threading.current_thread().name}: Получил ответ")
    return response.content

# Создаем потоки
start = time.time()
threads = []
for i in range(4):
    t = threading.Thread(target=download_site)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print(f"Время: {time.time() - start}")

def func_download(url):
    try:
        print(f'Поток {threading.get_ident()} начинает работу с url: {url}')
        response = requests.get(url, timeout=5, verify=False)
        # response.content содержит байты
        html_bytes = len(response.content)
        print(f'Поток {threading.get_ident()} загрузил {url} его вес {html_bytes}байт')
        return html_bytes
    except Exception as err:
        print(f'В потоке {threading.get_ident()} возникла ошибка {err}')


if __name__ =='__main__':
    start = datetime.now()
    total_bytes = 0
    urls = ['https://google.com',
            'https://httpbin.org/delay/2',
            'https://python.org',
            'https://github.com',
            'https://stackoverflow.com'
            ]
    # map() применяет функцию ко всем url и возвращает результаты в том же порядке
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(func_download, urls)

        # results - это итератор с результатами
        # total_bytes = sum(results)

        # Можно и поэлементно:
        for url, bytes_count in zip(urls, results):
            print(f"{url}: {bytes_count} байт")
            total_bytes += bytes_count

    print(f"Всего загружено: {total_bytes} байт")
    print(f'Общее время: {datetime.now() - start}')




