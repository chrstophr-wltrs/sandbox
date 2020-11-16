import subprocess
import random as rnd
rnd.seed()

class FlagSnatcher:
    """
    A class using cURL to download flags from the CIA website.
    
    Attributes:
        flag_url (str): the base string of the URL where all of the flags are located (def = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/')
        flag_file (str): the name of the file where the flag codes are stored (def = 'flags.txt')
    """

    def __init__(self, flag_url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/', flag_file = 'flags.txt'):
        """Reads in the file of flag codes, and chooses 10 random codes for download purposes."""
        self.flag_url = flag_url
        self.all_flags = []
        print(f"Created flag snatcher!")
        print(f"Reading flag codes from {flag_file}...")
        with open(flag_file, 'r') as file:
            for line in file:
                flag_code = line.strip().lower()
                self.all_flags.append(flag_code)
        print(f"Successfully imported all flag codes from {flag_file}")
        print(f"Choosing 10 random codes for exercise...")
        self.chosen_flags = rnd.sample(self.all_flags, 10)
        print(f"The chosen flag codes are {self.chosen_flags}")

def main():
    snatcher = FlagSnatcher()

if __name__ == "__main__":
    main()