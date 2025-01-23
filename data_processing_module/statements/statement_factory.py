import re
from data_processing_module.statements.amex_statement import AmexStatement
from data_processing_module.statements.amex_statement_2 import AmexStatement2
from data_processing_module.statements.amex_statement_3 import AmexStatement3
from data_processing_module.statements.cibc_statement import CibcStatement
from data_processing_module.statements.cibc_debit_statement import CibcDebitStatement
from data_processing_module.statements.consolidated_statement import ConsolidatedStatement
from data_processing_module.statements.rbc_statement import RbcStatement
from data_processing_module.statements.scotia_statement import ScotiaStatement

class StatementFactory():
    @staticmethod
    def create_statement(statement):
        first_row = statement[0]
        first_row_str = ",".join(first_row)
        try:
            if first_row_str == 'Account Type,Account Number,Transaction Date,Cheque Number,Description 1,Description 2,CAD$,USD$':
                return RbcStatement(statement)
            elif first_row_str == 'Bank,Account Type,Transaction Date,Description 1,Description 2,Amount,Category,Split With':
                return ConsolidatedStatement(statement)
            elif first_row_str == 'Date,Date Processed,Description,Card Member,Account #,Amount':
                return AmexStatement3(statement)
            elif 'Filter,Date,Description,Sub-description,Status,Type of Transaction,Amount' in first_row_str:
                return ScotiaStatement(statement)
            elif first_row_str == 'Date,Date Processed,Description,Amount':
                return AmexStatement2(statement)
            elif re.match(r'\d{2}/\d{2}/\d{4}', first_row[0]) and 'Reference:' in first_row[1]:
                return AmexStatement(statement)
            elif re.match(r'\d{4}-\d{2}-\d{2}', first_row[0]) and len(first_row) == 5 and re.search(r'\d{4}\*\*\*\*\*\*\*\*\d{4}', first_row[4]):
                return CibcStatement(statement)
            elif re.match(r'\d{4}-\d{2}-\d{2}', first_row[0]) and len(first_row) == 4 and (is_numeric(first_row[2]) or is_numeric(first_row[3])):
                return CibcDebitStatement(statement)
            else:
                raise ValueError("Unknown statement format")
        except Exception as e:
            raise ValueError("Unknown statement format")
        
def is_numeric(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False