#pylint:disable=E1101
from tkinter import Tk, Frame, Button, Label, Entry, StringVar
import operateaccount
import connect
class LoginDetails :
    con = ''
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Login Details")
        self.root.geometry("700x500")
        self.l1 = Label(self.root, text="User Name : ",
                             fg='red',
                             font="Times 20")

        self.l2 = Label(self.root, text="Password : ",
                             fg='red',
                             font="Times 20")

        self.e1 = Entry(self.root, width=20,
                        font=" Times 25")

        self.e2 = Entry(self.root, width=20,
                        font="Times 25")

        self.b1 = Button(self.root, text="Login",
                             width=20, height=2,
                             bg='light blue',
                             command=self.nextFrame)

        self.b2 = Button(self.root, text="Exit",
                             width=20, height=2,
                             bg='light blue',
                             command=self.exitWindow)
        
        self.l3 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 30")
        
        self.l1.place(x=100,y=100)
        self.e1.place(x=250,y=100)
        self.l2.place(x=100,y=220)
        self.e2.place(x=250,y=220)
        self.b1.place(x=200,y=330)
        self.b2.place(x=350,y=330)
        self.l3.place(x=150,y=400)
        
    def nextFrame(self):
        un = self.e1.get()
        pw = self.e2.get()
        if un=='':
            self.msg.set("User name cannot be empty")
            return
        elif pw=='':
            self.msg.set("Password cannot be empty")
        else:
            try:
                LoginDetails.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur = LoginDetails.con.cursor()
                cur.execute("select uname, password from login where uname='"+un+"'")
                row = cur.fetchone()           
                if un==row[0] and pw==row[1]:
                    self.root.destroy()
                    takeop = Tk()
                    operateaccount.TakeOperation(takeop)
                else:
                    self.msg.set("Exception : Invalid Login")

            finally:
                if LoginDetails.con != '':
                    LoginDetails.con.close()
                    print("Connection released")
        return

    def exitWindow(self):
        self.root.destroy()
        return

root = Tk()
msg = StringVar()
window = LoginDetails(root,msg)
root.mainloop()
