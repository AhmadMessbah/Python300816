from controller.financial_doc_controller import FinancialDoc_Controller

f_controller = FinancialDoc_Controller()

status, message =  f_controller.save(122,"incosdfsfme", "طی چک شماره 1022")

if status:
    # message.showinfo()
    print("Info")
    print(message)
else:
    # message.showerror()
    print("Error")
    print(message)