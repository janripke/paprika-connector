from datetime import datetime


def nvl(*args):
    count = len(args)
    if count != 2:
        raise RuntimeError("invalid number of arguments")

    if args[0] is not None:
        return args[0]
    return args[1]


def nvl2(*args):
    count = len(args)
    if count != 3:
        raise RuntimeError("invalid number of arguments")

    if args[0] is not None:
        return args[1]
    return args[2]


def nnvl(*args):
    count = len(args)
    if count != 2:
        raise RuntimeError("invalid number of arguments")
    if args[0] is None:
        return args[0]
    return args[1]


def nnvl2(*args):
    count = len(args)
    if count != 3:
        raise RuntimeError("invalid number of arguments")
    if args[0] is None:
        return args[1]
    return args[2]


def decode(*args):
    count = len(args)
    if count < 3:
        raise RuntimeError("not enough arguments for method")
    key = args[0]
    for i in range(1, count - 1, 2):
        if key == args[i]:
            return args[i + 1]
    if count % 2 == 0:
        return args[count - 1]


def nnvl_decode(*args):
    count = len(args)
    if count < 3:
        raise RuntimeError("not enough arguments for method")
    for i in range(0, count - 1, 2):
        if args[i]:
            return args[i + 1]
    if not count % 2 == 0:
        return args[count - 1]


def substr(s, start, count):
    if s:
        return s[start:count]
    return s


def fsdate(s, string_format, target_format):
    if s:
        return datetime.strftime(datetime.strptime(s, string_format), target_format)
    return None


def iif(*args):
    count = len(args)
    if count < 3:
        raise RuntimeError("not enough arguments for method")
    if args[0].has_key(args[1]):
        return args[0][args[1]]
    return args[2]
