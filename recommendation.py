

from textFormatting import TextFormatting

class Recommendation():
    def __init__(self):
        self.hour = None
        self.textString = None

    def analyzeWeather(self, hours):
        #parses the passed list of hours and chooses the one with the highest temperature to recommend
        #a fuller version of the app would have more complex criteria for choosing the 'best' hour, not just high temp
        bestHour = 0
        for n in range(len(hours)):
            if n == 0:
                highTemp = hours[n].temp
            if hours[n].temp > highTemp:
                highTemp = hours[n].temp
                bestHour = n

        self.hour = hours[bestHour]
        self.formatRecommendation(hours[bestHour])
    
    def formatRecommendation(self, recommendedHour):
        #makes the recommendation user readable
        dateString = TextFormatting('BOLD', recommendedHour.date)
        formattedRecommendation = dateString.formattedTextString + ": The best time for you to go outside on this day is " + recommendedHour.time + ". The weather will be " + recommendedHour.weatherDescription + " and the temperature will be " + str(recommendedHour.temp) + " degrees fahrenheit."

        self.textString = formattedRecommendation