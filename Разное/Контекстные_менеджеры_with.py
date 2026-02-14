

class ContextManager:
    def __enter__(self):
        print('Вход в контекстный менеджер')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выход из контекстного менеджера')
        if isinstance(exc_val, KeyError):
            print('Обработчик ключевых ошибок')
        elif isinstance(exc_tb, IndexError):
            print('Обработчик ошибок индекса')

with ContextManager():
    print('Объект внутри контекстного менеджера')

with ContextManager():
    raise KeyError(100)

with ContextManager():
    raise IndexError('people')