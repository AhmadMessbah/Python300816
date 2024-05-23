from tkinter import *
import tkinter.messagebox as msg

from controller.person_controller import PersonController
from view.component.label_text import TextWithLabel
from view.component.persian_calendar import PersianCalendar
from view.component.table import Table
from view.main_view import MainView



class AdminView:
    def reset_form(self):
        self.id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        status, person_list = PersonController.find_all()
        if status:
            self.table.refresh_table(person_list)

    def select_row(self, person):
        self.id.variable.set(person[0])
        self.name.variable.set(person[1])
        self.family.variable.set(person[2])
        self.birth_date.set_date(person[3])

    def save_click(self):
        status, message = PersonController.save(self.name.variable.get(), self.family.variable.get(),
                                                self.birth_date.gregorian_date)
        if status:
            msg.showinfo("Save Person", "Person Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = PersonController.edit(self.id.variable.get(), self.name.variable.get(),
                                                self.family.variable.get(), self.birth_date.gregorian_date)
        if status:
            msg.showinfo("Edit Person", "Person Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = PersonController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove Person", "Person Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_family(self, event):
        status, person_list = PersonController.find_by_family(self.search_family.variable.get())
        if status:
            self.table.refresh_table(person_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()

        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.geometry("600x300")
        self.win.title("Person")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name", 20, 60)
        self.family = TextWithLabel(self.win, "Family", 20, 100)
        Label(self.win, text="BirthDate").place(x=20,y=140)

        self.birth_date = PersianCalendar(self.win, 80, 140, self.user.person.birth_date)

        self.search_family = TextWithLabel(self.win, "Family", 300, 270)
        self.search_family.text_box.bind("<KeyRelease>", self.find_by_family)

        self.table = Table(self.win,
                           ["Id", "Name", "Family", "BirthDate"],
                           [60, 100, 100, 100],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(self.win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(self.win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()

        self.win.mainloop()
