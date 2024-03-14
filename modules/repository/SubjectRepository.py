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