import tkinter.messagebox as msg
from tkinter import *

from controller.user_controller import UserController
from view.component.label_text import TextWithLabel
from view.main_view import MainView


class LoginView:
    def login_click(self):
        ret, user = UserController.find_by_username_and_password(self.username.variable.get(),
                                                                 self.password.variable.get())
        if ret:
            self.win.destroy()
            main_view = MainView(user)
        else:
            msg.showerror("Login Error", "Access Denied !!!")

    def __init__(self):
        self.win = Tk()
        self.win.geometry("250x250")
        self.win.title("User")

        self.username = TextWithLabel(self.win, "Username", 20, 40)
        self.password = TextWithLabel(self.win, "Password", 20, 90)

        Button(self.win, text="Login", width=10, command=self.login_click).place(x=80, y=180)

        self.username.variable.set("ahmad")
        self.password.variable.set("ahmad123")

        self.win.mainloop()
