from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.lesson_controller import LessonController


class LessonView:
    def table_select(self):
        selected = self.table.focus()
        selected_lesson = self.table.item(selected)["values"]
        self.id.set(selected_lesson[0])
        self.name.set(selected_lesson[1])
        self.grade.set(selected_lesson[2])
        self.teacher.set(selected_lesson[3])
        self.year.set(selected_lesson[4])
        self.month.set(selected_lesson[5])
        self.day.set(selected_lesson[6])

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.grade.set("")
        self.teacher.set("")
        self.year.set(2024)
        self.month.set(1)
        self.day.set(1)
        self.refresh_table()

    def refresh_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

        status, lessons = self.controller.find_all()
        for lesson in lessons:
            start_day = lesson.start_day
            year = start_day.year
            month = start_day.month
            day = start_day.day

            self.table.insert("", END, values=(lesson.lesson_id, lesson.name, lesson.grade, lesson.teacher, year, month, day))

    def save_click(self):
        status, message = self.controller.save(self.name.get(),
                                               self.grade.get(),
                                               self.teacher.get(),
                                               self.year.get(),
                                               self.month.get(),
                                               self.day.get()
                                               )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = self.controller.edit(self.id.get(),
                                               self.name.get(),
                                               self.grade.get(),
                                               self.teacher.get(),
                                               self.year.get(),
                                               self.month.get(),
                                               self.day.get()
                                               )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = self.controller.remove(self.id.get())
        if msg.askyesno("Remove", "Are you sure?"):
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def __init__(self):
        self.controller = LessonController()
        win = Tk()
        win.title("Panel")
        # win.wm_protocol("WM_DELETE_WINDOW", exit_click)

        # center form
        x = (win.winfo_screenwidth() - 1160) // 2
        y = (win.winfo_screenheight() - 215) // 2
        win.geometry(f"1160x215+{x}+{y}")

        # id(lesson_id)
        Label(win, text="ID").place(x=20, y=20)
        self.id = IntVar()
        Entry(win, textvariable=self.id, state="readonly").place(x=100, y=20)

        # name
        Label(win, text="Name").place(x=20, y=60)
        self.name = StringVar()
        Entry(win, textvariable=self.name).place(x=100, y=60)

        # grade
        Label(win, text="Grade").place(x=20, y=100)
        self.grade = StringVar()
        Entry(win, textvariable=self.grade).place(x=100, y=100)

        # teacher
        Label(win, text="Teacher").place(x=20, y=140)
        self.teacher = StringVar()
        Entry(win, textvariable=self.teacher).place(x=100, y=140)

        # date
        Label(win, text="Year").place(x=20, y=180)
        Label(win, text="/Month").place(x=90, y=180)
        Label(win, text="/Day").place(x=165, y=180)
        self.year = IntVar()
        self.month = IntVar()
        self.day = IntVar()
        Entry(win, textvariable=self.year, width=4).place(x=60, y=180)
        Entry(win, textvariable=self.month, width=2).place(x=145, y=180)
        Entry(win, textvariable=self.day, width=2).place(x=205, y=180)

        # table
        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=8)
        self.table.place(x=250, y=20)
        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Grade")
        self.table.heading(4, text="Teacher")
        self.table.heading(5, text="Year")
        self.table.heading(6, text="Month")
        self.table.heading(7, text="Day")

        self.table.column(1, width=60)
        self.table.column(2, width=150)
        self.table.column(3, width=150)
        self.table.column(4, width=150)
        self.table.column(5, width=80)
        self.table.column(6, width=80)
        self.table.column(7, width=80)

        button_new = Button(win, text="New", width=15, command=self.reset_form, bg='#86CA93', fg='black')
        button_new.place(x=1025, y=20)

        button_save = Button(win, text="Save", width=15, command=self.save_click)
        button_save.place(x=1025, y=60)

        button_edit = Button(win, text="Edit", width=15, command=self.edit_click)
        button_edit.place(x=1025, y=100)

        button_remove = Button(win, text="Remove", width=15, command=self.remove_click, bg='#F23C3C', fg='black')
        button_remove.place(x=1025, y=140)

        # self.table.bind("<ButtonRelease>", self.table_select)
        self.table.bind("<KeyRelease>")

        self.reset_form()

        win.mainloop()


ui = LessonView()
