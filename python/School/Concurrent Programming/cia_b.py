import os
import requests as rq
import time
import concurrent.futures

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
        self.loaded_bytes = 0
        print(f"Created flag snatcher!")
        print(f"Reading flag codes from {flag_file}...")
        if os.path.isdir('cia_b') == False:
            os.mkdir('cia_b')
            print("Created sub-directory for flag output!")
        with open(flag_file, 'r') as file:
            for line in file:
                flag_code = line.strip().lower()
                self.all_flags.append(flag_code)
        print(f"Successfully imported all flag codes from {flag_file}")
    
    def download_flag(self, code):
        """
        Downloads the flag file from CIA website using flag_url, the flag code, and img_suffix, and increments loaded_bytes for final output

        Parameters:
            code (str): the two letter code of the country whose flag is being downloaded
        """
        full_url = (f"{self.url_base}{code}-lgflag.gif")
        print(f"Downloading {code.upper()} flag...")
        flag = rq.get(full_url)
        flag_bytes = len(flag.content)
        with open(f"cia_b/{code}.gif", 'wb') as file:
            file.write(flag.content)
        print(f"Successfully saved {code.upper()} flag ({flag_bytes} bytes) to {code}.gif")
        self.loaded_bytes += flag_bytes
    
    def download_all_flags(self):
        """Downloads all flag files from CIA website using flag_url, and the flag code, and increments loaded_bytes for final output"""
        print("Beginning download of all flags...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.download_flag, self.all_flags)
        print("Successfully downloaded all flags!")
        print(f"Total bytes downloaded: {self.loaded_bytes}")


def main():
    start = time.perf_counter()
    snatcher = FlagSnatcher()
    snatcher.download_all_flags()
    print(f"Finished function in {round(time.perf_counter() - start, 2)} seconds...")

if __name__ == "__main__":
    main()