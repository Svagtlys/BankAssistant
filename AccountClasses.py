class Account:

    def __init__(self, newname, newdetails, *sectionNames):
        self.name = newname
        self.details = newdetails
        self.sections = {key: 0 for key in sectionNames}

    def deposit(self, sectionName, money):
        self.sections[sectionName] += money
        return

    def withdraw(self, sectionName, money):
        self.sections[sectionName] -= money
        return



class CreditCard(Account):

    def __init__(self, newname, newdetails, cashbackPercent):
        super().__init__(newname, newdetails, "Cashback Rewards")
        self.cashback = cashbackPercent

    def calculateCashBack(self, money):
        self.sections['Cashback Rewards'] += money*self.cashback
        return