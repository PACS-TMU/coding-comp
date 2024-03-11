import unittest
import Tester
 
def romanToInt(numbers: str) -> int:
    ''' Given a roman numeral, convert it to an integer. '''
    dct = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(numbers)) :
        # Write your code here
        pass
    return result

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Tester))