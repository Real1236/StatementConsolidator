from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class RbcStatement(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for i in range(1, len(statement)):
            transaction = statement[i]
            transactions.append(Transaction(
                "RBC",
                transaction[0],
                datetime.strptime(transaction[2], "%m/%d/%Y").date(),
                transaction[4],
                transaction[5],
                float(transaction[6]) * - 1
            ))
        return transactions