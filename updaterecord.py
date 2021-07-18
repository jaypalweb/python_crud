#pylint:disable=E1101
from tkinter import Tk, Frame, Button, Label, Entry, StringVar
import operateaccount
import connect

class Update :
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Update Record")
        self.root.geometry("700x650")
        self.entryTextE1 = StringVar()
        self.entryTextE2 = StringVar()
        self.entryTextE3 = StringVar()
        self.head = Label(self.root, text="Enter Acc : ",
                             fg='red',
                             font="Times 30")
        self.l0 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e0 = Entry(self.root, width=20,
                        font=" Times 25")
        
        self.b0 = Button(self.root, text="Show Details",
                             width=20, height=2,
                             bg='light blue',
                             command=self.showDetail)
        
        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e1 = Entry(self.root, textvariable=self.entryTextE1, state='disabled', width=20,
                        font=" Times 25")

        self.l2 = Label(self.root, text="Name : ",
                             fg='blue',
                             font="Times 25")
        
        self.e2 = Entry(self.root, textvariable=self.entryTextE2, width=20,
                        font="Times 25")

        self.l3 = Label(self.root, text="Balance : ",
                             fg='blue',
                             font="Times 25")
        
        self.e3 = Entry(self.root, textvariable=self.entryTextE3, width=20,
                        font="Times 25")
        
        self.b1 = Button(self.root, text="Update",
                             width=20, height=2,
                             bg='light blue',
                             command=self.updateFrame)

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
        self.l0.place(x=100,y=100)
        self.e0.place(x=300,y=100)
        self.b0.place(x=250,y=150)
        self.l1.place(x=100,y=200)
        self.e1.place(x=300,y=200)
        self.l2.place(x=100,y=250)
        self.e2.place(x=300,y=250)
        self.l3.place(x=100,y=330)
        self.e3.place(x=300,y=330)
        self.b1.place(x=250,y=400)
        self.b2.place(x=400,y=400)
        self.b3.place(x=550,y=400)
        self.l4.place(x=100,y=500)
        #entryTextE1.set( "Hello World" )
        return
    def updateFrame(self):
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
                Update.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur = Update.con.cursor()
                cur.execute("update account set name = '"+name+"', amount = "+str(amount)+" where accno = "+str(ano)+"")
                Update.con.commit()
                self.msg.set("Successfully updated")
            finally:
                if Update.con != '':
                    Update.con.close()
                    print("Connection released")
        return
    def backWindow(self):
        self.root.destroy()
        takeop = Tk()
        operateaccount.TakeOperation(takeop)
        return
    def showDetail(self):
        ano = self.e0.get()
        try:
            Update.con = connect.DBConnect.getConn()
            print("Connected to database")
            cur = Update.con.cursor()
            cur.execute("select accno, name, amount from account where accno='"+ano+"'")
            row = cur.fetchone()           
            if row:
                self.entryTextE1.set( row[0] )
                self.entryTextE2.set( row[1] )
                self.entryTextE3.set( row[2] )
                self.msg.set("")
            else:
                self.msg.set("Invalid Account")
                self.entryTextE1.set("")
                self.entryTextE2.set("")
                self.entryTextE3.set("")

        finally:
            if Update.con != '':
                Update.con.close()
                print("Connection released")
        return
    def exitWindow(self):
        self.root.destroy()
        return
