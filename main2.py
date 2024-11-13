from database import Database
from dataxml import dataxml

db1 = Database()
data1 = dataxml(db1, 'old.xml', 'new.xml')
data1.read()
data1.write()
for k in db1.getContractCodes():
    print(db1.getContract(k).getDescription())