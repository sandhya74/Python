import unittest
from unittest import mock
from School_data import Student
class School_data_test(unittest.TestCase):

    def setUp(self):
        self.res=Student()

    def test_fees_payment(self):
        fees_amount=6000
        extra_charges=100
        total=fees_amount + extra_charges
        result=self.res.get_fees_details()
        self.assertEqual(result,total)
        
    def test_salary_details(self):
        
        total_amount=6100
        no_staff=2
        salary_per_staff=total_amount/no_staff
        result=self.res.get_salary_details()
        self.assertEqual(result, salary_per_staff)
        loss_pay=100
        abs_days=2
        loss_of_pay=100 * 2
        salary=total_amount - loss_of_pay
        result=self.res.get_salary_details()
        self.assertEqual(result,salary)

if __name__ == '__main__':
    unittest.main()    