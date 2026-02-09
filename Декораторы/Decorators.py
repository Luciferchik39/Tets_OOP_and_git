def decorator_fun(my_fun):
    def wrapper():
        # дейсвие до выполения фунцкции не затрагивая саму функцию
        print(f'Старт')
        result = my_fun()
        print(f'стоп') # действие после выполнения основной функции и опять код функции не трогался
        return result

    return wrapper # не вызываю функцию wrapper()


@decorator_fun
def my_fun():
    print(f'my_fun запустилась')

my_fun()