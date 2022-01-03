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
        self.cards = []

    def set(self, cards: list[Card]):
        self.cards = cards
        return self

    def deal(self, deck: list[Card], hand_size: int = 10):
        self.__init__()
        while len(self.cards) < hand_size:
            card = rnd.choice(deck)
            if card not in self.cards:
                self.cards.append(card)
        self.cards.sort(key=lambda card: int(card.value))
        return self

    def find_set(self, size: int, is_color_set: bool = False):
        """
        Checks for a set of a number of cards that have a matching value or color

        Args:
            size (int): the size (in cards) of the set
            is_color_set (bool): If true, then the function searches for color sets
                if false, the function searches for value sets
        """
        for i in self.number_cards:
            possible_set = []
            for j in self.number_cards:
                match_flag = i.color == j.color if is_color_set else i.value == j.value
                if match_flag:
                    possible_set.append(j)
            if len(possible_set) >= size:
                # We only want to remove just
                # enough cards to complete the set
                while len(possible_set) > size:
                    possible_set.pop()
                for card in possible_set:
                    self.number_cards.remove(card)
                return True
        return False

    def find_run(self, size: int, color_restricted: bool = False):
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
            color_restricted (bool): whether the run should be restricted based on color
        """

        def find_next(
            current_card: Card,
            source_list: list[Card],
            color_resitricted: bool,
        ):
            pass

        return False
