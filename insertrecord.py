#pylint:disable=E1101
from tkinter import Tk, Frame, Button, Label, Entry
import operateaccount
import connect

class Insert :
    con=''
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Insert Record")
        self.root.geometry("700x600")

        self.head = Label(self.root, text="Record Details : ",
                             fg='red',
                             font="Times 30")

        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e1 = Entry(self.root, width=20,
                        font=" Times 25")

        self.l2 = Label(self.root, text="Name : ",
                             fg='blue',
                             font="Times 25")
        
        self.e2 = Entry(self.root, width=20,
                        font="Times 25")

        self.l3 = Label(self.root, text="Balance : ",
                             fg='blue',
                             font="Times 25")
        
        self.e3 = Entry(self.root, width=20,
                        font="Times 25")
        
        self.b1 = Button(self.root, text="Insert",
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
        
        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 30")
        
        self.head.place(x=200,y=50)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.l2.place(x=100,y=220)
        self.e2.place(x=300,y=220)
        self.l3.place(x=100,y=330)
        self.e3.place(x=300,y=330)
        self.b1.place(x=250,y=400)
        self.b2.place(x=400,y=400)
        self.b3.place(x=550,y=400)
        self.l4.place(x=100,y=500)
        
    def nextFrame(self):
        ano = self.e1.get()
        name = self.e2.get()
        amount = self.e3.get()

        if ano=='':
            self.msg.set("accno field cannot be empty")
        elif name=='':
            self.msg.set("name field cannot be empty")
        elif amount=='':
            self.msg.set("amount field cannot be empty")
        else:
            try:
                ano = int(ano)
                amount = int(amount)
                Insert.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur = Insert.con.cursor()
                print("insert into account values("+str(ano)+",'"+name+"',"+str(amount)+")")
                cur.execute("insert into account values("+str(ano)+",'"+name+"',"+str(amount)+")")
                Insert.con.commit()
                self.msg.set("Successfully inserted")
            finally:
                if Insert.con != '':
                    Insert.con.close()
                    print("Connection released")
        return

    def exitWindow(self):
        self.root.destroy()
        return
    def backWindow(self):
        self.root.destroy()
        takeop = Tk()
        operateaccount.TakeOperation(takeop)
        return
