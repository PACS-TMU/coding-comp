import unittest
from shortestCommonPrefix import longestCommonPrefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_empty_array(self):
        self.assertEqual(longestCommonPrefix([]), "")

    def test_single_word(self):
        self.assertEqual(longestCommonPrefix(["apple"]), "apple")

    def test_single_letter_prefix(self):
        self.assertEqual(longestCommonPrefix(["ant", "apple", "ape"]), "a")

    def test_same_words(self):
        self.assertEqual(longestCommonPrefix(["hello", "hello", "hello"]), "hello")

    def test_long_prefix(self):
        self.assertEqual(longestCommonPrefix(["precondition", "precaution", "predict"]), "pre")

    def test_mixed_case(self):
        self.assertEqual(longestCommonPrefix(["Apple", "apple", "APPLE"]), "")

if __name__ == '__main__':
    unittest.main()
