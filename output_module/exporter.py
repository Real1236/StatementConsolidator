from filter import Filter
import xlsxwriter
from datetime import date
from data_processing_module.statements.transaction import Transaction

def camel_to_title(camel_str):
    words = [camel_str[0].upper()]
    
    for c in camel_str[1:]:
        if c.isupper() or c.isdigit():
            words.append(' ')
        words.append(c)
    
    return ''.join(words)

class Exporter(Filter):
    def process(self, data: list[Transaction]) -> None:
        workbook = xlsxwriter.Workbook('SpendTracker.xlsx')
        worksheet = workbook.add_worksheet()

        blank_transaction = Transaction()
        header = list(vars(blank_transaction).keys())
        for i, field in enumerate(header):
            worksheet.write(0, i, camel_to_title(field))
            worksheet.set_column_pixels(i, i, 100 if "description" not in field else 200)
        worksheet.set_row(0, cell_format=workbook.add_format({'bold': True}))

        row = 1
        for transaction in data:
            col = 0
            for value in vars(transaction).values():
                if (type(value) != date):
                    worksheet.write(row, col, value)
                else:
                    worksheet.write_datetime(row, col, value, workbook.add_format({'num_format': 'yyyy-mm-dd'}))
                col += 1
            row += 1
        
        workbook.close()
