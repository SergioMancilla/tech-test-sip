from gluon.dal import Field

from applications.sip_students.modules.models.Student import Student
from applications.sip_students.modules.models.Classroom import Classroom
from applications.sip_students.modules.repository.BaseRepository import BaseRepository

class ClassroomRepository(BaseRepository):
    
    __tablename__ = 'classrooms'

    def __init__(self):
        BaseRepository.__init__(self)

        self.table = self.db.define_table(
            self.__tablename__,
            Field('name', 'string'),
            Field('description', 'string'),
            Field('monitor', 'string'),
            format='%(name)s'
        )

    def get_model(self):
        ''' Return the table structure for SQLForm or other purposes '''
        return self.table
    
    def get_db_object(self):
        ''' Return database instance for classrooms '''
        return self.db[self.__tablename__]
    
    def get_all_classrooms(self):
        ''' Fetch all classrooms '''
        table = self.get_db_object()
        registers = self.db(table).select()
        return registers

    def save_classroom(self, classroom: Classroom) -> None:
        ''' Store a classroom in BD '''

        self.db[self.__tablename__].insert(
            name = classroom.name,
            description = classroom.description,
            monitor = classroom.monitor,
        )

