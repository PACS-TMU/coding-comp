import TestCases
import unittest

def longestCommonPrefix(strs: list[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    if not strs:
        return ""
        
    minimum = min([len(str) for str in strs])
    result = ""

    for i in range(1, minimum+1):
        prefix = strs[0][:i]
        
        for s in strs:
            if s[:i] != prefix:
                return result
        
        result = prefix
    
    return result

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(TestCases))