import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkinter import *

from controller.user_controller import UserController
from view.component.label_text import TextWithLabel
from view.component.table import Table


class UserView:
    def reset_form(self):
        self.id.variable.set("")
        self.username.variable.set("")
        self.password.variable.set("")
        self.person_id.variable.set("")
        ret, user_list = UserController.find_all()
        if ret:
            self.table.refresh_table(user_list)

    def select_row(self, user):
        self.id.variable.set(user[0])
        self.username.variable.set(user[1])
        self.password.variable.set(user[2])
        self.status.set(user[3])
        self.locked.set(user[4])
        self.person_id.variable.set(user[5])

    def save_click(self):
        ret, message = UserController.save(self.username.variable.get(),
                                           self.password.variable.get(),
                                           self.status.get(),
                                           self.locked.get(),
                                           self.person_id.variable.get())
        if ret:
            msg.showinfo("Save User", "User Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        ret, message = UserController.edit(self.id.variable.get(),
                                           self.username.variable.get(),
                                           self.password.variable.get(),
                                           self.locked.get(),
                                           self.status.get(),
                                           self.person_id.variable.get())
        if ret:
            msg.showinfo("Edit User", "User Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        ret, message = UserController.remove(self.id.variable.get())
        if ret:
            msg.showinfo("Remove User", "User Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_username(self, event):
        ret, user_list = UserController.find_by_username(self.search_username.variable.get())
        if ret:
            self.table.refresh_table(user_list)


    def __init__(self):
        self.win = Tk()
        self.win.geometry("750x310")
        self.win.title("User")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.username = TextWithLabel(self.win, "Username", 20, 60)
        self.password = TextWithLabel(self.win, "Password", 20, 100)
        self.person_id = TextWithLabel(self.win, "Person_id", 20, 180)
        self.search_username = TextWithLabel(self.win, "Username", 350, 260)
        self.search_username.text_box.bind("<KeyRelease>", self.find_by_username)

        self.status = BooleanVar()
        ttk.Checkbutton(text='Active', variable=self.status).place(x=80, y=140)
        self.status.set(True)

        self.locked = BooleanVar()
        ttk.Checkbutton(text='Locked', variable=self.locked).place(x=150, y=140)

        self.table = Table(self.win,
                           ["Id", "Username", "Password", "Status", "Locked", "person_id"],
                           [60, 100, 110, 60, 60, 60],
                           290,
                           20,
                           self.select_row)

        Button(self.win, text="Add", width=8, command=self.save_click).place(x=20, y=260)
        Button(self.win, text="Edit", width=8, command=self.edit_click).place(x=100, y=260)
        Button(self.win, text="Remove", width=8, command=self.remove_click).place(x=180, y=260)

        self.reset_form()

        self.win.mainloop()


UserView()
