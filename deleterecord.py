from tkinter import Tk, Frame, Button, Label, Entry
import connect
import operateaccount
class Delete :
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Delete Record")
        self.root.geometry("700x600")

        self.head = Label(self.root, text="Delete Acc : ",
                             fg='red',
                             font="Times 30")
        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e1 = Entry(self.root, width=20,
                        font=" Times 25")
        
        self.b1 = Button(self.root, text="Delete",
                             width=20, height=2,
                             bg='light blue',
                             command=self.nextFrame)
        self.b2 = Button(self.root, text="Exit",
                             width=20, height=2,
                             bg='light blue',
                             command=self.exitWindow)
        self.b3 = Button(self.root, text="Back",
                             width=20, height=2,
                             bg='light blue',
                             command=self.backWindow)
        self.l3 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 30")
        self.l1.place(x=100,y=100)
        self.e1.place(x=250,y=100)
        self.b1.place(x=200,y=200)
        self.b2.place(x=350,y=200)
        self.b3.place(x=500,y=200)
        self.l3.place(x=150,y=300)
        return
    def exitWindow(self):
        self.root.destroy()
        return
    def nextFrame(self):
        ano = self.e1.get()
        if ano=='':
            self.msg.set("Account no cannot be empty")
            return
        else:
            try:
                Delete.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur = Delete.con.cursor()
                cur.execute("select accno from account where accno="+ano)
                row = cur.fetchone()           
                if row:
                    #delete account
                    print("delete from account where accno="+ano)
                    cur.execute("delete from account where accno="+ano)
                    Delete.con.commit()
                    self.msg.set("Account deleted successfully")
                else:
                    self.msg.set("Exception : Account don't exist")

            finally:
                if Delete.con != '':
                    Delete.con.close()
                    print("Connection released")
        return
    def backWindow(self):
        self.root.destroy()
        takeop = Tk()
        operateaccount.TakeOperation(takeop)
        return
