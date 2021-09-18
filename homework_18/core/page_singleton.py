from typing import Type


def singleton(_class: Type):
    def inner(*args):
        name = f"_{_class.__name__}__instance"
        if not hasattr(_class, name):
            setattr(_class, name, _class(*args))
        return getattr(_class, name)
    return inner
