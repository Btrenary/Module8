import unittest

from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_True(self):
        self.assertEqual(True, dict_membership.in_dict({'A': '1', 'B': '2', 'C': '3'}, 'B'))

    def test_in_dict_False(self):
        self.assertEqual(False, dict_membership.in_dict({'A': '1', 'B': '2', 'C': '3'}, 'F'))


if __name__ == '__main__':
    unittest.main()
