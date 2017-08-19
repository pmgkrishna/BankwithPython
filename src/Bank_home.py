import cx_Oracle
from BankAccounts import *
from BankSignIn import *
from BankDebit  import *
from BankCredit  import *
#from BankFundTransfer  import*
from BankClosingAccounts import *
con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
cur = con.cursor();  
attempts=int(3)
choice=int(0)
while(choice!=3):   
   print("\n1.admin...\n2.sign up as a new user...\n3.sign in as a existing user...\n4.exit")
   choice=input("\nenter your option")
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
     if(retpassw=="closed"):
        print("your account is already closed...")
        break
     elif(password==retpassw):
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
           print("welcome to e-bank system..")
           ch=int(1)
           while(ch!=6):
             print("1.debit\n2.credit\n3.fund transfer\n4.bank statement\n5.close account\n6.logout")        
             ch=int(input("enter the choice..\n")) 
             if(ch==1): 
               d=Debit()
               d.debit(username)
             elif(ch==2): 
               c=Credit()
               c.credit(username)
             elif(ch==3):
               transfer=FundTransfer()
  
             elif(ch==4):
               bstmt=BankStmt()
 
             elif(ch==5):
                c=CloseAccount()
                c.closeaccount(username)
                print("your account is closed successfuly")
                break

             elif(ch==6):
                print("logout successfully..") 
                break;
             else:
                print("enter the correct option...")

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
