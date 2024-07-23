"""爬取豆瓣评分第一页网页数据"""

#get请求
#目的：爬取豆瓣电影一个页面的电影数据

import urllib.request
import urllib.parse
import json

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'#注意start = 0，limit = 20
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#数据读取
request = urllib.request.Request(url,headers = header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = json.loads(content)

#创建一个文本用于储存数据，open默认的编码格式是gbk，需要使用utf-8打开才能保留汉字
file = open('movies_rank.txt','w',encoding='utf-8')

#循环下载
for movies in content:
    file.write(movies['title']+'\n')

#提示下载完成
print("下载完成")