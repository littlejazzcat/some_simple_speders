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
        comic_pattern = re.compile('<div style="padding:0px 5px 0px 5px;">[.\s]*<a href=\'(?P<url>.*?)\'')#漫画地址、标题和作者
        score_pattern = re.compile('<p style=.*?[.\s]*.*?<b>(.*?)</b>')#评分
        title_pattern = re.compile('<div style="padding:0px 5px 0px 5px;">[.\s]*<a href=.*?>(?P<title>.*?)</a> <br />')#漫画标题
        author_pattern = re.compile('<font class="pagefoot">(.*?)</font>')

        img_urls = pic_pattern.findall(html,re.S)
        comic_urls = comic_pattern.findall(html,re.S)#漫画地址
        scores = score_pattern.findall(html,re.S)
        titles = title_pattern.findall(html,re.S)
        authors = author_pattern.findall(html,re.S)#作者

        #for score in scores: #it is ok
            #print(f'{score}')
        
        #for img_url in img_urls:#it is ok
            #print(f'{img_url}')

        #for comic_url in comic_urls:
            #print(f'{comic_url}')

        #for title in titles:
            #print(F"{title}")

        for author in authors:
            print(f"{author}")
                  #title,author

        #for img_url,detail,score in zip(img_urls,details,scores):
            #print(f"{img_url}\n{detail}\n{score}\n")

if __name__ == "__main__":

    read_html()
