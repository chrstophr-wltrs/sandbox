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
            Card("Red", "4", "a"),
            Card("Red", "4", "a"),
            Card("Red", "7", "b"),
            Card("Yellow", "3", "a"),
            Card("Yellow", "1", "a"),
            Card("Green", "12", "b"),
            Card("Green", "11", "b"),
            Card("Blue", "11", "a"),
            Card("Blue", "Wild", "b"),
            Card("Green", "Wild", "a"),
        ]
    ),
    Hand().set(
        [
            Card("Red", "4", "a"),
            Card("Red", "4", "a"),
            Card("Red", "4", "b"),
            Card("Yellow", "3", "a"),
            Card("Yellow", "1", "a"),
            Card("Green", "12", "b"),
            Card("Green", "11", "b"),
            Card("Blue", "11", "a"),
            Card("Blue", "5", "b"),
            Card("Green", "9", "a"),
        ]
    ),
]

if __name__ == "__main__":
    print(f"Test Hand 2:")
    print(f"\tColor Test 1: {test_hands[0].check_for_color_set(3)}")
    print(f"\tColor Test 2: {test_hands[0].check_for_color_set(4)}")
