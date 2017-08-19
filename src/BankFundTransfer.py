import cx_Oracle
from BankDebit  import *
from BankCredit  import *

class FundTransfer:
    def __init__(self):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();  
       try:
          cur.execute("create table fundtransfer(accountNumber number references customer(accountNumber),amount number not null,toAccno number not null,transferdate varchar2(30) not null)")
       except:
            print("")
            
    def fundTransfer(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();  
       toaccno=input("enter the recipient account number")
       amt=input("enter the amount to transfer...")
       d=Debit()        
       d.debit(accno,amt)
       c=Credit()
       c.credit(toaccno,amt)
       cur.execute("select sysdate from dual")
       date=0
       for res in cur:
            date=res[0]
       dat=str(date)     
       cur.execute("insert into fundtransfer values('"+accno+"','"+amt+"','"+toaccno+"','"+dat+"')")
       cur.execute("commit")
       print("amount transfered successfully...")


    
