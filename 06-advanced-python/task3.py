""""
class suppresses errors of a given class
"""


class Suppressor:
    def __init__(self, error, *args):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, *args):
        try:
            return True
        except self.error:
            pass
