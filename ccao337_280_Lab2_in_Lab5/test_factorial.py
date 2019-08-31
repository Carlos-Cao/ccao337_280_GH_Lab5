import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class MathTest():
    def test_factorial(self):
        #Arrange
        self.number = 5
        #Act
        result = maths.factorial(self.number)
        #Assert
        self.assertEqual(result, 120)

if __name__ == '__main__':
    unittest.main()
