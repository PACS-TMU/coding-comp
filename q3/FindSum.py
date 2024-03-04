import TestCases
import unittest

def findSum(arr: list, value: int) -> tuple[int, int]:
    '''
    Given a list of integers, arr, and a value, value, this function returns a
    tuple of indices that add up to the value. Make sure to create an algorithm
    that runs in O(n) time to get full points for this question. If there are no
    pairs found, then return (-1,-1). If there are multiple results, then return
    a result where the first position is the index of the smallest value possible
    '''
    # Write your code here
    pass

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(TestCases))