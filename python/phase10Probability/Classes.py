class Card:
    def __init__(self, color, value, duplicate):
        self.color = color
        self.value = value
        self.duplicate = duplicate

    def __str__(self):
        return f"{self.color}-{self.value}"


class Hand:
    def __init__(self):
        pass
