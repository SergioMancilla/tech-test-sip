from gluon.contrib.appconfig import AppConfig
from gluon import DAL

class BaseRepository:
    ''' Class for connecting with the DB '''

    _instance = None

    config = AppConfig(reload=True)

    def __init__(self):
        conn_string = self.get_db_connection_string()
        self.db = DAL(conn_string, migrate=False, migrate_enabled=False, pool_size=self.config.get('database.pool_size'))

    def get_db_connection_string(self):
        ''' Get the connection string for database '''
        return self.config.get('database.conn_string')