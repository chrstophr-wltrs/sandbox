import os
import requests as rq
import concurrent.futures
from PIL import Image
import time
from bs4 import BeautifulSoup

class RuneterraImageScraper:
    """
    A class that goes to an artist's website, searches for all of the card art, then downloads that art.

    Attributes:
        source(str): the source website of the artist
        dir(str): the sub-folder in which all art will be saved
        identifier(str): the CSS identifier that selects the desired images
        index_chop(int): the string index before which all the target URL's are identical
        pics_list(list[str]): the unique portion of the URL's that point to the desired images
        base_URL(str): the base URL, onto which is appended the image resolution and suffix
        save_size(str): "####x####" defines the image resolution for the download
        full_URL(str): constructed from base_URL, save_size, and the saved string
        filename_regex(str): the RegEx used to isolate the name of the file
        endex_chop(-int): the negative index, used to chop the extension (if so desired)
        save_name(str): the index pointing to the save file, constructed from dir, filename_regex, and endex_chop
    """

    def __init__(self, source:str, dir:str, identifier:str, index_chop:int, base_URL:str, save_size:str, filename_regex:str, endex_chop:int):
        """
        source(str): the source website of the artist
        dir(str): the sub-folder in which all art will be saved
        identifier(str): the CSS identifier that selects the desired images
        index_chop(int): the string index before which all the target URL's are identical
        base_URL(str): the base URL, onto which is appended the image resolution and suffix
        save_size(str): "####x####" defines the image resolution for the download
        filename_regex(str): the RegEx used to isolate the name of the file
        endex_chop(-int): the negative index, used to chop the extension (if undesired)
        """
        self.source = source
        self.dir = dir
        self.identifier = identifier
        self.index_chop = index_chop
        self.base_URL = base_URL
        self.save_size = save_size
        self.filename_regex = filename_regex
        self.endex_chop = endex_chop

    def collect_image_names(self):
        """Collects the desired image URL's from the source webpage."""
        self.pics_list = []
        page = rq.get(self.source)
        soup = BeautifulSoup(page.content, 'html.parser')
        pics = soup.select(self.identifier)[0]
        print(pics)

"""
Important Variables: 

    Source URL: https://sixmorevodka.com/work/legends-of-runeterra/
    Folder Name: SIXMOREVODKA
    Identifier: ".pswp__img"
    Image List: 
        Example String: "https://img2.storyblok.com/3000x0/filters:quality(90):format(webp)/f/84907/6000x3000/ac6f74581c/self-improvement-golem.jpg"
    Index Chop: 84
        Example Endstring: "/ac6f74581c/self-improvement-golem.jpg"
        Filename: "self-improvement-golem.jpg"
    Filename Regex: "[a-z, \-]+.jpg"
    Endex Chop: -4
    Base URL: "https://img2.storyblok.com/3000x0/filters:quality(90):format(png)/f/84907/"
    Save Size: "2160x1080"
    full_url: "{Base URL}{Save Size}{Endstring}"
    Save Name: "{Folder Name}/{Filename[:{Endex Chop}].png"
"""

def main():
    sixmorevodka = RuneterraImageScraper("https://sixmorevodka.com/work/legends-of-runeterra/","SIXMOREVODKA",'img[id^="sbimage"]',84,"https://img2.storyblok.com/3000x0/filters:quality(90):format(png)/f/84907/","2160x1080","[a-z, \-]+.jpg",-4)
    sixmorevodka.collect_image_names()

if __name__ == "__main__":
    main()

# region_list = ['BW', 'DE', 'FR', 'IO', 'MT', 'NX', 'PZ', 'SH', 'SI']

# class ImageSnatcher:
#     """
#     A class using requests to download images from a website.
    
#     Attributes:
#         url_base (str): the base string of the URL where all of the images are located (def = 'https://cdn-lor.mobalytics.gg/production/images/set2/en_us/img/card/game/02')
#      """

#     def __init__(self, img_front  = 'https://cdn-lor.mobalytics.gg/production/images/set', card_set = 2):
#         """Establishes the card set, URL, and the subfolder where the images will be saved."""
#         self.card_set = card_set
#         self.url_base = (f"{img_front}{card_set}/en_us/img/card/game/{self.card_set:02}")
#         print(f"Created image snatcher!")
#         self.all_codes = []
#         self.subfolder = (f"set_{card_set}/")
#         if os.path.isdir(self.subfolder) == False:
#             os.mkdir(f'set_{card_set}')
#             print(f"Created sub-directory '/set_{card_set}' for image output!")
        
#     def test_region(self, region = "BW"):
#         """Tests all the possible numbers in a region."""
#         number = 1
#         while number < 500:
#             self.test_suffixes(f"{region}{number:03}")
#             number += 1
#         return

#     def test_suffixes(self, code = "BW001"):
#         """
#         Tests all of the suffixes for a given number, including the plain name. 

#         Parameters:
#             code (str): 2-letter region + 3-digit number

#         Returns 0 if plain name image could not be found
#         """
#         suffix = 0
#         while True:
#             if suffix == 0:
#                 card_code = code
#             else:
#                 card_code = (f"{code}T{suffix}")
#             my_card = rq.get(f"{self.url_base}{card_code}-full.webp")
#             if (not my_card.ok) and (suffix > 10):
#                 return suffix
#             if not os.path.isfile(f"{self.subfolder}{self.card_set:02}{card_code}.png"):
#                 with open(f"{self.subfolder}{self.card_set:02}{card_code}.png", "wb") as file:
#                     file.write(my_card.content)
#             print(f"Found {self.card_set:02}{card_code}!")
#             suffix += 1
                        
#     def download_all_cards(self):
#         """Downloads all image files from target website using image_url, and the image code"""
#         print("Beginning download of all images...")
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             executor.map(self.test_region, region_list)
#         print("Successfully downloaded all images!")
    
#     def delete_square(self, name):
#         """
#         Deletes an image if its height and width match.
#         Note: This function assumes that the image is in the associated sub_folder from __init__
        
#         Parameters:
#             name(str): the filename, including extension (ex. "image.png")
#         """
#         path = (f"{self.subfolder}{name}")
#         img = Image.open(path)
#         if img.width == img.height:
#             img.close()
#             os.remove(path)
#             print(f"{name} was a spell, and has been deleted!")
    
#     def scrub_spells(self):
#         """Deletes all downloaded spells from the subfolder."""
#         print("Beginning deletion of all spells...")
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             executor.map(self.delete_square, os.listdir(self.subfolder))
#         print("All spells succesfully deleted!")