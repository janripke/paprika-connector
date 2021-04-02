def set_formatter(dict_, excludes):
    result = ''
    if dict_:
        keys = dict_.keys()
        for key in keys:
            if key not in excludes:
                result += '{}=:{}, '.format(key, key)
        result = result.rstrip(', ')
    return result


def values_formatter(dict_, excludes=[], ignore_none=True):
    columns = []
    values = []
    if dict_:
        keys = dict_.keys()
        for key in keys:
            if key not in excludes:
                if not ignore_none or dict_[key]:
                    columns.append(f'{key}')
                    values.append(f':{key}')
        columns = ",".join(columns)
        values = ",".join(values)
        return f'({columns}) values ({values})'
