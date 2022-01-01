import random as rnd

rnd.seed()


class Card:
    def __init__(self, color, value, duplicate):
        self.color = color
        self.value = value if value == "Wild" else int(value)
        self.duplicate = duplicate

    def __str__(self):
        return f"{self.color}-{self.value}"

    def __repr__(self):
        return f"{self.color}-{self.value}"


class Hand:
    def __init__(self):
        self.number_cards = []
        self.wilds = []

    def set(self, cards: list[Card]):
        self.__init__()
        for card in cards:
            if card.value == "Wild":
                self.wilds.append(card)
            else:
                self.number_cards.append(card)
        return self

    def deal(self, deck: list[Card], hand_size: int = 10):
        self.__init__()
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
        self.number_cards.sort(key=lambda card: int(card.value))
        return self

    def value_set(self, size: int):
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
            if len(possible_set) >= size - len(self.wilds):
                # We only want to remove just
                # enough cards to complete the set
                while len(possible_set) > size:
                    possible_set.pop()
                while len(possible_set) < size:
                    # There's enough cards for a set IF
                    # we use some wild cards
                    # Remove JUST enough wild cards to finish the set
                    possible_set.append(self.wilds.pop())
                for card in possible_set:
                    if card in self.number_cards:
                        self.number_cards.remove(card)
                return True
        return False

    def color_set(self, size: int):
        """
        Checks for a set of a number of cards that have a matching color

        Args:
            size (int): the size (in cards) of the set
        """
        for i in self.number_cards:
            possible_set = []
            for j in self.number_cards:
                if i.color == j.color:
                    possible_set.append(j)
            if len(possible_set) >= size - len(self.wilds):
                # We only want to remove just
                # enough cards to complete the set
                while len(possible_set) > size:
                    possible_set.pop()
                while len(possible_set) < size:
                    # There's enough cards for a set IF
                    # we use some wild cards
                    # Remove JUST enough wild cards to finish the set
                    possible_set.append(self.wilds.pop())
                for card in possible_set:
                    if card in self.number_cards:
                        self.number_cards.remove(card)
                return True
        return False

    def run(self, size: int):
        """
        Checks for a continuous run of a given size
        A run is a group of cards withcontinuously ascending values
        Similar to a "straight" in poker
        For the purposes of phase 10, a run can "wrap around" to the beginning

        Example Runs:
        1, 2, 3, 4, 5
        10, 11, 12, 1, 2

        Args:
            size (int): the minimum size (in cards) of the run
        """

        return False
