from tkinter import *
import tkinter.messagebox as msg

from controller.medical_controller import MedicalRecordController
from view.component.label_text import TextWithLabel
from view.component.table import Table


class MedicalView:
    def select_row(self,medical_record):
        self.id.variable.set(medical_record[0])
        self.disease.variable.set(medical_record[1])
        self.medicine.variable.set(medical_record[2])
        self.doctor.variable.set(medical_record[3])
        self.patient_id.variable.set(medical_record[4])

    def reset_form(self):
        self.id.variable.set("")
        self.disease.variable.set("")
        self.medicine.variable.set("")
        self.doctor.variable.set("")
        self.patient_id.variable.set("")
        status, medical_records_list = MedicalRecordController.find_all()
        if status:
            self.table.refresh_table(medical_records_list)

    def save_click(self):
        status, message = MedicalRecordController.save(self.disease.variable.get(), self.medicine.variable.get(),
                                                       self.doctor.variable.get(), self.patient_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "record saved successfully!")
        else:
            msg.showerror("Error", "failed to save record!")

    def edit_click(self):
        status, message = MedicalRecordController.edit(self.id.variable.get(), self.disease.variable.get(),
                                                       self.medicine.variable.get(),
                                                       self.doctor.variable.get(), self.patient_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "record edited successfully!")
        else:
            msg.showerror("Error", "failed to edit record!")

    def remove_click(self):
        status, message = MedicalRecordController.remove(self.id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "record deleted successfully!")
        else:
            msg.showerror("Error", "failed to delete record!")

    def search_by_id(self, event):
        status, medical_record_list = MedicalRecordController.find_by_id(self.search_id.variable.get())
        if status:
            self.table.refresh_table(medical_record_list)

    def __init__(self, user):
        self.user = user
        win = Tk()
        win.title('Medical Record')
        win.geometry('700x350')

        self.id = TextWithLabel(win, 'Record ID', 30, 30, 60, disabled=True)
        self.disease = TextWithLabel(win, 'Disease', 30, 80, 60)
        self.medicine = TextWithLabel(win, 'Medicine', 30, 130, 60)
        self.doctor = TextWithLabel(win, 'Doctor', 30, 180, 60)
        self.patient_id = TextWithLabel(win, 'Patient ID', 30, 230, 60)
        self.search_id = TextWithLabel(win, 'search ID', 250, 285, 60)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(win,
                      ['record ID', 'disease', 'medicine', 'doctor', 'Patient ID'],
                      [70, 70, 70, 70, 100],
                      250,
                      30,
                      self.select_row)

        Button(win, text='save', width=6, command=self.save_click).place(x=30, y=280)
        Button(win, text='edit', width=6, command=self.edit_click).place(x=95, y=280)
        Button(win, text='remove', width=6, command=self.remove_click).place(x=165, y=280)

        self.reset_form()

        win.mainloop()


MedicalView(None)