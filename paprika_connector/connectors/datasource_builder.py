import json


def build(filename):

    with open(filename) as fp:
        data = json.load(fp)
        return data
