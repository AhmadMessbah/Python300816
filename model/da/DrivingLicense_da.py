from model.da.da import Da
from ..entity.DrivingLicense import DrivingLicense


class DrivingLicenseDa(Da):
    def save(self, drivinnglicence):
        self.connect()
        self.cursor.execute(
            "INSERT INTO driving_license_tbl(CITY, DATE , SERIAL_NUMBER , EXPIRE_DATE) VALUES(%s,%s, %s, %s)",
            [drivinnglicence.city, drivinnglicence.date, drivinnglicence.serial_number, drivinnglicence.expire_date])
        self.connection.commit()
        self.disconnect()

    def edit(self, drivinnglicence):
        self.connect()
        self.cursor.execute(
            "UPDATE driving_license_tbl SET CITY=%S, DATE=$S, SERIAL_NUMBER=%S , expire_date=%s WHERE ID=%s",
            [drivinnglicence.city, drivinnglicence.date, drivinnglicence.serial_number, drivinnglicence.expire_date,
             drivinnglicence.id])
        self.connection.commit()
        self.disconnect()

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
        if driving_license_tuple_list:
            license_list = []
            for license_tuple in driving_license_tuple_list:
                license = DrivingLicense(license_tuple[1], license_tuple[2], license_tuple[3], license_tuple[4])
                license.id = license_tuple[0]
                license_list.append(license)
            return license_list
        else:
            raise ValueError("No license Found !")

    def find_by_id(self, drivnglicenc_id, drivnglicenc=None):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl WHERE ID=%s", [drivnglicenc_id])
        drivnglicenc_tuple = self.cursor.fetchone()
        self.disconnect()
        if drivnglicenc_tuple:
            drivingLicense = DrivingLicense(drivnglicenc_tuple[1], drivnglicenc_tuple[2], drivnglicenc_tuple[3],
                                            drivnglicenc_tuple[4])
            drivingLicense.id = drivnglicenc_tuple[0]
            return drivingLicense
        else:
            raise ValueError("No driving license Found !")

    def find_by_serial_number(self, serial_number):
        self.connect()
        self.cursor.execute("SELECT * FROM driving_license_tbl WHERE serial_number=%s", [serial_number])
        drivnglicenc_tuple = self.cursor.fetchone()
        self.disconnect()
        if drivnglicenc_tuple:
            drivingLicense = DrivingLicense(drivnglicenc_tuple[1], drivnglicenc_tuple[2], drivnglicenc_tuple[3],
                                            drivnglicenc_tuple[4])
            drivingLicense.id = drivnglicenc_tuple[0]
            return drivingLicense
        else:
            raise ValueError("No driving license Found !")
