from datetime import datetime
from tkinter import *
import tkinter.messagebox as msg
from controller.lesson_controller import LessonController
from view.component.label_text import TextWithLabel
from view.component.table import Table




def reset_form():
    id.variable.set("0")
    name.variable.set("")
    grade.variable.set("")
    teacher.variable.set("")
    year.variable.set(2024)
    month.variable.set(1)
    day.variable.set(1)
    status, lesson_list = LessonController.find_all()
    if status:
        table.refresh_table(lesson_list)


def select_row(lesson):
    id.variable.set(lesson[0])
    name.variable.set(lesson[1])
    grade.variable.set(lesson[2])
    teacher.variable.set(lesson[3])
    lesson_date = datetime.strptime(lesson[4], "%Y-%m-%d")
    year.variable.set(lesson_date.year)
    month.variable.set(lesson_date.month)
    day.variable.set(lesson_date.day)


def save_click():
    status, message = LessonController.save(name.variable.get(),
                                            grade.variable.get(),
                                            teacher.variable.get(),
                                            year.variable.get(),
                                            month.variable.get(),
                                            day.variable.get()
                                            )
    if status:
        msg.showinfo("Save Lesson", "Lesson Saved")
        reset_form()
    else:
        msg.showerror("Save Error", message)


def edit_click():
    status, message = LessonController.edit(id.variable.get(),
                                            name.variable.get(),
                                            grade.variable.get(),
                                            teacher.variable.get(),
                                            year.variable.get(),
                                            month.variable.get(),
                                            day.variable.get()
                                            )
    if status:
        msg.showinfo("Edit Lesson", "Lesson Edited")
        reset_form()
    else:
        msg.showerror("Edit Error", message)


def remove_click():
    status, message = LessonController.remove(id.variable.get())
    if status:
        msg.showinfo("Remove Lesson", "Lesson Removed")
        reset_form()
    else:
        msg.showerror("Remove Error", message)


def find_by_name(event):
    status, lesson_list = LessonController.find_by_name(search_name.variable.get())
    if status:
        table.refresh_table(lesson_list)


def find_by_teacher(event):
    status, lesson_list = LessonController.find_by_teacher(search_teacher.variable.get())
    if status:
        table.refresh_table(lesson_list)


win = Tk()
win.title("Panel")

# center form
x = (win.winfo_screenwidth() - 1050) // 2
y = (win.winfo_screenheight() - 300) // 2
win.geometry(f"850x300+{x}+{y}")

id = TextWithLabel(win, "ID", 20, 20, disabled=True)
name = TextWithLabel(win, "Name", 20, 60)
grade = TextWithLabel(win, "Grade", 20, 100)
teacher = TextWithLabel(win, "Teacher", 20, 140)

year = TextWithLabel(win, "Year", 20, 180, 30, "", 4)
month = TextWithLabel(win, "/Month", 90, 180, 45, "", 2)
day = TextWithLabel(win, "/Day", 165, 180, 30, "", 2)

search_name = TextWithLabel(win, "Find By Name", 250, 260, 100)
search_name.text_box.bind("<KeyRelease>", find_by_name)
search_teacher = TextWithLabel(win, "Find By Teacher", 550, 260, 100)
search_teacher.text_box.bind("<KeyRelease>", find_by_teacher)

table = Table(win,
              ["Id", "Name", "Grade", "Teacher", "Date"],
              [60, 150, 150, 150, 80],
              250,
              20,
              select_row)

Button(win, text="New", width=10, command=reset_form, bg='#86CA93', fg='black').place(x=20, y=220)
Button(win, text="Save", width=10, command=save_click).place(x=120, y=220)
Button(win, text="Edit", width=10, command=edit_click).place(x=20, y=260)
Button(win, text="Remove", width=10, command=remove_click, bg='#F23C3C', fg='black').place(x=120, y=260)

reset_form()

win.mainloop()
