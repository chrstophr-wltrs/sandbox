import hexgrid as hx
import random as rnd

LAND_DECK = ('brick', 'brick', 'brick', 'desert', 'ore', 'ore', 'ore', 'sheep', 'sheep', 'sheep','sheep', 'wheat', 'wheat', 'wheat', 'wheat', 'wood', 'wood','wood','wood')

NUM_TOKENS = (5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11)

NUM_VALS = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}

class Tile:
    """
    Represents a land tile

    Attributes:
        location (hex): the hex location of the tile
        number (int): the number that triggers resource generation (1-12)
        value (int): (1-5) indicates how likely the number is to be rolled
        land (str): the resource that is generated when the number is rolled 
    """

def main():
    pass

if __name__ == "__main__":
    main()