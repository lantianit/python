import unittest
from addtestcase import TestCaseAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCaseAdd))

unittest.TextTestRunner().run(suite)