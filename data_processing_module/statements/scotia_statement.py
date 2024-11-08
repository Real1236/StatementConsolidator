from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class ScotiaStatement(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for i in range(1, len(statement)):
            transaction = statement[i]
            transactions.append(Transaction(
                "SCOTIA",
                "Gold Amex",
                datetime.strptime(transaction[1], "%Y-%m-%d").date(),
                transaction[2].upper(),
                transaction[3].upper(),
                -float(transaction[6]) if transaction[5] == "Debit" else float(transaction[6])
            ))
        return transactions