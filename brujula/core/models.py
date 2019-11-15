
from datetime import date

from ..exception.brujula_exception import BrujulaException


class Person(object):
    """Person entity"""
    def __init__(self, name, surname, year_of_birth):
        if not name or len(name) > 20:
            raise BrujulaException("Invalid name")

        if not surname or len(surname) > 20:
            raise BrujulaException("Invalid surname")

        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth


    def complete_name(self):
        return f'{self.surname}, {self.name}'


    def age(self):
        today = date.today()
        return int(today.year - self.year_of_birth)


    def __str__(self):
        return self.surname


    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.surname == other.surname


    def __lt__(self, other):
        if self.surname and other.surname:
            return self.surname < other.surname
        elif other.surname:
            return True
        else:
            return False



class Professor(Person):
    """Professor entity"""
    def __init__(self, name, surname, year_of_birth, department):
        super(Professor, self).__init__(name, surname, year_of_birth)

        if not department or len(department) > 20:
            raise BrujulaException("Invalid department")

        self.department = department



class AssociateProfessor(Professor):
    """Associate Professor entity"""
    def __init__(self, name, surname, year_of_birth, department, start_date):
        super(AssociateProfessor, self).__init__(name, surname, year_of_birth, department)

        self.start_date = start_date



class ActingProfessor(Professor):
    """Associate Professor entity"""
    def __init__(self, name, surname, year_of_birth, department, end_date):
        super(ActingProfessor, self).__init__(name, surname, year_of_birth, department)

        if end_date < date.today():
            raise BrujulaException("End date invalid")

        self.end_date = end_date



class DepartmentProfessors(object):
    """Associate Professor entity"""
    def __init__(self, department_name, professors=[]):
        if not department_name or len(department_name) > 20:
            raise BrujulaException("Invalid department name")

        self.department_name = department_name
        self.professors = professors


    def list(self):
        self.professors.sort()
        return self.professors


    def add_professor(self, professor):
        if professor.department != self.department_name:
            raise BrujulaException("Professor department not valid")

        if professor not in self.professors:
            self.professors.append(professor)
