import os
import requests as rq
import concurrent.futures
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

    def __init__(self, source:str, dir:str, ident_regex:str, base_URL:str, save_size:str, nameReg:str):
        """
        source(str): the source website of the artist
        dir(str): the sub-folder in which all art will be saved
        ident_regex(str): the regex string that selects the desired images
        base_URL(str): the base URL, onto which is appended the image resolution and suffix
        save_size(str): "####x####" defines the image resolution for the download
        nameReg(str): the RegEx used to isolate the name of the file
        """
        self.source = source
        self.dir = dir
        self.ident_regex = ident_regex
        self.base_URL = re.sub(r"[0-9]+x[0-9]+", save_size, base_URL)
        self.save_size = save_size
        self.nameReg = nameReg
            
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
            print(f"Created sub-directory '{dir}' for image output!")
        self.pic_list = []
        self.collect_image_names()

    def collect_image_names(self):
        """Collects the desired image URL's from the source webpage."""
        def scan_for_dupes(list_to_scan: list, marker: str = "."):
            """Scans the given list for any values not in self.pics_list"""
            widReg = r'(\d+)x'
            hetReg = r'x(\d+)'
            notFlag = marker[0] == "-"
            if notFlag:
                marker = marker[1:]
            for i in list_to_scan:
                duple_flag = False
                imp_name = re.findall(self.nameReg, i)[0]
                imp_w = int(re.findall(widReg, i)[0])
                imp_h = int(re.findall(hetReg, i)[0])
                for j in self.pic_list:
                    pic_name = re.findall(self.nameReg, j)[0]
                    if imp_name == pic_name:
                        up_for_grabs = self.pic_list.index(j)
                        pic_w = int(re.findall(widReg, j)[0])
                        pic_h = int(re.findall(hetReg, j)[0])
                        duple_flag = True
                        if (imp_w > pic_w) or (imp_h > pic_h):
                            if imp_w == (imp_h * 2):
                                if ((notFlag and (marker not in i)) or ((not notFlag) and (marker in i))):
                                    self.pic_list[up_for_grabs] = i                              
                        else:
                            self.pic_list[up_for_grabs] = j
                if (not duple_flag) and (imp_w == (imp_h * 2)):
                    if (notFlag and (marker not in i)) or ((not notFlag) and (marker in i)):
                        self.pic_list.append(i)

        page = rq.get(self.source)
        soup = BeautifulSoup(page.content, "lxml")
        # Replace any problematic string fragments
        prettySoup = soup.prettify().replace("\\u002F", "/")
        duplicates_list = re.findall(self.ident_regex, prettySoup)
        lulu_list = []
        for i in duplicates_list:
            if "lulu" in i:
                lulu_list.append(i)
        
        # Go through the lists, and filter out any duplicates, keep whichever one has the largest dimensions
        # Scan for the PNG's first
        scan_for_dupes(duplicates_list, "png")
        
        lulu_list = []
        for i in self.pic_list:
            if "lulu" in i:
                lulu_list.append(i)

        # Scan for unusual file types
        scan_for_dupes(duplicates_list, "-jpg")

        lulu_list = []
        for i in self.pic_list:
            if "lulu" in i:
                lulu_list.append(i)

        # Scan for the jpg's
        scan_for_dupes(duplicates_list)
        lulu_list = []
        for i in self.pic_list:
            if "lulu" in i:
                lulu_list.append(i)
        
        lulu_list

    def download_image(self, image_string:str):
        """
        Downloads and saves the target image
        
        Attributes:
            image_string(str): the string pointing to the image
        """
        full_URL = f"{self.base_URL}{image_string}"
        file_name = re.findall(self.nameReg, image_string)[0] + ".png"
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