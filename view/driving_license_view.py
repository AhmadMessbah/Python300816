from datetime import datetime
from tkinter import *
import tkinter.messagebox as msg
from controller.driving_license_controller import DrivingLicenseController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class DrivingLicenseView:
    def reset_form(self):
        self.id.variable.set("0")
        self.serial_number.variable.set("")
        self.date.variable.set("")
        self.city.variable.set("")
        self.expire_date.variable.set("")
        status, dl_list = DrivingLicenseController.find_by_person_id(self.user.person.person_id)
        if status:
            self.table.refresh_table(dl_list)

    def select_row(self, driving_license):
        self.id.variable.set(driving_license[0])
        self.serial_number.variable.set(driving_license[1])
        self.date.variable.set(driving_license[2])
        self.city.variable.set(driving_license[3])
        self.expire_date.variable.set(driving_license[4])

    def save_click(self):
        status, message = DrivingLicenseController.save(self.serial_number.variable.get(),
                                                        self.date.variable.get(),
                                                        self.city.variable.get(),
                                                        self.expire_date.variable.get(),
                                                        self.person.variable.get()
                                                        )
        if status:
            msg.showinfo("Save DrivingLicense", "DrivingLicense Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)


    def edit_click(self):
        status, message = DrivingLicenseController.edit(self.serial_number.variable.get(),
                                                        self.date.variable.get(),
                                                        self.city.variable.get(),
                                                        self.expire_date.variable.get(),
                                                        self.person.variable.get()
                                                        )
        if status:
            msg.showinfo("Edit DrivingLicense", "DrivingLicense Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = DrivingLicenseController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove DrivingLicense", "DrivingLicense Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_serial_number(self, event):
        status, serial_number = DrivingLicenseController.find_by_serial_number_and_person_id(
            self.search_serial_number.variable.get(), self.user.person.person_id)
        if status:
            self.table.refresh_table(serial_number)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)


    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Panel")

        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # center form
        x = (self.win.winfo_screenwidth() - 1050) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"1000x400+{x}+{y}")

        self.id = TextWithLabel(self.win, "ID", 30, 20, disabled=True)
        self.serial_number = TextWithLabel(self.win, "SerialNumber", 30, 50)
        self.date = TextWithLabel(self.win, "Date", 30, 100)
        self.city = TextWithLabel(self.win, "City", 30, 150)
        self.expire_date = TextWithLabel(self.win, "ExpireDate", 30, 200)
        self.person = TextWithLabel(self.win, "Person", 30, 250, disabled=True)
        self.person.variable.set(f"{self.user.person.person_id} - {self.user.person.name} {self.user.person.family}")

        self.search_serial_number = TextWithLabel(self.win, "Find By Serial Number", 250, 300, 100)
        self.search_serial_number.text_box.bind("<KeyRelease>", self.find_by_serial_number)

        self.table = Table(self.win,
                           ["Id", "SerialNumber", "Date", "city", "ExpireDate"],
                           [60, 150, 150, 80, 150],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="New", width=10, command=self.reset_form, bg='#86CA93', fg='black').place(x=20, y=300)
        Button(self.win, text="Save", width=10, command=self.save_click).place(x=100, y=300)
        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=20, y=350)
        Button(self.win, text="Remove", width=10, command=self.remove_click, bg='#F23C3C', fg='black').place(x=100, y=350)

        self.reset_form()

        self.win.mainloop()
