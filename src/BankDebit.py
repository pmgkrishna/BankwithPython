import cx_Oracle
class Debit:
    def __init__(self):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();  
       try:
          cur.execute("create table debit(accountNumber number references customer(accountNumber),amount number not null,debitdate varchar2(30) not null)")
       except:
            print("")
       

    def debit(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();
       cur.execute("select sysdate from dual")
       date=0
       for res in cur:
            date=res[0]
       dat=str(date)     
       amt=input("enter the amount to withdraw...")
       cur.execute("select * from account where accountNumber='"+accno+"'")
       miniBal=0
       avlbal=0
       maxwd=0
       nowd=0
       for res in cur:
           minibal=res[2]
           avlbal=res[3]
           maxwd=res[4]
           nowd=res[5]
       amount=int(amt)
       total=((int(avlbal))-((int(minibal))))
       if(total>amount):
         if((int(nowd)<int(maxwd))): 
           cur.execute("insert into debit values('"+accno+"','"+amt+"','"+dat+"')")
           cur.execute("update account set availabeBalance=availabeBalance-'"+amt+"' where accountNumber='"+accno+"'")
           cur.execute("update account set numberOfWitdrawals=numberOfWitdrawals+'1' where accountNumber='"+accno+"'")
           cur.execute("select * from account where accountNumber='"+accno+"'")
           bal="0"
           for res in cur:
             bal=str(res[3])
           cur.execute("insert into printstmt values('"+accno+"','"+amt+"','debit','"+bal+"','"+dat+"')")
           cur.execute('commit')   
           print("the amount "+amt+"is debited successfuully...")
         else:
            print("you have reached your withdrawal limit..")
       else:
           print("\t\tinsufficient balance")
           print("\navailable balance"+str(avlbal))
           print("minimum balance of your account"+str(minibal))
           print("the entered amount... "+str(amt))
           
