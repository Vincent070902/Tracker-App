import matplotlib
import openpyxl as pyxl


class SleepTracker:
    def __init__(self,user,age,date,hours,quality,dream,weather):
        self.user=user
        self.age=age
        self.date=date
        self.hours=hours
        self.quality=quality
        self.dream=dream
        self.weather=weather
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
    def data_store(self):
        wb=pyxl.load_workbook("data.xlsx")
        sheet=wb.active
        i=1
        while True:
            if sheet["A"+str(i)].value==None:
                sheet["A"+str(i)]=self.date
                sheet["B"+str(i)]=self.user
                sheet["C"+str(i)]=self.age
                sheet["D"+str(i)]=self.hours
                sheet["E"+str(i)]=self.quality
                sheet["F"+str(i)]=self.dream
                sheet["K"+str(i)]=self.weather
                wb.save("data.xlsx")
                break
            else:
                i+=1
            