import unittest
import TestCases

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# make sure it is O(n) time. You only need one loop! We are testing the efficiency of your code.

def climbStairs(n: int) ->  int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # code here 
    pass

if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(TestCases))