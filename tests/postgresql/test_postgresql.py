import unittest
import os
from paprika_connector.connectors.connector_factory import ConnectorFactory
from paprika_connector.connectors import datasource_builder
from tests.postgresql.repositories.property.property_repository import PropertyRepository


# thread safety
# connect to azure mssql database using ssl.

# done, parameters
# done, insert return autoincrement
# done, multiple inserts, executemany
# done, insert transactions commit, rollback
# done, insert autonomous transactions


class TestPostgreSQL(unittest.TestCase):

    def system_environment(self):
        return os.environ.get('ENVIRONMENT', 'local')

    def test_is_connected(self):
        """
        This test succeeds when the connector.is_connected methods returns True
        when a database connection is established and False when there is no database connection.
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        expected = True
        self.assertEqual(expected, connector.is_connected(), 'not connected')

        connector.close()
        expected = False
        self.assertEqual(expected, connector.is_connected(), 'connected')

    def test_find_by_name(self):
        """
        This tests succeeds when the property application.version is returned.
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)
        property_ = property_repository.find_by_name('application.environment')

        self.assertIsNotNone(property_, 'no property')

        version = property_.get('value')
        self.assertIsNotNone('no environment')

        expected = self.system_environment()
        self.assertEqual(version, expected, 'invalid environment')

        connector.close()

    def test_list(self):
        """
        This test succeeds when a list of properties is returned.
        :return:
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)
        properties = property_repository.list()

        self.assertIsNotNone(properties, 'no properties')

        count = len(properties)
        expected = 0
        self.assertGreater(count, expected, 'invalid count')

        connector.close()

    def test_value(self):
        """
        This test succeeds when the value of the property application.version is returned.
        The expected value is 1.0.0
        :return:
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)
        environment = property_repository.value('application.environment')
        self.assertIsNotNone(environment, 'no environment')

        expected = self.system_environment()
        self.assertEqual(environment, expected, 'invalid environment')

        connector.close()

    def test_insert(self):
        """
        This test succeeds when the property application.name is insert and
        the new id is returned.
        :return:
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)

        property_ = {
            'name': 'application.name',
            'value': 'acme'
        }

        id_ = property_repository.insert(property_)

        property_ = property_repository.find_by_name('application.name')
        self.assertIsNotNone('no property')

        name = property_.get('value')
        self.assertIsNotNone('no application.name')

        expected = 'acme'
        self.assertEqual(name, expected, 'invalid name')

        expected = property_.get('id')
        self.assertIsNotNone(expected, 'no id')
        self.assertEqual(expected, id_, 'invalid id')
        connector.rollback()
        connector.close()

    def test_inserts(self):
        """
        This test succeeds when 2 properties are inserted using execute_many.
        :return:
        """
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)

        properties = list()

        property_ = dict(name='application.name', value='acme')
        properties.append(property_)

        property_ = dict(name='application.loglevel', value='debug')
        properties.append(property_)

        property_repository.inserts(properties)

        property_ = property_repository.find_by_name('application.name')
        self.assertIsNotNone(property_, 'no property')
        name = property_.get('value')
        self.assertIsNotNone(name, 'no application.name')
        expected = 'acme'
        self.assertEqual(name, expected, 'invalid name')

        connector.rollback()
        connector.close()

    def test_commit(self):
        """This tests succeeds when a property is committed and deleted."""
        datasource = datasource_builder.build("acme-ds.json")

        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)

        property_ = dict(name='test.application.name', value='acme')
        property_repository.insert(property_)

        connector.commit()
        connector.close()

        # open a new connection
        connector = ConnectorFactory.create_connector(datasource)
        connector.connect()

        property_repository = PropertyRepository(connector)
        property_ = property_repository.find_by_name('test.application.name')
        self.assertIsNotNone(property_, 'no property')
        id_ = property_.get('id')
        self.assertIsNotNone('no id')

        property_repository.delete_by_id(id_)

        connector.commit()
        connector.close()


if __name__ == '__main__':
    unittest.main()
