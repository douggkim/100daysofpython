def add(*args):
    result = 0
    for n in args:
        result += int(n)
    return result


print(add(3, 6, 20, 13, 17))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(key=1, num=2)


def cal_n(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


cal_n(3, add=2, multiply=2)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
