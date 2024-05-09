from tkinter import *

from view.lesson_view import LessonView
from view.person_view import PersonView
from view.sim_card_view import SimCardView


class MainView:
    def person_click(self):
        person_ui = PersonView(None)
    def user_click(self):
        user_view = UserView(None)
    def sim_click(self):
        sim_view= SimCardView(None)
    def military_click(self):
        military_view = MilitaryView(None)
    def medical_click(self):
        medical_view = MedicalView(None)
    def product_click(self):
        product_view = ProductView(None)
    def financial_click(self):
        financial_view = FinancialView(None)
    def lesson_click(self):
        lesson_view = LessonView(None)

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
