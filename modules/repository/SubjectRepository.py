from gluon.dal import Field

from applications.sip_students.modules.repository.BaseRepository import BaseRepository

class SubjectRepository(BaseRepository):

    __tablename__ = 'subjects'

    def __init__(self):
        BaseRepository.__init__(self)

        self.table = self.db.define_table(
            self.__tablename__,
            Field('name', 'string'),
            Field('description', 'string')
        )

    def get_model(self):
        ''' Return the table structure for SQLForm or other purposes '''
        return self.table
    
    def get_db_object(self):
        ''' Return database instance for subjects '''
        return self.db[self.__tablename__]
    
    def get_all_subjects(self):
        ''' Fetch all classrooms '''
        table = self.get_db_object()
        registers = self.db(table).select()
        return registers