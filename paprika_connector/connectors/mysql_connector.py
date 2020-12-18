import MySQLdb
from paprika_connector.system import strings
from paprika_connector.connectors.connector import Connector
from paprika_connector.connectors import helper


class MysqlConnector(Connector):

    def __init__(self, datasource):
        Connector.__init__(self, datasource)
        self.__host = datasource['host']
        self.__username = datasource['username']
        self.__password = datasource['password']
        self.__database = datasource['db']
        self.__charset = datasource.get('charset', 'utf8')

    def get_host(self):
        return self.__host

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_database(self):
        return self.__database

    def get_charset(self):
        return self.__charset

    def statement(self, statement, params):
        # retrieve the keywords in the statement
        keywords = strings.keywords(statement, ':')

        # replace the keywords with the expected binding character, differs per databases.
        s = statement
        for keyword in keywords:
            s = s.replace(":" + keyword, '%s', 1)

        # create the database typical binding parameters, a tuple
        if isinstance(params, list):
            bindings = helper.list_to_tuple(keywords, params)
        else:
            bindings = helper.dict_to_tuple(keywords, params)

        return s, bindings

    def connect(self):
        host = self.get_host()
        username = self.get_username()
        password = self.get_password()
        database = self.get_database()
        charset = self.get_charset()
        connection = MySQLdb.connect(host, username, password, database, charset=charset)
        self.set_connection(connection)

    def lastrowid(self, cursor):
        return cursor.lastrowid
