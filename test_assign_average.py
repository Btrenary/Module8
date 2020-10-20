import unittest

import assign_average


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual("You entered an A!", assign_average.switch_average('A'))

    def test_B(self):
        self.assertEqual("You entered a B!", assign_average.switch_average('B'))

    def test_C(self):
        self.assertEqual("You entered a C!", assign_average.switch_average('C'))

    def test_D(self):
        self.assertEqual("You entered a D!", assign_average.switch_average('D'))

    def test_F(self):
        self.assertEqual("You entered an F!", assign_average.switch_average('F'))

    def test_non_key(self):
        self.assertEqual("This is not a valid Grade", assign_average.switch_average('R'))


if __name__ == '__main__':
    unittest.main()
