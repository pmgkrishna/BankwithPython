import cx_Oracle
from BankAccounts import *
print("\n1.admin...\n2.sign up as a new user...\n3.sign in as a existing user...\n4.exit")
choice=input("\nenter your option")
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
     print("") 
   elif(choice=='4'):
     break;
   else:
     print("Enter the correct option")
   choice=input("\nenter your option")
