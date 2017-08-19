import cx_Oracle
class Balance:

    def balance(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();
       cur.execute("select * from account where accountNumber='"+accno+"'")
       bal=0
       for res in cur:
           bal=str(res[3])
       print("the available balance in your account is "+bal)
       
