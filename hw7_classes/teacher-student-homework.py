''' defines three classes for operating over homeworks
'''

import datetime


class Homework:
    # creates instances of homework with given text and days
    def __init__(self, text, num_days):
        self.text = text
        self.num_days = num_days
        self.created = str(datetime.datetime.now())
        self.deadline = str(datetime.timedelta(days=num_days))

    def is_active(self):
        try:
            if datetime.datetime.strptime(
                self.created, "%Y-%m-%d %H:%M:%S.%f"
            ) + datetime.timedelta(
                int(self.deadline.split(' ')[0])
            ) >= datetime.datetime.now():
                return True
            else:
                return False
        except (ValueError):
            return False


class Student:
    # checks if homework instance is active
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(Homework):
        if Homework.is_active():
            return Homework
        else:
            print("You're late")


class Teacher:
    # creates homeworks
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, num_days):
        return Homework(text, num_days)
