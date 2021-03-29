balance=10000

def swipe_card():
    
    print("swipe your card")
    pin=int(input("Enter your 4 Digit pin:"))
    if pin==1234:
        print("""............WELCOME..........
        1.Balance check
        2.WithDrawl
        3.Deposit
        4.Change Pin 
        5.Exit
        """)
        option=int(input("Enter your option:"))
        
    def check_balance():
        global balance
        if option==1:
            #print("Your available balance is ${}".format(balance))
            return  balance
        
    y=check_balance()
    print("Your available balance is ${}".format(y))
    def withdrawl():
        if option==2:
            global balance
            withdrawl_amount=int(input("Enter your withdrwal amount is :"))
            if withdrawl_amount>balance:
                print("Current balance is less then your withdrawl")
            else: 
                balance=(balance-withdrawl_amount)

                print("""............Transaction Being Processed...........""")
            
                print(""".............Collect Your Cash..........""")
                
            return balance
    x=withdrawl()
    print("Updated A\c balance is {}".format(x))


swipe_card()

        
    


   
   