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
        reader = self.prompterBox(title="Friends", promptString="Enter Reader Name: ", inputText="").strip().lower()
        try:
            self.messageBox(title=(f"Friends of {reader}"), message=bookrecs.friends(reader), width=50, height=3)
        except:
            self.messageBox(title="Error", message="No such reader.")

    def recommend(self):
        """Prompts user for a reader, then recommends
        books for that reader based on their friends."""
        reader = self.prompterBox(title="Recommendations", promptString="Enter Reader Name: ", inputText="").strip().lower()
        try:
            self.messageBox(title=(f"Recommendations for {reader}"), message=bookrecs.recommendations_list(reader), width=70, height=10)
        except:
            self.messageBox(title="Error", message="No such reader.")

    def report(self):
        """Generates book recommendations for every user."""
        self.messageBox(title="Report", message=bookrecs.report(), width=70, height=25)
        pass

if __name__ == "__main__":
    BooksGui().mainloop()