from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.military_controller import MilitaryController
from model.entity.military import Military
from view.component.label_text import TextWithLabel
from view.component.table import Table

def reset_form():
    id.variable.set("0")
    serial_number.variable.set("")
    city.variable.set("")
    organ.variable.set("")
    start_year.variable.set("")
    start_month.variable.set("")
    start_day.variable.set("")
    end_year.variable.set("")
    end_month.variable.set("")
    end_day.variable.set("")
    status, military_list = MilitaryController.find_all()
    if status:
        table.refresh_table(military_list)


def select_row(military):
    id.variable.set(military[0])
    serial_number.variable.set(str("{:011d}".format(military[1])))
    city.variable.set(military[2])
    organ.variable.set(military[3])

    start_year.variable.set(int(military[4][0:4]))
    start_month.variable.set(int(military[4][5:7]))
    start_day.variable.set(int(military[4][8:]))

    end_year.variable.set(int(military[5][0:4]))
    end_month.variable.set(int(military[5][5:7]))
    end_day.variable.set(int(military[5][8:]))

def save_click():
    status, message = MilitaryController.save(serial_number.variable.get(),
                                              city.variable.get(),
                                              organ.variable.get(),
                                              start_year.variable.get(),
                                              start_month.variable.get(),
                                              start_day.variable.get(),
                                              end_year.variable.get(),
                                              end_month.variable.get(),
                                              end_day.variable.get())
    if status:
        msg.showinfo("Save Record", "Record Saved")
        reset_form()
    else:
        msg.showerror("Save Error", message)

def edit_click():
    status, message = MilitaryController.edit(id.variable.get(),
                                              serial_number.variable.get(),
                                              city.variable.get(),
                                              organ.variable.get(),
                                              start_year.variable.get(),
                                              start_month.variable.get(),
                                              start_day.variable.get(),
                                              end_year.variable.get(),
                                              end_month.variable.get(),
                                              end_day.variable.get())
    if status:
        msg.showinfo("Edit Record", "Record Edited")
        reset_form()
    else:
        msg.showerror("Edit Error", message)

def remove_click():
    status, message = MilitaryController.remove(id.variable.get())
    if status:
        msg.showinfo("Remove Record", "Person Removed")
        reset_form()
    else:
        msg.showerror("Remove Error", message)

def find_by_city(event):
    status, military_list = MilitaryController.find_by_city(search_city.variable.get())
    if status:
        table.refresh_table(military_list)

def find_by_organ(event):
    status, military_list = MilitaryController.find_by_organ(search_organ.variable.get())
    if status:
        table.refresh_table(military_list)

def find_by_serial_number(event):
    status, military_list = MilitaryController.find_by_serial_number(search_serial_number.variable.get())
    if status:
        table.refresh_table(military_list)


win = Tk()
win.title("MilitaryRecord")

# CENTER FORM
x = (win.winfo_screenwidth() - 850) // 2
y = (win.winfo_screenheight() - 300) // 2
win.geometry(f"850x300+{x}+{y}")

# WIDGETS
id = TextWithLabel(win, "ID", 20, 20, disabled=True)
serial_number = TextWithLabel(win, "Serial", 20, 60)
city = TextWithLabel(win, "City", 20, 100)
organ = TextWithLabel(win, "Organ", 20, 140)

# SEARCH
search_city = TextWithLabel(win, "Find By City", 250, 260, distance=80, width=15)
search_city.text_box.bind("<KeyRelease>", find_by_city)
search_organ = TextWithLabel(win, "Find By Organ", 440, 260, distance=90, width=15)
search_organ.text_box.bind("<KeyRelease>", find_by_organ)
search_serial_number = TextWithLabel(win, "Find by Serial", 640, 260, distance=80, width=15)
search_serial_number.text_box.bind("<KeyRelease>", find_by_serial_number)

# START DATE
start_year = TextWithLabel(win, "Start Date", 20, 180, disabled=False, width=8)
start_month = TextWithLabel(win, "/", 130, 180, 12, disabled=False, width=4)
start_day = TextWithLabel(win, "/", 165, 180, 12, disabled=False, width=4)

# END DATE
end_year = TextWithLabel(win, "End Date", 20, 220, disabled=False, width=8)
end_month = TextWithLabel(win, "/", 130, 220, 12, disabled=False, width=4)
end_day = TextWithLabel(win, "/", 165, 220, 12, disabled=False, width=4)

table = Table(win,
              ["ID","Serial Number", "City", "Organ", "Start Date", "End Date"],
              [60, 100, 100, 100, 100, 100],
              250,
              20,
              select_row)

Button(win, text="Add",width=5, command=save_click, bg="#e2e2e2").place(x=15, y=260)
Button(win, text="Edit",width=5, command=edit_click, bg="#e2e2e2").place(x=70, y=260)
Button(win, text="Remove",width=7, command=remove_click, bg="#e2e2e2").place(x=125, y=260)
Button(win, text="♻️",width=2, command=reset_form, bg="#e2e2e2").place(x=193, y=260)

reset_form()

win.mainloop()
