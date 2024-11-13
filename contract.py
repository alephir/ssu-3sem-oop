from general import General
from branchlist import BranchList
from branch import Branch
from insurancetypelist import InsuranceTypeList
from insurancetype import InsuranceType

class Contract(General):
    def __init__(self, code = 0, name = '', date='', tariff = 0, branch = [], insuranceTypes = []):
        General.__init__(self, code, name)
        self.__total = 1
        self.__BranchList = BranchList()
        self.__InsuranceTypeList = InsuranceTypeList()
        self.setDate(date)
        self.setTariff(tariff)
        self.setBranch(branch)
        self.setInsuranceTypes(insuranceTypes)
        self.calculateTotal()
    def setDate(self, value):
        self.__date = value
    def setTariff(self, value):
        self.__tariff = value
    def setBranch(self, value):
        if isinstance(value, list):
            for l in value:
                if isinstance(value, Branch):
                    self.appendBranch(l)
        else:
            self.appendBranch(value)
    def appendInsuranceType(self, value):
        if isinstance(value, InsuranceType):
            self.__InsuranceTypeList.appendItem(value)
    def removeInsuranceType(self, value):
        if isinstance(value, InsuranceType):
            self.__InsuranceTypeList.removeItem(value)
    def setInsuranceTypes(self, value):
        for l in value:
            if isinstance(l, InsuranceType):
                self.appendInsuranceType(l)
    def calculateTotal(self):
        self.__total = 1
        x = self.__tariff
        for l in self.__InsuranceTypeList.getItems():
            x += l.getTariffCost()
        self.__total *= x
    def clearInsuranceTypes(self):
        self.__InsuranceTypeList.clear()
        self.calculateTotal()
    def appendBranch(self, value):
        if isinstance(value, Branch):
            self.__BranchList.appendItem(value)
    def removeBranch(self, value):
        if isinstance(value, Branch):
            self.__BranchList.removeItem(value)
    def getDate(self):
        return self.__date
    def getTotal(self):
        return self.__total
    def getTariff(self):
        return self.__tariff
    def getTariffTotal(self):
        x = self.__tariff
        for l in self.__InsuranceTypeList.getItems():
            x += l.getTariffCost()
        return x
    def getBranch(self):
        return self.__BranchList.getItems()
    def getInsuranceTypes(self):
        return self.__InsuranceTypeList.getItems()
    def getShortDescription(self):
        s = 'Имя застрахованного лица: ' + self.getName() + ' - '
        s += 'Дата: ' + self.getDate() + ' - '
        s += 'Тариф: ' + str(self.getTariffTotal()) + ' - '
        s += 'Всего: ' + str(self.getTotal())
        return s
    def getDescription(self):
        s = 'Договор номер: ' + str(self.getCode()) + '\n'
        s += 'Имя застрахованного лица: ' + self.getName() + '\n'                               
        s += 'Дата: ' + self.getDate() + '\n'
        s += 'Тарифная ставка: ' + str(self.getTariff()) + '\n'
        s += 'Конечная тарифная ставка: ' + str(self.getTariffTotal()) + '\n'
        s += 'Всего: ' + str(self.getTotal()) + '\n'
        s += 'Контрагент(ы): '
        for l in self.getBranch():
            s += l.getName() + ', '
            s += l.getAddress() + ', '
            s += l.getPhoneReadable() + '\n'
        s += 'Виды страхования:\n'
        i = 1
        for l in self.getInsuranceTypes():
            s += str(i) + '. ' + l.getName() + '\n'
            i+=1
        return s
    