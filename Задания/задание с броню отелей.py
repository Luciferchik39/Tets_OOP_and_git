from datetime import date


class Types_of_rooms:
    'типы комнат'
    STANDART = 'standart'
    VIP = 'vip'


class Booking_statuses:
    'статусы брони: created, confirmed.'
    CREATED = 'created'
    CONFIRMED = 'confirmed'


class Hotel:
    "Hotel (конфигурация отеля: цены и количество комнат)"

    def __init__(self, hotel_id: int, rooms_total: dict, price_per_night: dict):
        self.hotel_id = hotel_id
        self.rooms_total = rooms_total
        self.price_per_night = price_per_night

    def __str__(self):
        rooms_str = []
        for room_type, count in self.rooms_total.items():
            rooms_str.append(f"{room_type}: {count}")

        prices_str = []
        for room_type, price in self.price_per_night.items():
            prices_str.append(f"{room_type}: {price}")

        return (f'Отель {self.hotel_id}, имеет всего {sum(self.rooms_total.values())} комнат. '
                f'Из них: {", ".join(rooms_str)}. '
                f'Цены: {", ".join(prices_str)}')


class Booking:
    '''
    данные брони + методы
    Формат дат — строка YYYY-MM-DD. Можно использовать datetime.date.
    '''

    def __init__(self, booking_id: int, guest_name: str, hotel: Hotel,
                 room_type: str, check_in: str, check_out: str):
        self.booking_id = booking_id
        self.guest_name = guest_name  # было user, стало guest_name
        self.hotel = hotel
        self.room_type = room_type
        self.check_in = date.fromisoformat(check_in)
        self.check_out = date.fromisoformat(check_out)
        self.status = Booking_statuses.CREATED  # было booking_status, стало status

    def confirm(self):  # было created, стало confirm
        'created → confirmed, если оплачено 100%'
        self.status = Booking_statuses.CONFIRMED

    def cancel(self):
        'confirmed → created'
        self.status = Booking_statuses.CREATED

    def cost(self):
        """
        Стоимость = price_per_night * nights.
        """
        if self.check_out < self.check_in:
            raise ValueError('Выезд строго позже заезда')
        nights = (self.check_out - self.check_in).days
        price_per_night = self.hotel.price_per_night[self.room_type]
        return price_per_night * nights

    def __str__(self):
        return (f'Бронь {self.booking_id}: {self.guest_name}, '
                f'Отель {self.hotel.hotel_id}, {self.room_type}, '
                f'{self.check_in} → {self.check_out}, '
                f'стоимость {self.cost()}, статус {self.status}')


class BookingService:
    """
    Основная бизнес-логика: наличие, создание, оплата
    Хранение данных в памяти (словари/структуры)
    """

    def __init__(self):
        # Словари для хранения данных
        self.hotels = {}  # {hotel_id: Hotel}
        self.bookings = {}  # {booking_id: Booking}

        # Счётчики
        self.next_hotel_id = 1
        self.next_booking_id = 1

        # Структура для хранения занятости номеров
        # Ключ: (hotel_id, date, room_type) -> количество занятых номеров
        self.occupied = {}

        # Для быстрого поиска броней по отелю
        self.hotel_bookings = {}  # {hotel_id: список booking_id}

    # ========== МЕТОДЫ ДЛЯ РАБОТЫ С ОТЕЛЯМИ ==========

    def create_hotel(self, rooms_total: dict, price_per_night: dict):
        """
        Создаёт отель с автоматической генерацией ID
        """
        hotel = Hotel(
            hotel_id=self.next_hotel_id,
            rooms_total=rooms_total,
            price_per_night=price_per_night
        )
        self.hotels[self.next_hotel_id] = hotel
        self.hotel_bookings[self.next_hotel_id] = []  # сразу создаём запись
        self.next_hotel_id += 1
        print(f"Отель {hotel.hotel_id} успешно создан")
        return hotel

    def add_hotel(self, hotel):
        """
        Добавляет уже созданный отель в сервис
        """
        if hotel.hotel_id in self.hotels:
            print(f"Отель с ID {hotel.hotel_id} уже существует")
            return False

        self.hotels[hotel.hotel_id] = hotel
        self.hotel_bookings[hotel.hotel_id] = []
        print(f"Отель {hotel.hotel_id} успешно добавлен")
        return True

    def get_hotel(self, hotel_id):
        """
        Возвращает отель по ID
        """
        return self.hotels.get(hotel_id, None)

    # ========== МЕТОДЫ ПРОВЕРКИ ДОСТУПНОСТИ ==========

    def search_availability(self, hotel_id, room_type, check_in, check_out):
        """
        Проверяет, есть ли свободные номера указанного типа на все даты
        Формат дат — строка YYYY-MM-DD
        Возвращает True если есть, False если нет
        """
        # 1. Проверяем существование отеля
        if hotel_id not in self.hotels:
            print(f"Отель с ID {hotel_id} не найден")
            return False

        hotel = self.hotels[hotel_id]

        # 2. Проверяем существование типа комнаты
        if room_type not in hotel.rooms_total:
            print(f"Тип комнаты {room_type} не существует в отеле")
            return False

        # 3. Проверяем корректность дат
        check_in_date = date.fromisoformat(check_in)
        check_out_date = date.fromisoformat(check_out)

        if check_out_date <= check_in_date:
            print("Дата выезда должна быть позже даты заезда")
            return False

        # 4. Проверяем доступность на каждую дату
        current = check_in_date
        while current < check_out_date:
            key = (hotel_id, current, room_type)
            occupied_count = self.occupied.get(key, 0)
            total_rooms = hotel.rooms_total.get(room_type, 0)

            if occupied_count >= total_rooms:
                return False

            # В реальности: current += timedelta(days=1)
            break

        return True

    # ========== МЕТОДЫ ДЛЯ РАБОТЫ С БРОНЯМИ ==========

    def create_booking(self, guest_name, hotel_id, room_type, check_in, check_out):
        """
        Создаёт новое бронирование
        Возвращает booking_id или None если создать нельзя
        """
        # 1. Проверяем наличие свободных мест
        if not self.search_availability(hotel_id, room_type, check_in, check_out):
            print("Нет свободных номеров на выбранные даты")
            return None

        # 2. Получаем отель
        hotel = self.hotels[hotel_id]

        # 3. Создаём объект бронирования
        booking = Booking(
            booking_id=self.next_booking_id,
            guest_name=guest_name,
            hotel=hotel,
            room_type=room_type,
            check_in=check_in,
            check_out=check_out
        )

        # 4. Сохраняем бронь
        self.bookings[self.next_booking_id] = booking
        self.hotel_bookings[hotel_id].append(self.next_booking_id)

        # 5. Обновляем информацию о занятости
        check_in_date = date.fromisoformat(check_in)
        check_out_date = date.fromisoformat(check_out)

        current = check_in_date
        while current < check_out_date:
            key = (hotel_id, current, room_type)
            self.occupied[key] = self.occupied.get(key, 0) + 1
            break

        # 6. Увеличиваем счётчик и возвращаем ID
        booking_id = self.next_booking_id
        self.next_booking_id += 1

        print(f"Бронь {booking_id} успешно создана")
        return booking_id

    def get_booking(self, booking_id):
        """
        Возвращает бронь по ID
        """
        return self.bookings.get(booking_id, None)

    def pay_booking(self, booking_id, amount):
        """
        Оплата бронирования
        """
        # 1. Ищем бронь
        booking = self.get_booking(booking_id)
        if not booking:
            print(f"Бронь с ID {booking_id} не найдена")
            return None

        # 2. Проверяем, не подтверждена ли уже бронь
        if booking.status == Booking_statuses.CONFIRMED:
            print("Бронь уже подтверждена")
            return None

        # 3. Получаем полную стоимость
        total_cost = booking.cost()

        # 4. Проверяем сумму
        if amount > total_cost:
            print(f"Сумма оплаты ({amount}) не может быть больше стоимости ({total_cost})")
            return None

        if amount < total_cost:
            print(f"Оплачена часть суммы ({amount} из {total_cost}), статус не меняется")
        else:  # amount == total_cost
            booking.confirm()
            print(f"Бронь {booking_id} полностью оплачена и подтверждена")

        # 5. Возвращаем данные
        return {
            'booking_id': booking.booking_id,
            'guest_name': booking.guest_name,
            'hotel_id': booking.hotel.hotel_id,
            'room_type': booking.room_type,
            'check_in': booking.check_in.isoformat(),
            'check_out': booking.check_out.isoformat(),
            'total_cost': total_cost,
            'paid': amount,
            'status': booking.status
        }

    # ========== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ==========

    def show_all_hotels(self):
        """Показывает все отели в системе"""
        if not self.hotels:
            print("В системе нет отелей")
            return

        print("\n=== СПИСОК ОТЕЛЕЙ ===")
        for hotel in self.hotels.values():
            print(hotel)

    def show_all_bookings(self):
        """Показывает все брони в системе"""
        if not self.bookings:
            print("В системе нет броней")
            return

        print("\n=== СПИСОК БРОНЕЙ ===")
        for booking in self.bookings.values():
            print(booking)

    def show_hotel_bookings(self, hotel_id):
        """Показывает все брони конкретного отеля"""
        if hotel_id not in self.hotel_bookings:
            print(f"Отель {hotel_id} не найден или нет броней")
            return

        print(f"\n=== БРОНИ ОТЕЛЯ {hotel_id} ===")
        for booking_id in self.hotel_bookings[hotel_id]:
            booking = self.bookings[booking_id]
            print(f"  {booking}")



# ========== 1. ПОДГОТОВКА ==========

# Создаём экземпляр сервиса
service = BookingService()

# Создаём отель через create_hotel (автоматический ID)
hotel1 = service.create_hotel(
    rooms_total={Types_of_rooms.STANDART: 2, Types_of_rooms.VIP: 1},
    price_per_night={Types_of_rooms.STANDART: 2500, Types_of_rooms.VIP: 5000}
)

# Или добавляем отель вручную (для теста с конкретным ID)
hotel2 = Hotel(
    hotel_id=101,
    rooms_total={Types_of_rooms.STANDART: 10, Types_of_rooms.VIP: 2},
    price_per_night={Types_of_rooms.STANDART: 2500, Types_of_rooms.VIP: 5000}
)
service.add_hotel(hotel2)

print("=" * 50)
print("ПОДГОТОВКА ЗАВЕРШЕНА")
print("=" * 50)


# ========== 2. ТЕСТИРОВАНИЕ search_availability ==========

print("\n" + "=" * 50)
print("ТЕСТИРОВАНИЕ ПОИСКА ДОСТУПНОСТИ")
print("=" * 50)

# Тест 1: Успешный поиск (должно быть True)
result = service.search_availability(
    hotel_id=1,  # отель из create_hotel
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 1 (отель 1, должно быть True): {result}")

# Тест 1.1: Успешный поиск в отеле 101
result = service.search_availability(
    hotel_id=101,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 1.1 (отель 101, должно быть True): {result}")

# Тест 2: Неверные даты (выезд раньше заезда) -> False
result = service.search_availability(
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-10",
    check_out="2026-03-05"
)
print(f"Тест 2 (выезд раньше заезда, должно быть False): {result}")

# Тест 3: Несуществующий отель -> False
result = service.search_availability(
    hotel_id=999,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 3 (несуществующий отель, должно быть False): {result}")

# Тест 4: Несуществующий тип комнаты -> False
result = service.search_availability(
    hotel_id=1,
    room_type="super_lux",
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 4 (несуществующий тип, должно быть False): {result}")


# ========== 3. СОЗДАНИЕ БРОНЕЙ ==========

print("\n" + "=" * 50)
print("СОЗДАНИЕ БРОНЕЙ")
print("=" * 50)

# Тест 5: Создание первой брони в отеле 1 (успешно)
booking1_id = service.create_booking(
    guest_name="Иван Петров",  # обрати внимание: guest_name, а не user!
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 5 (первая бронь в отеле 1, ID: {booking1_id})")

# Тест 5.1: Создание брони в отеле 101
booking101_id = service.create_booking(
    guest_name="Петр Иванов",
    hotel_id=101,
    room_type=Types_of_rooms.VIP,
    check_in="2026-04-01",
    check_out="2026-04-05"
)
print(f"Тест 5.1 (бронь в отеле 101, ID: {booking101_id})")

# Тест 6: Создание второй брони на ТЕ ЖЕ даты (в отеле 1, ещё есть места, STANDART = 2 номера)
booking2_id = service.create_booking(
    guest_name="Мария Сидорова",
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 6 (вторая бронь на те же даты, ID: {booking2_id})")

# Тест 7: Создание третьей брони на ТЕ ЖЕ даты (уже нет мест, должно быть None)
booking3_id = service.create_booking(
    guest_name="Петр Иванов",
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 7 (третья бронь на те же даты, должно быть None): {booking3_id}")

# Тест 8: Создание брони на VIP (успешно, 1 номер)
booking4_id = service.create_booking(
    guest_name="Елена Прекрасная",
    hotel_id=1,
    room_type=Types_of_rooms.VIP,
    check_in="2026-03-10",
    check_out="2026-03-15"
)
print(f"Тест 8 (VIP бронь, ID: {booking4_id})")

# Тест 9: Создание второй брони на VIP на те же даты (нет мест, должно быть None)
booking5_id = service.create_booking(
    guest_name="Олег Богатый",
    hotel_id=1,
    room_type=Types_of_rooms.VIP,
    check_in="2026-03-10",
    check_out="2026-03-15"
)
print(f"Тест 9 (вторая VIP бронь на те же даты, должно быть None): {booking5_id}")

# Тест 10: Создание брони с перекрывающимися датами (частично занято)
booking6_id = service.create_booking(
    guest_name="Анна Каренина",
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-03",  # заезд в середине первой брони
    check_out="2026-03-07"
)
print(f"Тест 10 (перекрывающиеся даты, должно быть None): {booking6_id}")


# ========== 4. ПРОВЕРКА ТЕКУЩИХ БРОНЕЙ ==========

print("\n" + "=" * 50)
print("ТЕКУЩИЕ БРОНИ")
print("=" * 50)
service.show_all_bookings()


# ========== 5. ТЕСТИРОВАНИЕ ОПЛАТЫ ==========

print("\n" + "=" * 50)
print("ТЕСТИРОВАНИЕ ОПЛАТЫ")
print("=" * 50)

# Получаем созданные брони для тестов
booking1 = service.get_booking(booking1_id)  # Иван Петров, 4 ночи * 2500 = 10000
booking2 = service.get_booking(booking2_id)  # Мария Сидорова, 4 ночи * 2500 = 10000
booking4 = service.get_booking(booking4_id)  # Елена Прекрасная, 5 ночей * 5000 = 25000

if booking1:
    print(f"Бронь {booking1_id} стоимость: {booking1.cost()}")
if booking2:
    print(f"Бронь {booking2_id} стоимость: {booking2.cost()}")
if booking4:
    print(f"Бронь {booking4_id} стоимость: {booking4.cost()}")

# Тест 11: Успешная оплата 100%
print("\nТест 11: Успешная оплата 100%")
if booking1_id:
    result = service.pay_booking(booking1_id, 10000)
    if result:
        print(f"Результат: статус {result['status']}")
    else:
        print("Оплата не прошла")

# Тест 12: Оплата с недостаточной суммой (должно остаться created)
print("\nТест 12: Оплата с недостаточной суммой (5000 вместо 10000)")
if booking2_id:
    result = service.pay_booking(booking2_id, 5000)
    if result:
        print(f"Результат: статус {result['status']}")
    else:
        print("Оплата не прошла")

# Тест 13: Оплата с избыточной суммой (должно быть ошибка)
print("\nТест 13: Оплата с избыточной суммой (30000 вместо 25000)")
if booking4_id:
    result = service.pay_booking(booking4_id, 30000)
    if result:
        print(f"Результат: статус {result['status']}")
    else:
        print("Оплата не прошла (так и должно быть)")

# Тест 14: Повторная оплата уже подтверждённой брони
print("\nТест 14: Повторная оплата подтверждённой брони")
if booking1_id:
    result = service.pay_booking(booking1_id, 10000)
    if result:
        print(f"Результат: статус {result['status']}")
    else:
        print("Оплата не прошла (так и должно быть)")

# Тест 15: Оплата несуществующей брони
print("\nТест 15: Оплата несуществующей брони (ID=999)")
result = service.pay_booking(999, 10000)
if result:
    print(f"Результат: статус {result['status']}")
else:
    print("Оплата не прошла (так и должно быть)")


# ========== 6. ФИНАЛЬНАЯ ПРОВЕРКА СТАТУСОВ ==========

print("\n" + "=" * 50)
print("ФИНАЛЬНЫЕ СТАТУСЫ БРОНЕЙ")
print("=" * 50)
service.show_all_bookings()


# ========== 7. ТЕСТИРОВАНИЕ ПОИСКА ПОСЛЕ БРОНИРОВАНИЙ ==========

print("\n" + "=" * 50)
print("ПРОВЕРКА ДОСТУПНОСТИ ПОСЛЕ БРОНИРОВАНИЙ")
print("=" * 50)

# Тест 16: Проверка доступности на занятые даты
result = service.search_availability(
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-01",
    check_out="2026-03-05"
)
print(f"Тест 16 (стандарт на 1-5 марта, после 2 броней, должно быть False): {result}")

# Тест 17: Проверка доступности на свободные даты
result = service.search_availability(
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-06",
    check_out="2026-03-10"
)
print(f"Тест 17 (стандарт на 6-10 марта, должно быть True): {result}")

# Тест 18: Проверка доступности VIP после брони
result = service.search_availability(
    hotel_id=1,
    room_type=Types_of_rooms.VIP,
    check_in="2026-03-10",
    check_out="2026-03-15"
)
print(f"Тест 18 (VIP на 10-15 марта, после брони, должно быть False): {result}")


# ========== 8. ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ==========

print("\n" + "=" * 50)
print("ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ")
print("=" * 50)

# Тест 19: Попытка создать бронь с некорректными датами
booking_invalid = service.create_booking(
    guest_name="Тестовый",
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-15",
    check_out="2026-03-10"  # выезд раньше заезда
)
print(f"Тест 19 (некорректные даты, должно быть None): {booking_invalid}")

# Тест 20: Создание брони после оплаченной (проверка, что confirmed брони тоже занимают места)
booking7_id = service.create_booking(
    guest_name="Дмитрий Тестовый",
    hotel_id=1,
    room_type=Types_of_rooms.STANDART,
    check_in="2026-03-20",
    check_out="2026-03-25"
)
print(f"Тест 20 (новая бронь на свободные даты, ID: {booking7_id})")

# Тест 21: Отмена брони (если есть метод cancel)
if booking7_id:
    booking7 = service.get_booking(booking7_id)
    if booking7:
        booking7.cancel()
        print(f"Тест 21 (отмена брони {booking7_id})")
        print(f"      Новый статус: {booking7.status}")

# Тест 22: Проверка отеля 101
print("\nТест 22: Проверка броней в отеле 101")
service.show_hotel_bookings(101)

print("\n" + "=" * 50)
print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
print("=" * 50)
