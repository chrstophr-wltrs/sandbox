import random as rnd
rnd.seed()

class Card:
    def __init__(self, color, value, duplicate):
        self.color = color
        self.value = value
        self.duplicate = duplicate

    def __str__(self):
        return f"{self.color}-{self.value}"


class Hand:
    def __init__(self, deck: list[Card], hand_size: int = 10):
        self.number_cards = []
        self.wilds = []
        hand = []
        while len(hand) < hand_size:
            card = rnd.choice(deck)
            deck.remove(card)
            hand.append(card)
        for card in hand:
            if card.value == "Wild":
                self.wilds.append(card)
            else:
                self.number_cards.append(card)
