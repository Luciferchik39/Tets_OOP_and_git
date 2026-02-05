"""
1. Функции:

- validate_order(order, allowed_cities) — проверяет структуру заказа и базовые инварианты.

- calculate_base_total(items)

- calculate_discount(items, base_total, promo_code)

- calculate_delivery(base_total, city, payment_method, allowed_cities)

- calculate_payment_fee(amount_after_discount, payment_method)

- checkout(order) — собирает всё вместе и возвращает чек.

2. Декоратор:

- guarded_checkout(forbidden_categories, max_base_total, allowed_cities)
"""
from test import items

ALLOWED_CITIES = ["Berlin", "Hamburg", "Munich"]
FORBIDDEN_CATEGORIES = {"alcohol", "tobacco"}
MAX_BASE_TOTAL = 5_000_000  # in cents

def guarded_checkout(forbidden_categories, max_base_total, allowed_cities):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # your code here
            return func(*args, **kwargs)
        return wrapper
    return decorator


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
    if not isinstance(order['items'], list) or len(order["items"]) == 0:
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
            if not isinstance(qty, int) or qty <= 0:
                errors.append(f'Количесвто товара не должно быть меньше одного')
            if not isinstance(category, str):
                errors.append(f'Категория товара должны быть строкой')

    return len(errors) == 0, errors

"""1. **Базовая сумма** = сумма price * qty по всем позициям.
    
2. **Скидка по промокоду**:
    
- "SAVE10" — 10% скидка на базовую сумму, но **не более 50000** (т.е. 500.00 в валюте, если копейки).
    
- "FOOD15" — 15% скидка **только на позиции категории** **"food"**, без лимита.
    
- Любой другой промокод считается невалидным → скидка 0."""
def calculate_base_total(items):
    items= [
        {"sku": "A1", "name": "Bread", "price": 2500, "qty": 2, "category": "food"},
        {"sku": "B7", "name": "Book", "price": 4000, "qty": 1, "category": "books"},
    ]
    for item in items:
    pass


def calculate_discount(items, base_total, promo_code):
    pass


def calculate_delivery(base_total, city, payment_method, allowed_cities):
    pass


def calculate_payment_fee(amount_after_discount, payment_method):
    pass


# =========================
# Checkout
# =========================

@guarded_checkout(
    forbidden_categories=FORBIDDEN_CATEGORIES,
    max_base_total=MAX_BASE_TOTAL,
    allowed_cities=ALLOWED_CITIES,
)
def checkout(order):
    pass



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

receipt = checkout(order)
print(receipt)

if __name__ == "__main__":
    main()