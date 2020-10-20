from specialRolls import iRoll, sRoll
from math import ceil, floor
from encounterDictionaries import dayEncounters, nightEncounters

positiveInput = ["Y", "y", "yes", "Yes", "YES", "True", "true", True]

class randomEncounterPeriod:
    def __init__(self, partyHasGuides = False, timeIsNight = False, partyIsTravelling = True, partyByRoad = True, ):
        self.partyHasGuides = partyHasGuides # Is the group travelling with capable guides, such as Vistani or hunters?
        self.timeIsNight = timeIsNight # Is the encounter check happening during the day, or during night? 
        self.partyIsTravelling = partyIsTravelling # Is the group travelling or resting? 
        self.partyByRoad = partyByRoad # Is the group by/on a road, or in the wilderness? 
        self.recentEncounters = 0 # How many recent encounters have the players had?
        self.chunksSinceLastEncounter = 24 # How long has it been since the group's last encounter?
        self.encounterTime = 0 # How much time are the players at risk for an encounter?

    def userInput(self, infoCheckInstance):
        if infoCheckInstance == 0: # First time getting information for this session
            self.partyHasGuides = input("Is the group travelling with capable guides? ") in positiveInput
            self.partyByRoad = input("Is the group travelling on or by the road? ") in positiveInput
            pass
        elif infoCheckInstance != 0 and input("Has anything regarding the player's circumstances changed? ") in positiveInput: # Group circumstances have changed, getting info again
            self.partyHasGuides = input("Is the group travelling with capable guides? ") in positiveInput
            self.partyByRoad = input("Is the group travelling on or by the road? ") in positiveInput
            pass
        self.partyIsTravelling = input("Is the group travelling? ") in positiveInput # Determines group travelling status
        if self.partyIsTravelling == True: # Sets a string for other prompts
            partyActivity = "travelling"
            pass
        else:
            partyActivity = "resting"
            pass
        self.timeIsNight = input("Will the group be " + partyActivity + " during the night? ") in positiveInput # Time of when for when the group is travelling
    
    def convertMilesToEncounterHours(self): # Group is travelling, take input in miles instead of hours, then convert miles to hours
        travelPace = input("How quickly is the group travelling? (s/n/f) ") # The conversion rate differs depending on how quickly the group is travelling
        if travelPace in ["s", "S", "slow", "Slow", "SLOW"]:
            milesPerHour = float(2)
            maximumMilesPerDay = float(18)
            hoursInTravelDay = float(9)
            pass
        elif travelPace in ["f", "F", "fast", "Fast", "FAST"]:
            milesPerHour = float(4)
            maximumMilesPerDay = float(30)
            hoursInTravelDay = float(7.5)
            pass
        else:
            milesPerHour = float(3)
            maximumMilesPerDay = float(24)
            hoursInTravelDay = float(8)
            pass
        milesAlreadyTravelledToday = float(input("How many miles has the group already travelled today? ")) # How far the group has already travelled
        milesLeftToday = maximumMilesPerDay - milesAlreadyTravelledToday # The miles the group can travel today before risking exhaustion
        hoursLeftToday = hoursInTravelDay - (milesAlreadyTravelledToday / milesPerHour) # The number of hours during which the group can safely travel
        desiredTravelMiles = float(input("How far does the group wish to travel (in miles): ")) # Gets desired travel miles from user
        if desiredTravelMiles > milesLeftToday: # desired miles is greater than what they could safely travel 
            forcedMarchHours = int(round((desiredTravelMiles / milesPerHour) - hoursLeftToday)) # The number of hours they would need to continue travelling in order to meet their goal
            print("The players will not be able to travel that far with the remaining time they have today.")
            print("They would need to travel",forcedMarchHours,"additional hours beyond the",floor(hoursLeftToday),"they have left.")
            print("They can choose to continue, but there's a risk that they will suffer exhaustion.")
            if input("Do the players choose to continue? ") in positiveInput: # Group chooses to continue, risking exhaustion
                exhaustionDC = 10
                for i in range(forcedMarchHours): # The saves to determine whether the players suffer exhaustion
                    print("The characters make a DC",exhaustionDC,"Constitution saving throw, or suffer a level of exhaustion.")
                    exhaustionDC += 1
                self.encounterTime = round(desiredTravelMiles / milesPerHour) # Determines encounter hours based on desired travel time and travel rate
                pass
            else: # group chooses to stop after the safe maximum distance
                print("The players travel",milesLeftToday,"miles, leaving",str(desiredTravelMiles - milesLeftToday),"miles to be travelled tomorrow.") # Group has a distance left over to travel tomorrow
                self.encounterTime = round(milesLeftToday / milesPerHour)
                pass
            pass
        else:
            self.encounterTime = round(desiredTravelMiles / milesPerHour) # Group doesn't need to deal with exhaustion, encounters hours process as normal
            pass
    
    def determineEncounterHours(self): # Determines how long the group is at risk for an encounter
        if self.timeIsNight == True:
            dayNightCycle = "night"
            pass
        else:
            dayNightCycle = "day"
            pass
        if self.partyIsTravelling == True:
            self.convertMilesToEncounterHours()
            pass
        else:
            self.encounterTime = input("Hours spent resting during the",dayNightCycle,": ")
            pass
    
    def checkForEncounters(self): # Takes encounter hours and checks each "chunk" to see if an encounter occurs
        encountersHaveOccurred = False # No encounters have occured yet for this time
        for i in range(int(round(int(self.encounterTime) * 2 / 3))): # I actually want to check for encounters each hour and a half, not each hour itself
            encounterCheckRoll = iRoll('1d20') # Rolls to determine whether an encounter happens
            if self.partyByRoad == False and self.recentEncounters < 2: # Encounters are more likely to occur in the wild than by the road
                encounterCheckBool = encounterCheckRoll > 14
                pass
            elif self.partyByRoad == True and self.recentEncounters < 2:
                encounterCheckBool = encounterCheckRoll > 17
                pass
            else:
                encounterCheckBool = False
                pass
            if encounterCheckBool == True: # An encounter has occurred! Time to see what that encounter is
                if self.partyHasGuides == True: # Travelling with guides means that the risks the group faces are significantly less dangerous
                    encounterTableRoll = sRoll('1d12')
                    pass
                else:
                    encounterTableRoll = sRoll('1d20')
                    pass
                if self.timeIsNight == True: # The encounters that occur during the day and the night are different
                    if (self.partyIsTravelling == False and int(encounterTableRoll) not in [3,4,5,6,7]) or (self.partyIsTravelling == True): # Certain encounters only occur if the group is travelling
                        actualEncounter = encounter = nightEncounters.get(encounterTableRoll)
                        self.recentEncounters += 1
                        print("The players encounter",actualEncounter,".")
                        encountersHaveOccurred = True
                        pass
                    else: # The encounter that occured was one that is only supposed to happen while travelling
                        pass
                    pass
                else: # Daytime encounters
                    if (self.partyIsTravelling == False and int(encounterTableRoll) not in [4,5,6,9,10,15]) or (self.partyIsTravelling == True): # certain encounters only occur while travelling
                        actualEncounter = encounter = nightEncounters.get(encounterTableRoll)
                        self.recentEncounters += 1
                        print("The players encounter",actualEncounter,".")
                        encountersHaveOccurred = True
                        pass
                    else: # party is resting and one of the travel-only encounters occured
                        pass
                    pass
                pass
            else:
                pass
            self.chunksSinceLastEncounter -= 1 # After a certain number number of "chunks" have occured, the effective number of recent encounters goes down by one
            if self.chunksSinceLastEncounter <= 0: # Enough time has passed since the last encounter occured
                self.chunksSinceLastEancounter = 24 # Resets the number of "chunks"
                self.recentEncounters -= 1 # Lowers the number of "effective" recent encounters for determining whether or not an encounter occurs
                pass
            else:
                pass
        if encountersHaveOccurred == False: # No encounters have occurred
            print("The time passes uneventfully.")
            pass
        else: # Some encounters have occurred
            pass
        pass
    
currentTimeInstance = randomEncounterPeriod()

currentTimeInstance.userInput(0)
while True:
    currentTimeInstance.determineEncounterHours()
    currentTimeInstance.checkForEncounters()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    currentTimeInstance.userInput(1)