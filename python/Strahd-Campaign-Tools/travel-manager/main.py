from specialRolls import iRoll, sRoll
from encounterDictionaries import dayEncounters, nightEncounters
from math import ceil, floor

class timePeriod:
    def  __init__(self, vistGuide = False, isNight = False, areTravel = True, onRoad = True, recentEnc = 0, travelPace = "normal"):
        self.vistGuide = vistGuide # Are the players being guided by Vistani?
        self.isNight = isNight # Is it night time? 
        self.areTravel = areTravel # Are the players travelling, or camping?
        self.onRoad = onRoad # Are the players on/near the road, or in the wilderness?
        self.recentEnc = recentEnc # How many encounters have the players had in the last 12 hours?
        self.startEnc = recentEnc # How many encounters the players had before this time interval
        self.travelPace = travelPace # How quickly are the players travelling?

    def encounterRoll(self): # Rolls to determine which encounter occurs
        if self.vistGuide == True: # Players traveling with Vistani guides
            encRoll = sRoll('1d12')
        else: # Players traveling alone 
            encRoll = int(iRoll('1d12') + iRoll('1d8'))
        if self.areTravel == False: # Players are resting/camping
            if self.isNight == False: # Stationary during the day
                if encRoll not in [4,5,6,9,10,15]: # Not a travelling encounter
                    encRoll = str(encRoll)
                    self.recentEnc += 1 # Increases recent encounters
                    encounter = dayEncounters.get(encRoll) # Daytime Encounter
                    print("The players encounter " + encounter + ".") # Says what the players face
            else: # Stationary during the night
                if encRoll not in [3,4,5,6,7]: # Not a travelling encounter
                    encRoll = str(encRoll)
                    self.recentEnc += 1 # Increases recent encounters
                    encounter = nightEncounters.get(encRoll) # Nighttime Encounter
                    print("The players encounter " + encounter + ".") # Says what the players face
        else: # Players are travelling;  don't need to worry about specific encounters
            if self.isNight == False: # Travelling during day
                encRoll = str(encRoll)
                self.recentEnc += 1            
                encounter = dayEncounters.get(encRoll) # Daytime Encounter
                print("The players encounter " + encounter + ".") # Says what the players face
            else: # Travelling at night
                encRoll = str(encRoll)
                self.recentEnc += 1            
                encounter = nightEncounters.get(encRoll) # Nighttime Encounter
                print("The players encounter " + encounter + ".") # Says what the players face

    def encounterCheck(self): # Checks to see if players have a random encounter
        if self.recentEnc < 2: # Checks to see if players have already had many recent random encounters
            procRoll = iRoll('1d20')
            if self.onRoad == True: # Players are travelling on, or resting by, the road
                if procRoll >= 18: 
                    self.encounterRoll()
            else: # Players are travelling or resting in the wilderness
                if procRoll >= 15:                              
                    self.encounterRoll()
        self.recentEnc -= float(1/24) # Decreases the recentEnc points, as time passes

    def timeCheck(self): # Gauges how long the players are in the forest
        if self.isNight == False:
            time = "day"
        else:
            time = "night"
        if self.areTravel == True:
            self.forestTime = float(input("Distance travelled during the " + time + " (in miles): ")) # Players are travelling, asks for input in miles
            travelPace = str(input("How fast are the players travelling (s/n/f): ")) # Travel pace, slow/normal/fast
            if travelPace in ["fast","Fast","f","F"]:
                travelCap = float(30) # Distance (in miles) the party can travel in a day
                travelRate = float(4) # The miles travelled per hour
                travelDay = float(7.5) # The maximum number of hours the players can travel at this pace
            elif travelPace in ["slow","Slow","s","S"]:
                travelCap = float(18) # Distance (in miles) the party can travel in a day
                travelRate = float(2) # The miles travelled per hour
                travelDay = float(9) # The maximum number of hours the players can travel at this pacea
            else:
                travelCap = float(24) # Distance (in miles) the party can travel in a day
                travelRate = float(3) # The miles travelled per hour 
                travelDay = float(8) # The maximum number of hours the players can travel at this pace
            if self.forestTime > travelCap: #They are trying to travel too far for their pace, and risk exhausting themselves. 
                marchHours = float((self.forestTime / travelRate) - travelDay)
                print("The players won't be able to travel that far in a normal day.")
                print("They'd need to travel " + str(ceil(marchHours)) + " hours beyond the normal " + str(travelDay) + " to travel that far.")
                marchCheck = input("Do the players choose to continue travelling, even though they might suffer exhaustion? (y/n)")
                if marchCheck in ["True","true","y","Y","yes","Yes",True]: #Players choose to continue and risk exhaustion
                    exhaustDC = 11 #starting exhaustion DC
                    for change in range(ceil(marchHours)):
                        print("The players make a DC " + str(exhaustDC) + " CON save.")
                        exhaustDC += 1 #increases exhaust DC for next hour
                    self.forestTime = int(floor(travelDay + marchHours))
                else: #Players choose to forgo exhaustion and just travel the max for their pace
                    self.forestTime = int(travelDay)
            else: 
                self.forestTime = int(round(self.forestTime / travelRate)) # Players don't face exhaustion, they're traveling a normal distance
                        
        else:
            self.forestTime = int(input("Time spent resting during the " + time + " (in hours): ")) * 2 # Players are resting, don't need to check miles, just hours
        self.forestTime = round(self.forestTime * 2/3) # Changed encounter chunks to be 1.5 hours instead of .5 hours, for both resting and travelling
        for change in range(int(self.forestTime)): 
            self.encounterCheck()
        if self.recentEnc <= self.startEnc: # No encounters occurred
            print("The time passes uneventfully.")
