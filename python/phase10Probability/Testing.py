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


test_hands = [
    Hand().set(
        [
            Card("Red", "3", "a"),
            Card("Red", "4", "b"),
            Card("Yellow", "4", "b"),
            Card("Yellow", "6", "a"),
            Card("Green", "6", "a"),
            Card("Green", "10", "b"),
            Card("Green", "12", "b"),
            Card("Blue", "12", "a"),
            Card("Blue", "8", "b"),
            Card("Green", "9", "a"),
        ]
    ),
    Hand().set(
        [
            Card("Red", "1", "a"),
            Card("Red", "4", "a"),
            Card("Red", "6", "b"),
            Card("Yellow", "7", "a"),
            Card("Yellow", "7", "a"),
            Card("Green", "10", "b"),
            Card("Green", "10", "a"),
            Card("Blue", "11", "a"),
            Card("Blue", "12", "b"),
            Card("Green", "12", "a"),
        ]
    ),
]

if __name__ == "__main__":
    print(f"Test Hand 1:")
    print(f"\tValue Test 1: {test_hands[1].find_run(4)}")
    print(f"\tValue Test 2: {test_hands[1].find_set(3)}")
