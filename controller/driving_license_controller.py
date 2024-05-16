from model.da.driving_license_da import DrivingLicenseDa
from model.da.person_da import PersonDa
from model.entity.driving_license import DrivingLicense
from model.tools.decorators import exception_handling


class DrivingLicenseController:
    driving_license_da = DrivingLicenseDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, serial_number, date ,city , expire_date, person_id):
        if(person_id):
            person = cls.person_da.find_by_id(person_id)
            dl = DrivingLicense(serial_number, date, city, expire_date, person)
        else:
            dl = DrivingLicense(serial_number, date, city, expire_date)
        
        cls.driving_license_da.save(dl)
        return True, f"Driving License saved successfully\n{dl}"

    @classmethod
    @exception_handling
    def edit(cls, license_id, serial_number, date ,city , expire_date, person_id):
        person = cls.person_da.find_by_id(person_id)
        dl = DrivingLicense(serial_number, date, city, expire_date, person)
        dl.id = license_id
        old_dl = cls.driving_license_da.find_by_id(license_id)
        cls.driving_license_da.edit(dl)
        return True, (f"DrivingLicense edited successfully\nFrom : {old_dl}\nTo: {dl}")


    @classmethod
    @exception_handling
    def remove(cls, license_id):
        dl = cls.driving_license_da.find_by_id(license_id)
        cls.driving_license_da.remove(license_id)
        return True, f"DrivindLicense removed successfully\n{dl}"
    
    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.driving_license_da.find_all()
    
    @classmethod
    @exception_handling
    def find_by_id(cls, license_id):
        return True, cls.driving_license_da.find_by_id(license_id)
    
    
    @classmethod
    @exception_handling
    def find_by_seridal_number(cls, serial_number):
        return True, cls.driving_license_da.find_by_serial_number(serial_number)
    
    @classmethod
    @exception_handling
    def find_by_person_id(cls, person_id):
        return True, cls.driving_license_da.find_by_person_id(person_id)