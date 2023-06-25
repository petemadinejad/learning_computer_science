import unittest

from unittest_in_python.unit_test import code


class ExampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(code.add(4, 5), 9)
        self.assertEqual(code.add(-1, 4), 3)

    def test_subtract(self):
        self.assertEqual(code.subtract(5, 1), 2)

    def test_multiply(self):
        self.assertEqual(code.multiply(6, 5), 30)

    def test_division(self):
        self.assertEqual(code.division(30, 6), 5)
        self.assertRaises(ZeroDivisionError, code.division, 4, 0)


if __name__ == '__main__':
    unittest.main()
