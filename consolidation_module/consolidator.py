from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction
from filter import Filter

class Consolidator(Filter):
    def process(self, data: List[Statement]) -> List[Transaction]:
        # Consolidate and sort transactions from all statements
        transactions = []
        transactions_set = set()
        for statement in data:
            for transaction in statement.statement:
                if str(transaction) not in transactions_set:
                    transactions.append(transaction)
                    transactions_set.add(str(transaction))
                elif transaction.category:
                    for t in transactions:
                        if str(t) == str(transaction):
                            t.category = transaction.category
                            break

        transactions.sort(key=lambda x: x.transactionDate)
        return transactions

