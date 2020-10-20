from specialRolls import iRoll, sRoll
import dice

def advRoll():
    return max(dice.roll('2d20'))

def disadvRoll():
    return min(dice.roll('2d20'))

class character:
    def __init__(self, charName = "", initial = "", modifier = 0, adv = False, disadv = False):
        self.charName = charName # The character's full first name
        self.initial = initial # The Initial to signify the character, the first letter of the character's name
        self.modifier = modifier # The character's perception modifier (positive or negative)
        self.adv = adv # Whether or not the character has advantage
        self.disadv = disadv # Whether or not the character has disadvantage
    
    def characterPerceptionRoll(self): 
        if self.adv == True and self.disadv == True: # Accidentally gave a character advantage AND disadvantage, so the two cancel out
            self.adv == False # Disadvantage cancels out advantage
            self.disadv == False # Advantage cancels out the disadvantage
        if self.adv == True: # Character has advantage
            self.percRoll = int(advRoll()) +  self.modifier
        elif self.disadv == True: # Character has disadvantage
            self.percRoll = int(disadvRoll()) + self.modifier
        else: # Just a straight-across perception roll 
            self.percRoll = iRoll('1d20') + self.modifier
        
    def perceptionDCcheck(self, perceptionDC):
        if self.percRoll >= perceptionDC:
            print(self.charName + " perceived something!")
            return 1
        return 0

ashe = character("Ashe", "a", 0)
charles = character("Charles", "c", 3)
selamin = character("Selamin", "s", 3)
vye = character("Vye", "v", 2)

playerParty = [ashe, charles, selamin, vye] # the party, which contains all of the characters

def advantagePrompt(): 
    charactersWithAdvantage = input("Which characters (if any) have advantage: ") # Prompts the user for which characters have advantage
    charactersWithDisadvantage = input("Which characters (if any) have disadvantage: ") # Prompts the user for which characters have advantage
    for character in playerParty:
        character.adv = character.initial in charactersWithAdvantage # Sets advantage for each character based on input
        character.disadv = character.initial in charactersWithDisadvantage # Sets disadvantage for each character based on input

def partyPerceptionCheck(): # Each iteration is referred to as a 'cycle'
    playerPerceptionTrigger = 0 # Resets the trigger count for this "cycle"
    perceptionDC = int(input("The DC of the Perception Check: ")) # Prompts for the DC for this "cycle"; the DC is supposed to persist for the entire cycle
    advantagePrompt() # Finds which characters have dis/advantage
    for character in playerParty: # Goes through each character 
        character.characterPerceptionRoll() # Determines the character's perception roll
        playerPerceptionTrigger += character.perceptionDCcheck(perceptionDC) # Compares the character's roll to the DC, and prints that they saw something or not
    if playerPerceptionTrigger == 0: # No one exceeded the DC
        print("No one perceived anything...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # A separator, to make it easier to read between cycles

while True: # Repeats the perception check until the command prompt is closed
    partyPerceptionCheck()