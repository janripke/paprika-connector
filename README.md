paprika_connector
=

paprika_connector, this projects, is a package for developers who want to use a database without the burden of creating and maintaining an ORM.
The Repository concept is introduced instead. Every repository class reflects ideally a table in your database. Every method the action you want to execute on the data. Your SQL statement is visible and part of this method.


# Installation
paprika_connector currently supports Python 3.5 and higher.

## Install from github
```
$ pip install git+https://github.com/janripke/paprika-connector.git@0.0.6#egg=paprika_connector
```

## Clone and install from source
```
git clone https://github.com/janripke/paprika-connector.git
$ cd paprika-connector
# Checkout the release you want to use 
# (NOTE: the master branch is NOT guaranteed to be stable!)
$ git checkout tags/0.0.5
$ pip install . 
```

# Quick start

## minimal connection example
In the following example a connection is made to a postgresql database server.
It is assumed that the database server is present on your localhost.
It is also assumed that the database acme is present.

After connecting a cursor is retrieved and the system datetime is retrieved from
the data server.
```
from paprika_connector.connectors.connector_factory import ConnectorFactory

acme_ds = {
  'type': 'postgresql',
  'host': 'localhost',
  'db': 'acme',
  'username': 'acme_owner',
  'password': 'acme_owner' 
}

connector = ConnectorFactory.create_connector(acme_ds)
cursor = connector.cursor()
cursor.execute("select current_date")
results = cursor.fetchone()
print(results)
connector.connect()
connector.close()
```

