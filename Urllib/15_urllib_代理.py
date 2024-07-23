import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)


#请求对象的定制
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')


#handler请求对象的定制 handler build_opener() open

#使用代理ip
proxies = {
    'http':'122.136.212.132:53281'
}

handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

content = opener.open(request)

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)

print("完成")
