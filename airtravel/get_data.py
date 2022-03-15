import pandas as pd
from xlrd import open_workbook

book = open_workbook("./excel.xlsx")

for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "Expense Report" :
                print(sheet.name)
                print(colidx)
                print(rowidx)

