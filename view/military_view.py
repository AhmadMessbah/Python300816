from tkinter import *
import tkinter.messagebox as msg
from controller.military_controller import MilitaryController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class MilitaryView:

    def reset_form(self):
        self.serial_number.variable.set("")
        self.city.variable.set("")
        self.organ.variable.set("")
        self.start_year.variable.set("")
        self.start_month.variable.set("")
        self.start_day.variable.set("")
        self.end_year.variable.set("")
        self.end_month.variable.set("")
        self.end_day.variable.set("")
        self.soldier_id.variable.set(self.user.person.person_id)
        status, military_list = MilitaryController.find_by_soldier_id(self.user.person.person_id)
        if status:
            self.table.refresh_table(military_list)


    def select_row(self, military):
        self.id.variable.set(military[0])
        self.serial_number.variable.set(str("{:011d}".format(military[1])))
        self.city.variable.set(military[2])
        self.organ.variable.set(military[3])

        self.start_year.variable.set(int(military[4][0:4]))
        self.start_month.variable.set(int(military[4][5:7]))
        self.start_day.variable.set(int(military[4][8:]))

        self.end_year.variable.set(int(military[5][0:4]))
        self.end_month.variable.set(int(military[5][5:7]))
        self.end_day.variable.set(int(military[5][8:]))

    def save_click(self):
        status, message = MilitaryController.save(self.serial_number.variable.get(),
                                                  self.city.variable.get(),
                                                  self.organ.variable.get(),
                                                  self.start_year.variable.get(),
                                                  self.start_month.variable.get(),
                                                  self.start_day.variable.get(),
                                                  self.end_year.variable.get(),
                                                  self.end_month.variable.get(),
                                                  self.end_day.variable.get(),
                                                  self.soldier_id.variable.get())
        if status:
            msg.showinfo("Save Record", "Record Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = MilitaryController.edit(self.id.variable.get(),
                                                  self.serial_number.variable.get(),
                                                  self.city.variable.get(),
                                                  self.organ.variable.get(),
                                                  self.start_year.variable.get(),
                                                  self.start_month.variable.get(),
                                                  self.start_day.variable.get(),
                                                  self.end_year.variable.get(),
                                                  self.end_month.variable.get(),
                                                  self.end_day.variable.get(),
                                                  self.soldier_id.variable.get())
        if status:
            msg.showinfo("Edit Record", "Record Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = MilitaryController.remove(self.id.variable.get())
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

        Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)


        self.win.title("MilitaryRecord")
        self.win.resizable(width=False, height=False)

        # CENTER FORM
        x = (self.win.winfo_screenwidth() - 1165) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"1165x300+{x}+{y}")

        # WIDGETS
        self.soldier_id = TextWithLabel(self.win, "Person ID", 20, 20, width=6, disabled=True)
        self.id = TextWithLabel(self.win, "ID", 140, 20, disabled=True, distance=25, width=6)
        self.serial_number = TextWithLabel(self.win, "Serial", 20, 60)
        self.city = TextWithLabel(self.win, "City", 20, 100)
        self.organ = TextWithLabel(self.win, "Organ", 20, 140)

        # START DATE
        self.start_year = TextWithLabel(self.win, "Start Date", 20, 180, disabled=False, width=8)
        self.start_month = TextWithLabel(self.win, "/", 130, 180, 12, disabled=False, width=4)
        self.start_day = TextWithLabel(self.win, "/", 165, 180, 12, disabled=False, width=4)

        # END DATE
        self.end_year = TextWithLabel(self.win, "End Date", 20, 220, disabled=False, width=8)
        self.end_month = TextWithLabel(self.win, "/", 130, 220, 12, disabled=False, width=4)
        self.end_day = TextWithLabel(self.win, "/", 165, 220, 12, disabled=False, width=4)

        self.table = Table(self.win,
                           ["ID", "Serial Number", "City", "Organ", "Start Date", "End Date", "Person Information"],
                           [60, 100, 100, 100, 100, 100, 320],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="Add", width=7, command=self.save_click, bg="#e2e2e2").place(x=15, y=260)
        Button(self.win, text="Edit", width=7, command=self.edit_click, bg="#e2e2e2").place(x=90, y=260)
        Button(self.win, text="Remove", width=7, command=self.remove_click, bg="#e2e2e2").place(x=145, y=260)

        self.reset_form()
        self.win.mainloop()

