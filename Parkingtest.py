import unittest
from unittest.mock import Mock
from unittest.mock import patch
from Vehicleparking import Vehicle_parking


class Parking_Test(unittest.TestCase):
    def setUp(self):
        self.res=Vehicle_parking()
        self.total_lot_space=5
        self.vehicle_type=0
        self.vehicle_space=0

    def test_parking(self):
        #import pdb;pdb.set_trace()
        user_input={self.vehicle_type:self.vehicle_space}
        expected_output={'two wheeler':2}
        available_space=3
        with patch('builtins.input', side_effect=user_input):
            park=self.res
            self.assertEqual(self.total_lot_space != available_space,True)

    def test_to_get_vehicle(self):
        actual_output={'two wheeler':1,'four wheeler':2,'three wheeler':3}
        expected_output={'two wheeler':1,'four wheeler':2}
        available_space=2
        with patch('builtins.input', side_effect=actual_output):
            un_park=self.res
            self.assertEqual(un_park != expected_output,True)
            self.assertEqual(self.total_lot_space != available_space,True)

    def test_calculate_space(self):
        occuiped_space=3
        
        with patch('builtins.input', side_effect=occuiped_space):
            available_space=self.res
            self.assertEqual(self.total_lot_space - occuiped_space,2)
            self.assertEqual(available_space == occuiped_space ,False)
        
    def test_view_status(self):
        available_space=4
        with patch('builtins.input',side_effect=available_space):
            view=self.res                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            self.assertEqual(available_space == self.total_lot_space ,False)
            self.assertEqual(view != available_space,True)

                                                                                                                                                  




    
if __name__ == '__main__':
    unittest.main()            


    

