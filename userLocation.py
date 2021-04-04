
class UserLocation(object):
    def __init__(self,zip):
        self.zip = zip
        self.lat = None
        self.long = None

    def convertZiptoCoordinates(self):
        #this method would convert a users zip code into latitude and longitude coordinates
        #to use for fetching the weather data. Hard coding the lat and long for the purposes of this project
        
        self.lat = 42.40815470
        self.long = 71.0594985
    

    