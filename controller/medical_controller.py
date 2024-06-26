from model.da.medical_da import MedicalDa
from model.da.person_da import PersonDa
from model.entity.medical_record import MedicalRecord
from model.tools.decorators import exception_handling


class MedicalRecordController:
    medical_da = MedicalDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, disease, medicine, doctor, date_time, patient_id):
        if patient_id:
            patient = cls.person_da.find_by_id(patient_id)
            medical_record = MedicalRecord(disease, medicine, doctor, date_time, patient)
        else:
            medical_record = MedicalRecord(disease, medicine, date_time, doctor)

        cls.medical_da.save(medical_record)
        return True, f"record saved successfully\n{medical_record}"

    @classmethod
    @exception_handling
    def edit(cls, id, disease, medicine, doctor, date_time, patient_id):
        patient = cls.person_da.find_by_id(patient_id)
        medical_record = MedicalRecord(disease, medicine, doctor, date_time, patient)
        medical_record.id = id
        old_record = cls.medical_da.find_by_id(id)
        cls.medical_da.edit(medical_record)
        return True, f"record edited successfully\nFrom : {old_record}\nTo: {medical_record}"

    @classmethod
    @exception_handling
    def remove(cls, id):
        medical_record = cls.medical_da.find_by_id(id)
        cls.medical_da.remove(id)
        return True, f"record removed successfully\n{medical_record}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.medical_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.medical_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_patient_id(cls, patient_id):
        return True, cls.medical_da.find_by_patient_id(patient_id)
