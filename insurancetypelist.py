from generallist import GeneralList
from insurancetype import InsuranceType
import warnings

class InsuranceTypeList(GeneralList):
    def __init__(self):
        GeneralList.__init__(self)
    def appendItem(self, value):
        if isinstance(value, InsuranceType):
            self._list.append(value)
    def createItem(self, code=0, name='', tariffCost=0):
        if code == 0:
                warnings.warn("Рекомендуется использовать метод newItem")
        if code in self.getCodes(): 
            raise Exception("Объект с кодом %s уже существует"%(code))
        else:
            a = InsuranceType(code, name, tariffCost)
            self.appendItem(a)
            return a
    def newItem(self, name, tariffCost):
        a = InsuranceType(self.getNewCode(), name, tariffCost)
        self.appendItem(a)
        return a
    def removeItem(self, value):
        if isinstance(value, InsuranceType):
            self._list.remove(value)
        else:
            if isinstance(value, int):
                self._list.remove(self.findByCode(value))
    def getTariffCost(self, value):
        if isinstance(value, InsuranceType):
            return value.getTariffCost()
        else:
            if isinstance(value, int):
                return self._list.index(self.findByCode(value)).getTariffCost()