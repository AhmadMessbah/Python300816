from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.financial_doc_controller import FinancialDocController
from view.component.label_text import TextWithLabel
from view.component.table import Table
from view.main_view import MainView


class FinancialDocView:
    def reset_form(self):
        self.id.variable.set("")
        self.amount.variable.set("")
        self.description.variable.set("")
        status, financial_list = FinancialDocController.find_all()
        if status:
            self.table.refresh_table(financial_list)

    def select_row(self, financial_doc):
        self.id.variable.set(financial_doc[0])
        self.amount.variable.set(financial_doc[1])
        self.date_time.variable.set(financial_doc[2])
        self.doc_type.set(financial_doc[3])
        self.description.variable.set(financial_doc[4])

    def save_click(self):
        status, message = FinancialDocController.save(int(self.amount.variable.get()),
                                                      self.doc_type.get(),
                                                      self.description.variable.get(),
                                                      self.user.person.person_id)
        if status:
            msg.showinfo("Save Document", "Document Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)


    def edit_click(self):
        status, message = FinancialDocController.edit(self.id.variable.get(),
                                                      int(self.amount.variable.get()),
                                                      self.doc_type.get(),
                                                      self.description.variable.get())
        if status:
            msg.showinfo("Edit Document", "Document Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        status, message = FinancialDocController.remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove Document", "Document Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def find_by_date(self, event):
        status, financial_list = FinancialDocController.find_by_date(self.search_date_time.variable.get())
        if status:
            self.table.refresh_table(financial_list)

    def close_win(self):
       self.win.destroy()
       main_view = MainView(self.person)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.geometry("800x325")
        win.title("Financial Document")

        self.id = TextWithLabel(win, "  Id", 20, 20, disabled=True)
        self.amount = TextWithLabel(win, "Amount", 20, 60)
        Label(win, text="Doc Type").place(x=20, y=100)
        self.doc_type = ttk.Combobox(win, values=["income", "outcome"],state="readonly")
        self.doc_type.place(x=80, y=100, width=125)
        self.doc_type.current(0)
        self.description = TextWithLabel(win, "Describe:", 20, 140)
        self.person_id = TextWithLabel(win, "Person", 20, 180, disabled=True)
        self.person_id.variable.set(f"{self.user.person.person_id} - {self.user.person.name} {self.user.person.family}")
        self.date_time = TextWithLabel(win, "Date", 20, 220)
        self.search_date_time = TextWithLabel(win, "date time:", 300, 270,disabled=True)
        self.search_date_time.text_box.bind("<KeyRelease>", self.find_by_date)

        self.table = Table(win,
                           ["Id", "amount", "date_time", "doc_type", "description"],
                           [50, 100, 100, 100, 150],
                           250,
                           20,
                           self.select_row)

        Button(win, text="New", width=8, command=self.reset_form, bg="lightgreen").place(x=35, y=240)
        Button(win, text="Save", width=8, command=self.save_click).place(x=140, y=240)
        Button(win, text="Edit", width=8, command=self.edit_click).place(x=35, y=280)
        Button(win, text="Remove", width=8, command=self.remove_click, bg="red").place(x=140, y=280)

        self.reset_form()

        win.mainloop()
