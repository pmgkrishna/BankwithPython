import cx_Oracle
class SignIn:
    def signIn(self):
        print("\t\t\t\tLogin page\t\t\t\t\t\n\n")
        userName=input("Enter the username:")
        passWord=input("Enter the password:")
        con = cx_Oracle.connect('SYSTEM/pmgkrishna96')
        cur = con.cursor();
        cur.execute("select * from customer where accountNumber='"+userName+"'")
        res=cur.fetchall()
        passw="0"
        for row in res:
           passw=row[1]
        return(userName,passWord,passw)
