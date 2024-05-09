from datetime import datetime

from controller.financial_doc_controller import FinancialDocController
from model.da.financial_doc_da import FinancialDocDa
from model.entity.financial_doc import FinancialDoc
from model.entity.person import Person

person = Person("aaa", "bbb")
person.person_id = 1

doc = FinancialDoc(5000, datetime.now(),"income", "Description")
doc.financial_doc_id = 3
doc.person = person

da = FinancialDocDa()
#da.save(doc)
#da.edit(doc)
#da.remove(1)
da.find_all()


# f_controller = FinancialDocController()

# status, message =  f_controller.save(126,"outcome", "Check 1022")

