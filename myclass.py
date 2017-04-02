class MyClass:
    number = 0
    name = "noname"


def Main():
    me = MyClass()
    me.number = 1312
    me.name = "Alex"

    friend = MyClass()
    friend.number = 3
    friend.name = "Steve"

    empty = MyClass()

    print("Name: {}\tNumber: {}\nName: {}\tNumber: {}\nName: {}\tNumber: {}"
          .format(me.name, me.number, friend.name, friend.number, empty.name,
                  empty.number))
if __name__ == '__main__':
    Main()
