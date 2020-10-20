import dice

"""
dice is a critical library for the project, 
allowing the use of D&D (ie, passing in '2d6' to 
denote the addition of 2 rolls of six-sided dice). 
However, the function returns an array, 
with the rolls separated, which often isn't helpful.
"""

def iRoll(XdY): # Rolls dice, then adds them together by converting the array into a string
    return int(dice.roll(XdY))
                   
def sRoll(AdB): # does a iRoll, then converts the integer into a string that can be passeed into a dictionary or print statement
    return str(iRoll(AdB))