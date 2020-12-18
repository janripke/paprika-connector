import logging

import pyodbc

from paprika_connector.system import strings
from paprika_connector.connectors.connector import Connector
from paprika_connector.connectors import helper
from paprika_connector.system import connection_string_builders


class OdbcConnector(Connector):
    def __init__(self, datasource):
        Connector.__init__(self, datasource)
        self.__driver = datasource['driver']
        self.__host = datasource['host']
        self.__username = datasource['username']
        self.__password = datasource['password']
        self.__database = datasource['db']
        self.__charset = datasource.get('charset', 'utf-8')
        self.__autocommit = datasource.get('autocommit', False)

    def get_driver(self):
        return self.__driver

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

    def get_autocommit(self):
        return self.__autocommit

    def statement(self, statement, params):
        # retrieve the keywords in the statement
        keywords = strings.keywords(statement, ':')

        # replace the keywords with the expected binding character, differs per databases.
        s = statement
        for keyword in keywords:
            s = s.replace(":" + keyword, '?', 1)

        # create the database typical binding parameters, a tuple
        if isinstance(params, list):
            bindings = helper.list_to_tuple(keywords, params)
        else:
            bindings = helper.dict_to_tuple(keywords, params)

        return s, bindings

    def is_connected(self):
        try:
            connection = self.get_connection()
            if connection:
                cursor = connection.cursor()
                statement = "select getdate()"
                cursor.execute(statement)
                results = cursor.fetchone()

                if results:
                    return True
            return False
        except Exception:
            return False

    def autonomous_connect(self):
        driver = self.get_driver()
        host = self.get_host()
        username = self.get_username()
        password = self.get_password()
        database = self.get_database()
        charset = self.get_charset()
        autocommit = self.get_autocommit()

        connection_string = connection_string_builders.odbc(driver,
                                                            host, database, username, password)
        connection = pyodbc.connect(connection_string, autocommit=autocommit)
        connection.setencoding(charset)
        logging.debug('connected to mssql database at {}'.format(host))
        return connection

    def connect(self):
        driver = self.get_driver()
        host = self.get_host()
        username = self.get_username()
        password = self.get_password()
        database = self.get_database()
        charset = self.get_charset()
        autocommit = self.get_autocommit()
        connection_string = connection_string_builders.odbc(driver,
                                                            host, database, username, password)
        connection = pyodbc.connect(connection_string, autocommit=autocommit)
        connection.setencoding(charset)
        logging.debug('connected to mssql database at {}'.format(host))
        self.set_connection(connection)

    def lastrowid(self, cursor):
        cursor.execute("SELECT @@IDENTITY")
        # cursor.execute("SELECT SCOPE_IDENTITY()")
        result = cursor.fetchone()
        return result[0]
