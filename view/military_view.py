from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.military_controller import MilitaryController
from model.entity.military import Military
from view.component.label_text import TextWithLabel
from view.component.table import Table

class MilitaryView:

    def reset_form(self):
        self.id.variable.set("0")
        self.serial_number.variable.set("")
        self.city.variable.set("")
        self.organ.variable.set("")
        self.start_year.variable.set("")
        self.start_month.variable.set("")
        self.start_day.variable.set("")
        self.end_year.variable.set("")
        self.end_month.variable.set("")
        self.end_day.variable.set("")
        self.soldier_id.variable.set("")
        status, military_list = MilitaryController.find_all()
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
        self.soldier_id.variable.set(military[6])

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

    def find_by_city(self, event):
        status, military_list = MilitaryController.find_by_city(self.search_city.variable.get())
        if status:
            self.table.refresh_table(military_list)

    def find_by_organ(self, event):
        status, military_list = MilitaryController.find_by_organ(self.search_organ.variable.get())
        if status:
            self.table.refresh_table(military_list)

    def find_by_serial_number(self, event):
        status, military_list = MilitaryController.find_by_serial_number(self.search_serial_number.variable.get())
        if status:
            self.table.refresh_table(military_list)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.title("MilitaryRecord")

        # CENTER FORM
        x = (win.winfo_screenwidth() - 910) // 2
        y = (win.winfo_screenheight() - 300) // 2
        win.geometry(f"910x300+{x}+{y}")

        # WIDGETS
        self.soldier_id = TextWithLabel(win, "Soldier", 20, 20, width=5)
        self.id = TextWithLabel(win, "ID", 140, 20, disabled=True,distance=40, width=5)
        self.serial_number = TextWithLabel(win, "Serial", 20, 60)
        self.city = TextWithLabel(win, "City", 20, 100)
        self.organ = TextWithLabel(win, "Organ", 20, 140)

        # SEARCH
        self.search_city = TextWithLabel(win, "Find By City", 250, 260, distance=80, width=15)
        self.search_city.text_box.bind("<KeyRelease>", self.find_by_city)
        self.search_organ = TextWithLabel(win, "Find By Organ", 440, 260, distance=90, width=15)
        self.search_organ.text_box.bind("<KeyRelease>", self.find_by_organ)
        self.search_serial_number = TextWithLabel(win, "Find by Serial", 640, 260, distance=80, width=15)
        self.search_serial_number.text_box.bind("<KeyRelease>", self.find_by_serial_number)

        # START DATE
        self.start_year = TextWithLabel(win, "Start Date", 20, 180, disabled=False, width=8)
        self.start_month = TextWithLabel(win, "/", 130, 180, 12, disabled=False, width=4)
        self.start_day = TextWithLabel(win, "/", 165, 180, 12, disabled=False, width=4)

        # END DATE
        self.end_year = TextWithLabel(win, "End Date", 20, 220, disabled=False, width=8)
        self.end_month = TextWithLabel(win, "/", 130, 220, 12, disabled=False, width=4)
        self.end_day = TextWithLabel(win, "/", 165, 220, 12, disabled=False, width=4)

        self.table = Table(win,
                      ["ID", "Serial Number", "City", "Organ", "Start Date", "End Date", "Soldier ID"],
                      [60, 100, 100, 100, 100, 100, 60],
                      250,
                      20,
                      self.select_row)

        Button(win, text="Add", width=5, command=self.save_click, bg="#e2e2e2").place(x=15, y=260)
        Button(win, text="Edit", width=5, command=self.edit_click, bg="#e2e2e2").place(x=70, y=260)
        Button(win, text="Remove", width=7, command=self.remove_click, bg="#e2e2e2").place(x=125, y=260)
        Button(win, text="♻️", width=2, command=self.reset_form, bg="#e2e2e2").place(x=193, y=260)

        self.reset_form()

        win.mainloop()


