from specialRolls import sRoll, iRoll # Allows D&D dice notation (1d6, 2d4, etc)

def ravens():
    if iRoll('1d2') == 1:
        return (sRoll('1d4') + " swarms of ravens")
    else:
        return "a wereraven"

dayEncounters = { #The possible encounters during the day; each iten corresponds to an entry in my notes
    "2": sRoll('3d6') + " Barovian commoners",
    "3": sRoll('1d6') + " Barovian scouts",
    "4": "a Hunting trap",
    "5": "a Grave",
    "6": "a False trail",
    "7": str(iRoll('1d4') + 1)  + " Vistani bandits",
    "8": "a Skeletal rider",
    "9": "a Trinket",
    "10": "a Hidden bundle", 
    "11": ravens(),
    "12": sRoll('1d6') + " dire wolves",
    "13": sRoll('3d6') + " wolves",
    "14": sRoll('1d4') + " berserkers",
    "15": "a corpse",
    "16": sRoll('1d6') + " werewolves in human form",
    "17": "a druid with " + sRoll('2d6') + " twig blights",
    "18": sRoll('2d4') + " needle blights",
    "19": sRoll('1d6') + " scarecrows",
    "20": "a revenant"
}

nightEncounters = { # The possible encounters during the night
"2": "a ghost",
"3": "a Hunting trap",
"4": "a Grave",
"5": "a Trinket",
"6": "a Corpse",
"7": "a Hidden bundle",
"8": "a Skeletal rider",
"9": sRoll('1d8') + " swarm of bats",
"10": sRoll('1d6') + " dire wolves",
"11": sRoll('3d6') + " wolves",
"12": sRoll('1d4') + " berserkers",
"13": "a druid and " + sRoll('2d6') + " twig blights",
"14": sRoll('2d4') + " needle blights",
"15": sRoll('1d6') + " werewolves in wolf form",
"16": sRoll('3d6') + " zombies",
"17": sRoll('1d6') + " scarecrows",
"18": sRoll('1d8') + " Strahd zombies",
"19": "a will-o’-wisp",
"20": "a revenant",
}
