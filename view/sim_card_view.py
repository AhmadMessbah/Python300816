import tkinter.messagebox as msg
from tkinter import *
from controller.sim_card_controller import SimCardController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class SimCardView:
    def reset_form(self):
        self.number.variable.set("")
        self.operator.variable.set("")
        self.price.variable.set("")

        status, sim_card_list = SimCardController.find_all()
        if status:
            self.table.refresh_table(sim_card_list)

    def select_row(self, sim_card):
        self.id.variable.set(sim_card[0])
        self.number.variable.set(sim_card[1] if str(sim_card[1]).startswith("0") else f"0{sim_card[1]}")
        self.operator.variable.set(sim_card[2])
        self.price.variable.set(sim_card[3])

    def save_click(self):
        status, message = SimCardController.save(
            self.number.variable.get(),
            self.operator.variable.get(),
            self.price.variable.get(),
            self.owner.variable.get()
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = SimCardController.edit(self.id.variable.get(),
                                                 self.number.variable.get(),
                                                 self.operator.variable.get(),
                                                 self.price.variable.get(),
                                                 self.owner.variable.get()
                                                 )
        if status:
            msg.showinfo("Edit SimCard", "SimCard Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = SimCardController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove SimCard", "SimCard Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_number(self, event):
        status, sim_card_list = SimCardController.find_by_number(self.search_number.variable.get())
        if status:
            self.table.refresh_table(sim_card_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.geometry("600x300")
        self.win.title("SimCard")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.number = TextWithLabel(self.win, "Number", 20, 60)
        self.operator = TextWithLabel(self.win, "Operator", 20, 100)
        self.price = TextWithLabel(self.win, "Price", 20, 140)
        self.owner = TextWithLabel(self.win, "Owner", 20, 180, disabled=True)
        self.owner.variable.set(self.user.person.person_id)
        self.search_number = TextWithLabel(self.win, "SearchNumber", 300, 250)
        self.search_number.text_box.bind("<KeyRelease>", self.find_by_number)

        self.table = Table(self.win,
                           ["Id", "Number", "Operator", "Price", "Owner"],
                           [60, 100, 60, 80, 100],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(self.win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(self.win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()
        self.win.mainloop()
