import unittest
from findLongestCommonSubstring import findLongestCommonSubstring

class TestFindSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2]), [2])

    def test_all_negative(self):
        self.assertEqual(intersection([-5, -4, -3, -2, -1], [-6, -5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def no_intersection(self):
        self.assertEqual(intersection([1,2,3,4,5], [12,13,14,15,16]), [])

    def test_repeated_elements(self):
        self.assertEqual(intersection([2,3,3,4,5], [3,3,3,3,3]), [3])

    def test_empty_array(self):
        self.assertEqual(intersection([], [10,20,30,40,50]), [])

    def test_large_numbers(self):
        self.assertEqual(intersection([1000000000, 2000000000, 3000000000, 4000000000], [5000000000, 6000000000, 7000000000, 8000000000]), [])

    def test_equal(self):
        self.assertEqual(intersection([-1,0,1,2,3], [-1,0,1,2,3]), [-1,0,1,2,3])

    def test_mixed_positive_negative(self):
        self.assertEqual(intersection([-10,-5,0,5,10,15,20,25,30], [10,20,30,40,50,60,70,80,90]), [10,20,30])

    def test_single_element_array(self):
        self.assertEqual(intersection([10], [10]), [10])
        
if __name__ == '__main__':
    unittest.main() 