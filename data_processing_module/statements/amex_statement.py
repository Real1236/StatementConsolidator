from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class AmexStatement(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for transaction in statement:
            transactions.append(Transaction(
                "AMEX",
                "",
                datetime.strptime(transaction[0], "%m/%d/%Y").date(),
                transaction[3],
                transaction[4],
                float(transaction[2])
            ))
        return transactions