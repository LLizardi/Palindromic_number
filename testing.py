import unittest
from functions import palindrome,change_basis


class Test(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(palindrome(11), True)
        self.assertEqual(palindrome(101), True)
        self.assertEqual(palindrome(100), False)
        self.assertEqual(palindrome(212), True)
        self.assertEqual(palindrome(200), False)

        self.assertEqual(change_basis(21,2),10101)
        self.assertEqual(change_basis(21,3),210)
        self.assertEqual(change_basis(15,3),120)
        self.assertEqual(change_basis(7,3),21)
        self.assertEqual(change_basis(5,2),101)

if __name__ == "__main__": 
    unittest.main() 
