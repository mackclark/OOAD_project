
class UserPreferences(object):
    def __init__(self):
        self.maxTemp = None
        self.minTemp = None
        self.wakeUpTime = None 
        self.bedtime = None
    
    def setPreferences(self, max, min, wakeup, bedtime):
        self.maxTemp = max
        self.minTemp = min
        self.wakeUpTime = wakeup 
        self.bedtime = bedtime
    

    