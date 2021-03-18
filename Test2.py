import unittest

class File2(unittest.TestCase):
    def setUp(self):
        self.readname="sandhiya"
        self.writename="sandhiya"
        self.message="readname and writename are equal"
    def tast_positive(self):
        self.assertEqual(self.readname,self.writename,self.message)
if __name__ == "__main__":
    unittest.main()            