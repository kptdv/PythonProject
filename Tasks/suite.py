import unittest
from Tasks.suiteleveltest import Emp

e1=unittest.TestLoader().loadTestsFromTestCase(Emp)
suite=unittest.TestSuite(e1)
unittest.TextTestRunner().run(suite)