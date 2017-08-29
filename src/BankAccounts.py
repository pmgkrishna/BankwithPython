import cx_Oracle
class BankAccount:
    def customerCreation(self):
         con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
         cur = con.cursor()
         try:
           cur.execute("create table sequences(accnumber number not null)")
           cur.execute("insert into sequences values('11000')")
         except:
            print("") 
         try:
             cur.execute("create table customer(accountNumber number primary key,password varchar2(30) unique,firstName varchar2(30) not null,lastName varchar2(30))")
         except:
             print("")
         try:
            cur.execute("create table printstmt(accountNumber number references customer(accountNumber),amount number not null,msg varchar2(30),balance number not null,dates varchar2(30) not null)")
         except:
            print("")
         try:
          cur.execute("create table accountclosure(accountNumber number references customer(accountNumber),closedate varchar2(30) not null)")
         except:
            print("") 
         cur.execute("select * from sequences")
         res=cur.fetchall()
         accno="00000"
         for row in res:
           accno=row[0]
         fname=input("enter the first name ...")
         while(len(fname)!=1):
          fname=input("first name not to be an empty...")
         lname=input("enter the last name..")
         passw=input("enter the password to your account..")
         while(len(passw)!=4):
          passw=input("enter the password of 4 characters above...")
         cur.execute("insert into customer values('"+str(accno)+"','"+passw+"','"+fname+"','"+lname+"')")            
         accnos=str(int(accno)+((int(accno)%3)+5))
         cur.execute("update sequences set accnumber='"+accnos+"'")
         cur.execute('commit')
         return (str(accno),passw)

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
         while(len(pincode)!=6):
          pincode=input("enter the 6 digit pincode only...")
         cellno=input("enter the cell number of the customer..")
         while(len(cellno)!=10):
          cellno=input("enter the 10 digit cellphone number only...")
         cur.execute("insert into address values('"+number+"','"+cellno+"','"+street+"','"+area+"','"+district+"','"+state+"','"+pincode+"')")
         number=str(int(number)+((int(number)%3)+5))
         cur.execute("update sequences set accnumber='"+number+"'")
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
   
