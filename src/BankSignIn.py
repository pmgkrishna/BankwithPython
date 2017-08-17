import cx_Oracle

class SignIn:
    def signIn(self):
        userName=input("\nEnter the username:")
        passWord=input("\nEnter the password:")
        con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
        cur = con.cursor();
        cur.execute("select * from customer where accountNumber='"+userName+"'")
        res=cur.fetchall()
        for row in res:
           passw=row[1]
        return(userName,passWord,passw)
