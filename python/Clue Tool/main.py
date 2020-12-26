"""
A tool designed to aid in the notetaking for a specific method of playing the board game CLUE. 

Glossary:
    clue = a card, e.g. Mr Green, Knife, Conservatory
        suspect = e.g. Professor Plum, Colonel Mustard (NOTE: NOT the same as player)
        item = e.g. Candlestick, Revolver
        room = e.g. Balroom, Dining Room
    user = the player that's using the software
    player = OTHER players in the game
    clue_sheet = the user's information sheet, which contains all of the known information about their own hand, as well as all of the known information about the hands of the other players
    solution = 1 suspect, 1 item, 1 room; the user is trying to discover this information, by eliminating all other options 
"""

# These are just the default values from the original game. Ideally, the user will be able to input their own suspects, items, and rooms, but we'll start with these. 
DEFAULT_SUSPECTS = ('green', 'mustard', 'peacock', 'plum', 'scarlet', 'white')
DEFAULT_ROOMS = ("ballroom", "billiard", "conservatory", "dining", "hall", "kitchen", "library", "lounge", "study")
DEFAULT_ITEMS = ('candlestick', 'knife', 'pipe', 'revolver', 'rope', 'wrench')


# Just a handy tuple to handle text-based user input, to indentify multiple forms of "True" 
YES = ("y", "yes", "true", "t", True)

class Player():
    """
    One of the other players in the game. Initially, the user doesn't know what cards they have in their hand.
    
    Attributes:
        name(str): The name of the player
        clues(dict): A nested dictionary, containing all of the Clues, and the player's status for that clue. Statuses can be one of the following:
            None (default): There's no information regarding whether or not the player has this clue; represented as "( )"
            False: Player definitely does NOT have this clue; represented as "(-)"
            Possible (int): Player MIGHT have this clue, followed by the number of times they've disproven a suggestion which included this clue; represented as "(p#)" where # is the number of suggestions
            True: Player definitely DOES have this clue: represented as "(X)"
    """

    def __init__(self, name = ""):
        self.name = name
        self.clues = {}
        suspects = {}
        rooms = {}
        items = {}
        for i in DEFAULT_SUSPECTS:
            suspects[i] = None
        for i in DEFAULT_ITEMS:
            items[i] = None
        for i in DEFAULT_ROOMS:
            rooms[i] = None
        self.clues["suspects"] = suspects
        self.clues["rooms"] = rooms
        self.clues["items"] = items
    
    def __str__(self):
        return(f"Player: {self.name}")

    def suggest(self, suspect, room, item):
        """
        Proffers a suggestion regarding the player, setting what that player has, depending on the user's input. 

        Returns 1 if player could disprove suggestion
        Returns 0 if player could not refute suggestion
        Returns -1 if the user skips that player, for whatever reason
        
        Parameters:
            suspect (str): the suggested suspect
            room (str): the suggested room
            item (str): the suggested item
        """
        suggest_prompt = input(f"Can {self.name} disprove the suggestion? ")
        if suggest_prompt == "":
            return -1
        elif suggest_prompt in YES:
            # Check regarding the suspect
            pass
    
    def confirm(self, category, suggestion):
        """
        Eliminates some redundancy regarding updating the notes for each category of clues.
        
        Parameters:
            category (str): "suspects" or "rooms" or "items"
            suggestion (str): The suggested suspect/room/item
        """
        if self.clues[category][suggestion] == None:
            self.clues[category][suggestion] = "Possible 1"
        elif self.clues[category][suggestion].split(" ").lower()[0] == "possible":
            num = int(self.clues[category][suggestion].split(" ")[1])
            num += 1
            self.clues[category][suggestion] = f"Possible {num}"

    def take_confirmation_notes(self, suspect, room, item):
        """The notetaking process if a player is able to disprove a suggestion, should only be internally called from suggest()"""
        # Check to see if we already had information for this suggestion
        if (self.clues["suspects"][suspect] == True) or (self.clues["rooms"][room] == True) or (self.clues["items"][item] == True):
            print("We already knew that!")
            return

        # Set the status for the suspect
        



        


def main():
    Kate = Player("Kate")

if __name__ == "__main__":
    main()