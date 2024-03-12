import unittest
from ClimbStair import climbStairs

class TestClimbStair(unittest.TestCase):
    def test_three(self):
        self.assertEqual(climbStairs(3), 3)

    def test_four(self):
        self.assertEqual(climbStairs(4), 5)
    
    def test_five(self):
        self.assertEqual(climbStairs(5), 8)

    def test_eleven(self):
        self.assertEqual(climbStairs(11), 144)

    def test_fourty_five(self):
        self.assertEqual(climbStairs(45), 1836311903)

    def test_thirty_two(self):
        self.assertEqual(climbStairs(32), 3524578)

    def test_nine_plus_ten(self):
        self.assertEqual(climbStairs(21), 17711)
        
if __name__ == '__main__':
    unittest.main() 