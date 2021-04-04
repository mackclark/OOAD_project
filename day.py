#import Hour

#day is array of hours

class Day(object):
    def __init__(self,date,today,hours):
        self.date = date
        self.isToday = today
        self.hours = hours
        