import os
import requests as rq
import concurrent.futures
from PIL import Image
import time
from bs4 import BeautifulSoup
import re

class RuneterraImageScraper:
    """
    A class that goes to an artist's website, searches for all of the card art, then downloads that art.

    Attributes:
        source(str): the source website of the artist
        dir(str): the sub-folder in which all art will be saved
        ident_regex(str): the regex string that selects the desired images
        pics_list(list[str]): the unique portion of the URL's that point to the desired images
        base_URL(str): the base URL, onto which is appended the image resolution and suffix
        full_URL(str): constructed from base_URL, save_size, and the saved string
        file_regex(str): the RegEx used to isolate the name of the file
        endex_chop(-int): the negative index, used to chop the extension (if so desired)
        save_name(str): the index pointing to the save file, constructed from dir, file_regex, and endex_chop
    """

    def __init__(self, source:str, dir:str, ident_regex:str, base_URL:str, save_size:str, file_regex:str, endex_chop:int):
        """
        source(str): the source website of the artist
        dir(str): the sub-folder in which all art will be saved
        ident_regex(str): the regex string that selects the desired images
        base_URL(str): the base URL, onto which is appended the image resolution and suffix
        save_size(str): "####x####" defines the image resolution for the download
        file_regex(str): the RegEx used to isolate the name of the file
        endex_chop(-int): the negative index, used to chop the extension (if undesired)
        """
        self.source = source
        self.dir = dir
        self.ident_regex = ident_regex
        self.base_URL = re.sub(r"[0-9]+x[0-9]+", save_size, base_URL)
        self.save_size = save_size
        self.file_regex = file_regex
        self.endex_chop = endex_chop
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
            print(f"Created sub-directory '{dir}' for image output!")
        self.collect_image_names()

    def collect_image_names(self):
        """Collects the desired image URL's from the source webpage."""
        print(f"Scraping {self.dir} website for image names...")
        page = rq.get(self.source)
        soup = BeautifulSoup(page.content, "lxml")
        # Replace any problematic string fragments
        prettySoup = soup.prettify().replace("\\u002F", "/")
        imperfect_list = re.findall(self.ident_regex, prettySoup)
        png_list = re.findall(r'[0-9]+x[0-9]+\/[a-z0-9]+\/[a-z0-9\-]+.png', prettySoup)
        imperfect_list += png_list
        # Go through the list, and filter out any duplicates, keep whichever one has the largest dimensions
        self.pic_list = []
        fileReg = r"[a-z0-9\-]+.jpg"
        fileRegPng = r"[a-z0-9\-]+.png"
        widReg = r'(\d+)x'
        hetReg = r'x(\d+)'
        for i in imperfect_list:
            duple_flag = False
            try:
                imp_name = re.findall(fileReg, i)[0]
            except:
                imp_name = re.findall(fileRegPng, i)[0]
                print(f"found {imp_name}")
            imp_w = int(re.findall(widReg, i)[0])
            imp_h = int(re.findall(hetReg, i)[0])
            for j in self.pic_list:
                try:
                    pic_name = re.findall(fileReg, j)[0]
                except:
                    pic_name = re.findall(fileRegPng, j)[0]
                if imp_name == pic_name:
                    up_for_grabs = self.pic_list.index(j)
                    pic_w = int(re.findall(widReg, j)[0])
                    pic_h = int(re.findall(hetReg, j)[0])
                    duple_flag = True
                    if (imp_w > pic_w) or (imp_h > pic_h):
                        if imp_w == (imp_h * 2):
                            self.pic_list[up_for_grabs] = i
                    else:
                        self.pic_list[up_for_grabs] = j
            if (not duple_flag) and (imp_w == (imp_h * 2)):
                self.pic_list.append(i)        
        print("Successfully found all image names!")
    
    def download_image(self, image_string:str):
        """
        Downloads and saves the target image
        
        Attributes:
            image_string(str): the string pointing to the image
        """
        full_URL = f"{self.base_URL}{image_string}"
        file_name = re.findall(self.file_regex, image_string)[0][:self.endex_chop] + ".png"
        save_path = f"{self.dir}/{file_name}"
        if not os.path.isfile(save_path):
            page = rq.get(full_URL)
            with open(save_path, "wb") as file:
                file.write(page.content)
            print(f"{file_name} saved!")
    
    def download_all_images(self):
        """Begins the concurrent download of all images"""
        print("Beginning download of all images...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.download_image, self.pic_list)
        print("Successfully downloaded all images!")

"""
Important Variables: 

    Source URL: https://sixmorevodka.com/work/legends-of-runeterra/
    Folder Name: SIXMOREVODKA
    ident_regex: ".pswp__img"
    Image List: 
        Example String: "https://img2.storyblok.com/3000x0/filters:quality(90):format(webp)/f/84907/6000x3000/ac6f74581c/self-improvement-golem.jpg"
    Index Chop: 84
        Example Endstring: "/ac6f74581c/self-improvement-golem.jpg"
        Filename: "self-improvement-golem.jpg"
    Filename Regex: "[a-z, \-]+.jpg"
    Endex Chop: -4
    Base URL: "https://img2.storyblok.com/3000x0/filters:quality(100):format(png)/f/84907/"
    Save Size: "2160x1080"
    full_url: "{Base URL}{Save Size}{Endstring}"
    Save Name: "{Folder Name}/{Filename[:{Endex Chop}].png"
"""

def main():
    sixmorevodka = RuneterraImageScraper("https://sixmorevodka.com/work/legends-of-runeterra/","SIXMOREVODKA",r'[0-9]+x[0-9]+\/[a-z0-9]+\/[a-z0-9\-]+.jpg',"https://img2.storyblok.com/0000x0000/filters:quality(100):format(png)/f/84907/","2160x1080",r"[a-z0-9\-]+.jpg",-4)
    # sixmorevodka.download_all_images()
    
if __name__ == "__main__":
    main()