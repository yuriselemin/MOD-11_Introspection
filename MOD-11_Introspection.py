
# Домашнее задание по теме "Интроспекция"

def introspection_info(obj):
    # Получаем тип объекта
    type_name = type(obj).__name__
    # Получаем атрибуты объекта
    attributes = dir(obj)
    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj, '__module__', None)
    return {
    'type': type_name,
    'attributes': attributes,
    'methods': methods,
    'module': module
    }

number_info = introspection_info(42)
print(number_info)