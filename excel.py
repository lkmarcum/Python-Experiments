import openpyxl
import os
os.chdir('c:\\users\\larry\\documents')

workbook = openpyxl.load_workbook('Excel_Test.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
print('A1 cell value: ' + cell.value)

rowCount = 1

for row in sheet:
    if row[0].value == "Name":
        sheet.delete_rows(rowCount)
    rowCount += 1

workbook.save('Excel_Test_Edited.xlsx')
