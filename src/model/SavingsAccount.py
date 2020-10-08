from model.Account import Account


class SavingsAccount(Account):
    accountBalance: 0

    def __init__(self, row):
        self.accountType = row[2]
        self.accountHolderName = row[1]
        self.accountNumber = row[0]
        self.accountBalance = row[3]
        self.accountOpeningDate = row[4]
