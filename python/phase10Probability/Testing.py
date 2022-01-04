import random as rnd
from pickle import dump, load

from Classes import *

rnd.seed()

COLORS = ["Red", "Green", "Blue", "Yellow"]

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

DUPLICATES = ["a", "b"]

deck = []


def make_deck():
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
    make_deck()
    test_amounts = [1000000, 10000000, 25000000, 50000000, 100000000]
    for amount in test_amounts:
        hand_list = []
        for i in range(amount):
            hand_list.append(Hand().deal(deck))
        with open(f"test_hands_{amount / 1000000}mill.pickle", "wb") as file:
            dump(hand_list, file)
