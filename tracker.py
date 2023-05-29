class SleepTracker:
    def __init__(self,user,age,date,hours,quality,dream):
        self.user=user
        self.age=age
        self.date=date
        self.hours=hours
        self.quality=quality
        self.dream=dream
    def analyze_sleep(self):
        self.hour