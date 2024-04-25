from tkinter import *
import tkinter.messagebox as msg
from sim_card.controller.sim_card_controller import SimCardController


class PersonView:
    def save_click(self):
        status, message = self.controller.save(self.number.get(),
                                               self.operator.get(),
                                               self.price.get(),
                                               self.owner.get()
                                               )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def __init__(self):
        self.controller = SimCardController()
        print("View")
        win = Tk()
        win.geometry("250x200")
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

        Button(win, text="Save", command=self.save_click).place(x=80, y=150)

        win.mainloop()
