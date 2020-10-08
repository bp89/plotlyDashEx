from model.enums import AccountType


class Account(object):
    accountNumber = None
    accountHolderName = None
    accountType: AccountType = None
    accountOpeningDate = None

    # def __init__(self, accountNumber, accountHolderName, accountType):
    #     self.accountHolderName = accountHolderName
    #     self.accountType = accountType
    #     self.accountNumber = accountNumber
