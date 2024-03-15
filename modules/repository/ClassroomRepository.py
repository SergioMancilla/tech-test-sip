from gluon.dal import Field

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
