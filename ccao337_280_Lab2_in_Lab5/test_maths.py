import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''
        
    def test_add(self):
        ''' Tests the add function. '''
        #Arrange
        first = 1
        second = 2
        #Act
        self.equal = maths.add(first, second)
        #Assert
        self.assertEqual(3, self.equal, "Expects 3")       

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #Arrange
        self.length = 5
        #Act
        self.result = maths.fibonacci(self.length)
        #Assert
        self.assertEqual(5, self.result, "Expects 5")
    
    def test_convert_base(self):
        ''' Tests the convert_base function >= 10 '''
        #Arrange
        num1 = 10
        num2 = 16
        #Act
        self.base1 = maths.convert_base(num1, num2)
        #Assert
        self.assertEqual("A", self.base1, "Expects A")
        
        ''' Tests the convert_base function < 10. '''
        #Arrange
        num3 = 8
        num4 = 2
        #Act
        self.base2 = maths.convert_base(num3, num4)
        #Assert
        self.assertEqual("1000", self.base2, "Expects 1000")
        

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
