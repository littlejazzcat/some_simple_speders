import requests
import re
import threading
from lxml import etree
import time

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    #"Connection" : 'keep-alive'
}


def get_img(index_url,index):

    wallpaper_html = "wallpaper_html"
    res = requests.get(url = index_url,headers = headers, verify=True)

    if res is not None:
        with open(f'some_simple_spiders\\wallpaper_spider\\wallpaper_html\\page{index}.html', "w+", encoding='utf-8') as f:
            f.write(res.text)
            f.seek(0)  #将文件位置返回到文件开头，否则无法读取到数据（每次写完文件位置就会去到文件末尾）
            res = f.read()
            html = etree.HTML(res)

        #print(res.text)
        pattern_urls = re.compile('<img.*? lay-src="(.*?)"')
        pattern_titles = re.compile('<img.*? title="(.*?)"')
        urls = pattern_urls.findall(res)
        titles = pattern_titles.findall(res)

        for url,title in zip(urls,titles):
            save_img(url,title)

        print(urls,titles)
    else:
        print('res is None')

def save_img(url,title):
    try:
        print(f"{title} - {url}")
        res = requests.get(url = url, headers = headers, verify=True)

        if res != None:
            html = res.content

            with open(f"some_simple_spiders\\wallpaper_spider\\images\\{title}.jpg","wb+") as f:
                f.write(res.content)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    num = 0
    #semaphore = threading.BoundedSemaphore(5)
    semaphore = threading.BoundedSemaphore(5)
    '''for index in range(10):
        t = threading.Thread(target=get_img, args=(
            f"https://www.3gbizhi.com/sjbz/index_{index}.html",index,))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('所有线程运行完毕')'''
    for index in range(1,4):
        get_img(f"https://www.3gbizhi.com/sjbz/index_{index}.html",index)
        time.sleep(1)
    print('all threads are done')
'''文件读取的seek(0)文件位置问题
requests.get()超时问题
lxml的etree.HTML方法返回的文档和网页源码差别过大问题以及标签错乱问题
'''