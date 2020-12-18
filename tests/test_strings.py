import unittest
from paprika_connector.system import strings


class TestStrings(unittest.TestCase):
    def test_concat_pass(self):
        """
        This test succeeds when the connector.is_connected methods returns True
        when a database connection is established and False when there is no database connection.
        """
        expected = 'a b c'
        result = strings.concat('a', 'b')
        print(result)
        self.assertEqual(expected, result, 'concat failed')


if __name__ == '__main__':
    unittest.main()
