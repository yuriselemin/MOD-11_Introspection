import inspect
from pprint import pprint
# Домашнее задание по теме "Интроспекция"


class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.name} {self.model} заводит свой двигатель."

    def horn(self):
        return f"{self.name} издает сигнал Beep! Beep!"


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))],
        'methods': [meth for meth in dir(obj) if callable(getattr(obj, meth)) and not meth.startswith('__')],
        'module': inspect.getmodule(introspection_info).__name__,
    }
    return info


my_car = Car("Toyota", "Camry", 2022)
print(my_car.start_engine())
print(my_car.horn())
car_info = introspection_info(my_car)
pprint(car_info)


