from tkinter import *

from view import *

class MainView:
    def person_click(self):
        person_view = PersonView(self.user)

    def user_click(self):
        user_view = UserView()

    def sim_click(self):
        sim_view = SimCardView(self.user)

    def military_click(self):
        military_view = MilitaryView(self.user)

    def medical_click(self):
        medical_view = MedicalView(self.user)

    def product_click(self):
        product_view = ProductView(self.user)

    def financial_click(self):
        financial_view = FinancialDocView(self.user)

    def lesson_click(self):
        lesson_view = LessonView(self.user)

    def car_click(self):
        car_view = CarView(self.user)

    def driving_license_click(self):
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

