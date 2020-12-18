class ConnectorFactory:

    @staticmethod
    def create_connector(datasource):
        if datasource['type'] == 'mysql':
            from paprika_connector.connectors.mysql_connector import MysqlConnector
            return MysqlConnector(datasource)
        if datasource['type'] == 'postgresql':
            from paprika_connector.connectors.postgresql_connector import PostgresqlConnector
            return PostgresqlConnector(datasource)
        if datasource['type'] == 'mssql':
            from paprika_connector.connectors.mssql_connector import MssqlConnector
            return MssqlConnector(datasource)
        if datasource['type'] == 'odbc':
            from paprika_connector.connectors.odbc_connector import OdbcConnector
            return OdbcConnector(datasource)
