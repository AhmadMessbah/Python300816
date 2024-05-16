import tkinter.messagebox as msg
from tkinter import *

from controller.sim_card_controller import SimCardController
from view.component.label_text import TextWithLabel
from view.component.table import Table


class SimCardView:
    def save_click(self):
        status, message = SimCardController.save(self.number.get(),
                                                 self.operator.get(),
                                                 self.price.get(),
                                                 self.owner.get()
                                                 )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def reset_form(self):
        self.number.variable.set("")
        self.operator.variable.set("")
        self.price.variable.set("")
        self.owner.variable.set("")
        status, sim_card_list = SimCardController.find_all()
        if status:
            self.table.refresh_table(sim_card_list)

    def select_row(self, sim_card):
        self.number.variable.set(sim_card[0])
        self.operator.variable.set(sim_card[1])
        self.price.variable.set(sim_card[2])

    def edit_click(self):
        status, message = SimCardController.edit(self.number.variable.get(), self.operator.variable.get(),
                                                 self.price.variable.get())
        if status:
            msg.showinfo("Edit SimCard", "SimCard Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = SimCardController.remove(self.number.variable.get())
        if status:
            msg.showinfo("Remove SimCard", "SimCard Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_owner(self, event):
        status, sim_card_list = SimCardController.find_by_owner(self.search_owner.variable.get())
        if status:
            self.table.refresh_table(sim_card_list)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.geometry("600x300")
        win.title("SimCard")

        Label(win, text="Number").place(x=20, y=20)
        self.number = StringVar()
        Entry(win, textvariable=self.number).place(x=80, y=20)

        Label(win, text="Operator").place(x=20, y=60)
        self.operator = StringVar()
        Entry(win, textvariable=self.operator).place(x=80, y=60)

        Label(win, text="Price").place(x=20, y=100)
        self.price = StringVar()
        Entry(win, textvariable=self.price).place(x=80, y=100)

        Label(win, text="Owner").place(x=20, y=140)
        self.owner = StringVar()
        Entry(win, textvariable=self.owner).place(x=80, y=140)

        self.id = TextWithLabel(win, "Id", 20, 20, disabled=True)
        self.number = TextWithLabel(win, "PhoneNumber", 20, 60)
        self.operator = TextWithLabel(win, "Operator", 20, 60)
        self.price = TextWithLabel(win, "Price", 20, 100)
        self.owner = TextWithLabel(win, "Owner", 20, 100)
        self.search_owner = TextWithLabel(win, "Owner", 300, 270)
        self.search_owner.text_box.bind("<KeyRelease>", self.find_by_owner)

        self.table = Table(win,
                           ["Id", "Number", "Operator", "Price", "Owner"],
                           [60, 100, 60, 80, 100],
                           250,
                           20,
                           self.select_row)

        Button(win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()
        win.mainloop()


SimCardView(None)
