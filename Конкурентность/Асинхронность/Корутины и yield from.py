
def subgen():
    message = yield
    print('subgen recceived: ', message)

