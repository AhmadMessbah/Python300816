from model.da import person_da
from model.da.da import Da
from model.entity.medical_record import MedicalRecord
from model.da.person_da import PersonDa


class MedicalDa(Da):
    def save(self, medical_record):
        if (medical_record.patient and self.find_medical_record_count_by_patient_id(
                medical_record.patient.person_id) < 5):

            self.connect()
            self.cursor.execute(
                'INSERT INTO medical_record (disease, medicine, doctor,date_time,patient_id) VALUES (%s,%s,%s,%s,%s)',
                [medical_record.disease,
                 medical_record.medicine,
                 medical_record.doctor,
                 medical_record.date_time,
                 medical_record.patient.person_id if medical_record.patient else None])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Cant Save Any More!")

    def edit(self, medical_record):
        if (medical_record.patient and self.find_medical_record_count_by_patient_id(
                medical_record.patient.person_id) < 5):

            self.connect()
            self.cursor.execute(
                'UPDATE medical_record set disease = %s, medicine = %s, doctor = %s ,date_time = %s , patient_id = %s WHERE id = %s',
                [medical_record.disease,
                 medical_record.medicine,
                 medical_record.doctor,
                 medical_record.date_time,
                 medical_record.patient.person_id if medical_record.patient else None,
                 medical_record.id])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Cant Edit Any More!")

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM medical_record WHERE id = %s', [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM medical_record')
        medical_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if medical_tuple_list:
            medical_records_list = []
            for tuple_record in medical_tuple_list:
                medical_records = MedicalRecord(
                    tuple_record[1],
                    tuple_record[2],
                    tuple_record[3],
                    tuple_record[4],
                    person_da.find_by_id(tuple_record[5]))
                medical_records.id = tuple_record[0]
                medical_records_list.append(medical_records)
            return medical_records_list
        else:
            raise ValueError('No records found')

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM medical_record WHERE id like %s', [id])
        tuple_record = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if tuple_record:
            medical_records = MedicalRecord(tuple_record[1],
                                            tuple_record[2],
                                            tuple_record[3],
                                            tuple_record[4],
                                            person_da.find_by_id(tuple_record[5]))
            medical_records.id = tuple_record[0]
            return medical_records
        else:
            raise ValueError("No records found with this id")

    def find_by_patient_id(self, patient_id):
        self.connect()
        self.cursor.execute('SELECT * FROM medical_record WHERE patient_id = %s', [patient_id])
        medical_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if medical_tuple_list:
            medical_records_list = []
            for tuple_record in medical_tuple_list:
                medical_records = MedicalRecord(
                    tuple_record[1],
                    tuple_record[2],
                    tuple_record[3],
                    tuple_record[4],
                    person_da.find_by_id(tuple_record[5]))
                medical_records.id = tuple_record[0]
                medical_records_list.append(medical_records)
            return medical_records_list
        else:
            raise ValueError('No records found')

    def find_medical_record_count_by_patient_id(self, patient_id):
        self.connect()
        self.cursor.execute('SELECT count(*) FROM medical_record WHERE patient_id = %s', [patient_id])
        medical_records_count = self.cursor.fetchone()
        self.disconnect()
        if medical_records_count:
            return int(medical_records_count[0])
        else:
            return 0
