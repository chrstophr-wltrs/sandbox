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
        self.all_cards = []
        while len(self.all_cards) < hand_size:
            card = rnd.choice(deck)
            deck.remove(card)
            self.all_cards.append(card)
        for card in self.all_cards:
            if card.value == "Wild":
                self.wilds.append(card)
            else:
                self.number_cards.append(card)
        self.number_cards.sort(key=lambda card: int(card.value))

    def check_for_value_set(self, size: int):
        """
        Checks for a set of a number of cards that have a matching value

        Args:
            size (int): the size (in cards) of the set
        """
        for i in self.number_cards:
            possible_set = []
            for j in self.number_cards:
                if i.value == j.value:
                    possible_set.append(j)
            card_count = len(possible_set)
            if card_count >= size - len(self.wilds):
                if card_count < size:
                    """
                    There's enough cards for a set IF
                    we use some wild cards
                    """
                    # Remove JUST enough wild cards to finish the set
                    for i in range(size - card_count):
                        self.wilds.pop()
                for card in possible_set:
                    self.number_cards.remove(card)
                return True
        return False

    def check_for_color_set(self, size: int):
        """
        Checks for a set of a number of cards that have a matching value

        Args:
            size (int): the size (in cards) of the set
        """
