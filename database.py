from branchlist import BranchList
from insurancetypelist import InsuranceTypeList
from contractList import ContractList

class Database:
    def __init__(self, contractList = [], branchList = [], insuranceTypeList = []):
        self.__contractList = ContractList()
        self.__branchList = BranchList()
        self.__insuranceTypeList = InsuranceTypeList()
    def clear(self):
        self.__contractList.clear()
        self.__branchList.clear()
        self.__insuranceTypeList.clear()
    def createBranch(self, code=0, name='', address='', phone=0):
        return self.__branchList.createItem(code, name, address, phone)
    def newBranch(self, name, address, phone):
        return self.__branchList.newItem(name, address, phone)
    def removeBranch(self, value):
        self.__branchList.removeItem(value)
    def getBranch(self, code):
        return self.__branchList.findByCode(code)
    def getBranchList(self):
        return self.__branchList.getItems()
    def getBranchCodes(self):
        return self.__branchList.getCodes()
    def getBranchNewCode(self):
        return self.__branchList.getNewCode()
    

    def createInsuranceType(self, code=0, name='', tariffCost = 0):
        return self.__insuranceTypeList.createItem(code, name, tariffCost)
    def newInsuranceType(self, name, tariffCost):
        return self.__insuranceTypeList.newItem(name, tariffCost)
    def removeInsuranceType(self, value):
        self.__insuranceTypeList.removeItem(value)
    def getInsuranceType(self, code):
        return self.__insuranceTypeList.findByCode(code)
    def getInsuranceTypeList(self):
        return self.__insuranceTypeList.getItems()
    def getInsuranceTypeCodes(self):
        return self.__insuranceTypeList.getCodes()
    def getInsuranceTypeNewCode(self):
        return self.__insuranceTypeList.getNewCode()
    

    def createContract(self, code = 0, name = '', date='', tariff = 0, branch = [], insuranceTypes = []):
        return self.__contractList.createItem(code, name, date, tariff, branch, insuranceTypes)
    def newContract(self, name, date, tariff, branch, insuranceTypes):
        return self.__contractList.newItem(name, date, tariff, branch, insuranceTypes)
    def removeContract(self, value):
        self.__contractList.removeItem(value)
    def getContract(self, code):
        return self.__contractList.findByCode(code)
    def getContractList(self):
        return self.__contractList.getItems()
    def getContractCodes(self):
        return self.__contractList.getCodes()
    def getContractNewCode(self):
        return self.__contractList.getNewCode()