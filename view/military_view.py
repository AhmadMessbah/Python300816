from datetime import datetime
from tkinter import *
import tkinter.messagebox as msg
from controller.military_controller import MilitaryController
from view.component.label_text import TextWithLabel
from view.component.persian_calendar import PersianCalendar
from view.component.table import Table
from view.main_view import MainView


class MilitaryView:

    def reset_form(self):
        self.id.set("")
        self.serial_number.variable.set("")
        self.city.variable.set("")
        self.organ.variable.set("")

        status, military_list = MilitaryController.find_by_person(self.user.person.person_id)

        if status:
            self.table.refresh_table(military_list)
        else:
            self.table.refresh_table([])

    def select_row(self, military):
        self.id.set(military[0])
        self.serial_number.variable.set(str("{:011d}".format(military[1])))
        self.city.variable.set(military[2])
        self.organ.variable.set(military[3])

    def save_click(self):
        status, message = MilitaryController.save(self.serial_number.variable.get(),
                                                  self.city.variable.get(),
                                                  self.organ.variable.get(),
                                                  self.start_calendar.gregorian_date,
                                                  self.end_calendar.gregorian_date,
                                                  self.user.person.person_id)
        if status:
            msg.showinfo("Save Record", "Record Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = MilitaryController.edit(self.id.get(),
                                                  self.serial_number.variable.get(),
                                                  self.city.variable.get(),
                                                  self.organ.variable.get(),
                                                  self.start_calendar.gregorian_date,
                                                  self.end_calendar.gregorian_date,
                                                  self.user.person.person_id)
        if status:
            msg.showinfo("Edit Record", "Record Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = MilitaryController.remove(self.id.get())
        if status:
            msg.showinfo("Remove Record", "Person Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("MilitaryRecord")
        self.win.resizable(width=False, height=False)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 1145) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"1145x300+{x}+{y}")

        # MAIN_VIEW CONNECT
        Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # WIDGETS
        self.id = StringVar()
        self.serial_number = TextWithLabel(self.win, "Serial", 20, 60)
        self.city = TextWithLabel(self.win, "City", 20, 100)
        self.organ = TextWithLabel(self.win, "Organ", 20, 140)

        # PERSON ID
        self.soldier_id = TextWithLabel(self.win, "Person ID", 20, 20, disabled=True)
        self.soldier_id.variable.set(f"{self.user.person.person_id} - {self.user.person.name} {self.user.person.family}")

        # DATE
        Label(self.win, text="Start Date").place(x=20, y=180)
        self.start_calendar = PersianCalendar(self.win, 80, 180)
        Label(self.win, text="End Date").place(x=20, y=220)
        self.end_calendar = PersianCalendar(self.win, 80, 220)

        # TABLE
        self.table = Table(self.win,
                           ["ID", "Serial Number", "City", "Organ", "Start Date", "End Date", "Person Info"],
                           [60, 100, 100, 100, 100, 100, 300],
                           250,
                           20,
                           self.select_row)

        # BUTTONS
        Button(self.win, text="Add", width=7, command=self.save_click, bg="#e2e2e2").place(x=15, y=260)
        Button(self.win, text="Edit", width=7, command=self.edit_click, bg="#e2e2e2").place(x=85, y=260)
        Button(self.win, text="Remove", width=7, command=self.remove_click, bg="#e2e2e2").place(x=155, y=260)

        self.reset_form()
        self.win.mainloop()
