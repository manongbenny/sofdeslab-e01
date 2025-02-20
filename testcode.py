import code
import unittest

class TestCode(unittest.TestCase):
  def testdouble(self):
    self.assertEqual(code.return_double(2),4)
    self.assertEqual(code.return_double(4),8)
    self.assertEqual(code.return_double(0),0)
    self.assertEqual(code.return_double(-2),4)

if __name__=='__main__':
  unittest.main()
