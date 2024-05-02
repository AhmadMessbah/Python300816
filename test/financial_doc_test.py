from controller.financial_doc_controller import FinancialDocController

f_controller = FinancialDocController()

status, message =  f_controller.save(126,"outcome", "طی چک شماره 1022")

