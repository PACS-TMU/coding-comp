import unittest
from findLongestCommonSubstring import findLongestCommonSubstring

class TestFindLongestCommonSubstring(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(findLongestCommonSubstring(["appleisred", "grapeisreadytoeat", "johnisright", "thisisreal"]), "isr")

    def test_all_words_same(self):
        self.assertEqual(findLongestCommonSubstring(["apple", "apple", "apple", "apple"]), "apple")
    
    def test_no_common_substring(self):
        self.assertEqual(findLongestCommonSubstring(["apple", "grape", "john", "this"]), "")

    def test_single_word(self):
        self.assertEqual(findLongestCommonSubstring(["apple"]), "")

    def test_empty_list(self):
        self.assertEqual(findLongestCommonSubstring([]), "")

    def test_single_letter(self):
        self.assertEqual(findLongestCommonSubstring(["grace", "disgraceful", "grace", "joy"]), "grace")

    def test_single_letter_repeated(self):
        self.assertEqual(findLongestCommonSubstring(["a", "a", "a", "a"]), "a")

    def test_abc_case(self):
        self.assertEqual(findLongestCommonSubstring(["abcdef", "bcde", "cdefg"]), "bcde")
        
if __name__ == '__main__':
    unittest.main() 