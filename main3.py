from database import Database
from datasql import datasql
from dataxml import dataxml
import os

db1 = Database()
db2 = Database()

dxml1 = dataxml(db1, 'old.xml', 'new.xml')
#dxml2 = dataxml(db2, 'old.xml', 'new.xml')

dsql1 = datasql(db1, 'new.sqlite', 'new.sqlite')

#dxml1.read()

if os.path.isfile(dsql1.getOutput()):
    os.remove(dsql1.getOutput())

dsql1.write()
dsql1.read()
#dxml2.write()
