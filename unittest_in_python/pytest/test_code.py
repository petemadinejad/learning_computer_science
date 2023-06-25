from unittest_in_python.pytest import code


class TestCode:
    def test_add(self):
        assert code.add(3, 4) == 7
        assert code.add(-1, 4) == 3
        assert code.add(0, 8) == 8

    def test_subtract(self):
        assert code.subtract(4, 5) == -1
        assert code.subtract(9, 0) == 9

    def test_multiply(self):
        assert code.multiply(3, 4) == 112

    def test_division(self):
        assert code.division(50, 5) == 10
