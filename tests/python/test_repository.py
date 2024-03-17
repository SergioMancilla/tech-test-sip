import unittest

from modules.repository.StudentRepository import StudentRepository

class TestStudentReposiroty(unittest.TestCase):

    def __init__(self):
        self.student_repository = StudentRepository()

    def test_get_students_by_classroom(self):
        self.student_repository.get_students_by_classroom(1)