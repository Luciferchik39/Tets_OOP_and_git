from string import digits


class User:
    count_users = 0

    def __init__(self, name, pasword):
        self.__name = name
        self.__pasword = None
        self.pasword = pasword
        User.count_users += 1
        print(f'создался экземпляр класса {self.__class__.__name__}')

    @staticmethod
    def is_number_in_pasword(pasword):
        for i in digits:
            if i in pasword:
                return True
        return False

    @staticmethod
    def _validation_pasword(pasword):
        errors = []

        if not isinstance(pasword, str):
            errors.append('пароль должен быть строкой')
            return errors
        if len(pasword) < 4 or len(pasword) > 24:
            errors.append('пароль должен иметь длину в диапозоне от 4 до 24')

        if not User.is_number_in_pasword(pasword):
            errors.append('Пароль должен содержать цифры')

        return errors

    @property
    def pasword(self):
        """Геттер - только для чтения пароля"""
        if self.__pasword is None:
            return 'Пароль не задан'
        return f'Ваш пароль: {self.__pasword}'

    @pasword.setter
    def pasword(self, value):
        """Сеттер - валидирует и устанавливает пароль"""
        erors = self._validation_pasword(value)

        if erors:
            print(f'❌ Ошибки установки пароля для пользователя {self.__name}')
            for i in erors:
                print(f'*   {i}')
            print('пороль не установлен')
            return
        self.__pasword = value
        print(f'✅ Пароль для пользователя {self.__name} успешно установлен\n')

    @property
    def name(self):
        return self.__name


new_user = User('Ilya', 1234)
new_user.pasword = '123qweras'
new_user.pasword = 'qweqwe'
user_p = User('Pavel', 'qwe')


class Deportament:
    PY_DEV = 1
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.GO_DEV, self.REACT_DEV, self.PY_DEV)

a = Deportament()
print(a.PY_DEV)


