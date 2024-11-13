from branchlist import BranchList
from branch import Branch
from insurancetype import InsuranceType
from insurancetypelist import InsuranceTypeList
from contract import Contract
b = BranchList()
b1 = Branch(b.getNewCode(), "BlaBla", "st. BlaBla", +71234567890)

b.appendItem(b1)
print(b1.getPhoneReadable())
print(b.getCodes())
print(b.getPhoneReadable(b1))
print(b.getPhoneReadable(0))
print(b.findByCode(0).getAddress())

b.removeItem(b1)
print(b.getCodes())

b.clear()
print(b.getCodes())

i = InsuranceTypeList()
i1 = InsuranceType(i.getNewCode(), "BlaBla", 5.2)
i2 = InsuranceType(i.getNewCode(), "BlaBlaBla", 4)
print(i1.getTariffCost())
print(i.getTariffCost(i1))
b1 = Branch(b.getNewCode(), "BlaBla", "st. BlaBla", +71234567890)
c = Contract(12, "123", "21.10.2024", 3, b1, [i1,i2])
print(c.getTotal())
c.calculateTotal()
print(c.getTotal())
print(c.getShortDescription())
print(c.getDescription())
