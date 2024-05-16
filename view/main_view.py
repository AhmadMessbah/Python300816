from tkinter import *

from view.financial_doc_view import FinancialDocView
from view.lesson_view import LessonView
from view.medical_view import MedicalView
from view.person_view import PersonView
from view.product_view import ProductView
from view.sim_card_view import SimCardView
from view.user_view import UserView
from view.military_view import MilitaryView
from view.driving_license_view import DrivingLicenseView


class MainView:
    def person_click(self):
        person_view = PersonView(self.user)

    def user_click(self):
        user_view = UserView()

    def sim_click(self):
        sim_view = SimCardView(None)

    def military_click(self):
        military_view = MilitaryView(None)

    def medical_click(self):
        medical_view = MedicalView(None)

    def product_click(self):
        product_view = ProductView(None)

    def financial_click(self):
        financial_view = FinancialDocView(None)

    def lesson_click(self):
        lesson_view = LessonView(None)

    def driving_license_click(self):
        driving_license_view = DrivingLicenseView(None)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.geometry("300x700")
        self.win.title("Python App")
        Label(text=user.person.name + " " + user.person.family).place(x=20, y=20)

        Button(self.win, text="Person", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.person_click).place(x=50, y=50)
        Button(self.win, text="User", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.user_click).place(x=50, y=120)
        Button(self.win, text="SimCard", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.sim_click).place(x=50, y=190)
        Button(self.win, text="Military", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.military_click).place(x=50, y=260)
        Button(self.win, text="Medical", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.medical_click).place(x=50, y=330)
        Button(self.win, text="Product", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.product_click).place(x=50, y=400)
        Button(self.win, text="Financial", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.financial_click).place(x=50, y=470)
        Button(self.win, text="Lesson", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.lesson_click).place(x=50, y=540)
        Button(self.win, text="DrivingLicense", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.driving_license_click).place(x=50, y=610)

        self.win.mainloop()
