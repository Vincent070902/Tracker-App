from datetime import date
from tracker import SleepTracker
#name age date hours quality dream
name=input("What's your name? ")
age=input("How old are you? ")
hours=input("How long have you slept?(in hours) ")
quality=input("How did you sleep sleep (Good, Bad or Mediocre) ")
dream=input("Did you have a dream (Yes or No) ")
st=SleepTracker(name,age,date.today(),hours,quality,dream)
st.data_store()



# import matplotlib
# import openpyxl as pyxl
# wb=pyxl.load_workbook("data.xlsx")
# sheet=wb.active
# for i in range(1,11):
#     index="A"+str(i)
#     sheet[index]="hello"
#     print(sheet[index].value)
# wb.save("data.xlsx")
