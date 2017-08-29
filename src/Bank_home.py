import cx_Oracle
from BankAccounts import *
from BankSignIn import *
from BankDebit  import *
from BankCredit  import *
from BankStatement import *
from BankFundTransfer import*
from BankClosingAccounts import *
from BankBalance import *
con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
cur = con.cursor();  
attempts=int(3)
choice=int(0)
while(choice!=3):   
   print("\n1.admin...\n2.sign up as a new user...\n3.sign in as a existing user...\n4.exit")
   choice=input("\nenter your option..")
   if(choice=='1'):          
        userName=input("\nEnter the username:")
        passWord=input("Enter the password:")
        if(passWord=="admin",userName=="admin"):
           print("\n\t\t\t\t\twelcome ADMIN\t\t\t\t\t")
           choice=0
           while(choice!=3):
               choice=input("\n1.view locked accounts...\n2.view closed accounts...\n3.logout...\nenter the choice...")
               if(choice=='1'):          
                  cur.execute("select * from lockedaccount")
                  print("\n\t\t\t\t\tLOCKED ACCOUNTS\t\t\t\t\t")
                  i=int(0)
                  for res in cur:
                     i=i+1
                     rollno=str(res[0])
                     cur.execute("select * from customer where accountNumber='"+rollno+"'")
                     for result in cur:
                        print(str(i)+"."+"name="+str(result[2])+"\taccount number="+str(result[0])+"\tpassword="+str(result[1]))
                     
               elif(choice=='2'):
                  cur.execute("select * from accountclosure")
                  print("\n\t\t\t\t\tCLOSED ACCOUNTS\t\t\t\t\t")
                  i=int(0)
                  for res in cur:
                     i=i+1
                     rollno=str(res[0])
                     cur.execute("select * from customer where accountNumber='"+rollno+"'")
                     for result in cur:
                        print(str(i)+"."+"name="+str(result[2])+"\taccount number="+str(result[0])+"\tstatus="+str(result[1]))
               elif(choice=='3'):
                  print("logout successfully")
                  break
               else:
                  print("enter the corect option....")
   

   elif(choice=='2'):
     b=BankAccount() 
     (accno,passw)=b.customerCreation()
     b.addressInsertion(accno)
     b.accountCreation(accno)
     print("\naccount is successfully created...")
     print("\nyour user name is..."+accno+"\nyour password is...."+passw)
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
        lockpassw=0
        for row in res:
           lockpassw=row[1]
        if(password==str(lockpassw)):
           print("your is locked under bank..")
           break
        else: 
           attempts=int(3)
           print("login successully..")
           cur.execute("select firstname from customer where accountNumber='"+username+"'")
           result=cur.fetchall()
           custname=0;
           for res in result:
              custname=res[0]              
           print("\t\t\twelcome "+str(custname)+" to e-bank system\t\t\t\t\t")
           ch='0'
           while(ch!='7'):
             print("\n1.avaiable balance\n2.debit\n3.credit\n4.fund transfer\n5.bank statement\n6.close account\n7.logout")        
             ch=input("\nenter the choice..") 
             if(ch=='1'):
               bal=Balance()
               bal.balance(username)
             elif(ch=='2'): 
               d=Debit()
               amt=input("enter the amount to withdraw...")
               d.debit(username,amt)
             elif(ch=='3'): 
               c=Credit()
               amt=input("enter the amount to credit...")     
               c.credit(username,amt)
             elif(ch=='4'):
                f=FundTransfer() 
                f.fundTransfer(username)
             elif(ch=='5'):
               bstmt=Bankstmt()
               bstmt.stmt(username)
             elif(ch=='6'):
                c=CloseAccount()
                c.closeaccount(username)
                print("your account is closed successfuly")
                break
             elif(ch=='7'):
                print("logout successfully..") 
                break;  
             else:
                print("enter the correct option...")

     else:
        attempts=attempts-1
        print("password is incorect...")
        if(attempts<=0):
           try:  
            cur.execute("insert into lockedaccount values('"+username+"','"+retpassw+"')")
           except:
              print(str(username) + " is not a account number!please verify it...")
              break;
           cur.execute("commit")
           print("your account is locked")
           break;
   elif(choice=='4'):
     print("thank u")
     break;
   else:
     print("Enter the correct option")
