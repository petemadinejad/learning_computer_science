import time

import pytest

from unittest_in_python.fixtures.code import Person


class TestPerson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person('amir', 'big')
        self.p2 = Person('joen', 'doe')
        yield 'setup'
        time.sleep(2)
        print("done...........")  # no affect

    def test_fullname(self, setup):
        assert self.p1.fullname() == 'amir big'
        assert self.p2.fullname() == 'joen doe'

    def test_email(self, setup):
        assert self.p1.email() == 'amirbig@gmail.com'
        assert self.p2.email() == 'joendoe@gmail.com'
