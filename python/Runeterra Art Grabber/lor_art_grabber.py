import os
import requests as rq
import concurrent.futures
from PIL import Image

region_list = ['BW', 'DE', 'FR', 'IO', 'MT', 'NX', 'PZ', 'SI']

class ImageSnatcher:
    """
    A class using requests to download images from a website.
    
    Attributes:
        url_base (str): the base string of the URL where all of the flags are located (def = 'https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02')
        flag_file (str): the name of the file where the flag codes are stored (def = 'flags.txt')
        loaded_bytes (int): the number of bytes that have been downloaded by the snatcher
    """

    def __init__(self, img_front  = 'https://cdn-lor.mobalytics.gg/production/images/set', card_set = 2):
        """Reads in the file of flag codes, and chooses 10 random codes for download purposes."""
        self.card_set = card_set
        self.url_base = (f"{img_front}{card_set}/en_us/img/card/game/0{card_set}")
        print(f"Created image snatcher!")
        self.all_codes = []
        if os.path.isdir(f'set_{card_set}') == False:
            os.mkdir(f'set_{card_set}')
            print(f"Created sub-directory '/set_{card_set}' for image output!")
    
    def download_image(self, code):
        """
        Downloads the image file from target website using the base_url, and the codes in code_list

        Parameters:
            code (str): the two letter code of the country whose flag is being downloaded
        """
        full_url = (f"{self.url_base}{code}-lgflag.gif")
        print(f"Downloading {code.upper()} flag...")
        flag = rq.get(full_url)
        flag_bytes = len(flag.content)
        with open(f"set_{self.card_set}/{code}.png", 'wb') as file:
            file.write(flag.content)
        print(f"Successfully saved {code.upper()} flag ({flag_bytes} bytes) to {code}.gif")
    
    def find_cards(self):
        """
        Finds all valid card combinations for this set

        Returns valid_cards list
        """
        self.valid_cards = []
        for reg in region_list:
            pass

    
    def download_all_flags(self):
        """Downloads all image files from target website using image_url, and the image code"""
        print("Beginning download of all images...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.download_image, self.all_codes)
        print("Successfully downloaded all images!")

def main():
    # snatcher = ImageSnatcher()
    # snatcher.download_all_flags()
    unit = rq.get('https://cdn-lor.mobalytics.gg/production/images/set1/en_us/img/card/game/01IO009-full.webp')
    unit2 = rq.get('https://cdn-lor.mobalytics.gg/production/images/set1/en_us/img/card/game/01IO009T1-full.webp')
    spell = rq.get('https://cdn-lor.mobalytics.gg/production/images/set1/en_us/img/card/game/01IO009T3-full.webp')
    print(f"Zed Bytes: {len(unit.content)}, Shadow Bytes: {len(unit2.content)}, Spell Bytes: {len(spell.content)}")

if __name__ == "__main__":
    main()