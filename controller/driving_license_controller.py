from model.da.driving_license_da import DrivingLicenseDa
from model.entity.driving_license import DrivingLicense
from model.tools.validator import Validator


class DrivingLicenseController:
    def __init__(self):
        self.validator = Validator()

    def save(self, serial_number, date ,city , expire_date):
        try:
            drivingLicense = DrivingLicense(
                self.validator.name_validator(serial_number, "Invalid serial number"),
                date,
                self.validator.name_validator(city, "Invalid city"),
                expire_date
            )
            licenceDa = DrivingLicenseDa()
            licenceDa.save(drivingLicense)
            return True, f"DrivingLicense saved successfully\n{drivingLicense}"
        except Exception as e:
            return False, str(e)

    def edit(self, license_id, serial_number, date ,city , expire_date):
        try:
            drivingLicense = DrivingLicense(
                self.validator.name_validator(serial_number, "Invalid serial number"),
                date,
                self.validator.name_validator(city, "Invalid city"),
                expire_date
            )
            drivingLicense.id = license_id
            licenceDa = DrivingLicenseDa()
            licenceDa.edit(drivingLicense)
            return True, (f"DrivingLicense edited successfully")
        except Exception as e:
            return False, str(e)

    def remove(self, licenseId):
        try:
            licenceDa = DrivingLicenseDa()
            licenceDa.remove(licenseId)
            return True, f"DrivingLicense removed successfully"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            licenceDa = DrivingLicenseDa()
            return True, licenceDa.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, licenseId):
        try:
            licenceDa = DrivingLicenseDa()
            return True, licenceDa.find_by_id(licenseId)
        except Exception as e:
            return False, str(e)

    def find_by_serial_number(self, serialNumber):
        try:
            licenceDa = DrivingLicenseDa()
            return True, licenceDa.find_by_serial_number(
                self.validator.name_validator(serialNumber, "Invalid Serial Number")
            )
        except Exception as e:
            return False, str(e)
