"""请求对象的定制，访问https网站时，会受到反爬机制影响，需要添加headers，定制一个请求对象（定制一个含有特定headers的请求对像）"""

import urllib.request

# url = 'https://www.baidu.com'#采用https协议，更加安全，使用python爬取网页信息会遭受反爬机制。需要定制对象,定制用户代理（UA）
#
# response = urllib.request.urlopen(url)
# content = response.read().decode('UTF-8')
# print(content)

#请求对象的定制
url = 'https://www.baidu.com'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url,headers = headers)#创建一个请求对象，添加请求头，注意关键字传参
response = urllib.request.urlopen(request)

content = response.read().decode('UTF-8')
print(content)



