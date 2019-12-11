"""
class describes simple arithmetic operations over quaternions
"""
import numpy as np


class Quaternion:
    def __init__(self, matrix):
        self.a = matrix[0]
        self.i = matrix[1]
        self.j = matrix[2]
        self.k = matrix[3]
        self.scal = self.a
        self.vect = np.array([self.i, self.j, self.k])

    def __add__(self, other):
        if isinstance(other, Quaternion):
            scal_part = self.scal + other.scal
            vect_part = self.vect + other.vect
            substraction_result = [scal_part]
            substraction_result.extend(vect_part)
            return Quaternion(substraction_result)

    def __sub__(self, other):
        if isinstance(other, Quaternion):
            scal_part = self.scal - other.scal
            vect_part = self.vect - other.vect
            substraction_result = [scal_part]
            substraction_result.extend(vect_part)
            return Quaternion(substraction_result)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            scal_part = self.scal * other.scal - np.dot(self.vect, other.vect)
            vect_part = (
                np.cross(self.vect, other.vect)
                + self.scal * other.vect
                + other.scal * self.vect
            ).tolist()
            multiplication_result = [scal_part]
            multiplication_result.extend(vect_part)
            return Quaternion(multiplication_result)

    def __truediv__(self, other):
        if isinstance(other, Quaternion):
            if other.a == other.i == other.j == other.k == 0:
                raise ZeroDivisionError("division by zero not supported")
            scal_part = self.scal * other.scal + np.dot(self.vect, other.vect)
            vect_part = (
                -np.cross(self.vect, other.vect)
                - self.scal * other.vect
                + other.scal * self.vect
            ).tolist()
            division_result = [scal_part]
            division_result.extend(vect_part)
            return Quaternion(division_result)

    def __eq__(self, other):
        if isinstance(other, Quaternion):
            if self.scal == other.scal and \
                    self.vect.tolist() == other.vect.tolist():
                return True
            else:
                return False

    def __abs__(self):
        return round(np.sqrt(
            self.a ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2
        ), 3)

    def __str__(self):
        return f"{{:{self.a}}} {{:{self.i}}}i {{:{self.j}}}j {{:{self.k}}}k"

    def __repr__(self):
        return f"Quaternion({self.a}, {self.i}, {self.j}, {self.k})"
