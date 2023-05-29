"""
Author: https://www.linkedin.com/in/parisa-etemadinejad-809923206/
Date: 2023-05-29
This file consists all prerequisite's samples for SINGLETONE DP(design pattern)
for SINGLETONE DP we need three items you can click the url that front of the prerequisite and study about them :
1- __call__ in python (https://www.geeksforgeeks.org/__call__-in-python/)
2- __new__ in python (https://www.geeksforgeeks.org/__new__-in-python/)
3- metaclass in python (https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/)
"""

"""
    __new__
"""


class A:
    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == "parisa":
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


a1 = A("shahin")
a2 = A("parisa")
print(a1.__class__)
print(a1.__class__.__class__)
print(a2.__class__)

"""
    __call__
"""


class A:
    def __call__(self, name, *args, **kwargs):
        print(name)


a1 = A()
a1("parisa")

"""
    metaclass
"""


class A:
    # def __new__(cls, *args, **kwargs):
    #     print(cls)
    pass


a1 = A()
print(a1.__class__)
print(a1.__class__.__class__)
print(type(123))
# help(type)

a2 = type("Person", (), {})
print(a2)


class Singletone(type):
    """
    it's my own metaclass
    """
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Db(metaclass=Singletone):
    pass


d1 = Db()
d2 = Db()
print(id(d1))
print(id(d2))
