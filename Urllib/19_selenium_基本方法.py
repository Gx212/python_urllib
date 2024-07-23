from selenium import webdriver
#selenium4版本后
from selenium.webdriver.chrome.service import Service

#创建webdriver对象
wd = webdriver.Chrome(service=Service('chromedriver.exe'))
#全局等待
wd.implicitly_wait(10)

#get方法打开网址
wd.get('https://www.baidu.com')

#定位元素并进行操作
from selenium.webdriver.common.by import By
#find_element和find_elements的区别，前者返回个体元素，后者返回集体元素

#获取input的value属性内容
element = wd.find_element(By.XPATH,'//*[@id="su"]')
content = element.get_attribute('value')
print(content)

#输入框
element = wd.find_element(By.XPATH,'//*[@id="kw"]')#定位元素
element.clear()#清除字符串
element.send_keys('你好')

#点击元素
element = wd.find_element(By.XPATH,'//*[@id="su"]')
element.click()



input("输入任意值结束程序...")



