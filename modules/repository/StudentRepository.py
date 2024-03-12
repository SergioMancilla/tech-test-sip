from alembic import op
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

class StudentRepository:

    def __init__(self):
        self.table = table('students',
            column('id', Integer),
            column('name', String),
            column('last_name', String),
            column('birth_date', Date),
            column('id_number', String),
            column('phone', String)
        )

    def save_in_bd(self, obj: dict):
        ''' Save a student in BD, depending of the obj attribute with the fields: name, last_name, birth_date, id_number and phone '''
        op.bulk_insert(
            self.table,
            [
                {
                    'name': obj['name'],
                    'last_name': obj['last_name'],
                    'birth_date': obj['birth_date'],
                    'id_number': obj['id_number'],
                    'phone': obj['phone'],
                }
            ],
            multiinsert=False
        )