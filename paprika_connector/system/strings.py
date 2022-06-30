def concat(*args):
    count = len(args)
    result = ""
    for i in range(count):
        result = result + args[i] + ' '
    result.rstrip(' ')
    return result


def split_index(s: str, key: str) -> list[int]:
    """
    Returns a list containing the positions of the given key in the given string
    """
    count = len(s)
    result = []
    for i in range(0, count):
        if s[i] == key:
            result.append(i)
    return result


def word(s: str, index: int) -> str:
    """
    Returns the word starting at the given index
    """
    count = len(s)
    result = ''
    for i in range(index + 1, count):
        if s[i] not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            return result
        result += s[i]
    return result


def keywords(s: str, key: str) -> list[str]:
    """
    Returns a list of keywords. A keyword starts with the given key.
    """
    indexes = split_index(s, key)
    results = []
    for index in indexes:
        results.append(word(s, index))
    return results
