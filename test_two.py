# Задания
# 	1.	Найти минимум 2 проблемы в дизайне/логике (подсказка: поведение по умолчанию + ожидаемая фильтрация).
# 	2.	Исправить: если cities не задан — фильтровать только по возрасту, без ограничения по городу.
# 	3.	Сделать функцию устойчивой к отсутствию ключей ("age", "city") — такие записи пропускать, не падать.

def filter_users(users, min_age=18, cities=None):
    result = []
    for user in users:
        age = user.get("age")
        if age is None or not isinstance(age, (int)):
            continue

        if age < min_age:
            continue

        if cities is not None:
            city = user.get("city")
            if city is None or city not in cities:
                continue

        result.append(user)

    return result


users = [
    {"name": "Ann", "age": 20, "city": "Berlin"},
    {"name": "Bob", "age": 17, "city": "Paris"},
    {"name": "Eve", "age": 22, "city": "Rome"},
]
print(filter_users(users, cities=["Berlin"]))
print(filter_users(users))