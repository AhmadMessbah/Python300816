from tkinter import *
import tkinter.messagebox as msg

from controller.person_controller import PersonController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class PersonView:
    def reset_form(self):
        self.id.variable.set(self.user.person.person_id)
        self.name.variable.set(self.user.person.name)
        self.family.variable.set(self.user.person.family)


    def edit_click(self):
        status, message = PersonController.edit(self.id.variable.get(), self.name.variable.get(), self.family.variable.get())
        if status:
            msg.showinfo("Edit Person", "Person Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)


    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()

        # Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.geometry("250x250")
        self.win.title("Profile Person")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name", 20, 60)
        self.family = TextWithLabel(self.win, "Family", 20, 100)

        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=80, y=200)

        self.reset_form()

        self.win.mainloop()

