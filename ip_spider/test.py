import requests
import random

url_1 = 'https://ip.jiangxianli.com/?page=1'
url_2 = 'http://www.kxdaili.com/dailiip/1/1.html'
uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
        "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)",
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
]

ua = random.choice(uas)

headers = {
    'User-Agent' : ua,
    "referer": "https://www.baidu.com"
    }

#res = requests.get(url=url_1,headers=headers,verify=False,allow_redirects=False,timeout=5)
#print(res.status_code)
#print(res.text)
with open('D:\\python3_study\\some_simple_spiders\\ip_spider\\ip_porxy.txt','w',encoding = 'utf-8') as f:
    f.write('免费代理ip大全'+'\n')