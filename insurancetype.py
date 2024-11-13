from general import General

class InsuranceType(General):
    def __init__(self, code=0, name='', tariffCost=0):
        General.__init__(self, code, name)
        self.setTariffCost(tariffCost)
    def setTariffCost(self, value):
        self.__tariffCost = value
    def getTariffCost(self):
        return self.__tariffCost