import requests
import re
import threading


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    #"Cookie" : "wzws_sessionid=oGT6gveAMTQuMjMuMTgyLjY1gWJmZTJhM4IwZjU0MGU=; PHPSESSID=tof8jg7ispbg445roufpgsgh74; think_var=zh-cn",
    "Connection" : 'keep-alive'
}


def get_img(index_url):

    res = requests.get(url = index_url,headers = headers)
    if res is not None:
        html = res.text

        #print(res.text)
        pattern = re.compile(
            '<img lazysrc="(.*?)" lazysrc2x=".*?" width="221" height="362" alt=".*?" tltle="(.*?)"'
        )
        match_list = pattern.findall(html)
        for url,title in match_list:
            save_img(url[:url.find('jpg')+3],title)

        print(match_list)
    else:
        print('res is None')

def save_img(url,title):
    try:
        print(f"{title} - {url}")
        res = requests.get(url = url, headers = headers)

        if res != None:
            html = res.content

            with open(f"images/{title}.jpg","wb+") as f:
                f.write(res.content)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    num = 0
    #semaphore = threading.BoundedSemaphore(5)
    semaphore = threading.BoundedSemaphore(5)
    for index in range(10):
        t = threading.Thread(target=get_img, args=(
            f"https://www.3gbizhi.com/sjbz/index_{index}.html",))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('所有线程运行完毕')

