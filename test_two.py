# Задания
# 	1.	Объяснить, почему так происходит.
# 	2.	Исправить функцию, чтобы каждый вызов без cart создавал новый список.
# 	3.	Добавить тестовый кейс: передать свою корзину cart=["x"] и убедиться, что она изменяется только там.

# Ожидаемо: a и b должны быть независимыми.
def add_item(cart=None, item="apple"):
    if cart is None:
        cart = []

    cart.append(item)

    return cart


a = add_item(item="milk")
b = add_item(item="bread")
c = add_item(cart=['aple'], item='bread')
print("a:", a)
print("b:", b)
print(c)


# 1.	Написать функцию build_stats(events) -> dict, которая вернёт:
# 	•	by_action: сколько раз встречалась каждая action
# 	•	by_user: сколько событий у каждого user
# 	2.	Битые события (без action или user) не падать, а:
# 	•	считать в отдельный счётчик invalid
# 	3.	Запрещено использовать collections.Counter (чтобы прокачать dict).


def build_stats(events: list):
    invalid = 0
    answer = {
        # мы храним имя user и его количество
        'by_user': {},
        'by_action': {},
        'invalid': 0
    }
    by_action = {}
    by_user = {}
    for event in events:
        if "user" not in event or 'action' not in event:
            answer['invalid'] += 1
            continue
        a = event['user']
        b = event['action']

        if a in answer['by_user']:
            answer['by_user'][a] += 1
        else:
            answer['by_user'][a] = 1

        if b in answer['by_action']:
            answer['by_action'][b] += 1
        else:
            answer['by_action'][b] = 1
    return answer  # Нужно вернуть словарик
    # проверил вроде работает


# можно короче
#         else:
#             by_action[action] = by_action.get(action, 0) + 1
#             by_user[user] = by_user.get(user, 0) + 1

events = [
    {"user": "u1", "action": "click"},
    {"user": "u2", "action": "view"},
    {"user": "u1", "action": "click"},
    {"user": "u1", "action": "buy"},
    {"user": "u2", "action": "click"},
    {"user": "u3"},  # action отсутствует (битые данные)
]

# Написать декоратор @trace, который:
# 	1.	Печатает: имя функции, аргументы (аккуратно), время выполнения в мс.
# 	2.	Если функция завершилась успешно — печатает OK и короткий результат:
# 	    •	если результат str/int/float/bool/None — печатать полностью
# 	    •	иначе печатать type(result).__name__
# 	3.	Если упало исключение — печатает ERROR: <exc> и пробрасывает исключение дальше

import time


def trace(funck):
    def wrapper(*args, **kwargs):
        print(f'имя функции: {funck.__name__}')

        start_time = time.perf_counter()
        answer_arg = []

        for arg in args:
            answer_arg.append(str(arg))
        if len(answer_arg) > 0:
            print(f'Позиционные аргументы: {' | '.join(answer_arg)}')

        answer_kwargs = []
        for key, value in kwargs.items():
            answer_kwargs.append(f"{key}={value}")
        if len(kwargs) > 0:
            print(f'Именованные аргументы: {' | '.join(answer_kwargs)}')

        try:
            work_funk = funck(*args, **kwargs)
            if isinstance(work_funk, (str, int, float, bool, type(None))):
                print(f'ОК, результат = {work_funk}')
            else:
                print(f'ОК, результат = {type(work_funk).__name__}')
            end_time = time.perf_counter()
            # в секунде 1000 миллисикунд
            work_time = (end_time - start_time) * 1000
            print(f'Время выполнения в мс: {work_time:.2f}')
            return work_funk

        except Exception as e:
            end_time = time.perf_counter()
            work_time = (end_time - start_time) * 1000
            print(f'ERROR: <{type(e).__name__}> работал {work_time:.2f} ms')

            raise

    return wrapper


@trace
def slow_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s


@trace
def boom():
    raise ValueError("bad input")


print(f'тест 1')
slow_sum(100000)
print(f'test 2 ')
boom()


# Задания
# 	1.	Найти минимум 2 проблемы в дизайне/логике (подсказка: поведение по умолчанию + ожидаемая фильтрация).
# 	2.	Исправить: если cities не задан — фильтровать только по возрасту, без ограничения по городу.
# 	3.	Сделать функцию устойчивой к отсутствию ключей ("age", "city") — такие записи пропускать, не падать.

# Проблемы что при инициации создавали список и он в дальнейшем наполнялся, и исходя из 3 задания не учитывали
# что значение может остутствовать и код падал. это всё что я нашёл :)
def filter_users(users, min_age=18, cities=None):
    result = []
    for user in users:
        age = user.get("age")
        if age is None or not isinstance(age, int):
            continue

        if age < min_age:
            continue

        if cities is not None:
            city = user.get("city")
            if city is None or city not in cities:
                continue

        result.append(user)

    return result
