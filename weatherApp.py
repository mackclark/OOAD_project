#
from weatherApiHelper import WeatherApiHelper
from weatherDataParser import WeatherData
from user import User
from recommendation import Recommendation
from textFormatting import TextFormatting

class WeatherApp():
    def __init__(self):
        pass
    
    #a reusable method for prompting the user for a response and formatting the prompt blue
    def promptUserForResponse(self, askText):
        formattedAskText = TextFormatting('BLUE', askText)
        response = input(formattedAskText.formattedTextString)
        return response

    #the main app method, this kicks off all of the logic of the app
    def runWeatherApp(self):
        greeting = TextFormatting('BLUE', "Hello! Welcome to Weather App. I'm going to tell you when the best time to take your dumb little walk is.")
        print(greeting.formattedTextString)
        #gets basic info from user
        name = self.promptUserForResponse("What's your name? ")
        zip = self.promptUserForResponse("What's your 4 digit zip code? ")

        #instantiates user class with user inputted values
        user = User(name,zip)
        user.location.convertZiptoCoordinates()

        self.getUserPreferences()
        #setting user preferences with hard coded values for now, this code is not fully written
        user.preferences.setPreferences(90, 30, 7, 10)

        #get weather data from weather API
        rawWeatherData = WeatherApiHelper(user.location)
        rawWeatherData.getWeatherData()

        if(rawWeatherData.response != None):
            #parse the hour by hour forecast into useful days 
            parsedWeatherData = WeatherData()
            parsedWeatherData.parseWeatherData(rawWeatherData.response['hourly'])

            #iterate through data to find best hours for going outdoors
            userRecommendations = []
            for n in range(len(parsedWeatherData.days)):
                weatherRecommendation = Recommendation()
                weatherRecommendation.analyzeWeather(parsedWeatherData.days[n].hours)
                userRecommendations.append(weatherRecommendation)

            #format the recommendations into a readable statement for the user
            for n in range(len(userRecommendations)):
                print(userRecommendations[n].textString)
        else:
            #if the weather api returns an error, the user will see this error message
            print('oops, looks like there was an error. Please try again later')



    def getUserPreferences(self):
        #ask user if they want to set additional preferences and then prompts for them 
        promptConsent = self.promptUserForResponse("Would you like to set some preferences so that we can give you better recommendations? yes/no ")

        if(promptConsent == 'yes'):
            print('Great! Answer the following questions so we get a better idea of what you like.')
            maxTemp = self.promptUserForResponse("In degrees fahrenheit, at what temperature is it too hot for you to want to go outside? ")
            minTemp = self.promptUserForResponse("In degrees fahrenheit, at what temperature is it too cold for you to want to go outside? ")
            wakeUpTime = self.promptUserForResponse("What time do you wake up in the morning? ")
            bedtime = self.promptUserForResponse("What time do you go to bed? ")
            return [maxTemp, minTemp, wakeUpTime, bedtime]
        if(promptConsent == 'no'):
            print('ok')


if __name__ == "__main__":
    mainApp = WeatherApp()
    mainApp.runWeatherApp()