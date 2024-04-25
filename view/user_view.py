import tkinter
from tkinter import *
import tkinter.messagebox as msg

from controller.user_controller import UserController


class UserView:
    def save_click(self):
        status,message =  self.controller.save(self.username.get() ,self.password.get(), self.status.get(), self.locked.get())
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def __init__(self):
        self.controller = UserController()
        win = Tk()
        win.geometry("250x250")
        Label(win, text="Username").place(x=20, y=20)
        self.username = StringVar()
        Entry(win, textvariable=self.username).place(x=80, y=20)

        Label(win, text="Password").place(x=20, y=60)
        self.password = StringVar()
        Entry(win, textvariable=self.password).place(x=80, y=60)

        Label(win, text="Status").place(x=20, y=100)
        self.status = BooleanVar()
        tkinter.Checkbutton(text='Active', variable=self.status).place(x=80, y=100)

        Label(win, text="Locked").place(x=20, y=140)
        self.locked = BooleanVar()
        tkinter.Checkbutton(text='Locked', variable=self.locked).place(x=80, y=140)

        Button(win, text="Save", command=self.save_click).place(x=80, y=190)

        win.mainloop()
