from model.entity.base import Base
from model.tools.validator import Validator


class MedicalRecord(Base):
    def __init__(self, disease, medicine, doctor, date_time, patient=None):
        self.id = None
        self.disease = disease
        self.medicine = medicine
        self.doctor = doctor
        self.date_time = date_time
        self.patient = patient

    def get_disease(self):
        return self._disease

    def set_disease(self, disease):
        self._disease = Validator.name_validator(disease, "invalid disease")

    def get_medicine(self):
        return self._medicine

    def set_medicine(self, medicine):
        self._medicine = Validator.name_validator(medicine, "there is no medicine with this name")

    def get_doctor(self):
        return self._doctor

    def set_doctor(self, doctor):
        medical_record_validator = Validator()
        self._doctor = medical_record_validator.name_validator(doctor, "invalid name")

    def get_date_time(self):
        return self._date_time

    def set_date_time(self, date_time):
        self._date_time = Validator.date_validator(date_time, "invalid date_time")

    def get_patient(self):
        return self._patient

    def set_patient(self, patient):
        self._patient = patient

    disease = property(get_disease, set_disease)
    medicine = property(get_medicine, set_medicine)
    doctor = property(get_doctor, set_doctor)
    date_time = property(get_date_time, set_date_time)
    patient = property(get_patient, set_patient)
