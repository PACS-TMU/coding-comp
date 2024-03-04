import unittest
from RomanToInteger import romanToInt 

class TestFindSum(unittest.TestCase):
    def test_single_roman_digit(self):
        self.assertEqual(romanToInt("I"), 1)
        self.assertEqual(romanToInt("V"), 5)
        self.assertEqual(romanToInt("X"), 10)
        self.assertEqual(romanToInt("L"), 50)
        self.assertEqual(romanToInt("C"), 100)
        self.assertEqual(romanToInt("D"), 500)
        self.assertEqual(romanToInt("M"), 1000)
    
    def test_multiple_roman_digits(self):
        self.assertEqual(romanToInt("II"), 2)
        self.assertEqual(romanToInt("IV"), 4)
        self.assertEqual(romanToInt("IX"), 9)
        self.assertEqual(romanToInt("XX"), 20)
        self.assertEqual(romanToInt("XL"), 40)
        self.assertEqual(romanToInt("XC"), 90)
        self.assertEqual(romanToInt("CD"), 400)
        self.assertEqual(romanToInt("CM"), 900)
    
    def test_combinations(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("XIV"), 14)
        self.assertEqual(romanToInt("XXX"), 30)
        self.assertEqual(romanToInt("CCXLV"), 245)
        self.assertEqual(romanToInt("CDXLIV"), 444)
        self.assertEqual(romanToInt("CMXCIX"), 999)
        self.assertEqual(romanToInt("MMXXI"), 2021)
        self.assertEqual(romanToInt("MMMM"), 4000)
        self.assertEqual(romanToInt("MMCMXLVIII"), 2948)
        self.assertEqual(romanToInt("MMMMCMXCIX"), 4999)

if __name__ == '__main__':
    unittest.main() 