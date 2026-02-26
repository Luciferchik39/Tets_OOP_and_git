"""
Вычисляется хеш (__hash__). По этому хешу определяется «корзина», в которую нужно положить ключ.
Проверяется равенство (__eq__). В одной «корзине» может оказаться несколько ключей с одинаковым хешем
(это называется коллизией). Когда вы хотите получить значение по ключу, Python находит корзину по хешу,
а затем сравнивает ваш ключ-запрос с каждым ключом в корзине с помощью == (то есть __eq__).

__hash__ — отвечает за скорость поиска (находит нужную корзину).
__eq__ (перегрузка ==) — отвечает за точность поиска (находит точный ключ в корзине).
"""

"Хешфункция для чисел по последней цифре числа"

hesh_list = [[] for _ in range(10)] # последней цифрой числа могут быть значения от 0 до 9 поэтому 10 пустых списков
print(hesh_list)
def hesh_list_add_fun(number):
    hesh = number % 10
    hesh_list[hesh].append(number)

def find_x_in_hesh(x: int):
    for index, value in enumerate(hesh_list):
        if value:
            if x in value:
                return f'значение {x} находится в хэш листе с индексом {index}'
    return f'значение {x} в хеш листе не найденно'

hesh_list_add_fun(127)
hesh_list_add_fun(1237)
hesh_list_add_fun(121)
print(find_x_in_hesh(127))
print(find_x_in_hesh(121))
print(hesh_list)


"""
Хеш-функция должна превращать любой объект (строку, кортеж, свой класс) в целое число.
Это число должно обладать двумя главными свойствами:
Детерминированность: Один и тот же объект всегда возвращает один и тот же хеш.
Равномерность: Хеши разных объектов должны по возможности распределяться равномерно, чтобы избежать коллизий.
"""

"""
========     Хеш для символов       ===========
"""

class My_text_hesh:
    HASH_TABLE = [[] for _ in range(10)]

    def __init__(self, text: str):
        self._text = text
        self.__hesh = self._find_hesh
        bucket_index = self.__hesh % len(My_text_hesh.HASH_TABLE)
        My_text_hesh.HASH_TABLE[bucket_index].append(self.__hesh)



    def _find_hesh(self):
        my_result = 0
        random_number = 31
        modulus = 2 ** 32
        for i in self.text:
            my_result = (my_result * random_number + ord(i)) % modulus # присваивание нового значения на каждом этапе

        return my_result

    @property
    def hesh(self):
        """
        геттер должен возвращать хеш. Если хеша нет, нужно его вычислить (ленивое вычисление)
        """
        if self.__hesh is None:
            self.__hesh = self._find_hesh()
        return self.__hesh

    @property
    def text(self):
        return self._text


    @text.setter
    def text(self, new_text):
        if not isinstance(new_text, str):
            raise TypeError(f'{new_text} должен быть строкой')

        if hasattr(self, '_My_text_hesh__hesh') and self.__hesh is not None:
            old_index = self.__hesh % len(My_text_hesh.HASH_TABLE)
            My_text_hesh.HASH_TABLE[old_index].remove(self)

        self.text = new_text

        self.__hesh = self._find_hesh(new_text)

        new_index = self.__hesh % len(My_text_hesh.HASH_TABLE)
        My_text_hesh.HASH_TABLE[new_index].append(self)








