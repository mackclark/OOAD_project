#temp
#precipitation
#daylight


class Hour(object):
    def __init__(self,time,date,temp,clouds,windSpeed,description,weatherCode):
        self.time = time
        self.date = date
        self.temp = temp
        self.clouds = clouds
        self.windSpeed = windSpeed
        self.weatherDescription = description
        self.weatherCode = weatherCode
