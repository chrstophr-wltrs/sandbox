from random import random, seed
import dice
seed()
from sounds import softCons, midCons, vowels

# Rolls dice, then adds them together by converting the array into a
def iRoll(XdY):
    return int(dice.roll(XdY))

# performs an iRoll, then converts the integer into a string that can be passeed into a dictionary or print statement
def sRoll(AdB): 
    return str(iRoll(AdB))

class nameGenerator:
    def __init__(self, conSilentChance = .23, harshConChance = .50, softConChance =.20, begSecConChance = .34, endSecConChance = .34, syllables = 1):
        self.conSilentChance = conSilentChance # The chance (from 0 to 1) of a consonant sound being silent
        self.harshConChance = harshConChance # Chance for hard consonants like "k", "t"
        self.softConChance = softConChance # Chance for soft consonants like "f", "sh"
        self.begSecConChance = begSecConChance # Chance for a secondary consonant
        self.endSecConChance = endSecConChance # Chance for a secondary consonant
        self.syllables = syllables # The number of syllables in the word

    # checks with the user to determine how many syllables the name will have
    def userSyllables(self):
        self.syllables = int(input('How many syllables does the word have? '))
        pass
    
    def consonant(self, begin = False):
        harshConAdd = self.harshConChance + self.softConChance # Adds the chances together so we only need to do one roll to determine the consonant
        # Consonant is silent
        if random() <= self.conSilentChance:
            return " "
        # Consonant not silent
        else:
            consonantTypeRoll = random() # what type of consonant do we get?
            if consonantTypeRoll <= self.softConChance:
                return softCons.get(sRoll('1d15'))
                pass
            elif consonantTypeRoll > self.softConChance and consonantTypeRoll <= harshConAdd:
                if random() >= .500:
                    consonant = "t"
                    pass
                else:
                    consonant = "k"
                    pass
                pass
            else: 
                consonant = str(midCons.get(sRoll('1d4')))
                pass
            if (random() <= self.begSecConChance) and begin == True:
                secondaryConsonant = str(softCons.get(sRoll('1d15')))
                return str(consonant + " " + secondaryConsonant)
                pass
            elif (random() <= self.endSecConChance) and begin == False:
                secondaryConsonant = str(softCons.get(sRoll('1d15')))
                return str(secondaryConsonant + " " + consonant)
                pass
            else: 
                return str(consonant)
                pass
            pass
        pass

    def vowel(self):
        return vowels.get(sRoll('1d19'))
        pass

    def generateWord(self):
        word = ""
        self.userSyllables()
        for i in range (self.syllables - 1):
            word += self.consonant(True)
            word += " + "
            word += self.vowel()
            word += " + "
            word += self.consonant(False)
            word += " + "
        word += self.consonant(True)
        word += " + "
        word += self.vowel()
        word += " + "
        word += self.consonant(False)
        print(word)
        pass

humanName = nameGenerator(.32, .3, .4, .34, .35, 1)

humanName.generateWord()