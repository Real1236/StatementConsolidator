import os
import sys
import xlsxwriter.worksheet
from filter import Filter
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
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
        # Check if we are running as a frozen executable (e.g., packaged with PyInstaller)
        if getattr(sys, 'frozen', False):
            directory = os.path.dirname(sys.executable)
        else:
            directory = os.path.dirname(os.path.realpath(__file__)).replace("output_module", "resources")

        file_path = os.path.join(directory, 'SpendTracker.xlsx')
            
        workbook = xlsxwriter.Workbook(file_path)
        workbook.set_size(1500, 1000)
        transactionsWorksheet = workbook.add_worksheet(name="Transactions")
        monthlySummaryWorksheet = workbook.add_worksheet(name="Summary")

        self.createHeaders(workbook, transactionsWorksheet)
        self.recordTransactions(data, workbook, transactionsWorksheet)
        self.createSummarySheet(workbook, monthlySummaryWorksheet)
        
        workbook.close()

    def createHeaders(self, workbook, worksheet):
        blank_transaction = Transaction()
        header = list(vars(blank_transaction).keys())
        for i, field in enumerate(header):
            worksheet.write_string(0, i, camel_to_title(field))
            worksheet.set_column_pixels(i, i, 100 if "description" not in field else 200)
        worksheet.set_row(0, cell_format=workbook.add_format({'bold': True}))

    def recordTransactions(self, data: list[Transaction], workbook, worksheet):
        row = 1
        for transaction in data:
            col = 0
            for value in vars(transaction).values():
                if (type(value) == str):
                    worksheet.write_string(row, col, value)
                elif (type(value) == date):
                    worksheet.write_datetime(row, col, value, workbook.add_format({'num_format': 'yyyy-mm-dd'}))
                else:
                    worksheet.write_number(row, col, value)
                col += 1
            row += 1

    def createSummarySheet(self, workbook, worksheet):
        # Headers
        headers = ["Month", "Recreation", "Grocery", "Eating Out", "Transportation", "Shopping", "Miscellaneous", "One Time", "Total"]
        for i, header in enumerate(headers):
            worksheet.write_string(0, i, header)
            worksheet.set_column_pixels(i, i, 100)
        worksheet.set_row(0, cell_format=workbook.add_format({'bold': True}))

        # Summary
        for month in range(1, 13):
            monthCell = xl_rowcol_to_cell(month, 0)
            nextMonthCell = xl_rowcol_to_cell(month + 1, 0)
            worksheet.write_number(month, 0, month)
            for i in range(1, 8):
                headerCell = xl_rowcol_to_cell(0, i)
                worksheet.write_formula(month, i,
                    f"""=-SUMIFS(
                    Transactions!$F:$F,
                    Transactions!$C:$C, ">="&DATE(2024,{monthCell},1),
                    Transactions!$C:$C, "<"&DATE(2024,{nextMonthCell},1),
                    Transactions!$G:$G, {headerCell}
                    )
                    +SUMIFS(
                    Transactions!$F:$F,
                    Transactions!$C:$C, ">="&DATE(2024,{monthCell},1),
                    Transactions!$C:$C, "<"&DATE(2024,{nextMonthCell},1),
                    Transactions!$H:$H, "Naomi",
                    Transactions!$G:$G, {headerCell}
                    )/2
                    +SUMIFS(
                    Transactions!$F:$F,
                    Transactions!$C:$C, ">="&DATE(2024,{monthCell},1),
                    Transactions!$C:$C, "<"&DATE(2024,{nextMonthCell},1),
                    Transactions!$H:$H, "Mom",
                    Transactions!$G:$G, {headerCell})"""
                )
            worksheet.write_formula(month, 8, f"=SUM({xl_rowcol_to_cell(month, 1)}:{xl_rowcol_to_cell(month, 7)})")

            # Include 13 just for formula purposes, hidden in white
            worksheet.write_number(13, 0, 13, workbook.add_format({'font_color': '#FFFFFF'}))

