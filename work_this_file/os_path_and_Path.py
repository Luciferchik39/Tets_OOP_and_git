from os import path # объект
from pathlib import Path # импортируем КЛАССА


"""Для путей:
from pathlib import Path

Path() - создать
.exists() / .is_file() / .is_dir() - проверить
.name / .parent / .suffix - информация
.absolute() - абсолютный путь
.cwd() - текущая рабоачая директория
/ оператор - объединить

Для файлов:
print(f"1. имя текущего файла  файл: {__file__}")
6. .touch() / .mkdir() - создать
7. .read_text() / .write_text() - читать/писать
8. .rename() - переименовать
9. .unlink() / .rmdir() - удалить
10. .iterdir() - перебрать файлы в папке

Этих 10 команд хватит для 90% работы с файлами в Python!"""

# Функциональный подход к работе с файлами
print(path.abspath('..'))  # метод объекта  (абсолютный путь) ФУНКЦИОНАЛЬНЫЙ ПОДХОД
# C:\Users\Ilya\Documents\My_project\Project_path_to_the_offer
print(type(path))
# <class 'module'>


# ООП подход к работе с файлами
print(Path('..').absolute()) # экземпляр класса и Метод класса absolute() (абсолютный путь)
print(type(Path))
# <class 'type'>

""" Атрибуты класса Path"""

file_path = Path('test.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

"""мы создаём объект m проходимся циклом по всем методам класса и выводим все кроме магических методов"""
# ['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists',
# 'expanduser', 'glob', 'group', 'hardlink_to', 'home', 'is_absolute', 'is_block_device',
# 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_junction', 'is_mount', 'is_relative_to', 'is_reserved',
# 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'lstat', 'match', 'mkdir',
# 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'readlink',
# 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile',
# 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'walk', 'with_name',
# 'with_segments', 'with_stem', 'with_suffix', 'write_bytes', 'write_text']

print(Path.cwd())  # текущая рабоачая директория
""" Описываем путь (НИЧЕГО НЕ СОЗДАЁТСЯ!)"""
print(Path('C:/').joinpath('use').joinpath('Ilya')) # C:\use\Ilya
"""Проверяем, существует ли он?"""
a = (Path('C:/').joinpath('use').joinpath('Ilya'))
print(a.exists()) # False паки нет
"создаём папку"
a.mkdir(parents=True, exist_ok=True)
print(f"Папка создана: {a.exists()}")
# True С параметром parents=True метод .mkdir() создаёт все родительские папки, которых не существует.


"""Метод	Что удаляет	Когда использовать
.unlink()	Только файлы	path.unlink()
.rmdir()	Только ПУСТЫЕ папки	path.rmdir() (папка пустая)
shutil.rmtree()	Папку и ВСЁ внутри	shutil.rmtree(path) import shutil  # Нужен другой встроенный модуль"""

"Удалить ПУСТУЮ папку: .rmdir()"
a.rmdir()
print(f"Папка удалена: {a.exists()}")
print(Path('../test.py').exists())
print(Path('Ilya.txt').exists())
print(Path('/Users/Ilya/Documents/My_project/Project_path_to_the_offer').exists())

# проверка на фаил или директорию (папку)
print(Path('../mane.py').is_file())
print(Path('../../').is_file())
print(Path('../../').is_dir())

"как узнать в каком файле ты находишься и информацию о нём"
# самое простое это обратится к магическому методу напрямую
print(f"1. тукущего файла  файл: {__file__}")

# Способ 2: Через Path и __file__
current_file = Path(__file__)
print(f"2. Как Path объект: {current_file}")
print(f"   Имя файла: {current_file.name}")
print(f"   Расширение: {current_file.suffix}")
print(f"   Путь к папке файла: {current_file.parent}")


"""Создание и удаление путей """

my_dir = Path('C:/').joinpath('my_PC').joinpath('projects').joinpath('test')


if not my_dir.exists():
    my_dir.mkdir(parents=True) # parents=True означает: "Создай все родительские папки, если их нет"
    print(f'создал папку {my_dir}')


print(my_dir.exists())
# проверка на директорию выше parent - родительская папка .parent — это свойство (property), которое возвращает родительскую папку текущего пути.
print(my_dir)
a = my_dir.parent
b = my_dir.parent.parent
print(a)
print(b)

print(a.exists())
print(b.exists())

if my_dir.exists() and my_dir.is_dir():
    if not any(my_dir.iterdir()):  # проверка на пустоту
        my_dir.rmdir()
        print(f'папка удалена')

if a.exists() and a.is_dir():
    if not any(a.iterdir()):  # проверка на пустоту
        a.rmdir()
        print(f'папка удалена')

if b.exists() and b.is_dir():
    if not any(b.iterdir()):  # проверка на пустоту
        b.rmdir()
        print(f'папка удалена')
my_dir = Path('C:/').joinpath('my_PC').joinpath('projects').joinpath('test')
print(my_dir)
print(my_dir.exists())

path = Path('folder/file.txt')  # Создать объект пути
print(path.exists())    # Существует ли? (True/False)
print(path.is_file())   # Это файл?
print(path.is_dir())    # Это папка?
print(path.absolute()) # Преобразовать в абсолютный путь
      # относительынй путь
