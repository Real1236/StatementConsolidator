from abc import ABC, abstractmethod
from typing import List

from data_processing_module.statements.transaction import Transaction

class Statement(ABC):
    def __init__(self, statement):
        self.statement = self.process_statement(statement)

    @abstractmethod
    def process_statement(self, statement) -> List[Transaction]:
        pass

    def __str__(self) -> str:
        res = ""
        for transaction in self.statement:
            res += str(transaction) + "\n"
        return res