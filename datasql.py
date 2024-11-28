import os
import sqlite3 as db
from data import Data

emptydb = """
PRAGMA foreign_keys = ON;

create table branch (
    code integer primary key, 
    name text, 
    address text, 
    phone integer
);

create table insurance_type (
    code integer primary key, 
    name text, 
    tariff_cost integer
);

create table contract (
    code integer primary key, 
    name text, 
    date text, 
    tariff integer
);

create table contract_insurance_type (
    contract integer references contract(code) on update cascade on delete cascade,
    insurance_type integer references insurance_type(code) on update cascade on delete cascade,
    unique(contract, insurance_type)
);

create table contract_branch (
    contract integer references contract(code) on update cascade on delete cascade,
    branch integer references branch(code) on update cascade on delete cascade,
    unique(contract, branch)
);
"""

class datasql(Data):
    def read(self):
        conn = db.connect(self.getInput())
        curs = conn.cursor()
        
        # Read branches
        curs.execute('select code, name, address, phone from branch')
        data = curs.fetchall()
        for r in data:
            self.getDatabase().createBranch(r[0], r[1], r[2], r[3])
        
        # Read insurance types
        curs.execute('select code, name, tariff_cost from insurance_type')
        data = curs.fetchall()
        for r in data:
            self.getDatabase().createInsuranceType(r[0], r[1], r[2])
        
        # Read contracts
        curs.execute('select code, name, date, tariff from contract')
        data = curs.fetchall()
        for r in data:
            contract = self.getDatabase().createContract(r[0], r[1], r[2], r[3], [], [])
            
            # Add insurance types to contract
            curs.execute('select insurance_type from contract_insurance_type where contract = ?', (r[0],))
            insurance_type_codes = curs.fetchall()
            for ins_type in insurance_type_codes:
                insurance_type = self.getDatabase().getInsuranceType(ins_type[0])
                contract.appendInsuranceType(insurance_type)
            
            # Add branches to contract
            curs.execute('select branch from contract_branch where contract = ?', (r[0],))
            branch_codes = curs.fetchall()
            for branch_code in branch_codes:
                branch = self.getDatabase().getBranch(branch_code[0])
                contract.appendBranch(branch)
        
        conn.close()

    def write(self):
        conn = db.connect(self.getOutput())
        curs = conn.cursor()
        
        # Execute the SQL to create empty database schema
        curs.executescript(emptydb)
        
        # Insert branches
        for branch in self.getDatabase().getBranchCodes():
            branch = self.getDatabase().getBranch(branch)
            curs.execute(
                "insert into branch(code, name, address, phone) values (?, ?, ?, ?)",
                (branch.getCode(), branch.getName(), branch.getAddress(), branch.getPhone())
            )
        
        # Insert insurance types
        for insuranceType in self.getDatabase().getInsuranceTypeCodes():
            insuranceType = self.getDatabase().getInsuranceType(insuranceType)
            curs.execute(
                "insert into insurance_type(code, name, tariff_cost) values (?, ?, ?)",
                (insuranceType.getCode(), insuranceType.getName(), insuranceType.getTariffCost())
            )
        
        # Insert contracts
        for contract in self.getDatabase().getContractCodes():
            contract_obj = self.getDatabase().getContract(contract)
            curs.execute(
                "insert into contract(code, name, date, tariff) values (?, ?, ?, ?)",
                (contract_obj.getCode(), contract_obj.getName(), contract_obj.getDate(), contract_obj.getTariff())
            )
            
            # Insert contract-insurance type relationships
            for insuranceType in contract_obj.getInsuranceTypes():
                curs.execute(
                    "insert into contract_insurance_type(contract, insurance_type) values (?, ?)",
                    (contract_obj.getCode(), insuranceType.getCode())
                )
            
            # Insert contract-branch relationships
            for branch in contract_obj.getBranch():
                curs.execute(
                    "insert into contract_branch(contract, branch) values (?, ?)",
                    (contract_obj.getCode(), branch.getCode())
                )
        
        conn.commit()
        conn.close()