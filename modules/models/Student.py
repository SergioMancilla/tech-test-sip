from applications.sip_students.modules.repository.StudentRepository import StudentRepository
from applications.sip_students.modules.models.Base import Base

class Student:
    table_name = 'students'
    obj = {}

    def __init__ (self, name, last_name, birth_date, id_number, phone):
        Base.__init__(self)
        self.obj.name = name
        self.obj.last_name = last_name
        self.obj.birth_date = birth_date
        self.obj.id_number = id_number
        self.obj.phone = phone

    def save(self) -> None:
        StudentRepository.save_in_bd(self.obj)