import time
class Atm_machine:
    def __init__(self,balance,pin,new_pin):
        self.balance=balance
        self.pin=pin
        self.new_pin=new_pin
        

    def swipe_card(self):
        print("swipe your card")
        pin=int(input("Enter your 4 Digit pin:"))
        if pin==1234:
            
            print("""....WELCOME.....
            1.Balance Enquire
            2.Cash Withdrawl
            3.Deposite
            4.Change Pin
            5.Quit
            """) 
            option=int(input("enter your option:"))
            if option==1:
                
                print("A/c balance is ${}".format(self.check_balance()))
            if option==2:
                 
                print("your updated A/c balance is ${}".format(self.withdrawl() ))
            if option==3:
               
                print("your updated A/c balance is ${}".format(self.deposit()))
            if option==4:
                new_pin = self.change_pin()
                change_pin = self.print_pin(new_pin)
                if change_pin:
                    print('Pin changed')
                print("your pin number changed",self.change_pin() )
            if option==5:
                self.quit() 
        else:
            print("incorrect pin number ")   
        #self.swipe_card()
    def print_pin(self, newPin):
        print("Changed to New Pin", newPin)
        return True
    def check_balance(self):
        #import pdb;pdb.set_trace()
        return self.balance
       
    def withdrawl(self):        
        withdrawl_amount=int(input("Enter your withdrwal amount is :"))
        if (withdrawl_amount>self.balance):
            print("Current balance is less then your withdrawl")
        else: 
            self.balance=(self.balance-withdrawl_amount)

            print("""............Transaction Being Processed...........""")
            
            print(""".............Collect Your Cash..........""")
            return self.balance
               
    def deposit(self):
        deposit=int(input("Enter your deposite amount:"))
        if (deposit<0):
            print("invaild amount")
            
        else:
            self.balance=self.balance+deposit
            return self.balance

    def change_pin(self):            
        
        pin=int(input("Enter your old pin:"))
        new_pin=int(input("Enter your new pin:"))
        if not pin == new_pin:
            return new_pin
        else:
            print("Invalid Pin Number")
                
    def quit(self):                    
        print("Thanks for your transaction")
        quit()    
obj1=Atm_machine(50000,1234,2356)
#obj1.swipe_card()   
   
   