from datetime import datetime
from typing import List
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction

class CibcStatement(Statement):
    def __init__(self, statement):
        super().__init__(statement)

    def process_statement(self, statement) -> List[Transaction]:
        transactions = []
        for transaction in statement:
            if transaction[2] == "":
                continue
            transactions.append(Transaction(
                "CIBC",
                "",
                datetime.strptime(transaction[0], "%Y-%m-%d").date(),
                transaction[1],
                "",
                -float(transaction[2])
            ))
        return transactions