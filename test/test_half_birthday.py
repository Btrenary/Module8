import unittest

import datetime_assignmet
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(datetime(2020, 8, 19, 12), datetime_assignmet.half_birthday(2020, 2, 19))


if __name__ == '__main__':
    unittest.main()
