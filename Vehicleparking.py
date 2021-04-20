class Vehicle_parking:
    def __init__(self):
        self.total_lot_space=5
        # self.2_wheeler_space=1
        # self.3_wheeler_space=3
        # self.4_wheeler_space=4
        # self.others=5
        self.floor4={}
        self.floor3={}
        self.floor2={}
        self.floor1={}
    def user_input(self):
        print("\n1.To Park","\n2.To Get Your Vehicle","\n3.View Status")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            self.parking()
        if choice==2:
            self.to_get_vehicle()
        if choice==3: 
            self.view_status()

    def parking(self):
        #import pdb;pdb.set_trace()
        vehicle_type=str(input("Enter the Vehicle Type:"))
        vehicle_space=int(input("Enter the Vehicle Space:"))
        
        floor_4 = sum(self.floor4.values())
        if vehicle_space>(self.total_lot_space - floor_4):
            print("space not available")
            print(self.floor3)
        else:    
        
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
            if vehicle_space>(self.total_lot_space - floor_3):
                print("space not available")
                print(self.floor2)
            else:    
                if floor_3 != 5:
                    #import pdb;pdb.set_trace()
                    self.floor3.update({vehicle_type:vehicle_space})
                    print(self.floor3)
                    self.calculate_space()
                else:
                    print(" 3RD Floor Parking Area is full Go to Next")
                    print(self.floor3)
                floor_2=sum(self.floor2.values())
                if vehicle_space>(self.total_lot_space - floor_2):
                    print("space not available")
                    print(self.floor1)
                else:    
                    if floor_2 !=5:
                        self.floor2.update({vehicle_type:vehicle_space})
                        print(self.floor2)
                        self.calculate_space()
                    else:
                        print(" 2ND Floor Parking Area is full Go to Next")
                        print(self.floor2)
                floor_1=sum(self.floor1.values())
                if vehicle_space>(self.total_lot_space - floor_1):
                    print("space not available")
                else:
                    if floor_1!=5:
                        self.floor1.update({vehicle_type:vehicle_space})
                        print(self.floor1)
                        self.calculate_space()
                    else:
                        print(" Parking slot not available")
                        print(self.floor1)
                    
        # else: 
            
        #     print("Available Space is:",occuiped_space)            
        #     return self.available_space        
                    
                          
                    
                    
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
        
        
        if occuiped_space4<5:
            print("Available Space in 4TH floor is:",occuiped_space4)
        if occuiped_space3<5:    
            print("Available Space in 3RD floor is:",occuiped_space3)
        if occuiped_space2<5:    
            print("Available Space in 2ND floor is:",occuiped_space2)
        if occuiped_space1<5:    
            print("Available Space in 1st floor is:",occuiped_space1)
        self.user_input()
        

    def view_status(self):
        print("\n1","\n2","\n3","\n4")
        slot=int(input("Enter the Slot:"))
        if slot==4:
            if self.floor4=={}:
                print("Available space is:",self.total_lot_space)
            else:    
                print(self.floor4)
                self.calculate_space()

        if slot==3:
            if self.floor3=={}:
                print("Available space is:",self.total_lot_space)
            else:    
                print(self.floor3)
                self.calculate_space()
        if slot==2:
            if self.floor2=={}:
                print("Available space is:",self.total_lot_space)
            else:    
                print(self.floor2)
                self.calculate_space()
        if slot==1:
            if self.floor1=={}:
                print("Available space is:",self.total_lot_space)
            else:    
                print(self.floor1)
                self.calculate_space()       
        
    def to_get_vehicle(self):
        print("\n1.1st Floor","\n2.2nd Floor","\n3.3rd Floor","\n4.4th Floor")
                 
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
