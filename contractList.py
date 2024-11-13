from generallist import GeneralList
from contract import Contract
import warnings

class InsuranceTypeList(GeneralList):
    def __init__(self):
        GeneralList.__init__(self)
    def appendItem(self, value):
        if isinstance(value, Contract):
            self._list.append(value)
    def createItem(self, code=0, name = '', date='', tariff = 0, branch = None, insuranceTypes = []):
        if code == 0:
                warnings.warn("Рекомендуется использовать метод newItem")
        if code in self.getCodes(): 
            raise Exception("Объект с кодом %s уже существует"%(code))
        else:
            a = Contract(code, name, date, tariff, branch, insuranceTypes)
            self.appendItem(a)
            return a
    def newItem(self, name, date, tariff, branch, insuranceTypes):
        a = Contract(self.getNewCode(), name, date, tariff, branch, insuranceTypes)
        self.appendItem(a)
        return a
    def removeItem(self, value):
        if isinstance(value, Contract):
            self._list.remove(value)
        else:
            if isinstance(value, int):
                self._list.remove(self.findByCode(value))