from paprika_connector.connectors import helper
import inspect
import os


class Repository(object):
    def __init__(self, connector):
        object.__init__(self)
        self.__connector = connector
        self.__sequence = None

    def to_param(self, record):
        result = ''
        fields = record.keys()
        for field in fields:
            result = result + ":" + field + ","
        result = result.rstrip(',')
        return result

    def _load(self, filename):
        path = os.path.join(os.path.dirname(inspect.getfile(self.__class__)), filename)

        f = open(path)
        statement = f.read()
        f.close()
        return statement

    def _delete(self, statement, params):
        connector = self.get_connector()
        cursor = connector.cursor()

        statement, parameters = self.statement(statement, params)
        cursor.execute(statement, parameters)
        cursor.close()

    def _find(self, statement, params):
        connector = self.get_connector()
        cursor = connector.cursor()

        statement, parameters = self.statement(statement, params)
        cursor.execute(statement, parameters)
        result = helper.cursor_to_json(cursor) or []
        cursor.close()

        if len(result) == 0:
            return None

        return result[0]

    def _list(self, statement, params=None):
        connector = self.get_connector()
        cursor = connector.cursor()

        if params:
            statement, parameters = self.statement(statement, params)
            cursor.execute(statement, parameters)
        else:
            cursor.execute(statement)

        return helper.cursor_to_json(cursor) or []

    def _insert(self, statement, params=None):
        connector = self.get_connector()
        cursor = connector.cursor()

        statement, parameters = self.statement(statement, params)

        cursor.execute(statement, parameters)
        return connector.lastrowid(cursor)

    def _inserts(self, statement, params=None):
        connector = self.get_connector()
        cursor = connector.cursor()

        statement, parameters = self.statement(statement, params)
        cursor.executemany(statement, parameters)

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, sequence):
        self.__sequence = sequence

    def nextval(self):
        sequence = self.get_sequence()

        if sequence:
            with self.get_connection() as cursor:
                params = dict()

                statement = "select " + sequence + ".nextval from dual"
                statement, parameters = self.statement(statement, params)

                cursor.execute(statement, parameters)
                result = helper.cursor_to_json(cursor)

            if len(result) == 0:
                return None
            return result[0].get('nextval')

        return None

    def get_connector(self):
        return self.__connector

    def get_connection(self):
        connector = self.get_connector()
        if not connector.is_connected():
            connection = connector.connect()
            connector.set_connection(connection)
        return connector.get_connection()

    def statement(self, statement, message):
        connector = self.get_connector()
        return connector.statement(statement, message)

    def has_lastrowid(self):
        connector = self.get_connector()
        datasource = connector.get_datasource()
        if datasource['type'] in ['oracle', 'postgresql']:
            return False
        return True
