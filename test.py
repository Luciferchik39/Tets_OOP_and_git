# # def validate_order(order, allowed_cities):
# #     # возможные ошибки
# #     errors = []
# #
# #     list_validate = ["customer_id", "city", "payment_method", "items", "promo_code"]
# #     for i in list_validate:
# #         if i not in order:
# #             errors.append(f"Отсутствует обязательное поле: {i}")
# #             return errors
# #     if errors: return False, errors
# #
# #     if not isinstance(order["customer_id"], str) or not order["customer_id"].strip():
# #         errors.append('поле customer_id должно быть не пустой строкой')
# #
# #     if not isinstance(order['city'], str):
# #         errors.append(f'поле city должно быть строкой')
# #     elif order['city'] not in allowed_cities:
# #         errors.append(f'в этот город не добавляем')
# #     if not isinstance(order['payment_method'], str):
# #         errors.append(f'поле payment_method должно быть строкой')
# #     if order['promo_code'] is not None and not isinstance(order['promo_code'], str):
# #         errors.append('поле promo_code должно быть или None или строкой')
# #     if not isinstance(order['items'], list) and len(order["items"]) == 0:
# #         errors.append('поле items должно быть непустым списком')
# #     else:
# #         items_list = ["sku", "name", "price", "qty", "category"]
# #         for index, item in enumerate(order["items"]):
# #             for field in items_list:
# #                 if field not in item:
# #                     errors.append(f'отсутвует поле {field} в товаре')
# #
# #             sku = item['sku']
# #             name = item['name']
# #             price = item['price']
# #             qty = item['qty']
# #             category = item['category']
# #
# #             if not isinstance(sku, str):
# #                 errors.append(f'код {sku} товара должен быть в виде строки')
# #             if not isinstance(name, str):
# #                 errors.append(f'Наименование товара {name} товара должен быть в виде строки')
# #             if not isinstance(price, int) or price <= 0:
# #                 errors.append(f'Цена товара должны быть целым положительным числом')
# #             if not isinstance(price, int) or price <= 0:
# #                 errors.append(f'Цена товара должны быть целым положительным числом')
# #             if not isinstance(qty, int) or qty <= 0:
# #                 errors.append(f'Количесвто товара не должно быть меньше одного')
# #             if not isinstance(category, str):
# #                 errors.append(f'Категория товара должны быть строкой')
# #             if errors:
# #                 return False, errors
# #
# #     return errors
# #
# #
# # order = {
# #         "customer_id": "CUST-001",
# #         "city": "Berlin",
# #         "payment_method": "card",
# #         "promo_code": "SAVE10",
# #         "items": [
# #             {"sku": "A1", "name": "Bread", "price": 2500, "qty": 2, "category": "food"},
# #             {"sku": "B7", "name": "Book", "price": 4000, "qty": 1, "category": "books"},
# #         ],
# #     }
# #
# # allowed_cities = ['Berlin']
# #
# # print(validate_order(order, allowed_cities))
#
#
# # Написать декоратор @trace, который:
# # 	1.	Печатает: имя функции, аргументы (аккуратно), время выполнения в мс.
# # 	2.	Если функция завершилась успешно — печатает OK и короткий результат:
# # 	    •	если результат str/int/float/bool/None — печатать полностью
# # 	    •	иначе печатать type(result).__name__
# # 	3.	Если упало исключение — печатает ERROR: <exc> и пробрасывает исключение дальше
#
#
# import time
# def trace(funck):
#     def wrapper(*args, **kwargs):
#         print(f'имя функции: {funck.__name__}')
#
#         start_time = time.perf_counter()
#         answer_arg = []
#
#         for arg in args:
#             answer_arg.append(str(arg))
#         if len(answer_arg) > 0:
#             print(f'Позиционные аргументы: {' | '.join(answer_arg)}')
#
#         answer_kwargs = []
#         for key, value in kwargs.items():
#             answer_kwargs.append(f"{key}={value}")
#         if len(kwargs) > 0:
#             print(f'Именованные аргументы: {' | '.join(answer_kwargs)}')
#
#         try:
#             work_funk = funck(*args, **kwargs)
#             if isinstance(work_funk, (str, int, float, bool, type(None))):
#                 print(f'ОК, результат = {work_funk}')
#             else:
#                 print(f'ОК, результат = {type(work_funk).__name__}')
#             end_time = time.perf_counter()
#             # в секунде 1000 миллисикунд
#             work_time = (end_time - start_time) * 1000
#             print(f'Время выполнения в мс: {work_time:.2f}')
#             return work_funk
#
#         except Exception as e:
#             end_time = time.perf_counter()
#             work_time = (end_time - start_time) * 1000
#             print(f'ERROR: <{type(e).__name__}> работал {work_time:.2f} ms')
#
#             raise
#
#     return wrapper
#
#
#
#
#
# @trace
# def slow_sum(n):
#     s = 0
#     for i in range(n):
#         s += i
#     return s
#
# @trace
# def boom():
#     raise ValueError("bad input")
# print(f'тест 1')
# slow_sum(100000)
# print(f'test 2 ')
# boom()

# Задания
# 	1.	Найти минимум 2 проблемы в дизайне/логике (подсказка: поведение по умолчанию + ожидаемая фильтрация).
# 	2.	Исправить: если cities не задан — фильтровать только по возрасту, без ограничения по городу.
# 	3.	Сделать функцию устойчивой к отсутствию ключей ("age", "city") — такие записи пропускать, не падать.


def filter_users(users, min_age=18, cities=None):
    result = []
    for user in users:
        user_age = user.get('age')
        if user_age is None or not isinstance(user_age, int):
            continue
        if user_age < min_age:
            continue
        if cities is not None:
            city = user.get('city')
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