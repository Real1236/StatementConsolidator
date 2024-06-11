from typing import List
from data_processing_module.statements.statement import Statement
from filter import Filter
from data_processing_module.statements.statement_factory import StatementFactory

class Processor(Filter):
    def process(self, data: dict) -> List[Statement]:
        processed_statements = []
        for fileName, statement in data.items():
            try:
                processed_statements.append(StatementFactory.create_statement(statement))
            except ValueError as e:
                print(fileName + " error: " + str(e))

        return processed_statements
    
