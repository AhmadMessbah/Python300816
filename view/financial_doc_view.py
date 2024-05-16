from tkinter import *
import tkinter.messagebox as msg

from controller.financial_doc_controller import FinancialDocController
from view.component.label_text import TextWithLabel
from view.component.table import Table

class FinancialDocView:
    def reset_form(self):
        self.id.variable.set("")
        self.amount.variable.set("")
        self.doc_type.variable.set("")
        self.description.variable.set("")
        status, financial_list = FinancialDocController.find_all()
        if status:
            self.table.refresh_table(financial_list)

    def select_row(self, financial_doc):
        self.id.variable.set(financial_doc[0])
        self.amount.variable.set(financial_doc[1])
        self.date_time.variable.set(financial_doc[2])
        self.doc_type.variable.set(financial_doc[3])
        self.description.variable.set(financial_doc[4])

    def save_click(self):
        status, message = FinancialDocController.save(self.amount.variable.get(),
                                                      self.doc_type.variable.get(),
                                                      self.description.variable.get(),
                                                      self.person_id.variable.get())
        if status:
            msg.showinfo("Save Document", "Document Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = FinancialDocController.edit(self.id.variable.get(),
                                                self.amount.variable.get(),
                                                self.doc_type.variable.get(),
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

    def find_by_date(self,event):
        status, financial_list = FinancialDocController.find_by_date(self.search_date_time.variable.get())
        if status:
            self.table.refresh_table(financial_list)


    # def close_win(self):
         #self.win.destroy()
        # main_view = MainView(self.person)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.geometry("800x300")
        win.title("Financial Document")

        self.id = TextWithLabel(win, "  Id:", 20, 20, disabled=True)
        self.amount = TextWithLabel(win, "amount:", 20, 60)
        self.search_date_time  = TextWithLabel(win, "date time:", 300, 270)
        self.search_date_time.text_box.bind("<KeyRelease>", self.find_by_date)
        self.doc_type = TextWithLabel(win, "doc type:", 20, 110)
        self.description = TextWithLabel(win, "description:", 20, 150)
        self.person_id = TextWithLabel(win, "Person Id", 20, 190, disabled=True)
        self.person_id.variable.set( self.user.person.person_id)

        self.table = Table(win,
                      ["Id", "amount", "date_time", "doc_type", "description"],
                      [50, 100, 100,100,150],
                      250,
                      20,
                      self.select_row)

        Button(win, text="Add", width=8, command=self.save_click).place(x=20, y=250)
        Button(win, text="Edit", width=8, command=self.edit_click).place(x=100, y=250)
        Button(win, text="Remove", width=8, command=self.remove_click).place(x=180, y=250)

        self.reset_form()

        win.mainloop()

