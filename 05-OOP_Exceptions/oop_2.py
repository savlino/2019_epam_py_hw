"""
defines updated version of three classes for operating over homeworks
"""

import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Homework:
    """creates instances of homework with given text and days"""
    def __init__(self, text, num_days):
        self.text = text
        self.num_days = num_days
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=num_days)

    def is_active(self):
        if (self.deadline + self.created) > datetime.datetime.now():
            return True
        else:
            return False


class Person:
    """parent class for person's names"""
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """checks if homework instance is active"""
    def do_homework(self, Homework, solution):
        if Homework.is_active():
            return HomeworkResult(self.last_name, Homework, solution)
        else:
            raise DeadlineError("You're late")


class HomeworkHadler(Person):
    """class, containing set of methods to handle homeworking process"""
    homework_done = defaultdict(list)

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def check_homework(self, hw):
        if len(hw.solution) > 5:
            self.homework_done[hw.homework].append(hw)
            return True
        else:
            return False

    def reset_results(*hw):
        if hw:
            HomeworkHadler.homework_done.remove(hw)
        else:
            HomeworkHadler.homework_done = None


class Teacher(HomeworkHadler):
    """creates homeworks"""
    def create_homework(self, text, num_days):
        return Homework(text, num_days)


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError('You gave a not Homework object')

        if type(solution) == str:
            self.solution = solution
        else:
            raise ValueError('solution must be a string')
        self.created = datetime.datetime.now()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
