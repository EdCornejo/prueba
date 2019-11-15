import unittest
import sys
from datetime import datetime, date, time, timedelta

import constantes
sys.path.append('..')

from brujula.exception.brujula_exception import BrujulaException
from brujula.core.models import Person, Professor, ActingProfessor, DepartmentProfessors


class MainTest(unittest.TestCase):

	def test_departmentProfessors_list_same(self):

		profesor1 = Professor(constantes.NOM_JUAN, constantes.SURNAME_PEREZ, constantes.YEAR_90, constantes.DEPARTMENT_MATHS)
		profesor2 = Professor(constantes.NOM_MANOLO, constantes.SURNAME_CASARES, constantes.YEAR_80, constantes.DEPARTMENT_MATHS)
		profesor3 = Professor(constantes.NOM_JOSE, constantes.SURNAME_MORALES, constantes.YEAR_70, constantes.DEPARTMENT_MATHS)

		department_professors = DepartmentProfessors(constantes.DEPARTMENT_MATHS)
		department_professors.add_professor(profesor1)
		department_professors.add_professor(profesor2)
		department_professors.add_professor(profesor3)

		list_professors = []
		list_professors.append(profesor2)
		list_professors.append(profesor3)
		list_professors.append(profesor1)

		current_department_professors = department_professors.list()

		self.assertListEqual(list_professors, current_department_professors)

	def test_professorSurname_too_long(self):
		with self.assertRaises(BrujulaException) as e:
			Professor(constantes.NOM_MARIA, constantes.SURNAME_TOO_LONG, constantes.YEAR_90, constantes.DEPARTMENT_MATHS)

	def test_professor_with_distinct_department(self):
		department_professors = DepartmentProfessors(constantes.DEPARTMENT_MATHS)
		distinct_deptartment_professor = Professor(constantes.NOM_JUAN, constantes.SURNAME_LOPEZ, constantes.YEAR_90, constantes.DEPARTMENT_HISTORY)

		with self.assertRaises(BrujulaException) as e:
			department_professors.add_professor(distinct_deptartment_professor)

	def test_acting_professor_enddate_below_today(self):
		end_date_yesterday = date.today() - timedelta(days=1)

		with self.assertRaises(BrujulaException) as e:
			ActingProfessor(constantes.NOM_MARTA, constantes.SURNAME_GUTIERREZ, constantes.YEAR_90, constantes.DEPARTMENT_MATHS, end_date_yesterday)

	def test_professor_complete_name(self):
		professor = Professor(constantes.NOM_ELENA, constantes.SURNAME_JIMENEZ, constantes.YEAR_90, constantes.DEPARTMENT_MATHS)
		expected_professor_complete_name = '{}, {}'.format(constantes.SURNAME_JIMENEZ, constantes.NOM_ELENA)

		self.assertEqual(expected_professor_complete_name, professor.complete_name())

	def test_person_age(self):
		today = date.today()
		local_date_of_bird = date(1990, 1, 1)
		person = Person(constantes.NOM_JORGE, constantes.SURNAME_RAMOS, constantes.YEAR_90)
		expected_age_for_born_in_90 = today.year - local_date_of_bird.year

		self.assertEqual(expected_age_for_born_in_90, person.age())

	def test_department_name_null(self):
		with self.assertRaises(BrujulaException) as e:
			departmentProfessors = DepartmentProfessors(None)


if __name__ == "__main__":
	unittest.main()