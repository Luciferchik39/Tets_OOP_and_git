def validate_order(order, allowed_cities):
    # возможные ошибки
    errors = []

    list_validate = ["customer_id", "city", "payment_method", "items", "promo_code"]
    for i in list_validate:
        if i not in order:
            errors.append(f"Отсутствует обязательное поле: {i}")
            return errors
    if errors: return False, errors

    if not isinstance(order["customer_id"], str) or not order["customer_id"].strip():
        errors.append('поле customer_id должно быть не пустой строкой')

    if not isinstance(order['city'], str):
        errors.append(f'поле city должно быть строкой')
    elif order['city'] not in allowed_cities:
        errors.append(f'в этот город не добавляем')
    if not isinstance(order['payment_method'], str):
        errors.append(f'поле payment_method должно быть строкой')
    if order['promo_code'] is not None and not isinstance(order['promo_code'], str):
        errors.append('поле promo_code должно быть или None или строкой')
    if not isinstance(order['items'], list) and len(order["items"]) == 0:
        errors.append('поле items должно быть непустым списком')
    else:
        items_list = ["sku", "name", "price", "qty", "category"]
        for index, item in enumerate(order["items"]):
            for field in items_list:
                if field not in item:
                    errors.append(f'отсутвует поле {field} в товаре')

            sku = item['sku']
            name = item['name']
            price = item['price']
            qty = item['qty']
            category = item['category']

            if not isinstance(sku, str):
                errors.append(f'код {sku} товара должен быть в виде строки')
            if not isinstance(name, str):
                errors.append(f'Наименование товара {name} товара должен быть в виде строки')
            if not isinstance(price, int) or price <= 0:
                errors.append(f'Цена товара должны быть целым положительным числом')
            if not isinstance(price, int) or price <= 0:
                errors.append(f'Цена товара должны быть целым положительным числом')
            if not isinstance(qty, int) or qty <= 0:
                errors.append(f'Количесвто товара не должно быть меньше одного')
            if not isinstance(category, str):
                errors.append(f'Категория товара должны быть строкой')
            if errors:
                return False, errors

    return errors


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

allowed_cities = ['Berlin']

print(validate_order(order, allowed_cities))
