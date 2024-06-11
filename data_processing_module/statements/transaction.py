from datetime import date

class Transaction():
    def __init__(self, bank: str, accountType: str, transactionDate: date, description1: str, description2: str, amount: float):
        self.bank = bank
        self.accountType = accountType
        self.transactionDate = transactionDate
        self.description1 = description1
        self.description2 = description2
        self.amount = amount

    def __str__(self):
        return f"bank={self.bank}, accountType={self.accountType}, transactionDate={self.transactionDate}, description1={self.description1}, description2={self.description2}, amount={self.amount}"