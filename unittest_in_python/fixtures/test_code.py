import unittest

from unittest_in_python.fixtures.code import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('amir', 'big')
        self.p2 = Person('joen', 'doe')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'amir big')
        self.assertEqual(self.p2.fullname(), 'joen doe')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'amirbig@gmail.com')
        self.assertEqual(self.p2.email(), 'joendoe@gmail.com')


if __name__ == '__main__':
    unittest.main()
