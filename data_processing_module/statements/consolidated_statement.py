from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class ConsolidatedStatement(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for i in range(1, len(statement)):
            transaction = statement[i]
            transactions.append(Transaction(
                transaction[0] if transaction[0] else "",
                transaction[1] if transaction[1] else "",
                transaction[2].date(),
                transaction[3] if transaction[3] else "",
                transaction[4] if transaction[4] else "",
                float(transaction[5])
            ))
        return transactions