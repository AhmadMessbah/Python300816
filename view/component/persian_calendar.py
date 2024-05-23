import tkinter.ttk

from tkinter import ttk
from datetime import datetime, date

from persiantools.jdatetime import JalaliDate


class PersianCalendar:
    def set_date(self, d_date):
        if type(d_date) == str:
            d_date = datetime.strptime(d_date.replace("/", "-"), '%Y-%m-%d')
        self.gregorian_date = d_date
        self.persian_date = JalaliDate(d_date)

        self.year.set(self.persian_date.year)
        self.month.set(self.persian_date.month)
        self.day.set(self.persian_date.day)

    def change_date(self, event):
        y = int(self.year.get())
        m = int(self.month.get())
        d = int(self.day.get())
        days = JalaliDate.days_in_month(m, y)
        self.day["values"] = list(range(1, days + 1))
        y = int(self.year.get())
        m = int(self.month.get())
        d = int(self.day.get())
        self.persian_date = JalaliDate(y, m, d)
        self.gregorian_date = self.persian_date.to_gregorian()

    def __init__(self, master, x, y, date=None, width=4, distance=40):
        if date:
            self.gregorian_date = date
            self.persian_date = JalaliDate(self.gregorian_date)
        else:
            self.gregorian_date = JalaliDate.today().to_gregorian()
            self.persian_date = JalaliDate.today()

        self.year = ttk.Combobox(master, width=width)
        self.year["values"] = list(range(1300, 1451))

        self.year.bind("<<ComboboxSelected>>", self.change_date)
        self.year.set(self.persian_date.year)
        self.year.place(x=x, y=y)

        self.month = ttk.Combobox(master, width=width - 2)
        self.month["values"] = list(range(1, 13))
        self.month.set(self.persian_date.month)
        self.month.bind("<<ComboboxSelected>>", self.change_date)
        self.month.place(x=x + 10 + distance, y=y)

        self.day = ttk.Combobox(master, width=width - 2)
        self.day["values"] = list(range(1, JalaliDate.days_in_month(1, 1403) + 1))
        self.day.set(self.persian_date.day)
        self.day.bind("<<ComboboxSelected>>", self.change_date)
        self.day.place(x=x + 10 + distance * 2, y=y)
