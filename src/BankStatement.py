import cx_Oracle
class Bankstmt:
    
  def stmt(self,accno):
       con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
       cur = con.cursor();
       cur.execute("select * from printstmt where accountNumber='"+accno+"'")
       print("\t\t\t\tBANK STATEMENT\t\t\t\t")
       for res in cur:
           print("accno:"+str(res[0])+" amount:"+str(res[1])+"\t"+str(res[2])+"\tat"+"\t"+str(res[4])+"\tavailable balance ="+str(res[3]))
       return
