from gluon.dal import Field

from applications.sip_students.modules.models.Student import Student
from applications.sip_students.modules.models.Classroom import Classroom
from applications.sip_students.modules.repository.BaseRepository import BaseRepository
from applications.sip_students.modules.repository.ClassroomRepository import ClassroomRepository

class StudentRepository(BaseRepository):

    __tablename__ = 'students'

    def __init__(self):
        BaseRepository.__init__(self)

        classroom_table = self.get_classroom_model()

        self.table = self.db.define_table(
            self.__tablename__,
            Field('name', 'string'),
            Field('last_name', 'string'),
            Field('birth_date', 'date'),
            Field('id_number', 'string', unique=True),
            Field('phone', 'string'),
            Field('classroom_id', classroom_table),
            format='%(name)s'
        )

    def get_classroom_model(self):
        ''' Used for references classroom_id field '''
        return self.db.define_table('classrooms')

    def get_model(self):
        ''' Return the table structure '''
        return self.table

    def save(self, student: Student) -> None:
        ''' Store a student in BD '''

        classroom_id = student.classroom.id if student.classroom else None

        self.db[self.__tablename__].insert(
            name = student.name,
            last_name = student.last_name,
            birth_date = student.birth_date,
            id_number = student.id_number,
            phone = student.phone,
            classroom_id = classroom_id
        )

    def get_db_object(self):
        ''' Return database instance for classrooms '''
        return self.db[self.__tablename__]

    def get_students_by_classroom(self, classroom_id: int):
        ''' Return the list of students for a given classroom '''

        students_table = self.get_db_object()
        query = students_table.classroom_id == classroom_id
        students = self.db(query).select()
        return students
        