import requests
import re
import time
import random
import threading
import os

base_url = 'https://kox.moe/l/all/'
USER_AGENT = [
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Chrome	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Microsoft Edge	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Chrome	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Firefox 7	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
]

def get_img(base_url, index):
    headers = {
        "User-Agent": random.choice(USER_AGENT)
    }
    print(f'第{index}页正在抓取')
    
    try:
        url = base_url+str(index)+'.htm'
        res = requests.get(url=url,headers=headers, allow_redirects=False, timeout=10)
        print(res.status_code)
        while res.status_code == 302:
            #访问该网址获取一个IP地址
            ip_json = requests.get("http://118.24.52.95:5010/get/", headers=headers).json()
            ip = ip_json["proxy"]
            proxies = {
                "http":ip,
                "https":ip
            }
            print(proxies)
            #使用代理IP继续爬取
            res = requests.get(url=url, headers=headers, proxies=proxies, allow_redirects=False, timeout=10)
            time.sleep(5)
            print(res.status_code)
        else:
            html = res.text
            #将静态文件保存到本地
            with open(f"some_simple_spiders\\comic_spider\\still_html\\{index}.html","w+", encoding="utf-8") as f:
                f.write(html)
        
        semaphore.release()
    except Exception as e:
        print(e)
        print("睡眠 5s，再重新抓取")
        time.sleep(5)
        get_img(base_url, index)


if __name__ == '__main__':
    num = 0
    #开启五个线程
    semaphore = threading.BoundedSemaphore(5)
    lst_record_threads = []
    for index in range(1,30):
        semaphore.acquire()
        t = threading.Thread(target=get_img,args=(
            f"https://kox.moe/l/all/",index))
        t.start()
        lst_record_threads.append(t)

    for rt in lst_record_threads:
        rt.join()
