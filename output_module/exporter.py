from filter import Filter
import xlsxwriter
from datetime import date
from data_processing_module.statements.transaction import Transaction

class Exporter(Filter):
    def process(self, data: list[Transaction]) -> None:
        workbook = xlsxwriter.Workbook('SpendTracker.xlsx')
        worksheet = workbook.add_worksheet()

        blank_transaction = Transaction()
        header = list(vars(blank_transaction).keys())
        for i, field in enumerate(header):
            worksheet.write(0, i, field)

        row = 0
        for transaction in data:
            row = 1
            col = 0
            for value in vars(transaction).values():
                if (type(value) != date):
                    worksheet.write(row, col, value)
                else:
                    worksheet.write(row, col, value.strftime('%Y-%m-%d'))
                col += 1
            row += 1
        
        workbook.close()
