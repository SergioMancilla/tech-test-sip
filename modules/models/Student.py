from datetime import date

from applications.sip_students.modules.models.Classroom import Classroom

class Student:
    def __init__ (self, name: str, last_name: str, birth_date: date, id_number: str, phone: str, classroom: Classroom = None):

        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id_number = id_number
        self.phone = phone
        self.classroom = classroom
