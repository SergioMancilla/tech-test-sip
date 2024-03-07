import gluon.dal as dal

class Base():
    table = None

    def __init__(self):
        self.db = dal.DAL('postgres://postgres:123456@localhost/school', migrate_enabled=False)