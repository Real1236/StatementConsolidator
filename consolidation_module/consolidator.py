from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction
from filter import Filter

class Consolidator(Filter):
    def process(self, data: List[Statement]) -> List[Transaction]:
        # Consolidate and sort transactions from all statements
        transactions = []
        for statement in data:
            for transaction in statement.statement:
                transactions.append(transaction)

        transactions.sort(key=lambda x: x.transactionDate)
        return transactions

