import cx_Oracle
from BankAccounts import *
from BankSignIn import *
print("\n1.admin...\n2.sign up as a new user...\n3.sign in as a existing user...\n4.exit")
choice=input("\nenter your option")
con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
cur = con.cursor();  
attempts=int(3)
while(choice!=3):   
   if(choice=='1'):          
     print("")  
   elif(choice=='2'):
     accno=input("enter the accno to your account..")
     b=BankAccount() 
     (accountno,passw)=b.customerCreation(accno)
     b.addressInsertion(accno)
     b.accountCreation(accno)
     print("\naccount is successfully created...")
     print("\nyour user name is..."+accountno+"\nyour password is...."+passw)
   elif(choice=='3'):
     b=BankAccount()
     b.lockingAccounts()
     login=SignIn()
     (username,password,retpassw)=login.signIn()
     if(password==retpassw):
        cur.execute("select * from lockedaccount where accountNumber='"+username+"'")
        res=cur.fetchall()
        for row in res:
           lockpassw=row[1]
        try:
         if(password==lockpassw):
           print("your is locked under bank..")
           break
        except: 
           attempts=int(3)
           print("login successully..")
     else:
        attempts=attempts-1
        print("password is incorect...")
        if(attempts<=0):
           cur.execute("insert into lockedaccount values('"+username+"','"+retpassw+"')")
           cur.execute("commit")
           print("your account is locked")
           break;
   elif(choice=='4'):
     print("thank u")
     break;
   else:
     print("Enter the correct option")
   choice=input("\nenter your option")
