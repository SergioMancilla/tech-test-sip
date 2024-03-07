from .. import db

class Classroom:
    table_name = 'classrooms'

    def __init__ (self):
        self.db = db.define_table(self.table_name,
            Field('name'),
            Field('description'),
            Field('monitor'),
            format='%(nombre)s'
        )
    
    def getModel(self):
        return self.db