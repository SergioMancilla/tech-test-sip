from applications.sip_students.modules.models.Base import Base
import gluon.dal as dal

class Classroom:
    table_name = 'classrooms'

    def __init__ (self):
        Base.__init__(self)

        self.table_for_show = self.db.define_table(self.table_name,
            dal.Field('name', 'string'),
            dal.Field('description', 'string'),
            dal.Field('monitor', 'string'),
            format='%(nombre)s'
        )

    def get_model(self):
        '''Returns the DB classroom object for use in SQLFORM.grid'''
        return self.table_for_show
    