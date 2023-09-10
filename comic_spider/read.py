import os
import requests
import re
import threading
import sys



def read_html(file_index):
    path = "D:\\python3_study\\some_simple_spiders\\comic_spider\\still_html"
    #read file
    #files = os.listdir(path)
    #获取路径下所有文件的路径
    
    Semaphore.acquire()  #获取进程锁
        #拼接路径
    with open(path+'\\'+str(file_index)+'.html',"r", encoding="utf-8") as f:
            #f.seek(0)
            html = f.read()

    #print(html)
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



    for score,img_url,comic_url,title,author in zip(scores,img_urls,comic_urls,titles,authors):
        print(f"{img_url}\n{comic_url} -- {title} -- {author} -- {score}")
        #title,author

    save_info(zip(titles,authors,comic_urls,scores),file_index)

    for url,title in zip(img_urls,titles):
        save_img(title,url)#details->[(漫画地址,标题,作者)]
    Semaphore.release()

def save_img(title,url):
    print(f'正在抓取{title}')
    headers = {
        "User-Agent" : 'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    try:
        res = requests.get(url,headers=headers,allow_redirects=False,timeout=10)
        print(res.status_code)

        data = res.content
        with open(f'some_simple_spiders\\comic_spider\\cover_pic\\{title}.jpg','wb+') as f:
            f.write(data)

    except Exception as e:
        print(e)

def save_info(details,file_index):
    page_info = f"这是第{file_index}页"
    page_down = "%s,%s,%s,%s\n" % (page_info,'','','')
    with open("D:\\python3_study\\some_simple_spiders\\comic_spider\\comic2.csv","a+",encoding="utf-8") as f:
            f.write(page_down)  #插入页码信息
    for detail in details:
        info_str = "%s,%s,%s,%s\n" % (detail[0].replace(",","，"),detail[1].replace(",","，"),detail[2].replace(",","，"),
                                      detail[3])
        with open("D:\\python3_study\\some_simple_spiders\\comic_spider\\comic2.csv","a+",encoding="utf-8") as f:
            f.write(info_str)


if __name__ == "__main__":
    Semaphore = threading.BoundedSemaphore(5) #一次最多允许五个线程执行
    lst = []
    maxpage = 30
    for file_index in range(1,maxpage):
        t = threading.Thread(target=read_html,args=(file_index,))
        t.start()
        lst.append(t)
    for rt in lst:
        rt.join()
