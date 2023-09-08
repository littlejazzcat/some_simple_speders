import requests
from lxml import etree


test = '<img src="/assets/mobile/images/loading.gif" lay-src="https://pic.3gbizhi.com/uploads/20230906/513145cb098219328ae51597e96ea7f3.jpg" alt="嘴巴叼着树叶的赵丽颖着白色高领衣眼神专注安静高清手机壁纸" title="嘴巴叼着树叶的赵丽颖着白色高领衣眼神专注安静高清手机壁纸" />'

html = etree.HTML(test)
info = html.xpath('//img/@lay-src')
title = html.xpath('//img/@title')

print(str(info),str(title))

with open(f"some_simple_spiders\\wallpaper_spider\\images\\{title}.jpg","wb+") as f:
    f.write()