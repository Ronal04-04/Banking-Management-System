import mysql.connector
from datetime import datetime
from decimal import Decimal
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bms"
)

cursor = mydb.cursor()

def account(F_Name,M_Name,L_Name,DOB,Address,Email_address,Adhar_no,Pan_no):
    create = "Insert into account_details(F_Name,M_Name,L_Name,DOB,Address,Email_address,Adhar_no,Pan_no)	VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    dob = datetime.strptime(DOB,"%Y-%m-%d").date()
    val = (F_Name,M_Name,L_Name,dob,Address,Email_address,Adhar_no,Pan_no)
    cursor.execute(create,val)
    mydb.commit()
    print("Account is been by the name",F_Name,M_Name,L_Name)

    # Fetch the newly account
    remove = "Select * from account_details Where Adhar_no = %s"
    value = (Adhar_no,)
    cursor.execute(remove,value)
    mynumber = cursor.fetchone()
    if mynumber:
      no = mynumber[0]
      print ("\n",F_Name,M_Name,L_Name, "your Account Number is", no)

def view_account(Account_no):
    # Viewing the account details by entering account no
    view = "Select * from account_details Where Account_no=%s"
    val = (Account_no,)     
    cursor.execute(view,val)
    number = cursor.fetchone()
    if number:
          print(f"\n Account No:{number[0]}, \n First Name :{number[1]}, \nMiddle Name :{number[2]}, \n Last Name :{number[3]}, \n Date of birth :{number[4]},\n Address :{number[5]},\n  Email Address :{number[6]},\n  Adhar Number :{number[7]}, \n Pancard Number :{number[8]},\n Total Balance :{number[9]}")
    else:
       print("No Account found for the Account number",Account_no)
       print("Try again by entering proper Account number.")

def credit(Account_no,Credit):
#   adding money to the account 
   let = "Insert into entry(Account_no,Date,Credit,Total_balance) Values(%s,CURDATE(),%s,%s)"

#    Fetching the total balance to add to the credited money
   put = "SELECT * FROM account_details WHERE Account_no = %s"
   run = (Account_no,)
   cursor.execute(put,run)
   result = cursor.fetchone()
   if result:
        current_balance = result[9]
   else:
      print("Account not found.")
      return     

    #  Calculating the total balance
   Balance = Decimal(current_balance) +Decimal( Credit) 
   go = (Account_no,Credit,Balance)
   cursor.execute(let,go)
   mydb.commit()

#    Updating Total Balance in Account_details
   val = "Update account_details SET Total_Balance = %s Where Account_no = %s"
   erd = (Balance,Account_no)
   cursor.execute(val,erd)
   mydb.commit()
   print(cursor.rowcount,"inserted Successfully.")
   
    # Check if the update was successful
   if cursor.rowcount == 0:
        print("Failed to update the account balance. Make sure the account number exists.")
   else:
        print(f"\nReceipt \nAccount Number: {Account_no} \nCredited: {Credit} \nDate: {datetime.now().date()} \nTotal Balance: {Balance}")

def debit(Account_no,Debit):
#   adding money to the debit table 
   let = "Insert into entry(Account_no,Date,Debit,Total_balance) Values(%s,CURDATE(),%s,%s)"

#    Fetching the total balance to add to the credited money
   put = "SELECT * FROM account_details WHERE Account_no = %s"
   sql = (Account_no,)
   cursor.execute(put,sql)
   result = cursor.fetchone()
   if result:
        c_balance = result[9]

   else:
        print("Account not Found.")
   
   if Decimal(Debit) > Decimal( c_balance) :
        print("Insufficient balance.")
        return
     
    #  Calculating the total balance
   Balance =  Decimal(c_balance) -Decimal( Debit)
   go = (Account_no,Debit,Balance)
   cursor.execute(let,go)
   mydb.commit( )

#    Updating Total Balance in Account_details
   val = "Update account_details SET Total_balance = %s Where Account_no = %s"
   erd = (Balance,Account_no)
   cursor.execute(val,erd)
   mydb.commit()
   print(cursor.rowcount,"inserted Successfully.")
   # Check if the update was successful
   if cursor.rowcount == 0:
        print("Failed to update the account balance. Make sure the account number exists.")
   else:
        print(f"\nReceipt \nAccount Number: {Account_no} \n Debited: {Debit} \nDate: {datetime.now().date()} \nTotal Balance: {Balance}")

def delete_account(Account_no):
#    Deleting the Account Using Account Number
   val ="Delete From account_details Where Account_no = %s"
   sql = (Account_no,)    
   cursor.execute(val,sql)
   mydb.commit()
   print("Account no",Account_no,"Has been Deleted Successfully .")

def view_entry():
   Val = "Select * from entry Where Account_no like %s"
   sal = (Account_no,)
   cursor.execute(Val,sal)
   res = cursor.fetchone()
   if res:
      print(f"\n Account Number:{res[1]},Date :{res[2]}, Credit :{res[3]},Debit:{res[4]},Total Balance :{res[5]}")  

   else:
      print("Account not found")
      return    

# Starting the program sequence   
if __name__ :"__main__"
while True:
   print("-----------Banking Management System----------")
   print("\n---------------- Welcome------------ ")
   print("\n New User Than login by entering \"N\".")
   print("\n Already User Than login by entering \"O\".")

   enter = input("Enter your choice here :-").strip().upper()#Enter the choice to execute

   if enter == "N":
      print("/n -------New User Login-------")
      F_Name = input("First Name:-")
      M_Name = input("Middle Name:-")
      L_Name = input("Last Name:-")
      DOB = input("Date of birth(YYYY-MM-DD):-")
      Address = input("Address:-")
      Email_address = input("Email Address:-")
      Adhar_no = int(input("Aadhar Number:-"))
      Pan_no = input("Pan Card :-")
      account(F_Name,M_Name,L_Name,DOB,Address,Email_address,Adhar_no,Pan_no)

   elif enter == "O":
      print("\n--------------")
      Account_no = int(input("Enter your Account Number :-"))
      print("To view Details press 1")
      print("To Credit Money to the Account press 2")
      print("To Debit the money press 3")
      print("To Delete press 4")
      print("To View Transactions press 5")
      print("To Exit press 6")

      press = int(input("Press the Number :- "))

      if press == 1:
         print("----------Account Details----------")
         view_account(Account_no)

      elif press == 2:
         Credit = input("Enter your Amount :-")
         credit(Account_no,Credit)

      elif press == 3:
         Debit = input("Enter your Amount :-")
         debit(Account_no,Debit)

      elif press == 4:       
        print("Are you sure Want to delete the Account with Account Number ", Account_no)
        write = input("Enter Yes or No to continue :-").strip()
        if write == "Yes" :
         delete_account(Account_no)

        elif write=="No":
            break

        else:
           exit()

      elif press == 5:
         view_entry()
              

      elif press == 6:
         break

      else:
         exit()
         print("Invalid input.")

   elif enter.lower() == "exit":
        print("Exiting the program.")
        break  # Exit the main loop
      
   else:
      exit()
      print("Invalid input. Try Entering \"N\" , \"O\"  or  \"exit\".")        
               
      
  
   