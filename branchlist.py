from generallist import GeneralList
from branch import Branch
import warnings

class BranchList(GeneralList):
    def __init__(self):
        GeneralList.__init__(self)
    def appendItem(self, value):
        if isinstance(value, Branch):
            self._list.append(value)
    def createItem(self, code=0, name='', address='', phone=0):
        if code == 0:
                warnings.warn("Рекомендуется использовать метод newItem")
        if code in self.getCodes(): 
            raise Exception("Объект с кодом %s уже существует"%(code))
        else:
            a = Branch(code, name, address, phone)
            self.appendItem(a)
    def newItem(self, name, address, phone):
        a = Branch(self.getNewCode(), name, address, phone)
        self.appendItem(a)
        return a
    def removeItem(self, value):
        if isinstance(value, Branch):
            self._list.remove(value)
        else:
            if isinstance(value, int):
                self._list.remove(self.findByCode(value))
    def getAddress(self, value):
        if isinstance(value, Branch):
            return value.getAddress()
        else:
            if isinstance(value, int):
                return (self._list.index(self.findByCode(value))).getAddress()
    def getPhone(self, value):
        if isinstance(value, Branch):
            return value.getPhone()
        else:
            if isinstance(value, int):
                return self.findByCode(value).getPhone()
    def getPhoneReadable(self, value):
        if isinstance(value, Branch):
            return value.getPhoneReadable()
        else:
            if isinstance(value, int):
                return self.findByCode(value).getPhoneReadable()