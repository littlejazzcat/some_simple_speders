import os
import requests
import re

def read_html():
    path = "some_simple_spiders\\comic_spider\\still_html"
    #read file
    files = os.listdir(path)
    #获取路径下所有文件的路径
    
    for file in files:
        #拼接路径
        file_path = os.path.join(path,file)
        with open(file_path,"r", encoding="utf-8") as f:
            html = f.read()
        pic_pattern = re.compile('<div[.\s]style="background:url\((.*?)\)')