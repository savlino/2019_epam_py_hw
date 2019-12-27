"""
implementing Abstract Factory pattern via python
"""

import yaml
from datetime import *
from calendar import day_name

with open(r'./menu/menu.yml') as m:
    menulist = yaml.load(m, Loader=yaml.FullLoader)


class AbstractMenu:
    def create_first_course(self):
        raise NotImplementedError()

    def create_second_course(self):
        raise NotImplementedError()

    def create_drink(self):
        raise NotImplementedError()


class FirstCourse:
    def __init__(self, menu):
        today = day_name[date.weekday(datetime.now())]
        self.serving = menulist[today]['first_courses'][menu]

    def __str__(self):
        return f"serve {self.serving}"


class SecondCourse:
    def __init__(self, menu):
        today = day_name[date.weekday(datetime.now())]
        self.serving = menulist[today]['second_courses'][menu]

    def __str__(self):
        return f"serve {self.serving}"


class Drink:
    def __init__(self, menu):
        today = day_name[date.weekday(datetime.now())]
        self.serving = menulist[today]['drinks'][menu]

    def __str__(self):
        return f"serve {self.serving}"


class VeganMenu(AbstractMenu):
    def __init__(self):
        self.menu = 'vegan'

    def serve_first_course(self):
        return FirstCourse(self.menu)

    def serve_second_course(self):
        return SecondCourse(self.menu)

    def serve_drink(self):
        return Drink(self.menu)


class ChildMenu(AbstractMenu):
    def __init__(self):
        self.menu = 'child'

    def serve_first_course(self):
        return FirstCourse(self.menu)

    def serve_second_course(self):
        return SecondCourse(self.menu)

    def serve_drink(self):
        return Drink(self.menu)


class ChineseMenu(AbstractMenu):
    def __init__(self):
        self.menu = 'china'

    def serve_first_course(self):
        return FirstCourse(self.menu)

    def serve_second_course(self):
        return SecondCourse(self.menu)

    def serve_drink(self):
        return Drink(self.menu)
