from datetime import datetime
from tkinter import *
import tkinter.messagebox as msg
from controller.lesson_controller import LessonController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class LessonView:
    def reset_form(self):
        self.id.variable.set("0")
        self.name.variable.set("")
        self.grade.variable.set("")
        self.year.variable.set(2024)
        self.month.variable.set(1)
        self.day.variable.set(1)
        self.teacher.variable.set("")
        status, lesson_list = LessonController.find_all()
        if status:
            self.table.refresh_table(lesson_list)

    def select_row(self, lesson):
        self.id.variable.set(lesson[0])
        self.name.variable.set(lesson[1])
        self.grade.variable.set(lesson[2])
        lesson_date = datetime.strptime(lesson[3], "%Y-%m-%d")
        self.year.variable.set(lesson_date.year)
        self.month.variable.set(lesson_date.month)
        self.day.variable.set(lesson_date.day)
        self.teacher.variable.set(lesson[4])


    def save_click(self):
        status, message = LessonController.save(self.name.variable.get(),
                                                self.grade.variable.get(),
                                                self.year.variable.get(),
                                                self.month.variable.get(),
                                                self.day.variable.get(),
                                                self.teacher.variable.get()
                                                )
        if status:
            msg.showinfo("Save Lesson", "Lesson Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = LessonController.edit(self.id.variable.get(),
                                                self.name.variable.get(),
                                                self.grade.variable.get(),
                                                self.year.variable.get(),
                                                self.month.variable.get(),
                                                self.day.variable.get(),
                                                self.teacher.variable.get()
                                                )
        if status:
            msg.showinfo("Edit Lesson", "Lesson Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = LessonController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove Lesson", "Lesson Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_name(self, event):
        status, lesson_list = LessonController.find_by_name(self.search_name.variable.get())
        if status:
            self.table.refresh_table(lesson_list)

    def find_by_teacher(self, event):
        status, lesson_list = LessonController.find_by_teacher(self.search_teacher.variable.get())
        if status:
            self.table.refresh_table(lesson_list)

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Lesson Viewer")

        Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        # center form
        x = (self.win.winfo_screenwidth() - 1050) // 2
        y = (self.win.winfo_screenheight() - 300) // 2
        self.win.geometry(f"850x300+{x}+{y}")

        self.id = TextWithLabel(self.win, "ID", 20, 20, disabled=True)
        self.name = TextWithLabel(self.win, "Name", 20, 60)
        self.grade = TextWithLabel(self.win, "Grade", 20, 100)


        self.year = TextWithLabel(self.win, "Year", 20, 140, 30, "", 4)
        self.month = TextWithLabel(self.win, "/Month", 90, 140, 45, "", 2)
        self.day = TextWithLabel(self.win, "/Day", 165, 140, 30, "", 2)
        self.teacher = TextWithLabel(self.win, "Teacher", 20, 180)

        self.search_name = TextWithLabel(self.win, "Find By Name", 250, 260, 100)
        self.search_name.text_box.bind("<KeyRelease>", self.find_by_name)
        self.search_teacher = TextWithLabel(self.win, "Find By Teacher", 550, 260, 100)
        self.search_teacher.text_box.bind("<KeyRelease>", self.find_by_teacher)

        self.table = Table(self.win,
                           ["Id", "Name", "Grade", "Date", "Teacher"],
                           [60, 150, 150, 80, 150],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="New", width=10, command=self.reset_form, bg='#86CA93', fg='black').place(x=20, y=220)
        Button(self.win, text="Save", width=10, command=self.save_click).place(x=120, y=220)
        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=20, y=260)
        Button(self.win, text="Remove", width=10, command=self.remove_click, bg='#F23C3C', fg='black').place(x=120, y=260)

        self.reset_form()

        self.win.mainloop()


