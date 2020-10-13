from model.enums import AccountType


class Account(object):
    accountNumber = None
    accountHolderName = None
    accountType: AccountType = None
    accountOpeningDate = None

