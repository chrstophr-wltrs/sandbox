import random as rnd

from Classes import *

rnd.seed()

COLORS = ["Red", "Green", "Blue", "Yellow"]

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "Wild"]

DUPLICATES = ["a", "b"]

deck = []


def make_deck():
    for i in range(4):
        deck.append(Card("Blue", "SKIP", i + 1))
    for i in COLORS:
        for j in NUMBERS:
            for k in DUPLICATES:
                deck.append(Card(i, j, k))

if __name__ == "__main__":
    print(int("1") < 2)
    # make_deck()
    # for i in range(5):
    # my_hand = draw_hand(10)
    # print(f"Hand {i+1}: {my_hand}")
