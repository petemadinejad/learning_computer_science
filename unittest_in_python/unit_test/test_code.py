import unittest
import code

class ExampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(unit_test_example_1.add(4, 5), 9)
        self.assertEqual(unit_test_example_1.add(-1, 4), 3)
    def test_subtract(self):
        self.assertEqual(unit_test_example_1.subtract(5, 1), 4)
    def test_multiply(self):
        self.assertEqual(unit_test_example_1.multiply(6, 5), 30)
    def test_division(self):
        self.assertEqual(unit_test_example_1.division(30, 6), 5)
        self.assertRaises(ZeroDivisionError, unit_test_example_1.division, 4, 0)

if __name__=='__main__':
    unittest.main()
