from tkinter import *

from view.person_view import PersonView


class MainView:
    def person_click(self):
        person_ui = PersonView(None)
    def user_click(self):pass
    def sim_click(self):pass
    def military_click(self):pass
    def medical_click(self):pass
    def product_click(self):pass
    def financial_click(self):pass
    def lesson_click(self):
        lesson_view = LessonView()

    def __init__(self):
        win = Tk()
        win.geometry("300x650")
        win.title("Python App")

        Button(win, text="Person",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.person_click).place(x=50, y=50)
        Button(win, text="User",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.user_click).place(x=50, y=120)
        Button(win, text="SimCard",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.sim_click).place(x=50, y=190)
        Button(win, text="Military",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.military_click).place(x=50, y=260)
        Button(win, text="Medical",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.medical_click).place(x=50, y=330)
        Button(win, text="Product",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.product_click).place(x=50, y=400)
        Button(win, text="Financial",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.financial_click).place(x=50, y=470)
        Button(win, text="Lesson",width=15 ,bg="lightblue", height=2, font=("Arial", 15), command=self.lesson_click).place(x=50, y=540)

        win.mainloop()
