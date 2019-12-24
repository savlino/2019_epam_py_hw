"""
Describes metaclass, which provides next opportunities for subclasses:
* instances with same attributes are same object
* instances with different attributes are different objects
* any object can access any object of same class
"""

import weakref


class Dict(dict):
    pass


class Instances:
    def __get__(self, instance, cls):
        return [x for x in cls._pool]


class MetaMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._pool = Dict()
        cls.pool = Instances()

    def __call__(cls, *args, **kwargs):
        full_args = tuple([n for n in args] + [kwargs['a']])

        def connect(self, x, y, a):
            return self._pool[(x, y, a)]

        if full_args in cls._pool:
            return cls._pool[full_args]
        else:
            instance = super().__call__(*args, **kwargs)
            cls._pool[full_args] = instance
            cls.connect = connect
            return instance


class SiamObj(metaclass=MetaMeta):
    def __init__(self, attr1, attr2, a):
        self.attr1 = attr1
        self.attr2 = attr2
        self.a = a
