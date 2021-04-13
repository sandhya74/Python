class Vehicle_parking:
    def __init__(self):
        self.total_lot_space=5
        self.available_space=0
        self.floor4={}
        self.floor3={}
        self.floor2={}
        self.floor1={}
    def user_input(self):
        print("1.To Park")
        print("2.To Get Your Vehicle")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            self.parking()
        if choice==2:
            self.to_get_vehicle()
        

    def parking(self):
        #import pdb;pdb.set_trace()
    
        vehicle_type=str(input("Enter the Vehicle Type:"))
        vehicle_space=int(input("Enter the Vehicle Space:"))
        
        floor_4 = sum(self.floor4.values())
        
        if floor_4 != 5:
            
            if vehicle_type in self.floor4:
                self.floor4[vehicle_type] += vehicle_space
            else:
                self.floor4[vehicle_type] = vehicle_space
            print(self.floor4)
            self.calculate_space()
        elif floor_4 == 5:
            print("4TH Floor Parking Area is full Go to Next")
            print(self.floor4)
            
            floor_3 = sum(self.floor3.values())
            if floor_3 != 5:
                self.floor3.update({vehicle_type:vehicle_space})
                print(self.floor3)
                self.calculate_space()
            else:
                print(" 3RD Floor Parking Area is full Go to Next")
                print(self.floor3)
                floor_2=sum(self.floor2.values())
                if floor_2 !=5:
                    self.floor2.update({vehicle_type:vehicle_space})
                    print(self.floor2)
                    self.calculate_space()
                else:
                    print(" 2ND Floor Parking Area is full Go to Next")
                    print(self.floor2)
                floor_1=sum(self.floor1.values())
                if floor_1!=5:
                    self.floor1.update({vehicle_type:vehicle_space})
                    print(self.floor1)
                    self.calculate_space()
                else:
                    print(" Parking slot not available")
                    print(self.floor1)
                    
        else: 
            
            print("Available Space is:",occuiped_space)            
            return self.available_space        
                    
                    
    def calculate_space(self):
        #import pdb;pdb.set_trace()
        list4=self.floor4.values()
        list3=self.floor3.values()
        list2=self.floor2.values()
        list1=self.floor1.values()
        occuiped_space4=(self.total_lot_space-sum(list4))
        occuiped_space3=(self.total_lot_space-sum(list3))
        occuiped_space2=(self.total_lot_space-sum(list2))
        occuiped_space1=(self.total_lot_space-sum(list1))
        
        
        print("Available Space in 4TH floor is:",occuiped_space4)
        print("Available Space in 3RD floor is:",occuiped_space3)
        print("Available Space in 2ND floor is:",occuiped_space2)
        print("Available Space in 1st floor is:",occuiped_space1)
        self.user_input()
        
    def to_get_vehicle(self):
        print("""........1.1st Floor.......
                 ........2.2nd Floor.......
                 .........3.3rd Floor......
                 .........4.4th Floor.......
                 """)
        level=int(input("Enter the Level:"))
        vehicle_type=str(input("Enter the Vehicle Type:"))
        if level==4:
            #import pdb;pdb.set_trace()
            if vehicle_type in self.floor4:
                self.floor4[vehicle_type] -=1
                if self.floor4[vehicle_type]==0:
                    del self.floor4[vehicle_type]
                print(self.floor4)
                self.calculate_space()
            else:
                print("Your vehicle is not Available in this slot")
        if level==3:
            if vehicle_type in self.floor3:
                self.floor3[vehicle_type] -=1
                if self.floor3[vehicle_type]==0:
                    del self.floor3[vehicle_type]
                print(self.floor3)
                self.calculate_space()
            else:
                print("Your vehicle is not Available in this slot")
        if level==2:
            if vehicle_type in self.floor2:
                self.floor3[vehicle_type] -=1
                if self.floor2[vehicle_type]==0:
                    del self.floor2[vehicle_type]
                print(self.floor2)
                self.calculate_space()
            else:
                print("Your vehicle is not Available in this slot")
        if level==1:
            if vehicle_type in self.floor1:
                self.floor1[vehicle_type] -=1
                if self.floor1[vehicle_type]==0:
                    del self.floor1[vehicle_type]
                print(self.floor1)
                self.calculate_space()
            else:
                print("Your vehicle is not Available in this slot")
        return self.available_space
       
obj=Vehicle_parking()
obj.user_input()
