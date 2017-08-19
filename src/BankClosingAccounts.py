import cx_Oracle

class CloseAccount:
     def __init__(self):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();  
       try:
          cur.execute("create table accountclosure(accountNumber number references customer(accountNumber),closedate varchar2(30) not null)")
       except:
            print("")
       
     def closeaccount(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();
       cur.execute("select sysdate from dual")
       date=0
       for res in cur:
            date=res[0]
       dat=str(date)
       close="closed"
       cur.execute("insert into accountclosure values('"+accno+"','"+dat+"')")
       cur.execute("update customer set password='"+close+"' where accountNumber='"+accno+"'")
       cur.execute("commit")
           
