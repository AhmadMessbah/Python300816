from tkinter import *
import tkinter.messagebox as msg
from controller.product_controller import ProductController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class ProductView:
    def reset_form(self):
        self.id.variable.set("")
        self.name.variable.set("")
        self.brand.variable.set("")
        self.serial.variable.set("")
        self.buy_price.variable.set("")
        status, product_list = ProductController.find_all()
        if status:
            self.table.refresh_table(product_list)

    def select_row(self, product):
        self.id.variable.set(product[0])
        self.name.variable.set(product[1])
        self.brand.variable.set(product[2])
        self.serial.variable.set(product[3])
        self.buy_price.variable.set(product[4])

    def save_click(self):
        status, message = ProductController.save(self.name.variable.get(),
                                                 self.brand.variable.get(),
                                                 self.serial.variable.get(),
                                                 self.buy_price.variable.get(),
                                                 self.person_id.variable.get()
                                                 )
        if status:
            msg.showinfo("Save Product", "Product Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = ProductController.edit(self.id.variable.get(),
                                                 self.name.variable.get(),
                                                 self.brand.variable.get(),
                                                 self.serial.variable.get(),
                                                 self.buy_price.variable.get(),
                                                 self.person_id.variable.get()
                                                 )
        if status:
            msg.showinfo("Edit Product", "Product Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = ProductController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove Product", "Product Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_person_id(self, event):
        status, product_list = ProductController.find_by_person_id(self.search_person_id.variable.get())
        if status:
            self.table.refresh_table(product_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.geometry("800x300")
        self.win.title("Product")

        self.id = TextWithLabel(self.win, "Id", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name", 20, 60)
        self.brand = TextWithLabel(self.win, "Brand", 20, 100)
        self.serial = TextWithLabel(self.win, "Serial", 20, 140)
        self.buy_price = TextWithLabel(self.win, "Buy_price", 20, 180)
        self.person_id = TextWithLabel(self.win, "Person", 20, 220, disabled=True)
        self.person_id.variable.set(f"{self.user.person.person_id} - {self.user.person.name} {self.user.person.family}")

        self.search_person_id = TextWithLabel(self.win, "product_id", 300, 270)
        self.search_person_id.text_box.bind("<KeyRelease>", self.find_by_person_id)

        self.table = Table(self.win,
                           ["Id", "Name", "Brand", "Serial", "Buy_price"],
                           [60, 100, 100, 100, 100],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(self.win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(self.win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()

        self.win.mainloop()