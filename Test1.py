import unittest
import Task1
class TestProgram(unittest.TestCase):
    """
    def setUp(self):
        self.name="sandhiya"
    def test_read(self):
        self.assertEquals(self.name=="sandhiya",True)
    def test_not_read(self):
        self.assertEquals(self.name!="sandhiya",False)  
    """
    def setUp(self):
        self.readfile="sandhiya"
        self.writefile="SANDHIYA"
        self.message="read file and write file are not equal"
    def test_File(self):
        self.assertEqual(self.readfile,self.writefile,self.message)        
if __name__ == "__main__":
    unittest.main()    
    
       
        