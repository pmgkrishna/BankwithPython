import cx_Oracle
class Credit:
    def __init__(self):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();  
       try:
          cur.execute("create table printstmt(accountNumber number references customer(accountNumber),amount number not null,msg varchar2(30),balance number not null,date varchar2(30) not null)")
       except:
          print("")  
              
       

    def credit(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();
       cur.execute("select sysdate from dual")
       date=0
       for res in cur:
            date=res[0]
       dat=str(date)     
       amt=input("enter the amount to credit...")     
       cur.execute("insert into credit values('"+accno+"','"+amt+"','"+dat+"')")
       cur.execute("update account set availabeBalance=availabeBalance+'"+amt+"' where accountNumber='"+accno+"'")
       cur.execute("select * from account where accountNumber='"+accno+"'")
       bal=0
       for res in cur:
           bal=str(res[3])
       cdt="credit"    
       cur.execute("insert into printstmt values('"+accno+"','"+amt+"','"+cdt+"','"+bal+"','"+dat+"')")
       cur.execute('commit')   
       print("the amount "+amt+"is credited successfuully...")
       return
