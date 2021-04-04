from userLocation import UserLocation
from userPreferences import UserPreferences

class User(object):
    def __init__(self,name, zip):
        self.name = name
        self.location = UserLocation(zip)
        self.preferences = UserPreferences()