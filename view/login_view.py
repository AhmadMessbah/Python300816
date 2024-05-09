import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkinter import *

from controller.user_controller import UserController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class LoginView:
    def login_click(self):
        ret, user = UserController.find_by_username_and_password(self.username.variable.get(), self.password.variable.get())
        if ret:
            main_view = MainView(self, user)
        else:
            msg.showerror("Login Error", "Access Denid !!!")


    def __init__(self):
        win = Tk()
        win.geometry("710x310")
        win.title("User")


        self.username = TextWithLabel(win, "Username", 20, 60)
        self.password = TextWithLabel(win, "Password", 20, 100)


        Button(win, text="Login", width=8, command=self.login_click).place(x=100, y=260)

        win.mainloop()