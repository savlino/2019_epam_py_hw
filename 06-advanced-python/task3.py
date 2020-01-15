""""
class suppresses errors of a given class(es)
"""


class Suppressor:
    def __init__(self, *args):
        self.errors_to_skip = args

    def __enter__(self):
        pass

    def __exit__(self, *args):
        return issubclass(args[0], self.errors_to_skip)


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
