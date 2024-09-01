from typing import List
from data_processing_module.statements.consolidated_statement import ConsolidatedStatement
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction
from filter import Filter

class Consolidator(Filter):
    def process(self, data: List[Statement]) -> List[Transaction]:
        # Get existing category assignments
        consolidatedStatement = None
        for statement in data:
            if isinstance(statement, ConsolidatedStatement):
                consolidatedStatement = statement
        itemToCategory = self.getCategories(consolidatedStatement) if consolidatedStatement else {}

        # Consolidate and sort transactions from all statements
        transactions = []
        transactions_set = set()
        for statement in data:
            for transaction in statement.statement:
                if str(transaction) not in transactions_set:
                    if not transaction.category:
                        transaction.category = itemToCategory[transaction.description1] if transaction.description1 in itemToCategory else None
                    transactions.append(transaction)
                    transactions_set.add(str(transaction))
                else:
                    if transaction.category or transaction.splitWith:
                        for t in transactions:
                            if str(t) == str(transaction):
                                if transaction.category:
                                    t.category = transaction.category
                                if transaction.splitWith:
                                    t.splitWith = transaction.splitWith
                                break

        transactions.sort(key=lambda x: x.transactionDate)
        return transactions
    
    def getCategories(self, consolidatedStatement: ConsolidatedStatement) -> dict:
        # Get all unique categories from all transactions
        itemToCategory = {}
        for transaction in consolidatedStatement.statement:
            if transaction.category and transaction.description1 != "Email Trfs":
                itemToCategory[transaction.description1] = transaction.category

        return itemToCategory

