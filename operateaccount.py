from tkinter import Tk, Frame, Button, Label, StringVar
import insertrecord
import deleterecord
import updaterecord
import displayrecord

class TakeOperation :
    def __init__(self, root):
        self.root = root
        self.root.title("Account Operations")
        self.root.geometry("500x600")

        self.b1 = Button(self.root, text="Insert record",
                             width=40, height=2,
                             bg='light blue',
                             command=self.remove1)
        self.b2 = Button(self.root, text="Delete record",
                             width=40, height=2,
                             bg='light blue',
                             command=self.remove2)
        self.b3 = Button(self.root, text="Update record",
                             width=40, height=2,
                             bg='light blue',
                             command=self.remove3)
        self.b4 = Button(self.root, text="Display record",
                             width=40, height=2,
                             bg='light blue',
                             command=self.remove4)
        self.b5 = Button(self.root, text="Exit",
                             width=25, height=2,
                             bg='red',
                             command=self.exitWindow)


        self.b1.place(x=100,y=50)
        self.b2.place(x=100,y=150)
        self.b3.place(x=100,y=250)
        self.b4.place(x=100,y=350)
        self.b5.place(x=150,y=450)
        
    def remove1(self):
        self.root.destroy()
        ins_rec = Tk()
        msg = StringVar()
        insertrecord.Insert(ins_rec, msg)
        return

    def remove2(self):
        self.root.destroy()
        del_rec = Tk()
        msg = StringVar()
        deleterecord.Delete(del_rec, msg)
        return

    def remove3(self):
        self.root.destroy()
        upd_rec = Tk()
        msg = StringVar()
        updaterecord.Update(upd_rec, msg)
        return

    def remove4(self):
        self.root.destroy()
        dis_rec = Tk()
        msg = StringVar()
        displayrecord.Display(dis_rec,msg)
        return

    def exitWindow(self):
        self.root.destroy()
        return

