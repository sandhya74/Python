
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from Atm import Atm_machine

class Atm_Test(unittest.TestCase):
    def setUp(self):
        self.res=Atm_machine(50000,1234,2356)
        #self.res=swipe_card(50000,1234)
   
    def test_swipe_card(self):
        self.assertEqual(self.res.pin==1234,True)
        self.assertEqual(self.res.pin!=1234,False)
    def test_check_balance(self):
        self.assertEqual(self.res.balance==50000,True)    
    def test_withdrawl(self):
        
        user_input=[10000]
        expected_balance=[40000]
        with patch('builtins.input', side_effect=user_input):
            balance=self.res.withdrawl()
            self.assertEqual(balance == 40000,True)
            self.assertEqual(balance != 40000,False)
    def test_deposit(self):
        #import pdb;pdb.set_trace()
        user_input=[1000] 
        expected_balance=[41000] 
        with patch('builtins.input',side_effect=user_input):
            balance=self.res.deposit()
            self.assertEqual(balance == 41000,True)
            self.assertEqual(balance != 41000,False)      
    def test_change_pin(self):
        
        self.assertEqual(self.res.new_pin != 1234,True)
        self.assertEqual(self.res.new_pin == 1234,False)
        
if __name__ == "__main__":
    unittest.main()        
