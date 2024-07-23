"""post请求和get请求的不同之处"""

#post请求和get请求的异同：GET请求将数据附加在URL的查询字符串中，而POST请求将数据包含在请求体中。
import urllib.request
import urllib.parse
import json


url = 'https://fanyi.baidu.com/sug'# https://fanyi.baidu.com/sug指的是百度翻译的建议功能的URL。sug是指百度翻译的建议（suggestion）功能，用于获取与给定关键词相关的翻译建议。
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
    'kw':'wonderful'
}
#进行编码,由于urllib.Request的data参数是字节类型，使用encode('utf-8')转换成字节类型
data = urllib.parse.urlencode(data).encode('utf-8')
#请求对象定制
request = urllib.request.Request(url = url,data = data,headers = headers)
#模拟向浏览器发送请求
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')#获取的数据是json数据格式，需要将json数据转换成响应的对象
content_dict = json.loads(content)#由于得到的数据是json格式的字典类型数据，所以转换后的数据类型是字典
print(content_dict)
print(type(content_dict))
