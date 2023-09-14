import random
from lxml import etree
import requests
import telnetlib

def get_headers():#获取http请求头headers
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
        "user-agent": ua,
        "referer": "https://www.baidu.com"
    }
    return headers

def get_html(url):
    headers = get_headers()
    try:
        res = requests.get(url = url, headers = headers)
        return res.text
    except Exception as e:
        print(f"请求网址异常\n{e}")
        return None

def check_ip_port(ip_port):#检测ip是否可用
    for item in ip_port:
        ip = item['ip']
        port = item['port']
        try:
            tn = telnetlib.Telnet(ip,port=port,timeout=2)
        except:
            print(f'[-] ip:{ip}:{port}')
        else:
            print(f'[+] ip:{ip}:{port}')
            with open('ip_porxy.txt','a') as f:
                f.write(ip+':'+port+'\n')
    print('检测完毕')

def format_html(text, ip_xpath, port_xpath):#解析出ip和端口
    ret = []
    res = etree.HTML(text)
    ips = res.xpath(ip_xpath)
    ports = res.xpath(port_xpath)
    for ip,port in zip(ips,ports):
        item = {'ip':ip.strip(),'port':port.strip()}
        ret.append(item)
    return ret

#从ip89网站获取免费Ip并检测是否可用再保存到txt文本中
def ip89(pagesize):

    url_format = "https://www.89ip.cn/index_{}.html"
    for page in range(1,pagesize+1):
        url = url_format.format(page)
        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/text()'
        port_xpath = '//tbody/tr/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        # 检测代理是否可用
        check_ip_port(ret)
        # check_proxy(ret)

