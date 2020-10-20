from breezypythongui import EasyFrame
import bookrecs

class BooksGui(EasyFrame):
    def __init__(self):
        """Sets up the window, label, and buttons"""
        EasyFrame.__init__(self, title="Book Recommendation GUI")

        # Adds the buttons
        self.addButton(text="Friends", row=0, column=0, command=self.friends)
        self.addButton(text="Recommend", row=0, column=1, command=self.recommend)
        self.addButton(text="Report", row=0, column=2, command=self.report)
    
    def friends(self):
        """Prompts user for a reader, then finds
        and prints the friends of that reader."""
        pass

    def recommend(self):
        """Prompts user for a reader, then recommends
        books for that reader based on their friends."""
        pass

    def report(self):
        """Generates book recommendations for every user."""
        pass