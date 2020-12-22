def set_formatter(dict_, excludes):
    result = ''
    if dict_:
        keys = dict_.keys()
        for key in keys:
            if key not in excludes:
                result += '{}=:{}, '.format(key, key)
        result = result.rstrip(', ')
    return result
