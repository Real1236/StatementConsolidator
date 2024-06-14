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
                transaction[0],
                transaction[1],
                transaction[2].date(),
                transaction[3],
                transaction[4],
                float(transaction[5]),
                transaction[6]
            ))
        return transactions