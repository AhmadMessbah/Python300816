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
        status, product_list = ProductController.find_by_person_id(self.user.person.person_id)
        if status:
            self.table.refresh_table(product_list)
        else:
            self.table.refresh_table([])

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

    def reset_click(self):
        self.name.variable.set("")
        self.brand.variable.set("")
        self.serial.variable.set("")
        self.buy_price.variable.set("")

    def find_by_product_id(self, event):
        status, product_list = ProductController.find_by_person_and_product_id(self.user.person.person_id,
                                                                               self.search_person_id.variable.get())
        if status:
            self.table.refresh_table(product_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.geometry("800x320")
        self.win.title("Product")
        self.id = TextWithLabel(self.win, "Id :", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name :", 20, 60)
        self.brand = TextWithLabel(self.win, "Brand :", 20, 100)
        self.serial = TextWithLabel(self.win, "Serial :", 20, 140)
        self.buy_price = TextWithLabel(self.win, "Buy Price :", 20, 180)
        self.person_id = TextWithLabel(self.win, "Person id :", 20, 220, disabled=True)
        self.person_id.variable.set(self.user.person.person_id)

        self.search_person_id = TextWithLabel(self.win, "Product id : ", 280, 270, distance=80)
        self.search_person_id.text_box.bind("<KeyRelease>", self.find_by_product_id)

        self.table = Table(self.win,
                           ["Id", "Name", "Brand", "Serial", "Buy Price"],
                           [60, 100, 100, 100, 100],
                           280,
                           20,
                           self.select_row)


        Button(self.win, text="Add", width=10, command=self.save_click, bg="lightgreen").place(x=20, y=250)
        Button(self.win, text="Edit", width=10, command=self.edit_click, bg="lightblue").place(x=20, y=285)
        Button(self.win, text="Remove", width=10, command=self.remove_click, bg="red").place(x=125, y=250)
        Button(self.win, text="Reset", width=10, command=self.reset_click, bg="gray").place(x=125, y=285)

        self.reset_form()

        self.win.mainloop()
