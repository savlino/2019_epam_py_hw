"""
simple conformity check using Chain of Responsipility pattern on python
"""
from abc import ABC, abstractmethod


class AvailChecker(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    def check(self, checklist):
        pass


class AbstractChecker(AvailChecker):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def check(self, checklist):
        if self._next_handler:
            return self._next_handler.check(checklist)
        return None


class EggsCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['eggs'] > fridge['eggs']:
            print("need more eggs")
        if self._next_handler:
            return super().check(checklist)


class FlourCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['flour'] > fridge['flour']:
            print("need more flour")
        if self._next_handler:
            return super().check(checklist)


class MilkCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['milk'] > fridge['milk']:
            print("need more milk")
        if self._next_handler:
            return super().check(checklist)


class SugarCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['sugar'] > fridge['sugar']:
            print("need more sugar")
        if self._next_handler:
            return super().check(checklist)


class OilCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['oil'] > fridge['oil']:
            print("need more oil")
        if self._next_handler:
            return super().check(checklist)


class ButterCheck(AbstractChecker):
    def check(self, checklist):
        if checklist['butter'] > fridge['butter']:
            print("need more butter")
        if self._next_handler:
            return super().check(checklist)


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


def check_ingridients(checklist):
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

    is_enough_eggs.check(checklist)


check_ingridients(ingridients_list)
