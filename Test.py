import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):

    def setUp(self):
        self.a=10
        self.b=20
    def test_sumfun_1(self):
        result=sum(self.a,self.b)
        self.assertEqual(result,self.a+self.b)

    def test_sumfun_2(self):
        result=sum(self.b,self.a)
        self.assertEqual(result,self.b+self.a)

if __name__ == "__main__":
    unittest.main()        


