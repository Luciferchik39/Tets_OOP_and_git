
"""
Классы — это шаблоны (чертежи) для создания объектов.
Атрибуты класса включают: свойства класса (общие данные) и методы (общее поведение (функции действия)).
Экземпляры могут иметь собственные атрибуты (данные), уникальные для каждого объекта.
Экземпляры наследуют атрибуты класса:
Могут читать и использовать их
При попытке записи в переменную класса создается локальная копия у экземпляра
Изменять оригинальные атрибуты класса для всех экземпляров можно только через сам класс"""

def my_func(x):
    "моя функция"
    return x * 2

print(dir(my_func))
print(my_func.__name__)    # 'my_func' ← АТРИБУТ!
print(my_func.__doc__)     # None или строка документации
print(my_func.__code__)    # <code object> ← АТРИБУТ!
print([x for x in dir(my_func) if not x.startswith('__')])

# Библиотека (класс) имеет книги (методы)
class Library:
    books = {
        'greet': "Книга про приветствия",
        'calculate': "Книга математики"
    }

# Читатель (экземпляр) приходит в библиотеку
reader = Library()

# Читатель может ЧИТАТЬ книги из библиотеки
print(reader.books['greet'])  # "Книга про приветствия"

# Но читатель НЕ УНОСИТ книги домой
print(reader.__dict__)  # {} - у него нет своих книг

# Если читатель скажет "у меня есть книга 'greet'"
reader.books = {"greet": "Моя личная книга"}

# То это будет ЕГО ЛИЧНАЯ копия, а не библиотечная
print(reader.__dict__)  # {'books': {"greet": "Моя личная книга"}}
print(Library.books)    # {"greet": "Книга про приветствия", ...} - не изменилась!

"""
Класс Robot:
├── ПЕРЕМЕННЫЕ КЛАССА (общие свойства для ВСЕХ роботов):
│   ├── name = 'имя'              ← Cвойство: индивидуальное имя
│   ├── madel = 'модель'          ← Cвойство: модель
│   ├── material = "металл"       ← СВОЙСТВО: из чего сделан
│   └── power_source = "аккумулятор" ← СВОЙСТВО: источник питания
│
└── МЕТОДЫ КЛАССА (общее поведение для ВСЕХ роботов):
    ├── __init__()                ← УМЕНИЕ: родиться с именем и моделью
    ├── move()                    ← УМЕНИЕ: перемещаться
    ├── charge()                  ← УМЕНИЕ: заряжаться
    └── get_info()                ← УМЕНИЕ: рассказать о себе"""

class Robot:
    # ---------- ПЕРЕМЕННЫЕ КЛАССА ----------
    # ОБЩИЕ СВОЙСТВА для ВСЕХ роботов этого типа
    qnt_robots = 0
    def __init__(self, name, model, material, power_source):
        # ПЕРЕМЕННЫЕ ЭКЗЕМПЛЯРА (индивидуальные свойства)
        self.name = name
        self.model = model
        self.material = material
        self.power_source = power_source
        # update
        self.qnt_robots += 1

    # ---------- МЕТОДЫ КЛАССА ----------
    # ОБЩЕЕ ПОВЕДЕНИЕ для ВСЕХ роботов этого типа
    def move(self):
        return f'движение'

    def charge(self):
        return 'заряжаемся'

    def get_info(self):
        move_name = self.move.__name__
        charge_name = self.charge.__name__
        get_info_name = self.get_info.__name__
        return (f'Я как экземпляр класса имею свойства: Имя: {self.name}, Модель: {self.model}, Материал: {self.material}, Источник питания: {self.power_source}\n'
                f'так же я умею использовать методы класса такие как {move_name}, {charge_name} и {get_info_name} ')


litle_robot = Robot('Пупс','litle', 'бронза', "батарейки")

print(litle_robot)
print(litle_robot.move())
print(litle_robot.charge())
print(litle_robot.get_info())
