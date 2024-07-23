import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#获取的网页源码
request = urllib.request.Request(url = url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

#解析网页源码中的数据，此次解析其中的“百度一下”四个字
from lxml import etree

#解析获取的服务器响应的文件
tree = etree.HTML(content)

#解析服务器响应的文件，利用XPath路径查找,XPath的返回值是一个列表形式的值
result = tree.xpath("//*[@id='su']/@value")[0]

print(result)


