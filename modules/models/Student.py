class Student:
    table_name = 'students'

    def __init__ (self):
        self.db = db.define_table(self.table_name,
            Field('name'),
            Field('last_name'),
            Field('birth_date', 'date'),
            Field('id_number'),
            Field('phone'),
            format='%(nombre)s'
        )
    
    def getModel(self):
        return self.db