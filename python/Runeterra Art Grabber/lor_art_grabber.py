import os
import requests as rq
import concurrent.futures
from PIL import Image
import time

"""
Example URL = https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02BW022T2-full.webp
"""


region_list = ['BW', 'DE', 'FR', 'IO', 'MT', 'NX', 'PZ', 'SI']

class ImageSnatcher:
    """
    A class using requests to download images from a website.
    
    Attributes:
        url_base (str): the base string of the URL where all of the images are located (def = 'https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02')
     """

    def __init__(self, img_front  = 'https://cdn-lor.mobalytics.gg/production/images/set', card_set = 2):
        """Reads in the file of flag codes, and chooses 10 random codes for download purposes."""
        self.card_set = card_set
        self.url_base = (f"{img_front}{card_set}/en_us/img/card/game/{self.card_set:02}")
        print(f"Created image snatcher!")
        self.all_codes = []
        if os.path.isdir(f'set_{card_set}') == False:
            os.mkdir(f'set_{card_set}')
            print(f"Created sub-directory '/set_{card_set}' for image output!")
        
    def test_region(self, region = "BW"):
        number = 1
        while True:
            if self.test_suffixes(f"{region}{number:03}") == 0 and number > 5:
                return
            number += 1

    def test_suffixes(self, code = "BW001"):
        suffix = 0
        while True:
            if suffix == 0:
                card_code = code
            else:
                card_code = (f"{code}T{suffix}")
            my_card = rq.get(f"{self.url_base}{card_code}-full.webp")
            if my_card.ok == False:
                print(f"Couldn't find {card_code}, moving on...")
                return suffix
            with open(f"set_{self.card_set}/{card_code}.png", "wb") as file:
                file.write(my_card.content)
            print(f"Found {card_code}!")
            suffix += 1
                        
    def download_all_cards(self):
        """Downloads all image files from target website using image_url, and the image code"""
        print("Beginning download of all images...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.test_region, region_list)
        print("Successfully downloaded all images!")

def main():
    thingie = ImageSnatcher()
    thingie.download_all_cards()

if __name__ == "__main__":
    main()