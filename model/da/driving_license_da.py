from model.da.da import Da
from ..entity.driving_license import DrivingLicense
from model.da.person_da import PersonDa



class DrivingLicenseDa(Da):
    def save(self, drivinnglicence):
        if(drivinnglicence.person and self.find_driving_license_count_by_person_id(drivinnglicence.person.person_id)< 3):
            self.connect()
            self.cursor.execute(
                "INSERT INTO driving_license_tbl(CITY, DATE , SERIAL_NUMBER , EXPIRE_DATE, PERSON_ID) VALUES(%s,%s, %s, %s, %s)",
                [drivinnglicence.city, drivinnglicence.date, drivinnglicence.serial_number, drivinnglicence.expire_date, drivinnglicence.person.person_id])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Person Or Cant Save Any More !!!")

    def edit(self, drivinnglicence):
        if(drivinnglicence.person and self.find_driving_license_count_by_person_id(drivinnglicence.person.person_id)< 3):
            self.connect()
            self.cursor.execute(
                "UPDATE driving_license_tbl SET CITY=%s, DATE=%s, SERIAL_NUMBER=%s , expire_date=%s , person_id=%s WHERE ID=%s",
                [drivinnglicence.city, drivinnglicence.date, drivinnglicence.serial_number, drivinnglicence.expire_date,drivinnglicence.person.person_id,
                drivinnglicence.id])
            self.connection.commit()
            self.disconnect()
        else:
            raise ValueError("Error in Person Or Cant Save Any More !!!")

    def remove(self, drivnglicenc_id):
        self.connect()
        self.cursor.execute("DELETE FROM driving_license_tbl WHERE ID=%s",
                            [drivnglicenc_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl")
        driving_license_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if driving_license_tuple_list:
            license_list = []
            for license_tuple in driving_license_tuple_list:
                license = DrivingLicense(license_tuple[1], license_tuple[2], license_tuple[3], license_tuple[4], person_da.find_by_id(license_tuple[5]))
                license.id = license_tuple[0]
                license_list.append(license)
            return license_list
        else:
            raise ValueError("No license Found !")

    def find_by_id(self, driving_license_id):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl WHERE ID=%s", [driving_license_id])
        drivnglicenc_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if drivnglicenc_tuple:
            drivingLicense = DrivingLicense(drivnglicenc_tuple[1], drivnglicenc_tuple[2], drivnglicenc_tuple[3],
                                            drivnglicenc_tuple[4], person_da.find_by_id(drivnglicenc_tuple[5]))
            drivingLicense.id = drivnglicenc_tuple[0]
            return drivingLicense
        else:
            raise ValueError("No driving license Found !")

    def find_by_serial_number(self, serial_number):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl WHERE serial_number=%s", [serial_number])
        drivnglicenc_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if drivnglicenc_tuple:
            drivingLicense = DrivingLicense(drivnglicenc_tuple[1], drivnglicenc_tuple[2], drivnglicenc_tuple[3],
                                            drivnglicenc_tuple[4], person_da.find_by_id(drivnglicenc_tuple[5]))
            drivingLicense.id = drivnglicenc_tuple[0]
            return drivingLicense
        else:
            raise ValueError("No driving license Found !")

    def find_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl where person_id=%s", [person_id])
        driving_license_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if driving_license_tuple_list:
            license_list = []
            for license_tuple in driving_license_tuple_list:
                license = DrivingLicense(license_tuple[1], license_tuple[2], license_tuple[3], license_tuple[4], person_da.find_by_id(license_tuple[5]))
                license.id = license_tuple[0]
                license_list.append(license)
            return license_list
        else:
            raise ValueError("No license Found !")
        
    def find_driving_license_count_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl WHERE person_id=%s", [person_id])
        l_count = self.cursor.fetchone()
        self.disconnect()
        if l_count:
            return int(l_count[1])
        else:
            return 0