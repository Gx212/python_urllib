#HTTPErrr和UrlError

import urllib.request

url = 'https://blog.csdn.net/sheji888/article/details/140522047'
url_HTTPError = 'https://blog.csdn.net/sheji888/article/details/140522047250250250'
url_URLError = 'https://ababababbabb.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url= url_URLError,headers= headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    print("完成")
except urllib.error.HTTPError:
    print("HTTPError!!")
except urllib.error.URLError:
    print("URLError!!")
