from datetime import date

class Transaction():
    def __init__(
        self, 
        bank: str = '', 
        accountType: str = '', 
        transactionDate: date = date.today(), 
        description1: str = '', 
        description2: str = '', 
        amount: float = 0.0,
        category: str = '',
        splitWith: str = ''
    ):
        self.bank = bank
        self.accountType = accountType
        self.transactionDate = transactionDate
        self.description1 = description1
        self.description2 = description2
        self.amount = amount
        self.category = category
        self.splitWith = splitWith

    def __str__(self):
        return (
            f"bank={self.bank},\n"
            f"accountType={self.accountType},\n"
            f"transactionDate={self.transactionDate},\n"
            f"description1={self.description1},\n"
            f"amount={self.amount}"
        )