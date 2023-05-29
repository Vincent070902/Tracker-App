import matplotlib
import openpyxl as pyxl
wb=pyxl.load_workbook("data.xlsx")
sheet=wb.active
for i in range(1,11):
    index="A"+str(i)
    sheet[index]="hello"
    print(sheet[index].value)
wb.save("data.xlsx")
