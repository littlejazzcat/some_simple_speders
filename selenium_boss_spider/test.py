from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

'''
selenium使用流程：
1、确定浏览器驱动
2、确定访问网址
2.5、设置等待时间(如果是显式时间可以配合后面的元素查找一起设置)
3、查找元素、执行action_chain、执行action_chains4、、cchcho4、获取网页元素并提取数据
5、重复3和4直到任务完成

0、访问异常问题的解决：确定网址的有效性、ip是否可用
   解决反爬问题：设置代理ip，设置睡眠时间，js反爬等
'''

driver = webdriver.Chrome()
driver.get("https://www.zhipin.com/?ka=header-home")

locator = (By.CLASS_NAME, 'search-hot')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    #presence_of_element_located(tuple)方法用于检测传入的  元组  对应的元素是否在dom中出现了
except TimeoutError as e:
    print(e)

btn = driver.find_elements(By.CSS_SELECTOR,'div.search-hot > a:nth-child(2)')[0]
#通过css选择器查找对应的元素，返回的是一个可以执行js的对象

btn.click()  # 打开一个新选项卡窗口

all_handles = driver.window_handles  # 获取所有窗口句柄

driver.switch_to.window(all_handles[0])  # 切换到首页句柄
time.sleep(2)
js = "alert('提示弹窗')"  # js 代码
driver.execute_script(js)  # 执行JS
alt = driver.switch_to.alert  # 捕获网页弹窗
print(alt.text)  # 打印弹窗文本
time.sleep(2)
