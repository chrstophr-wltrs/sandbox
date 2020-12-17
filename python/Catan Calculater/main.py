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

_node_tile_offsets = {
    'NW': -0x21,
    'NE': +0x01,
    'S': -0x01,
    'SE': +0x10,
    'N': -0x10,
    'SW': -0x12 
}

tile_coord_to_id = {v: k for k, v in hx._tile_id_to_coord.items()}

class Tile:
    """
    Represents a land tile

    Attributes:
        location (hex): the hex location of the tile
        number (int): the number that triggers resource generation (2-12)
        value (int): (1-5) indicates how likely the number is to be rolled
        land (str): the resource that is generated when the number is rolled
    """

    def __init__(self, location, land):
        self.location = location
        self.land = land
        self.number = 0

    def place_token(self, num):
        """
        Places a number on the tile, and calculates the number's value.

        Parameters:
            num (int): the number to place on the tile (2-12)
        """ 
        self.number = num
        self.value = NUM_VALS[num]

class Node:
    """
    Node location, where a city/settlement can be placed. 

    Attributes:
        location (hex): the hex location of the node
        sum_score (int): the sum of the values for the numbers of the adjacent tiles
        avg_score (float): the average score for the values of the numbers of the adjacent tiles
        type (string): Y/spider, determines which tiles the node will reference to calculate its scores
    """

    def __init__(self, location, all_tiles):
        self.location = location
        if ((int(location) + 46) % 34) == 0:
            self.type = 'Y'
        else:
            self.type = 'spider'
    
    def calc_scores(self):
        """calculates the sum and average score, using the neighboring tiles"""
        if self.type in ["Y", "y"]:
            return ['NW', 'NE', 'S']
        else:
            return ['N', 'SW', 'SE']

class Board:
    """
    A board of tiles and numbers, 19 total tiles, and a number of nodes. 
    """
    pass


def main():
    if 0x55 in tile_coord_to_id:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()