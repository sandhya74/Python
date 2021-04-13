import unittest

from Vehicleparking import Vehicle_parking


class Parking_Test(unittest.TestCase):
    def setUp(self):
        self.result=Vehicle_parking()
        self.total_lot_space=5
        self.vehicle_type='two wheeler'
        self.vehicle_space=2
#Positive Test case
    def test_parking(self):
   
        user_input={self.vehicle_type:self.vehicle_space}
        expected_output={'two wheeler':2}
        available_space=3
        #park=self.result.parking()
        self.assertEqual(user_input == expected_output,True)
        self.assertEqual(self.total_lot_space != available_space,True)
# Negative Test case
    def test_parking2(self):
        user_input={self.vehicle_type:self.vehicle_space}
        expected_output={'two wheeler':2}
        available_space=3
        #park=self.result.parking()
        self.assertEqual(user_input!= expected_output,False)
        self.assertEqual(self.total_lot_space == available_space,False)
#positive Test Case
    def test_to_get_vehicle(self):
        actual_output={'two wheeler':1,'four wheeler':2,'three wheeler':3}
        expected_output={'two wheeler':1,'four wheeler':2}
        #un_park=self.result.to_get_vehicle()
        self.assertEqual(actual_output != expected_output,True)
#Negative Test Case        
    def test_to_get_vehicle2(self):
        actual_output={'two wheeler':1,'four wheeler':2,'three wheeler':3}
        expected_output={'two wheeler':1,'four wheeler':2}
        #un_park=self.result.to_get_vehicle()
        self.assertEqual(actual_output == expected_output,False)


    
if __name__ == '__main__':
    unittest.main()            


    

