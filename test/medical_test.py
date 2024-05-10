from controller.medical_controller import MedicalRecordController

#passed-(save)
#status,message = MedicalRecordController.save("cold","jkhnjhhk","ahmadi",3)

#passed-(remove)
#status,message = MedicalRecordController.remove("4")

#passed-(findall)
#status,message=MedicalRecordController.find_all()

#passed-(find by id)
#status,message=MedicalRecordController.find_by_id("5")

#passed-(find by patient id)
#status,message=MedicalRecordController.find_by_patient_id("3")


#todo :test pass nashode-error
status, message = MedicalRecordController.edit("6", "anfolanza", "aaaaa", "mirhosseini", "4")

if status:
    print(message)
else:
    print(message)
