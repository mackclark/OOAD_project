#import days
#parses data, returns array of days

from datetime import datetime
import pytz    
import tzlocal 
from hour import Hour
from day import Day

class WeatherData():
    def __init__(self):
        self.days = None

    def parseWeatherData(self, rawJson):
        hours = []
        dateRange = []
        
        #iterates over raw hourly data from weather API  
        for n in range(len(rawJson)):
            item = rawJson[n]
            itemWeather = item['weather'][0]
            utcTime, hourDate = self.parseDateTime(item['dt'])
            #compile array of dates for separating hours into the days they belong to
            if n == 0:
                dayDate = hourDate
                dateRange.append(dayDate)
            if hourDate != dayDate:
                dayDate = hourDate
                dateRange.append(dayDate)
            
            parsedHour = Hour(utcTime,hourDate,item['temp'],item['clouds'],item['wind_speed'],itemWeather['description'],itemWeather['id'])
            hours.append(parsedHour)
        
        #iterates over available dates to create Day objects and assign each Day its Hours
        days = []
        for n in range(len(dateRange)):
            dayHours = []
            for x in range(len(hours)):
                if hours[x].date == dateRange[n]:
                    dayHours.append(hours[x])
            days.append(Day(dateRange[n],n == 0,dayHours))

        self.days = days

    def parseDateTime(self, ts):
        ts = int(ts)
        # https://stackoverflow.com/a/32904812
        utcTime = datetime.utcfromtimestamp(ts).strftime('%H:%M')
        hourDate = datetime.utcfromtimestamp(ts).strftime('%a %m-%d')
        #utcTime = convertToLocalTime(utcTime)
        return (utcTime, hourDate)


    def convertToLocalTime(self, time):
        #ran out of time to get this to work, this would convert the time to the users local time

        #local_timezone = tzlocal.get_localzone() # get pytz tzinfo
        #TODO figure out why this timezone conversion isn't working
        #local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
        return
