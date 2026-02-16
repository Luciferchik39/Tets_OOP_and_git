ALLOWED_CITIES = ["Berlin", "Hamburg", "Munich"]



" validate_order(order, allowed_cities) — проверяет структуру заказа и базовые инварианты. "

def validate_order(order, allowed_cities):
    error_validate = []

    validate_list = ['customer_id', 'city', 'payment_method', 'promo_code', 'items']
    for elem in validate_list:
        if elem not in order:
            error_validate.append(f'Отсутствует обязательное поле {elem}')
    if error_validate:
        return error_validate

    customer_id = order['customer_id']
    city = order['city']
    payment_method = order['payment_method']
    promo_code = order['promo_code']
    items = order['items']

    if not isinstance(customer_id, str):
        error_validate.append('поле customer_id должно быть строкой')

    if not isinstance(city, str) or city not in allowed_cities:
        error_validate.append(f'поле {city} должно быть строкой и город должен быть из списка разрешённых городов')

    if not isinstance(payment_method, str):
        error_validate.append(f'поле {payment_method} должно быть строкой')

    if promo_code is not None and not isinstance(promo_code, str):
        error_validate.append(f'поле {promo_code} должен быть строкой или отсутствовать')

    if not isinstance(items, list) or len(items) == 0:
        error_validate.append(f'поле {items} должен быть не пустым списком')

    for ind, value in enumerate(items):

        # Шаг 1: Проверяем наличие всех ключей
        validate_order_list = ["sku", "name", "price", "qty", "category"]
        key_missing = False

        for elem in validate_order_list:
            if elem not in value:
                error_validate.append(f'Товар {ind}: отсутствует поле {elem}')
                keys_missing = True  # Отмечаем, что были пропуски

        # Шаг 2: Если были пропущены ключи — переходим к следующему товару
        if key_missing:
            continue  # Пропускаем проверку типов для этого товара

        # Шаг 3: Проверяем типы полей (сюда попадаем, только если все ключи есть)
        sku = value['sku']
        name = value['name']
        price = value['price']
        qty = value['qty']
        category = value['category']

        if not isinstance(sku, str):
            error_validate.append(f'поле {sku} дожно быть строкой')

        if not isinstance(name, str):
            error_validate.append(f'поле {name} дожно быть строкой')

        if not isinstance(price, int) or price <= 0:
            error_validate.append(f'поле {price} дожно быть положительны числом')

        if not isinstance(qty, int) or qty <= 0:  # ✅ Ошибка, если qty меньше или равно 0
            error_validate.append(f'поле {qty} дожно быть больше 0')

        if not isinstance(category, str):
            error_validate.append(f'поле {category} дожно быть строкой')

    return error_validate

order = {
    "customer_id": "CUST-001",
    "city": "Berlin",
    "payment_method": "card",
    "promo_code": "SAVE10",
    "items": [
        {"sku": "A1", "name": "Bread", "price": 2500, "qty": 2, "category": "food"},
        {"sku": "B7", "name": "Book", "price": 4000, "qty": 1, "category": "books"},
    ],
}
