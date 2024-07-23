import json

import jsonpath
import urllib.request

#jsonpath用于锁定JSON文件中的元素位置，区别与xpath，后者用于锁定html中的元素位置
#抓取网页中的JSON数据

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1721550868407_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'Referer': 'https://www.taopiaopiao.com/?tbpm=3'
}

request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

#将json文件写入本地
with open('taopiaopiao.json','w',encoding='gbk') as fp:
    fp.write(content)

#使用jsonpath进行定位，或者参考11_处理json文件,使用jsonpath能更简洁对json文件进行处理

with open('taopiaopiao.json','r',encoding='gbk') as file:
    data = json.load(file)

city_list = jsonpath.jsonpath(data,'$..regionName')
print(len(city_list))






