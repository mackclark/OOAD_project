#GET weather data

import requests


class WeatherApiHelper():
    def __init__(self, location):
        self.url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + str(location.lat) + '&lon=' + str(location.long) + '&exclude=minutely&units=imperial&appid=df5f5d432a0b16123a61eea90ab43718'
        self.response = None
    def getWeatherData(self): 
        resp = requests.get(self.url)
        if resp.status_code != 200:
            print(resp.status_code)
        else:
            self.response = resp.json()
