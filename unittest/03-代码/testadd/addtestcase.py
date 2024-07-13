import unittest
from add import add

class TestCaseAdd(unittest.TestCase):
    def test_01(self):
        if 2 == add(1,1):
            print(f'1 1 2测试用例通过')
        else:
            print(f'测试用例不通过')