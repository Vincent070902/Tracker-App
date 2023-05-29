import matplotlib
import openpyxl as pyxl
# wb=pyxl.load_workbook("data.xlsx")
# sheet=wb.active
# for i in range(1,11):
#     index="A"+str(i)
#     sheet[index]="hello"
#     print(sheet[index].value)
# wb.save("data.xlsx")

class SleepTracker:
    def __init__(self,user,age,date,hours,quality,dream):
        self.user=user
        self.age=age
        self.date=date
        self.hours=hours
        self.quality=quality
        self.dream=dream
    def analyze_sleep(self):
        if self.age<5 and self.age>=3:
            if self.hours<=11 and self.hours>=10:
                return "right enough"
            if self.hours<10:
                return "not enough"
            if self.hours>11:
                return "too much"
        if self.age<12 and self.age>=5:
            if self.hours<=10 and self.hours>=9:
                return "right enough"
            if self.hours<9:
                return "not enough"
            if self.hours>10:
                return "too much"
        if self.age<18 and self.age>=12:
            if self.hours<=9 and self.hours>=8:
                return "right enough"
            if self.hours<8:
                return "not enough"
            if self.hours>9:
                return "too much"
        if self.age>=18:
            if self.hours<=8 and self.hours>=7:
                return "right enough"
            if self.hours<7:
                return "not enough"
            if self.hours>8:
                return "too much"