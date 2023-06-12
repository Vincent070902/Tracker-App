from datetime import date
from tracker import SleepTracker
from actracker import activity_tracker
import matplotlib.pyplot as plt
import openpyxl as pyxl

# plt.plot(x,y)
# plt.show()
# #name age date hours quality dream
# name=input("What's your name? ")
# age=input("How old are you? ")
# hours=input("How long have you slept?(in hours) ")
# quality=input("How did you sleep sleep (Good, Bad or Mediocre) ")
# dream=input("Did you have a dream (Yes or No) ")
# st=SleepTracker(name,age,date.today(),hours,quality,dream)
# e_hours=input("How long you have spent on the activity?")
# what_did=input("What did you do?")
# feelings=input("How did you feel?")
# at=activity_tracker(e_hours,what_did,feelings)
# at.analyze_activity()
# st.data_store()
# at.data_store()
wb=pyxl.load_workbook("data.xlsx")
sheet=wb.active
print(sheet.max_row)
sl=[]
dt=[]
for i in range(1,sheet.max_row+1):
    sl.append(sheet["D"+str(i)].value)
    dt.append(i)
plt.plot(dt,sl)
plt.title("sleep hours")
plt.show()    

# import matplotlib
# import openpyxl as pyxl
# wb=pyxl.load_workbook("data.xlsx")
# sheet=wb.active
# for i in range(1,11):
#     index="A"+str(i)
#     sheet[index]="hello"
#     print(sheet[index].value)
# wb.save("data.xlsx")
