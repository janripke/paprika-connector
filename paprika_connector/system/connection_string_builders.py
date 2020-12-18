def parameter(option, value):
    if value:
        return "{}{};".format(option, value)


def odbc(driver, host, db, username, password):
    result = "{}{}{}{}{}".format(
        parameter('DRIVER=', driver),
        parameter('SERVER=', host),
        parameter('DATABASE=', db),
        parameter('UID=', username),
        parameter('PWD=', password)
    )
    return result.strip(' ')

