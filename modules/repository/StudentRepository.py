from gluon.dal import Field

from applications.sip_students.modules.models.Student import Student
from applications.sip_students.modules.repository.BaseRepository import BaseRepository

class StudentRepository(BaseRepository):

    __tablename__ = 'students'

    def __init__(self):
        BaseRepository.__init__(self)

        self.table = self.db.define_table(
            self.__tablename__,
            Field('name', 'string'),
            Field('last_name', 'string'),
            Field('birth_date', 'date'),
            Field('id_number', 'string'),
            Field('phone', 'string'),
            format='%(name)s'
        )

    def save(self, student: Student) -> None:
        ''' Save a student in BD '''
        self.db[self.__tablename__].insert(
            name = student.name,
            last_name = student.last_name,
            birth_date = student.birth_date,
            id_number = student.id_number,
            phone = student.phone
        )
        