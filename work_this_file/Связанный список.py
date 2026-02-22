
class Node:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

    def __repr__(self):
        return f'Объект {self.obj} является узлом'


class New_cls:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return 'контейнер связного списка'

my_list = New_cls()
my_list.head = Node(1)
two = Node(2)
three = Node(3)

print(my_list.head)
print(my_list.head.obj)
print(two.obj)
print(three.obj)
print(str(my_list))


