# Unit Test
import unittest
a = 3
b = 5
class Test_53a_UnitTest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(3 + 4, a + b)

    def test_greater(self):
        self.assertTrue(a + b > 3 + 4)

if __name__ == '__main__':
    unittest.main()