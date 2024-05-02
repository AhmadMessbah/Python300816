from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.person_controller import PersonController
from model.entity.person import Person
from view.component.label_text import TextWithLabel
from view.component.table import Table


def reset_form():
    id.variable.set("")
    name.variable.set("")
    family.variable.set("")
    status, person_list = PersonController.find_all()
    if status:
        table.refresh_table(person_list)


def select_row(person):
    id.variable.set(person[0])
    name.variable.set(person[1])
    family.variable.set(person[2])


def save_click():
    status, message = PersonController.save(name.variable.get(), family.variable.get())
    if status:
        msg.showinfo("Save Person", "Person Saved")
        reset_form()
    else:
        msg.showerror("Save Error", message)

def edit_click():
    status, message = PersonController.edit(id.variable.get(), name.variable.get(), family.variable.get())
    if status:
        msg.showinfo("Edit Person", "Person Edited")
        reset_form()
    else:
        msg.showerror("Edit Error", message)

def remove_click():
    status, message = PersonController.remove(id.variable.get())
    if status:
        msg.showinfo("Remove Person", "Person Removed")
        reset_form()
    else:
        msg.showerror("Remove Error", message)

def find_by_family(event):
    status , person_list = PersonController.find_by_family(search_family.variable.get())
    if status:
        table.refresh_table(person_list)

win = Tk()
win.geometry("600x300")

id = TextWithLabel(win, "Id", 20, 20, disabled=True)
name = TextWithLabel(win, "Name", 20, 60)
family = TextWithLabel(win, "Family", 20, 100)
search_family = TextWithLabel(win, "Family", 300, 270)
search_family.text_box.bind("<KeyRelease>" , find_by_family)

table = Table(win,
              ["Id", "Name", "Family"],
              [60, 100, 100],
              250,
              20,
              select_row)

Button(win, text="Add",width=8, command=save_click).place(x=20, y=250)
Button(win, text="Edit",width=8, command=edit_click).place(x=100, y=250)
Button(win, text="Remove",width=8, command=remove_click).place(x=180, y=250)

reset_form()

win.mainloop()

