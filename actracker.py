import matplotlib
import openpyxl as pyxl
#feedback_health_status
#feedback_exercise_amount
l=["badminton","soccer","basketball","ski","football","handball","walk","run","anaerobic","volleyball","exercise","tennis"]
class activity_tracker:
    def __init__(self,e_hours,what_did,feeling):
        self.e_hours=e_hours
        self.what_did=what_did
        self.feeling=feeling
        self.did_exercise=False
    def analyze_activity(self):
        for i in l:
            if i in self.what_did.lower():
                self.did_exercise=True

    def data_store(self):
        wb=pyxl.load_workbook("data.xlsx")
        sheet=wb.active
        i=1
        while True:
            if sheet["G"+str(i)].value==None:
                sheet["G"+str(i)]=self.e_hours
                sheet["H"+str(i)]=self.what_did
                sheet["I"+str(i)]=self.feeling
                sheet["J"+str(i)]=self.did_exercise
                wb.save("data.xlsx")
                break
            else:
                i+=1