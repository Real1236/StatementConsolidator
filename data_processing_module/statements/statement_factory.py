import re
from data_processing_module.statements.rbc_statement import RbcStatement

class StatementFactory():
    @staticmethod
    def create_statement(statement):
        first_row = ",".join(statement[0])
        if first_row == 'Account Type,Account Number,Transaction Date,Cheque Number,Description 1,Description 2,CAD$,USD$':
            return RbcStatement(statement)
        # elif re.match(r'\d{2}/\d{2}/\d{4}', first_row[0]) and 'Reference:' in first_row[1]:
        #     return AmexStatement(statement)
        # elif re.match(r'\d{4}-\d{2}-\d{2}', first_row[0]) and re.search(r'\d{3}\*\*\*\*\*\*\*\*\*\*\*\d{4}', first_row[4]):
        #     return CibcStatement(statement)
        else:
            raise ValueError("Unknown statement format")