from pathlib import Path


"""
    1. Запись (перезапись)
with open('file.txt', 'w') as f:
    f.write('Новый текст')  # Стирает старое, пишет новое

    2. Добавление
with open('file.txt', 'a') as f:
    f.write('\nДобавленная строка')  # Добавляет в конец

    3. Чтение
with open('file.txt', 'r') as f:
    content = f.read()  # Читает весь файл

    4. Чтение и запись
with open('file.txt', 'r+') as f:
    # Можно и читать и писать (курсор в начале)
    
    5. ОТКРЫТИЕ

    with open(путь, режим, encoding='utf-8') as f: Всегда используй encoding='utf-8' для текстовых файлов

    # РЕЖИМЫ:
    # 'r'  - чтение (по умолчанию)
    # 'w'  - запись (стирает старое)
    # 'a'  - добавление в конец
    # 'r+' - чтение и запись
    # 'rb'/'wb' - бинарные файлы
    
    # ЧТЕНИЕ:
    весь_текст = f.read()           # Всё как строка
    список_строк = f.readlines()    # Список строк
    for string in f: ...           # Построчно
    
    # ЗАПИСЬ:
    f.write(текст)                  # Записать строку
    f.writelines(список_строк)      # Записать список
    
    # ПОЗИЦИЯ:
    позиция = f.tell()              # Где курсор
    f.seek(0)                       # Переместить в начало
    f.seek(0, 2)                    # Переместить в конец
    
    # ИНФОРМАЦИЯ:
    имя = f.name                    # Имя файла
    режим = f.mode                  # Режим открытия
    
    """


a = Path('test.txt')
print(a.exists())
my_dir = Path('.').absolute()
print(my_dir)
a.touch() # ← СОЗДАЁТ пустой файл
print(a.exists())
my_dir = Path("new_file.txt")
my_dir.write_text("Привет, мир!") # ← Создаёт файл с содержимым

if not a.exists():
    pass
if my_dir.exists():
    with open('new_file.txt') as test_file:
        print(test_file.read())

with open('new_file.txt', 'r') as f:
    print(f.name)      # Имя файла
    print(f.mode)      # Режим ('r', 'w', etc.)
    print(f.closed)    # False (пока открыт)
print(f.closed)        # True (после with)
