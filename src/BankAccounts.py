import cx_Oracle
class BankAccount:
    def customerCreation(self,accno):
         #cur.execute("create sequence accountnumber start with '"+strt+"' increment by '"+fnis+"' nocycle nocache;")
         con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
         cur = con.cursor();  
         try:
             cur.execute("create table customer(accountNumber number primary key,password varchar2(30) unique,firstName varchar2(30) not null,lastName varchar2(30))")
         except:
             print("")
         fname=input("enter the first name ...")
         lname=input("enter the last name..")
         passw=input("enter the password to your account..")            
         cur.execute("insert into customer values('"+accno+"','"+passw+"','"+fname+"','"+lname+"')")            
         cur.execute('commit')
         return (accno,passw)

    def addressInsertion(self,number):
         con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
         cur = con.cursor();  
         try:
             cur.execute("create table address(accountNumber number references customer(accountNumber),cellno number primary key,streetName varchar2(30) not null,area varchar2(30) not null,district varchar2(30) not null,state varchar2(30) not null,pinCode number not null)")
         except:
             print("")
         street=input("enter the street name..")
         area=input("enter the living area..")
         district=input("enter the district  name..")
         state=input("enter the state of the customer..")
         pincode=input("enter the pincode of your address..")
         cellno=input("enter the cell number of the customer..")
         cur.execute("insert into address values('"+number+"','"+cellno+"','"+street+"','"+area+"','"+district+"','"+state+"','"+pincode+"')")
         cur.execute('select * from address')
         cur.execute('commit')
         
    def accountCreation(self,number):
         con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
         cur = con.cursor();  
         try:
            cur.execute("create table account(accountNumber number references customer(accountNumber),accType varchar2(30),minimumBalance integer not null,availabeBalance integer  not null,maximumWithdrawal integer not null,numberOfWitdrawals integer not null)")
         except:
            print("")
         choice=int(input("enter the choice..\n1.SAVINGS\n2.CURRENT ACCOUNT\n"))
         if(choice==1):
              accType="savings";
              totalWd=str(10);
              minimumBalance=str(0);
              availableBalance=str(0);
              noWd=str(0);
              cur.execute("insert into account values('"+number+"','"+accType+"','"+minimumBalance+"','"+availableBalance+"','"+totalWd+"','"+noWd+"')")
              cur.execute('commit')
         else :
              accType="current"
              totalWd=str(999);
              minimumBalance=str(5000);
              availableBalance=str(5000);
              noWd=str(0);
              cur.execute("insert into account values('"+number+"','"+accType+"','"+minimumBalance+"','"+availableBalance+"','"+totalWd+"','"+noWd+"')")
              cur.execute('commit')

    def lockingAccounts(self):
        
         con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
         cur = con.cursor();  
         try:
            cur.execute("create table lockedaccount(accountNumber number references customer(accountNumber),password varchar2(30) not null)")
         except:
            print("")
   