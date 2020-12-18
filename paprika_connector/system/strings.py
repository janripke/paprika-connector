def concat(*args):
    count = len(args)
    result = ""
    for i in range(count):
        result = result + args[i] + ' '
    result.rstrip(' ')
    return result


def split_index(s, key):
    count = len(s)
    result = []
    for i in range(0, count):
        if s[i] == key:
            result.append(i)
    return result


def word(s, index):
    count = len(s)
    result = ''
    for i in range(index + 1, count):
        if s[i] not in ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'):
            return result
        result += s[i]
    return result


def keywords(s, key):
    indexes = split_index(s, key)
    results = []
    for index in indexes:
        results.append(word(s, index))
    return results
