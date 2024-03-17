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

        print('aquí')
        engine = self.config.get('postgres_connection.engine')
        host = self.config.get('postgres_connection.host')
        user = self.config.get('postgres_connection.user')
        password = self.config.get('postgres_connection.password')
        database = self.config.get('postgres_connection.database')

        print(engine)

        conn_string = self.config.get('database.conn_string')

        formatted_conn_string = conn_string.format(
            engine=engine, user=user, password=password, host=host, database=database
        )

        print(formatted_conn_string)

        return formatted_conn_string