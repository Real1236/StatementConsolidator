from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class AmexStatement2(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for i in range(1, len(statement)):
            transaction = statement[i]
            transactions.append(Transaction(
                "AMEX",
                "",
                datetime.strptime(transaction[0], "%d %b %Y").date(),
                transaction[2],
                "",
                float(transaction[3])
            ))
        return transactions