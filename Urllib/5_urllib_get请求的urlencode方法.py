"""使用urlencode可以将字典或列表转成unicode编码"""

#urlencode的应用场景：多个参数的时候 会将 字典 中的键值对使用 & 拼接起来
import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

data = urllib.parse.urlencode(data)
url = base_url + data#请求资源的路径

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('UTF-8')
print(content)
