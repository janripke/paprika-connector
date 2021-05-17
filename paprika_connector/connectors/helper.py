import datetime
from paprika_connector.system import ora


def cursor_to_json(cursor):
    results = cursor.fetchall()
    response = list()
    for r in range(len(results)):
        descriptions = cursor.description
        record = dict()
        for i in range(0, len(cursor.description)):
            field_name = descriptions[i][0].lower()

            # in postgresql the fieldnames are returned in bytes
            if isinstance(field_name, bytes):
                field_name = field_name.decode()

            if str(results[r][i]) == 'None':
                record[field_name] = ''
            if isinstance(results[r][i], datetime.datetime):
                record[field_name] = str(results[r][i])
            else:
                record[field_name] = results[r][i]
        response.append(record)
    return response


def dict_to_tuple(keywords, params):
    bindings = list()
    for keyword in keywords:
        bindings.append(params.get(keyword))
    return tuple(bindings)


def list_to_tuple(keywords, params):
    bindings = list()
    for param in params:
        bindings.append(dict_to_tuple(keywords, param))
    return tuple(bindings)
