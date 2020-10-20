from breezypythongui import EasyFrame
import bookrecs

class BooksGui(EasyFrame):
    def __init__(self):
        """Sets up the window, label, and buttons"""
        EasyFrame.__init__(self, title="Book Recommendation GUI")

        