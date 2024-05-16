from tkinter import *


class MainView:
    def person_click(self):
        self.win.destroy()
        from view import PersonView
        person_view = PersonView(self.user)

    def user_click(self):
        self.win.destroy()
        from view import UserView
        user_view = UserView()

    def sim_click(self):
        self.win.destroy()
        from view import SimCardView
        sim_view = SimCardView(self.user)

    def military_click(self):
        self.win.destroy()
        from view import MilitaryView
        military_view = MilitaryView(self.user)

    def medical_click(self):
        self.win.destroy()
        from view import MedicalView
        medical_view = MedicalView(self.user)

    def product_click(self):
        self.win.destroy()
        from view import ProductView
        product_view = ProductView(self.user)

    def financial_click(self):
        self.win.destroy()
        from view import FinancialDocView
        financial_view = FinancialDocView(self.user)

    def lesson_click(self):
        self.win.destroy()
        from view import LessonView
        lesson_view = LessonView(self.user)

    def car_click(self):
        self.win.destroy()
        from view import CarView
        car_view = CarView(self.user)

    def driving_license_click(self):
        self.win.destroy()
        from view import DrivingLicenseView
        driving_license_view = DrivingLicenseView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        self.win.geometry("300x750")
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
        Button(self.win, text="Car", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.car_click).place(x=50, y=610)
        Button(self.win, text="DrivingLicense", width=15, bg="lightblue", height=2, font=("Arial", 15),
               command=self.driving_license_click).place(x=50, y=680)

        self.win.mainloop()

