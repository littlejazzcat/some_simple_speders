import os
import requests
import re
from lxml import etree
import sys

def read_html():
    path = "D:\\python3_study\\some_simple_spiders\\comic_spider\\still_html"
    #read file
    #files = os.listdir(path)
    #获取路径下所有文件的路径
    
    for file_index in range(2,3):
        #拼接路径
        with open(path+'\\'+str(file_index)+'.html',"r", encoding="utf-8") as f:
            #f.seek(0)
            html = f.read()

        print(html)
        pic_pattern = re.compile('<div.*?style="background:url\((.*?)\)')#封面图地址
        title_pattern = re.compile('<div style="padding:0px 5px 0px 5px;">.*?<a href=\'(?P<url>.*?)\'>(?P<title>.*?)</a> <br />.*?\
                                   <font class="pagefoot">(?P<author>.*?)</font>')#漫画地址、标题和作者
        score_pattern = re.compile('<p style=.*?<b>(.*?)</b>')#评分
        

        img_urls = pic_pattern.findall(html,re.S)
        details = title_pattern.findall(html,re.S)
        scores = score_pattern.findall(html,re.S)

        for img_url,detail,score in zip(img_urls,details,scores):
            print(f"{img_url}\n{detail}\n{score}\n")

        #save_info(details,scores)

        #for index,url in enumerate(img_urls):
            #save_img(details[index][1],url)#details->[(漫画地址,标题,作者)]

def save_img(title,url):
    print(f'正在抓取{title}')
    headers = {
        'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    try:
        res = requests.get(url,headers=headers,allow_redirects=False,timeout=10)

        data = res.content
        with open(f'some_simple_spiders\\comic_spider\\cover_pic\\{title}.jpg','wb+') as f:
            f.write(data)

    except Exception as e:
        print(e)

def save_info(details,scores):
    for index,detail in enumerate(details):
        info_str = "%s,%s,%s,%s\n" % (detail[index][1].replace(",","，"),detail[index][0],detail[index][2].replace(",","，"),scores[index])
        with open("./comic.csv","a+",encoding="utf-8") as f:
            f.write(info_str)


if __name__ == "__main__":
    read_html()
