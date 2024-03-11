import unittest
import Tester
 
def romanToInt(numbers: str) -> int:
    dct = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(numbers)) :
        result += dct[numbers[i]]
        if i != len(numbers)-1 and dct[numbers[i]] <  dct[numbers[i + 1]]:
            result += -2 * dct[numbers[i]]
    return result

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Tester))