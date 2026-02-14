"""
== - сравнение по ЗНАЧЕНИЮ (value equality)
is - сравнение по ПАМЯТИ (identity/object equality)
"""

"по ЗНАЧЕНИЮ"
10 == 10  # True - числа одинаковые
[1, 2, 3] == [1, 2, 3]  # True - списки содержат одинаковые значения
"hello" == "hello"  # True - строки одинаковые


"по ПАМЯТИ"
a = []
b = []
a is b  # False - это РАЗНЫЕ объекты в памяти!


# None, True, False - всегда один объект
print(None is None)  # True
print(True is True)  # True

a = None
b = None
print(a is b)  # True - всегда один None!

