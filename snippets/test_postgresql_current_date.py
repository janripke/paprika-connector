from paprika_connector.connectors.connector_factory import ConnectorFactory

acme_ds = {
  'type': 'postgresql',
  'host': 'localhost',
  'db': 'acme',
  'username': 'acme_owner',
  'password': 'acme_owner'
}


class Cursor:
    def __init__(self, cursor):
        self.__cursor = cursor


connector = ConnectorFactory.create_connector(acme_ds)
cursor = connector.cursor()

# trying to return a json object instead of a tuple
cursor = Cursor(cursor)


print(cursor)
exit(0)

cursor.execute("select current_date")
results = cursor.fetchone()
print(results)
connector.connect()
connector.close()
