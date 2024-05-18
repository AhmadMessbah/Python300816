import tkinter.messagebox as msg
from tkinter import *
from controller.car_controller import CarController
from view.component.label_text import TextWithLabel
from view.component.table import Table







class CarView:
    def save_click(self):
        status, message = CarController.save(self.model.get(),
                                                 self.name.get(),
                                                 self.color.get(),
                                                 self.owner.get()
                                                 )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def reset_form(self):
        self.model.variable.set("")
        self.name.variable.set("")
        self.color.variable.set("")
        self.owner.variable.set("")
        status, car_list = CarController.find_all()
        if status:
            self.table.refresh_table(car_list)


    def select_row(self, car):
        self.model.variable.set(car[0])
        self.name.variable.set(car[1])
        self.color.variable.set(car[2])
        self.owner.variable.set(car[3])

    def edit_click(self):
        status, message = CarController.edit(self.model.variable.get(),
                                                 self.name.variable.get(),
                                                 self.color.variable.get(),
                                                 self.owner.variable.get()
                                                 )
        if status:
            msg.showinfo("Edit Car", "Car Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = CarController.remove(self.model.variable.get())
        if status:
            msg.showinfo("Remove Car", "Car Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_owner(self, event):
        status, car_list = CarController.find_by_owner(self.search_owner.variable.get())
        if status:
            self.table.refresh_table(car_list)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.geometry("600x300")
        win.title("Car")

        Label(win, text="Model").place(x=20, y=20)
        self.model = StringVar()
        Entry(win, textvariable=self.model).place(x=80, y=20)

        Label(win, text="Name").place(x=20, y=60)
        self.name = StringVar()
        Entry(win, textvariable=self.name).place(x=80, y=60)

        Label(win, text="Color").place(x=20, y=100)
        self.color = StringVar()
        Entry(win, textvariable=self.color).place(x=80, y=100)

        Label(win, text="Owner").place(x=20, y=140)
        self.owner = StringVar()
        Entry(win, textvariable=self.owner).place(x=80, y=140)

        self.id = TextWithLabel(win, "Id", 20, 20, disabled=True)
        self.model = TextWithLabel(win, "CarModel", 20, 40)
        self.name = TextWithLabel(win, "Name", 20, 60)
        self.color = TextWithLabel(win, "Color", 20, 80)
        self.owner = TextWithLabel(win, "Owner", 20, 100)
        self.search_owner = TextWithLabel(win, "Owner", 300, 250)
        self.search_owner.text_box.bind("<KeyRelease>", self.find_by_owner)

        self.table = Table(win,
                           ["Id", "Model", "Name", "Color", "Owner"],
                           [60, 100, 60, 80, 100],
                           250,
                           20,
                           self.select_row)

        Button(win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()
        win.mainloop()
