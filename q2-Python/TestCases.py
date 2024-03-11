import unittest
from FindSum import findSum

class TestFindSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(findSum([1, 2, 3, 4, 5], 7), (1, 4))

    def test_all_negative(self):
        self.assertEqual(findSum([-5, -4, -3, -2, -1], -6), (0, 4))

    def test_no_pair_sum(self):
        self.assertEqual(findSum([1,2,3,4,5], 12), (-1, -1))

    def test_repeated_elements(self):
        self.assertEqual(findSum([2,3,3,4,5], 6), (0, 3))

    def test_empty_array(self):
        self.assertEqual(findSum([], 10), (-1, -1))

    def test_large_numbers(self):
        self.assertEqual(findSum([1000000000, 2000000000, 3000000000, 4000000000], 5000000000), (0, 3))

    def test_negative_target(self):
        self.assertEqual(findSum([-1,0,1,2,3], -1), (0, 1))

    def test_mixed_positive_negative(self):
        self.assertEqual(findSum([-10,-5,0,5,10,15,20,25,30], 10), (0, 6))

    def test_single_element_array(self):
        self.assertEqual(findSum([10],10), (-1, -1))
        
if __name__ == '__main__':
    unittest.main() 