"""
==============    ПОЛИМОРФИЗМ — многообразие форм  ============

Когда ты видишь объект с методом append, правильнее думать не "это список", а "это объект, который ведет себя
как коллекция, поддерживающая добавление элементов".
Разница тонкая, но важная:
Первое (это список) — ограничивает твое мышление
Второе (ведет себя как коллекция) — открывает возможност
"""
"""
1. Оптимистичный подход (EAFP — Easier to Ask for Forgiveness than Permission)
"Легче попросить прощения, чем разрешения" — основной стиль Python.
"""

def proces_data(data):
    # Мы не знаем, что такое data, но нам нужно с ним работать
    # Вариант 1: Если нам нужно добавить элемент
    if hasattr(data, 'append'):
        data.append['Доаблено при 1-ом if']
        return print(f'Полученный объект расширен')
    try:
        for item in data:
            print(f'действие с {item} из {data}')
    except Exception as e:
        print(f'получили ошибку {e}')
        print(f'объект не итерируемый')
        print(f'Объект: {data}')

"""
2. Проверка наличия метода (LBYL — Look Before You Leap)
"Посмотри перед прыжком" — более осторожный подход.
"""

def process_if_possible(obj):
    if hasattr(obj, 'append') and callable(obj.append):
        # Да, у объекта есть метод append, и его можно вызвать
        obj.append("данные")
        return True
    else:
        print("Объект не умеет append")
        return False

class EnergyManager:
    """Отвечает ТОЛЬКО за управление энергией"""
    def __init__(self, max_energy=100):
        self.energy = max_energy
        self.max_energy = max_energy

    def increase(self, amount):
        self.energy = min(self.energy + amount, self.max_energy)

    def decrease(self, amount):
        self.energy = max(self.energy - amount, 0)

    def can_perform(self, required_energy):
        return self.energy >= required_energy


class MessageFormatter:
    """Отвечает ТОЛЬКО за формирование сообщений"""

    @staticmethod
    def eat_message(name, is_trained=False):
        if is_trained:
            return f'{name} аккуратно поел'
        return f'{name} поел, но немного испачкался'


class Animal:
    def __init__(self, name, age, number_of_limbs):
        self.name = name
        self.age = age
        self.number_of_limbs = number_of_limbs
        self.energy_manager = EnergyManager()  # Композиция
        self.is_alive = True

    def eat(self):
        if self.is_alive and self.energy_manager.energy <= 90:
            self.energy_manager.increase(10)
            return f'{self.name} немного насытился'
        return f'животное {self.name} сыто'

    def sleap(self):
        if self.is_alive and self.energy <= 80:
            self.energy += 20
            return f'животное {self.name} отдохнуло'
        return f'Животное {self.name} слишком бодрое'

    def breathe(self):
        """Дышать могут все"""
        return f"{self.name} дышит"

    def make_sound(self):
        """
        Это метод который используется для экземпляров класса но не имеет своей реализации так как сначала нужно
        определить кто будет произносить звук и какой у него результат
        """
        raise NotImplementedError("Каждое животное должно определить свой звук!")



class Dog(Animal):
    """Класс собак, наследник Animal"""
    def __init__(self, name, age, number_of_limbs, is_trained=False):
        # ВАЖНО! Сначала вызываем конструктор родителя
        super().__init__(name, age, number_of_limbs) # Что бы не писать каждый раз self.name = name и другие пересекающиеся
        # свойства мы их наследуем у родителя класса и после уже обрабатываем индивидуальные свойтсва класса.

        # Теперь добавляем свойства, специфичные ТОЛЬКО для собак
        self.is_trained = is_trained # Дрессировка специфична для собак
        self.tail_wagging = True  # Виляют хвостом

    def eat(self):
        base_result = super().eat()
        if not self.is_trained and 'насытился' in base_result:
            return base_result + " Но разбросал еду!"
        return base_result

    def make_sound(self):
        if self.energy >= 5:
            self.energy -= 5
            return f'{self.name} произносит Гав! Гав!'
        return f'{self.name} пытается лаять но он слишком устал и получается только ели слышимый звук который не разобрать'



