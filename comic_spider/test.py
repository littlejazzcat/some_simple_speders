import requests
import re
import sys

def read_html():
    path = "D:\\python3_study\\some_simple_spiders\\comic_spider\\still_html"
    
    #获取路径下所有文件的路径
    for file_index in range(2,3):
        #拼接路径
        with open(path+'\\'+str(file_index)+'.html',"a+", encoding="utf-8") as f:
            f.seek(0)
            html = f.read()

        pic_pattern = re.compile('<div[.\s]*style="background:url\((.*?)\)')#封面图地址
        title_pattern = re.compile('<div style="padding:0px 5px 0px 5px;">[.\s]*<a href=\'(?P<url>.*?)\'.*?>(?P<title>.*?)</a> <br />.*?\
                                   [.\s]*<font class="pagefoot">(?P<author>.*?)</font>')#漫画地址、标题和作者
        score_pattern = re.compile('<p style=.*?[.\s]*.*?<b>(.*?)</b>')#评分
        

        img_urls = pic_pattern.findall(html,re.S)
        details = title_pattern.findall(html,re.S)
        scores = score_pattern.findall(html,re.S)

        #for score in scores: #it is ok
            #print(f'{score}')
        
        #for img_url in img_urls:#it is ok
            #print(f'{img_url}')

        for comic_url,title,author in details:
            print(f'{comic_url},{title},{author}')

        #for img_url,detail,score in zip(img_urls,details,scores):
            #print(f"{img_url}\n{detail}\n{score}\n")

if __name__ == "__main__":

    read_html()
