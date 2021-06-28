from pdb import set_trace
import mysql.connector
global connection,cursor
connection = mysql.connector.connect(host='localhost',
                                            database='School',
                                            user='root',
                                            password='root')
cursor=connection.cursor()                                            

class School(object):
    def report_menu(self):
        print("....school Record....")
        print("""1.student details
                 2.fees details
                 3.teaching_staff detail
                 4.salary details
                 5.exit
                 """)

        option=input("enter the option:")
        
        if option==str(1):
            
            Student.get_student_details(self)
        elif option==str(2):
            Student.get_fees_details(self)
        elif option==str(3):
            Student.get_staff_details(self)
        elif option==str(4):
            Student.get_salary_details(self)  

class Student(School):

    def fees_payment():
        cursor.execute('select sum(total_amount) from Fees_payment')
        record = cursor.fetchone()
        return record

    def find_salary(teach_id):
        cursor.execute('select * from salary_details where id ={}'.format(teach_id))
        record = cursor.fetchone()
        return record

    # The following function get the student details 

    def get_student_details(self):
        try:
            std_name=input("enter the student name:")
            pre_days=input("enter the present days:")
            abs_days=input("enter the absend days:")
            
            # This quary used to check the user input already exit or not in Fees_payment table

            sql='select * from Students where std_name like "%{}%"'.format(std_name)
            cursor.execute(sql)
            
            record=cursor.fetchone()
            if record==None:
                
                # This quary used to insert the values in student table
                 
                std_details= 'insert into Students(std_name,present_days,absent_days) values("{}",{},{});'.format(std_name,pre_days,abs_days)
                cursor.execute(std_details)
                
                print('New record added successfully')
                connection.commit()
                obj.report_menu()
            else:
                print('\n\n record already Exist.........\n\n press to continue')
                wait= input()
                obj.report_menu()
        except mysql.connector.Error as error:
            print("Failed to insert record into Student table{}".format(error))
 
      # The following function used to get the fees_details '

    def get_fees_details(self):
        try:
            std_id=input("enter stdudent id:")
            fees_amount=input("enter the fees_amount:")
            extra_charges=input("enter extra charges:")
            
            # This quary used to check the user input already exit or not in Fees_payment table

            sql_quary='select * from Fees_payment where std_id like "%{}"'.format(std_id)
            cursor.execute(sql_quary)
            
            record=cursor.fetchone()
            if record==None:
                total_amount=int(fees_amount)+int(extra_charges)
               
                # This quary used to insert tha values in fees_payment table

                fees_details='insert into Fees_payment(std_id,fees_amount,extra_charges,Total_amount) values({},{},{},{});'.format(std_id,fees_amount,extra_charges,total_amount)
                cursor.execute(fees_details)
               
                print('\n\n New record added successfully')
                connection.commit()
                obj.report_menu()
            else:
                print('\n\n record already Exist......\n\n press to continue')
                wait=input()
                obj.report_menu()
        except mysql.connector.Error as error:
            print("Failed to insert record into Fees_details table {}".format(error)) 

    #  This following function used to get the Staff details

    def get_staff_details(self):
        try:
            name=input("enter the teacher name:")
            pre_days=input("enter present days:")
            abs_days=input("enter the absend days:")
            
            # This quary used to check the user input already exit or not in staff table

            sql_quary='select * from Staff where teach_name like "%{}"'.format(name)
            cursor.execute(sql_quary)
            
            record=cursor.fetchone()
            if record==None:

                # This quary used to insert the values in staff table

                teach_details='insert into Staff(teach_name,pre_days,abs_days) values("{}",{},{})'.format(name,pre_days,abs_days)
                cursor.execute(teach_details)
               
                print('\n\n new record added successfully')        
                connection.commit()
                obj.report_menu()
            else:
                print('\n\n record already Exist........\n\n press to cintinue')
                wait=input()
                obj.report_menu()
        except mysql.connector.Error as error:
            print("Failed to insert record into Staff details table {}".format(error)) 
     
    # This function used get the Salary details from Salary table
     
    def get_salary_details(self):
        try:
        #import pdb;pdb.set_trace()
            loss_of_pay=100
            no_of_staff=input("enter no of staffs:")
            id=input("enter staff  id:")
            
            # This quary used to join the Fees_payment table and Salary table for total amount

            join='SELECT fees_payment.pay_id, salary_details.id, fees_payment.total_amount FROM Salary_details INNER JOIN Fees_payment ON Fees_payment.pay_id = Salary_details.pay_id'
            cursor.execute(join)
            
           # This quary used to calculate sum(total_amount) in salary table

            total_amount='select sum(total_amount) from Salary_details'
            cursor.execute(total_amount)
            for x in total_amount:
                print(x)
            amount_to_pay = total_amount/no_of_staff
            
            #This quary used to filter the present days in staff table using tech_id 
            
            present_days='select pre_days from Staff where teach_id={}'.format(id)
            cursor.execute(present_days)
            if present_days==10:
                final_salary=amount_to_pay
                
                # This quary used to insert the values in salary table

                salary_details='insert into Salary_details(no_staff,total_amount,teach_id,salary) values({},{},{},{})'.format(no_of_staff,total_amount,id,final_salary)
                cursor.execute(salary_details)

                print("record addes successfully")
                connection.commit()
                obj.report_menu()
            else:
                # This Quary used to filter the absend days in staff table using teach_id

                abs_days='select abs_days from Staff where taech_id={}'.format(id) 
                
                loss_amount = abs_days * loss_of_pay  
                final_salary = amount_to_pay - loss_amount

                # This quary used to insert the values in salary table
                  
                salary_details='insert into Salary_details(no_staff,total_amount,teach_id,salary) values({},{},{},{})'.format(no_of_staff,total_amount,id,final_salary) 
                cursor.execute(salary_details)
                
                print("record added successfully")
                connection.commit()
                obj.report_menu()
        except mysql.connector.Error as error:
            print("Failed to insert record into salary table {}".format(error))        

obj=Student()
obj.report_menu()