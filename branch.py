from general import General

class Branch(General):
    def __init__(self, code=0, name='', address='', phone=0):
        General.__init__(self, code, name)
        self.setAddress(address)
        self.setPhone(phone)
    def setAddress(self, value):
        self.__address = value
    def setPhone(self, value):
        self.__phone = value
    def getAddress(self):
        return self.__address
    def getPhone(self):
        return self.__phone
    def getPhoneReadable(self):
        phonestr = str(self.__phone)
        return '+' + phonestr[0] + ' (' + phonestr[1:4] + ') ' + phonestr[4:7] + '-' + phonestr[7:]