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

        status, lesson_list = LessonController.find_by_teacher(self.user.person.person_id)

        if status:
            self.table.refresh_table(lesson_list)
        else:
            self.table.refresh_table([])

    def select_row(self, lesson):
        self.id.variable.set(lesson[0])
        self.name.variable.set(lesson[1])
        self.grade.variable.set(lesson[2])
        lesson_date = datetime.strptime(lesson[3], "%Y-%m-%d")
        self.year.variable.set(lesson_date.year)
        self.month.variable.set(lesson_date.month)
        self.day.variable.set(lesson_date.day)

    def save_click(self):
        status, message = LessonController.save(self.name.variable.get(),
                                                self.grade.variable.get(),
                                                self.year.variable.get(),
                                                self.month.variable.get(),
                                                self.day.variable.get(),
                                                self.user.person.person_id
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
                                                self.user.person.person_id
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

    def find_by_name_for_teacher(self, event):
        teacher_id = self.user.person.person_id
        status, lesson_list = LessonController.find_by_name_for_teacher(self.search_name.variable.get(), teacher_id)
        if status:
            self.table.refresh_table(lesson_list)
            if self.search_name.variable.get() == '':
                self.reset_form()

    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.title("Lesson Viewer")

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
        self.teacher = TextWithLabel(self.win, "Teacher Id", 20, 180, disabled=True)
        self.teacher.variable.set(f"{self.user.person.person_id} - {self.user.person.name} {self.user.person.family}")

        self.search_name = TextWithLabel(self.win, "Find Lesson Name", 250, 260, 120)
        self.search_name.text_box.bind("<KeyRelease>", self.find_by_name_for_teacher)

        self.table = Table(self.win,
                           ["Id", "Name", "Grade", "Date", "Teacher"],
                           [60, 150, 150, 80, 150],
                           250,
                           20,
                           self.select_row)

        Button(self.win, text="New", width=10, command=self.reset_form, bg='#86CA93', fg='black').place(x=20, y=220)
        Button(self.win, text="Save", width=10, command=self.save_click).place(x=120, y=220)
        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=20, y=260)
        Button(self.win, text="Remove", width=10, command=self.remove_click, bg='#F23C3C', fg='black').place(x=120,
                                                                                                             y=260)

        self.reset_form()

        self.win.mainloop()
