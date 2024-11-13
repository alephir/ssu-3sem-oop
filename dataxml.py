import os, xml.dom.minidom
from data import Data

class dataxml(Data):
    def read(self):
        dom = xml.dom.minidom.parse(self.getInput())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'branch'):
                code, name, address, phone = 0, '', '', 0
                for t in node.attributes.items():
                    if t[0]=='code': code = int(t[1])
                    if t[0]=='name': name = t[1]
                    if t[0]=='address': address = t[1]
                    if t[0]=='phone': phone = int(t[1])
                self.getDatabase().createBranch(code, name, address, phone)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'insuranceType'):
                code, name, tariffCost = 0, '', 0
                for t in node.attributes.items():
                    if t[0]=='code': code = int(t[1])
                    if t[0]=='name': name = t[1]
                    if t[0]=='tariffCost': tariffCost = int(t[1])
                self.getDatabase().createInsuranceType(code, name, tariffCost)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'contract'):
                code, name, date, tariff = 0, '', '', 0
                for t in node.attributes.items():
                    if t[0]=='code': code = int(t[1])
                    if t[0]=='name': name = t[1]
                    if t[0]=='date': date = t[1]
                    if t[0]=='tariff': tariff = int(t[1])
                contract = self.getDatabase().createContract(code, name, date, tariff, [], [])
                for n in node.childNodes:
                    if(n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'insuranceType'):
                        for t in n.attributes.items():
                            if t[0] == 'code':
                                insuranceType = self.getDatabase().getInsuranceType(int(t[1]))
                            contract.appendInsuranceType(insuranceType)
                    if(n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'branch'):
                        for t in n.attributes.items():
                            if t[0] == 'code':
                                branch = self.getDatabase().getBranch(int(t[1]))
                            contract.appendBranch(branch)
    def write(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement('database')
        dom.appendChild(root)
        for branch in self.getDatabase().getBranchCodes():
            branch = self.getDatabase().getBranch(branch)
            node = dom.createElement('branch')
            node.setAttribute('code', str(branch.getCode()))
            node.setAttribute('name', branch.getName())
            node.setAttribute('address', branch.getAddress())
            node.setAttribute('phone', str(branch.getPhone()))
            root.appendChild(node)
        for insuranceType in self.getDatabase().getInsuranceTypeCodes():
            insuranceType = self.getDatabase().getInsuranceType(insuranceType)
            node = dom.createElement('insuranceType')
            node.setAttribute('code', str(insuranceType.getCode()))
            node.setAttribute('name', insuranceType.getName())
            node.setAttribute('tariffCost', str(insuranceType.getTariffCost()))
            root.appendChild(node)
        for contract in self.getDatabase().getContractCodes():
            contract = self.getDatabase().getContract(contract)
            node = dom.createElement('contract')
            node.setAttribute('code', str(contract.getCode()))
            node.setAttribute('name', contract.getName())
            node.setAttribute('date', contract.getDate())
            node.setAttribute('tariff', str(contract.getTariff()))
            node.setAttribute('branch', str(contract.getBranch()))
            node.setAttribute('insuranceTypes', str(contract.getInsuranceTypes()))
            for insuranceType in contract.getInsuranceTypes():
                ins = dom.createElement('insuranceType')
                ins.setAttribute('code', str(insuranceType.getCode()))
                node.appendChild(ins)
            for branch in contract.getBranch():
                br = dom.createElement('branch')
                br.setAttribute('code', str(branch.getCode()))
                node.appendChild(br)
            root.appendChild(node)
        f = open(self.getOutput(), 'w', encoding='utf-8')
        f.write(dom.toprettyxml(indent='  '))
        f.close()
        