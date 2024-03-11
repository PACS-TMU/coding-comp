import unittest
import TestCases

# Given a list of words, find the longest common substring among all the words.
# For example, given the list ["appleisred", "grapeisreadytoeat", "johnisright", "thisisreal"], the longest common substring is "is".
def findLongestCommonSubstring(words):
    n = len(words)
    baseWord = words[0]
    baseLen = len(baseWord)
    result = " "

    for i in range(baseLen):
        for j in range(i + 1, baseLen + 1):
            stem = baseWord[i:j]
            k = 1
            for k in range(1, n):
                pass

            if true:
                pass

    return result

if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(TestCases))