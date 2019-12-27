"""
simple conformity check using Chain of Responsipility pattern on python
"""
from abc import ABC, abstractmethod


class AvailChecker(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    def check(self, list):
        pass


class AbstractChecker(AvailChecker):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def check(self, list):
        if self._next_handler:
            return self._next_handler.check(list)
        return None


class EggsCheck(AbstractChecker):
    def check(self, list):
        if list['eggs'] >= fridge['eggs']:
            print("need more eggs")
        if self._next_handler:
            return super().check(list)


class FlourCheck(AbstractChecker):
    def check(self, list):
        if list['flour'] >= fridge['flour']:
            print("need more flour")
        if self._next_handler:
            return super().check(list)


class MilkCheck(AbstractChecker):
    def check(self, list):
        if list['milk'] >= fridge['milk']:
            print("need more milk")
        if self._next_handler:
            return super().check(list)


class SugarCheck(AbstractChecker):
    def check(self, list):
        if list['sugar'] >= fridge['sugar']:
            print("need more sugar")
        if self._next_handler:
            return super().check(list)


class OilCheck(AbstractChecker):
    def check(self, list):
        if list['oil'] >= fridge['oil']:
            print("need more oil")
        if self._next_handler:
            return super().check(list)


class ButterCheck(AbstractChecker):
    def check(self, list):
        if list['butter'] >= fridge['butter']:
            print("need more butter")
        if self._next_handler:
            return super().check(list)


fridge = {
    'eggs': 10,
    'flour': 2000,
    'milk': 1000,
    'cheeze': 50,
    'sugar': 10,
    'oil': 100,
    'butter': 20
}

ingridients_list = {
    'eggs': 2,
    'flour': 300,
    'milk': 500,
    'sugar': 100,
    'oil': 10,
    'butter': 120
}


def check_ingridients(list):
    is_enough_eggs = EggsCheck()
    is_enough_flour = FlourCheck()
    is_enough_milk = MilkCheck()
    is_enough_sugar = SugarCheck()
    is_enough_oil = OilCheck()
    is_enough_butter = ButterCheck()

    is_enough_eggs.set_next(
        is_enough_flour
    ).set_next(
        is_enough_milk
    ).set_next(
        is_enough_sugar
    ).set_next(
        is_enough_oil
    ).set_next(
        is_enough_butter
    )

    is_enough_eggs.check(list)


check_ingridients(ingridients_list)
