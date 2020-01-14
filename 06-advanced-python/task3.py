""""
class suppresses errors of a given class(es)
"""


class Suppressor:
    def __init__(self, *args):
        self.errors_to_skip = []
        for arg in args:
            if issubclass(arg, BaseException):
                self.errors_to_skip.append(arg)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        try:
            return issubclass(args[0], tuple(self.errors_to_skip))
        finally:
            pass


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")

with Suppressor(IndexError):
    arr = [1]
    arr[4]
print("That's still fine")

with Suppressor(ArithmeticError, AttributeError):
    1/0
print("works now")

with Suppressor(IndexError):
    1/0
print("It isn't")
