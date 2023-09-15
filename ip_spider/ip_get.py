import random
from lxml import etree
import requests
import telnetlib
import threading
from threading import Thread
from threading import Semaphore

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
    semaphore.acquire()
    headers = get_headers()
    try:
        res = requests.get(url = url, headers = headers)
        return res.text
    except Exception as e:
        print(f"请求网址异常\n{e}")
        return None

def check_ip_port(ip_port,page):#检测ip是否可用
    #semaphore.acquire()
    if(ip_port == None):
        print('检测失败')
        return
    for item in ip_port:
        ip = item['ip']
        port = item['port']
        try:
            tn = telnetlib.Telnet(ip,port=port,timeout=2)
        except:
            print(f'[-] ip:{ip}:{port}')
        else:
            print(f'[+] ip:{ip}:{port}')
            with open('D:\\python3_study\\some_simple_spiders\\ip_spider\\ip_porxy.txt','a') as f:
                f.write(ip+':'+port+'\n')
        semaphore.release()
    print(f'第{page}页检测完毕')

def format_html(text, ip_xpath, port_xpath):#解析出ip和端口
    if(text == None):
        print('网址请求异常')
        return None
    ret = []
    res = etree.HTML(text)
    ips = res.xpath(ip_xpath)
    ports = res.xpath(port_xpath)
    for ip,port in zip(ips,ports):
        item = {'ip':ip.strip(),'port':port.strip()}
        ret.append(item)
    return ret

class ipwebsite:
#从ip89网站获取免费Ip并检测是否可用再保存到txt文本中
    def ip89(pagesize):#2023.9.15有85页

        url_format = "https://www.89ip.cn/index_{}.html"
        for page in range(1,pagesize+1):
            url = url_format.format(page)
            text = get_html(url)
            ip_xpath = '//tbody/tr/td[1]/text()'
            port_xpath = '//tbody/tr/td[2]/text()'
            ret = format_html(text, ip_xpath, port_xpath)
            # 检测代理是否可用
            check_ip_port(ret,page)
            # check_proxy(ret)

    def ip66(pagesize):#2023.9.15有3196页
        url_format = "http://www.66ip.cn/{}.html"
        for page in range(1,pagesize+1):
            url = url_format.format(page)
            text = get_html(url)
            ip_xpath = '//table/tr[position()>1]/td[1]/text()'
            port_xpath = '//table/tr[position()>1]/td[2]/text()'
            ret = format_html(text, ip_xpath, port_xpath)
            check_ip_port(ret,page)

    def ip3366(pagesize):#免费代理只有10页
        url_format = "https://proxy.ip3366.net/free/?action=china&page={}"
        for page in range(1,pagesize+1):
            url = url_format.format(page)
            text = get_html(url)
            ip_xpath = '//td[@data-title="IP"]/text()'
            port_xpath = '//td[@data-title="PORT"]/text()'
            ret = format_html(text, ip_xpath, port_xpath)
            check_ip_port(ret,page)

    def ip_huan():#该网址暂不能用
        url = "https://ip.ihuan.me/?page=b97827cc"
        text = get_html(url)
        ip_xpath = '//tbody/tr/td[1]/a/text()'
        port_xpath = '//tbody/tr/td[2]/text()'
        ret = format_html(text, ip_xpath, port_xpath)
        check_ip_port(ret,page=None)

    def ip_kuai(pagesize):#2023.9.15有6696页，有时无法访问
        url_format = "https://www.kuaidaili.com/free/inha/2/"
        for page in range(1,pagesize+1):
            url = url_format.format(page)
            text = get_html(url)
            ip_xpath = '//td[@data-title="IP"]/text()'
            port_xpath = '//td[@data-title="PORT"]/text()'
            ret = format_html(text, ip_xpath, port_xpath)
            check_ip_port(ret,page)

    def ip_jiangxi(pagesize):#无法访问
        url_format = "https://ip.jiangxianli.com/?page=1"
        for page in range(1,pagesize+1):
            url = url_format.format()
            text = get_html(url)
            ip_xpath = '//tbody/tr[position()!=7]/td[1]/text()'
            port_xpath = '//tbody/tr[position()!=7]/td[2]/text()'
            ret = format_html(text, ip_xpath, port_xpath)
            check_ip_port(ret,page)

    def ip_kaixin(pagesize):#有两种类型，每种类型有10页
        url_format = "http://www.kxdaili.com/dailiip/{}/{}.html"
        for kind in range(1,3):
            for page in range(1,pagesize+1):
                url = url_format.format(kind,page)
                text = get_html(url)
                ip_xpath = '//tbody/tr/td[1]/text()'
                port_xpath = '//tbody/tr/td[2]/text()'
                ret = format_html(text, ip_xpath, port_xpath)
                check_ip_port(ret,page)

def all_ip(page1,page2,page3,page4):
    if(page1<1 | page2<1 | page3<1 | page4<1):
        print('请输入大于0的页数\n')
        return
    ipget = ipwebsite
    ipget.ip89(page1)
    ipget.ip66(page2)
    ipget.ip3366(page3)
    ipget.ip_kaixin(page4)

if __name__ == '__main__':
    #with open('D:\\python3_study\\some_simple_spiders\\ip_spider\\ip_porxy.txt','w',encoding = 'utf-8') as f:
        #f.write('免费代理ip大全'+'\n')

    semaphore = threading.Semaphore(5)
    lst = []
    t = threading.Thread(target=all_ip,args=(85,3196,10,10))
    t.start()
    lst.append(t)
    for rt in lst:
        rt.join()
