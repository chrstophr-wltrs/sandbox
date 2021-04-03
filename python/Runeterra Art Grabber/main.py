from lor_ArtGrabber import RuneterraImageScraper
import re




def main():
    def scan_for_dupes(list_to_scan: list, marker: str = "."):
        """Scans the given list for any values not in self.pics_list"""
        widReg = r'(\d+)x'
        hetReg = r'x(\d+)'
        nameReg = r"\/([a-z0-9\-]+)\."
        notFlag = marker[0] == "-"
        if notFlag:
            marker = marker[1:]
        for i in list_to_scan:
            duple_flag = False
            imp_name = re.findall(nameReg, i)[0]
            imp_w = int(re.findall(widReg, i)[0])
            imp_h = int(re.findall(hetReg, i)[0])
            for j in pic_list:
                pic_name = re.findall(nameReg, j)[0]
                if imp_name == pic_name:
                    up_for_grabs = pic_list.index(j)
                    pic_w = int(re.findall(widReg, j)[0])
                    pic_h = int(re.findall(hetReg, j)[0])
                    duple_flag = True
                    if (imp_w > pic_w) or (imp_h > pic_h):
                        if imp_w == (imp_h * 2):
                            if ((notFlag and (marker not in i)) or ((not notFlag) and (marker in i))):
                                pic_list[up_for_grabs] = i                              
                    else:
                        pic_list[up_for_grabs] = j
            if (not duple_flag) and (imp_w == (imp_h * 2)):
                if (notFlag and (marker not in i)) or ((not notFlag) and (marker in i)):
                    pic_list.append(i)
    
    sixmorevodka = RuneterraImageScraper("https://sixmorevodka.com/work/legends-of-runeterra/","SIXMOREVODKA",r'[0-9]+x[0-9]+\/[a-z0-9]+\/[a-z0-9\-]+\.[a-z]+',"https://img2.storyblok.com/0000x0000/filters:quality(100):format(png)/f/84907/","2160x1080", r"\/([a-z0-9\-]+)\.")
    base_list = ['2560x1280/lulu-level-01.jpg', '764x795/lulu-level-01.png', '2560x1280/lulu-level-02.jpg', '641x822/lulu-level-02.png']
    pic_list = []
    scan_for_dupes(base_list, "png")

if __name__ == "__main__":
    main()