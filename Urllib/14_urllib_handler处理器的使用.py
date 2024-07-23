#使用Handler使请求过程更加的精细可控
import urllib.request
url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url,headers = headers)

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(content)
print("完成")
