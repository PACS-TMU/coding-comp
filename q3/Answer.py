import TestCases
import unittest
def findSum(arr: list, value: int) -> tuple[int, int]:
    startIdx = 0
    endIdx = len(arr) - 1
    while (startIdx < endIdx):
        if arr[startIdx] + arr[endIdx] < value:
            startIdx += 1
        elif arr[startIdx] + arr[endIdx] > value:
            endIdx -= 1
        else:
            return (startIdx, endIdx)
    return (-1, -1)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(TestCases))