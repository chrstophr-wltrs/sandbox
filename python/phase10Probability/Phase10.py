import random as rnd

from Classes import *

rnd.seed()

colors = ["Red", "Green", "Blue", "Yellow"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "Wild"]

duplicates = ["a", "b"]

deck = []


def make_deck():
    for i in range(4):
        deck.append(Card("Blue", "SKIP", i))
    for i in colors:
        for j in numbers:
            for k in duplicates:
                deck.append(Card(i, j, k))


def draw_hand(hand_size: int):
    counter = 0
    hand = []
    while counter < hand_size:
        card = rnd.choice(deck)
        deck.remove(card)
        hand.append(card)
        counter += 1
    return hand


def check_for_sets(hand: list, set_size: int, number_of_sets: int = 1):
    set_count = 0
    working_hand = hand.copy()
    for i in hand:
        if i.value != "Wild":
            counter = 0
            for j in working_hand:
                if (i.value == j.value) or (j.value == "Wild"):
                    counter += 1
                    working_hand.remove(j)
            set_count += 1 if counter >= set_size else 0
        if set_count >= number_of_sets:
            return True
    return False


if __name__ == "__main__":
    print(int("1") < 2)
    # make_deck()
    # for i in range(5):
    # my_hand = draw_hand(10)
    # print(f"Hand {i+1}: {my_hand}")
