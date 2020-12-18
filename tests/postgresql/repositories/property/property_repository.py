from isc_connector.connectors.repository import Repository


class PropertyRepository(Repository):
    FIND_BY_NAME = 'application_properties_find_by_name.sql'
    INSERT = 'application_properties_insert.sql'
    INSERTS = 'application_properties_inserts.sql'
    VALUE = 'application_properties_value.sql'
    LIST = 'application_properties_list.sql'
    DELETE_BY_ID = 'application_properties_delete_by_id.sql'

    def find_by_name(self, name):

        # with self.get_connection() as cursor:
        statement = self._load(PropertyRepository.FIND_BY_NAME)
        params = {
            'name': name
        }

        return self._find(statement, params)

    def insert(self, property_):

        statement = self._load(PropertyRepository.INSERT)
        return self._insert(statement, property_)

    def inserts(self, properties):
        statement = self._load(PropertyRepository.INSERTS)
        self._inserts(statement, properties)

    def value(self, name, default=None):
        statement = self._load(PropertyRepository.VALUE)

        params = {
            'name': name
        }

        result = self._find(statement, params)

        if len(result) == 0:
            return default

        return result['value']

    def list(self):
        statement = self._load(PropertyRepository.LIST)

        params = dict()
        return self._list(statement, params)

    def delete_by_id(self, id_):
        statement = self._load(PropertyRepository.DELETE_BY_ID)

        params = {
            'id': id_
        }

        return self._delete(statement, params)
