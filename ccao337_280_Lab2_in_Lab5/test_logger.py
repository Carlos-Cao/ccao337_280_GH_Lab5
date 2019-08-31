import unittest
from logger import Logger

class Target(unittest.TestCase):

    def test_set_text(self):
        #Arrange
        t = Target()
        self.log = Logger(t.test_set_text)
        #Act
        self.log.info("message")
        #Assert
        self.assertEqual("[INFO] message", t.test_set_text)
                  
    def test_get_text(self):
        #Arrange
        t = Target()
        self.log = Logger(t.test_get_text)
        #Act
        self.log.error("message")
        #Assert
        self.assertEqual("[WARNING] message",t.test_get_text)
        
        
if __name__ == '__main__':
    unittest.main()

