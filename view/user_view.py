import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkinter import *

from controller.user_controller import UserController
from view.component.label_text import TextWithLabel
from view.component.table import Table


def reset_form():
    id.variable.set("")
    username.variable.set("")
    password.variable.set("")
    status, user_list = UserController.find_all()
    if status:
        table.refresh_table(user_list)


def select_row(user):
    id.variable.set(user[0])
    username.variable.set(user[1])
    password.variable.set(user[2])


def save_click():
    ret, message = UserController.save(username.variable.get(), password.variable.get(), status.get(),
                                          locked.get())
    if ret:
        msg.showinfo("Save User", "User Saved")
        reset_form()
    else:
        msg.showerror("Save Error", message)


def edit_click():
    ret, message = UserController.edit(id.variable.get(), username.variable.get(), password.variable.get() , locked.get() , status.get())
    if ret:
        msg.showinfo("Edit User", "User Edited")
        reset_form()
    else:
        msg.showerror("Edit Error", message)


def remove_click():
    ret, message = UserController.remove(id.variable.get())
    if status:
        msg.showinfo("Remove User", "User Removed")
        reset_form()
    else:
        msg.showerror("Remove Error", message)


def find_by_username(event):
    ret, user_list = UserController.find_by_username(search_username.variable.get())
    if ret:
        table.refresh_table(user_list)


win = Tk()
win.geometry("710x310")

id = TextWithLabel(win, "Id", 20, 20, disabled=True)
username = TextWithLabel(win, "Username", 20, 60)
password = TextWithLabel(win, "Password", 20, 100)
search_username = TextWithLabel(win, "Username", 350, 260)
search_username.text_box.bind("<KeyRelease>", find_by_username)

status = BooleanVar()
ttk.Checkbutton(text='Active', variable=status).place(x=80, y=140)
status.set(True)

locked = BooleanVar()
ttk.Checkbutton(text='Locked', variable=locked).place(x=150, y=140)

table = Table(win,
              ["Id", "Username", "Password", "Status", "Locked"],
              [60, 100, 110, 60, 60],
              290,
              20,
              select_row)

Button(win, text="Add", width=8, command=save_click).place(x=20, y=260)
Button(win, text="Edit", width=8, command=edit_click).place(x=100, y=260)
Button(win, text="Remove", width=8, command=remove_click).place(x=180, y=260)

reset_form()

win.mainloop()
