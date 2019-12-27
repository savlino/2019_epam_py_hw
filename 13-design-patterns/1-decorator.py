"""
add components to basic coffee and increases cost using Decorator pattern
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffe(Component):
    def __init__(self):
        self.coffe_components = 'coffee'

    def get_cost(self):
        return 90


class Whip:
    def __init__(self, coffe):
        self.coffe = coffe
        self.coffe_components = coffe.coffe_components + ', whip'

    def get_cost(self):
        return self.coffe.get_cost() + 12


class Marshmallow:
    def __init__(self, coffe):
        self.coffe = coffe
        self.coffe_components = coffe.coffe_components + ', marshmallow'

    def get_cost(self):
        return self.coffe.get_cost() + 23


class Syrup:
    def __init__(self, coffe):
        self.coffe = coffe
        self.coffe_components = coffe.coffe_components + ', syrup'

    def get_cost(self):
        return self.coffe.get_cost() + 34


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))
