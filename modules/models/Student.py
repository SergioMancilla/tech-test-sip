from applications.sip_students.modules.models.Base import Base
import gluon.dal as dal

class Student:
    table_name = 'students'

    def __init__ (self):
        Base.__init__(self)

        self.table = self.db.define_table(self.table_name,
            dal.Field('name', 'string'),
            dal.Field('last_name', 'string'),
            dal.Field('birth_date', 'date'),
            dal.Field('id_number', 'string'),
            dal.Field('phone', 'string'),
            format='%(nombre)s'
        )

    def get_model(self):
        '''Returns the DB student object for use in SQLFORM.grid'''
        return self.table
    