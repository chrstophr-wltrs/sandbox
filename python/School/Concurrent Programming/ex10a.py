import subprocess
import random as rnd
rnd.seed()

class FlagSnatcher:
    """
    A class using cURL to download flags from the CIA website.
    
    Attributes:
        url_base (str): the base string of the URL where all of the flags are located (def = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/')
        flag_file (str): the name of the file where the flag codes are stored (def = 'flags.txt')
        loaded_bytes (int): the number of bytes that have been downloaded by the snatcher
    """

    def __init__(self, flag_url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/', flag_file = 'flags.txt'):
        """Reads in the file of flag codes, and chooses 10 random codes for download purposes."""
        self.url_base = flag_url
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
    
    def download_flags(self, img_suffix = "-lgflag.gif"):
        """
        Downloads the flag files from CIA website using flag_url, the flag code, and img_suffix.
        
        Parameters:
            img_suffix (str): the text appended after the flag code to form the full URL, leading to the flag image file (def = "-lgflag.gif")
        """
        loaded_bytes = 0
        print("Beginning download of the chosen flags...")
        for code in self.chosen_flags:
            full_url = (f"{self.url_base}{code}{img_suffix}")
            print(f"Downloading {code.upper()} flag...")
            downloaded_flag = subprocess.check_output(f"curl -o {code}.gif {full_url}", shell=True, stderr=open('NUL'))
            flag_bytes = len(downloaded_flag)
            print(f"Successfully saved {code.upper()} flag ({flag_bytes} bytes) to {code}.gif")
            loaded_bytes += flag_bytes
        print("Successfully downloaded all flags!")
        print(f"Total bytes downloaded: {loaded_bytes}")


def main():
    snatcher = FlagSnatcher()
    snatcher.download_flags()

if __name__ == "__main__":
    main()