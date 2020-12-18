import logging


class Connector:
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__connection = None

    def __del__(self):
        self.close()

    def get_datasource(self):
        return self.__datasource

    def get_connection(self):
        return self.__connection

    def set_connection(self, connection):
        self.__connection = connection
        
    def connect(self):
        pass

    def cursor(self):
        if not self.is_connected():
            self.connect()
            
        connection = self.get_connection()
        return connection.cursor()

    def is_connected(self):
        connection = self.get_connection()
        if connection:
            if connection.open:
                return True
        return False

    def commit(self):
        connection = self.get_connection()
        connection.commit()

    def rollback(self):
        connection = self.get_connection()
        connection.rollback()

    def close(self):
        connection = self.get_connection()
        if connection:
            if self.is_connected():
                connection.close()
                ds = self.get_datasource()
                logging.debug('closed connection to {} on host {}'.format(ds['type'], ds['host']))
            self.set_connection(None)

    def lastrowid(self, cursor):
        pass
