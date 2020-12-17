import os
import requests as rq
import concurrent.futures
from PIL import Image
import time

"""
Example URL = https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02BW022T2-full.webp

02 = {self.card_set:02}
"BW" = region
022 = {number:03}
T2 = "T" + suffix_num

Pseudocode:

For each region in region_list
    number starts at 1
        card_code = card_set + region + number
        check if card exists at url
            if card does exist, append it to card list, suffix = 1
            if card doesn't exist and number > 5, go to next region
            card_code = card_set + region + number + "T" + suffix
            check if card exists with suffix
                if card w/ suffix does exist, append to card list, go to next suffix
                if card w/ suffix doesn't exist, go to next number
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
    
    def download_cards(self):
        """
        Finds all valid card combinations for this set

        Returns valid_cards list
        """
        test_list = [True, False, True, True, True, False, False, True, True, True, False]
        sub_list = 
        index = -1
        for region in region_list:
            number = 1
            while index < (len(test_list) - 1):
                card_code = (f"{region}{number:03}")
                index += 1
                if test_list[index] == True:
                    print(f"{card_code}: True")
                    number += 1
                else:
                    print(f"{card_code}: False")
                    break
                        


            

    
    def download_all_flags(self):
        """Downloads all image files from target website using image_url, and the image code"""
        print("Beginning download of all images...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.download_image, self.all_codes)
        print("Successfully downloaded all images!")

def main():
    thingie = ImageSnatcher()
    thingie.download_cards()

if __name__ == "__main__":
    main()