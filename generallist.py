from general import General
import warnings

class GeneralList:
    def __init__(self):
        self._list = []
    def clear(self):
        self._list = []
    def getCodes(self):
        return [s.getCode() for s in self._list]
    def findByCode(self, code):
        for l in self._list:
            if l.getCode() == code:
                return l
    def getNewCode(self):
        if self._list == []:
            return 0
        return max(self.getCodes())+1
    def appendItem(self, value):
        if isinstance(value, General):
            self._list.append(value)
    def createItem(self, code=0, name=''):
        if code == 0:
                warnings.warn("Рекомендуется использовать метод newItem")
        if code in self.getCodes(): raise Exception("Объект с кодом %s уже существует"%(code))
        else:
            a = General(code, name)
            self.appendItem(a)
    def newItem(self, name):
        a = General(self.getNewCode(), name)
        self.appendItem(a)
        return a
    def removeItem(self, value):
        if isinstance(value, General):
            self._list.remove(value)
        else:
            if isinstance(value, int):
                self._list.remove(self.findByCode(value))
    def getItems(self):
        return self._list