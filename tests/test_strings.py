from paprika_connector.system import strings


def test_two_keywords():
    """
    This test passes when the keywords name and value are returned in a list.
    """
    statement = "select * from application_properties where name=:name and value=:value"
    keywords = strings.keywords(statement, ':')
    assert keywords == ['name', 'value'], "invalid keywords, ['name', 'value'] expected"


def test_no_keywords():
    """
    This test passes when no keywords are found in the given string, an empty list is returned,
    """
    statement = "select name, value from application_properties"
    keywords = strings.keywords(statement, ':')
    assert keywords == [], "invalid keywords, empty list expected"

    statement = ""
    keywords = strings.keywords(statement, ':')
    assert keywords == [], "invalid keywords, empty list expected"


def test_two_indexes():
    """
    This test passes when the given key is found two times in the given string
    A list is returned containing the indexes of the given key in the given string.
    """
    statement = "select * from application_properties where name=:name and value=:value"
    indexes = strings.split_index(statement, ":")
    assert indexes == [48, 64], "invalid indexes, keys expected on position 48, 64"


def test_one_index():
    """
    This test passes when the given key is found once in the given string.
    A list is returned containing the index of the given key in the given string.
    """
    statement = ":name"
    indexes = strings.split_index(statement, ":")
    assert indexes == [0], "invalid indexes, keys expected on position 0"

    statement = " :name "
    indexes = strings.split_index(statement, ":")
    assert indexes == [1], "invalid indexes, keys expected on position 1"


def test_word():
    """
    This test passes when the word starting at the given index is returned
    """
    statement = ":name "
    word = strings.word(statement, 0)
    assert word == 'name'

    statement = ":name"
    word = strings.word(statement, 0)
    assert word == 'name'

    statement = ":name and value=:value"
    word = strings.word(statement, 0)
    assert word == 'name'


# class TestStrings(unittest.TestCase):
#     def test_concat_pass(self):
#         """
#         This test succeeds when the connector.is_connected methods returns True
#         when a database connection is established and False when there is no database connection.
#         """
#         expected = 'a b c'
#         result = strings.concat('a', 'b')
#         print(result)
#         self.assertEqual(expected, result, 'concat failed')
#
#
# if __name__ == '__main__':
#     unittest.main()
