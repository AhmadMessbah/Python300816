from tkinter import *
import tkinter.messagebox as msg
from view.main_view import MainView
from datetime import datetime
from view.component.persian_calendar import PersianCalendar
from controller.medical_controller import MedicalRecordController
from view.component.label_text import TextWithLabel
from view.component.table import Table


class MedicalView:
    def select_row(self,medical_record):
        self.id.variable.set(medical_record[0])
        self.disease.variable.set(medical_record[1])
        self.medicine.variable.set(medical_record[2])
        self.doctor.variable.set(medical_record[3])
        date_time = datetime.strptime(medical_record[4], "%Y-%m-%d")
        self.calendar.set_date(date_time)



    def reset_form(self):
        self.id.variable.set("")
        self.disease.variable.set("")
        self.medicine.variable.set("")
        self.doctor.variable.set("")
        status, medical_records_list = MedicalRecordController.find_by_patient_id(self.user.person.person_id)
        if status:
            self.table.refresh_table(medical_records_list)

    def save_click(self):
        status, message = MedicalRecordController.save(self.disease.variable.get(),
                                                       self.medicine.variable.get(),
                                                       self.doctor.variable.get(),
                                                       self.calendar.gregorian_date,
                                                       self.patient_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "record saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = MedicalRecordController.edit(self.id.variable.get(),
                                                       self.disease.variable.get(),
                                                       self.medicine.variable.get(),
                                                       self.doctor.variable.get(),
                                                       self.calendar.gregorian_date,
                                                       self.patient_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "record edited successfully!")
        else:
            msg.showerror("Error", message)

    def remove_click(self):
        status, message = MedicalRecordController.remove(self.id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "record deleted successfully!")
        else:
            msg.showerror("Error", message)

    def search_by_id(self, event):
        if self.search_id.variable.get():
            status, medical_record_list = MedicalRecordController.find_by_id(self.search_id.variable.get())
            if status:
                self.table.refresh_table([medical_record_list])
        else:
            status, medical_record_list = MedicalRecordController.find_all()
            if status:
                self.table.refresh_table(medical_record_list)



    def close_win(self):
        self.win.destroy()
        main_view = MainView(self.user)

    def __init__(self, user):
        self.user = user
        self.win = Tk()
        #Label(text=user.person.name + " " + user.person.family).place(x=0, y=0)
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.title('Medical Record')
        self.win.geometry('700x350')

        self.patient_id = TextWithLabel(self.win, 'Patient', 30, 20, 60,disabled=True)
        self.patient_id.variable.set(f"{self.user.person.person_id}-{self.user.person.name}-{self.user.person.family}")
        self.id = TextWithLabel(self.win, 'Record ID', 30, 60, 60, disabled=True)
        self.disease = TextWithLabel(self.win, 'Disease', 30, 100, 60)
        self.medicine = TextWithLabel(self.win, 'Medicine', 30, 140, 60)
        self.doctor = TextWithLabel(self.win, 'Doctor', 30, 180, 60)
        Label(self.win, text="Date").place(x=30, y=220)
        self.calendar = PersianCalendar(self.win, 90, 220)
        self.search_id = TextWithLabel(self.win, 'Search ID', 250, 280, 60)
        self.search_id.text_box.bind("<KeyRelease>", self.search_by_id)

        self.table = Table(self.win,
                      ['Record ID', 'Disease', 'Medicine', 'Doctor','Date'],
                      [70, 90, 90, 90,90],
                      250,
                      20,
                      self.select_row)

        Button(self.win, text='Save', width=10,bg="green", command=self.save_click).place(x=30, y=260)
        Button(self.win, text='Edit', width=10,bg="gray", command=self.edit_click).place(x=135, y=260)
        Button(self.win, text='Remove', width=10,bg="red", command=self.remove_click).place(x=30, y=300)
        Button(self.win, text='Reset', width=10,bg="gray", command=self.reset_form).place(x=135, y=300)

        self.reset_form()

        self.win.mainloop()
