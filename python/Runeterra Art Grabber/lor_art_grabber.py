import os
import requests as rq
import concurrent.futures
from PIL import Image
import time

"""
Example URL = https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02BW022T2-full.webp
"""
# https://cdn-lor.mobalytics.gg/production/images/set3/en_us/img/card/game/03MT217-full.webp

region_list = ['BW', 'DE', 'FR', 'IO', 'MT', 'NX', 'PZ', 'SI']

class ImageSnatcher:
    """
    A class using requests to download images from a website.
    
    Attributes:
        url_base (str): the base string of the URL where all of the images are located (def = 'https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02')
     """

    def __init__(self, img_front  = 'https://cdn-lor.mobalytics.gg/production/images/set', card_set = 2):
        """Establishes the card set, URL, and the subfolder where the images will be saved."""
        self.card_set = card_set
        self.url_base = (f"{img_front}{card_set}/en_us/img/card/game/{self.card_set:02}")
        print(f"Created image snatcher!")
        self.all_codes = []
        self.subfolder = (f"set_{card_set}/")
        if os.path.isdir(self.subfolder) == False:
            os.mkdir(f'set_{card_set}')
            print(f"Created sub-directory '/set_{card_set}' for image output!")
        
    def test_region(self, region = "BW"):
        """Tests all the possible numbers in a region."""
        number = 1
        while number < 1000:
            self.test_suffixes(f"{region}{number:03}")
            number += 1

    def test_suffixes(self, code = "BW001"):
        """
        Tests all of the suffixes for a given number, including the plain name. 

        Parameters:
            code (str): 2-letter region + 3-digit number

        Returns 0 if plain name image could not be found
        """
        suffix = 0
        while True:
            if suffix == 0:
                card_code = code
            else:
                card_code = (f"{code}T{suffix}")
            my_card = rq.get(f"{self.url_base}{card_code}-full.webp")
            if my_card.ok == False:
                print(f"Couldn't find {card_code}, moving to next card code...")
                return suffix
            with open(f"{self.subfolder}{self.card_set}{card_code}.png", "wb") as file:
                file.write(my_card.content)
            print(f"Found {card_code}!")
            suffix += 1
                        
    def download_all_cards(self):
        """Downloads all image files from target website using image_url, and the image code"""
        print("Beginning download of all images...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.test_region, region_list)
        print("Successfully downloaded all images!")
    
    def delete_square(self, name):
        """
        Deletes an image if its height and width match.
        Note: This function assumes that the image is in the associated sub_folder from __init__
        
        Parameters:
            name(str): the filename, including extension (ex. "image.png")
        """
        path = (f"{self.subfolder}{name}")
        img = Image.open(path)
        if img.width == img.height:
            img.close()
            os.remove(path)
            print(f"{name} was a spell, and has been deleted!")
    
    def scrub_spells(self):
        """Deletes all downloaded spells from the subfolder."""
        print("Beginning deletion of all spells...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.delete_square, os.listdir(self.subfolder))
        print("All spells succesfully deleted!")


def main():
    thingie = ImageSnatcher(card_set = 1)
    thingie.download_all_cards()
    thingie.scrub_spells()

if __name__ == "__main__":
    main()