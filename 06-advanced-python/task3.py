""""
class suppresses errors of a given class
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
            if args[0] in self.errors_to_skip:
                return True
        except (self.error):
            return False


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")

with Suppressor(IndexError):
    arr = [1]
    arr[4]
print("That's still fine")

with Suppressor(IndexError):
    1/0
print("It isn't")
