"""使用quote方法将中文转换成unicode编码，加入url中"""

import urllib.request
import urllib.parse #注意添加parse

# url = 'https://www.baidu.com/s?wd=%E5%B0%9A%E9%9B%AF%E5%A9%95'#wd=后面跟着的是unicode编码下的‘尚雯婕’

url = 'https://www.baidu.com/s?wd='
name = '周杰伦'

url = url +(urllib.parse.quote(name))#将周杰伦转换成unicode编码格式

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

request = urllib.request.Request(url,headers = headers)#解决反爬的第一种手段
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')
print(content)
