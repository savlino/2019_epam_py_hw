"""
defines three classes for operating over homeworks
"""

import datetime


class Homework:
    # creates instances of homework with given text and days
    def __init__(self, text, num_days):
        self.text = text
        self.num_days = num_days
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=num_days)

    def is_active(self):
        if (self.deadline + self.created) < datetime.datetime.now():
            return True
        else:
            return False


class Student:
    # checks if homework instance is active
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, Homework):
        if Homework.is_active():
            return Homework
        else:
            print("You're late")


class Teacher:
    # creates homeworks
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, num_days):
        return Homework(text, num_days)


if __name__ == '__main__':
    teacher = Teacher('Shadrin', 'Daniil')
    student = Student('Petrov', 'Roman')
    teacher.first_name  # Daniil
    student.last_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
