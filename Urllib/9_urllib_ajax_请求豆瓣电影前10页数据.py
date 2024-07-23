"""下载豆瓣电影前10页数据"""
import urllib.request
import urllib.parse
import json

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20
#规律 start = （page-1）*20


start_page = int(input("输入起始页码"))
end_page = int(input("输入截止页码"))

headers = {
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',#这句一定注释掉
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'bid=JU_5WMiQAVw; _pk_id.100001.4cf6=3ce5bcd411c1b310.1705138099.; ll="118323"; _vwo_uuid_v2=D9DB1F9283DED2AB238AF42A94A92A6F8|c36a3d198fb7b57c527962d08213a478; ap_v=0,6.0; __utma=30149280.434252480.1705138099.1705382629.1705408355.4; __utmb=30149280.0.10.1705408355; __utmc=30149280; __utmz=30149280.1705408355.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1626457362.1705138099.1705382629.1705408355.4; __utmb=223695111.0.10.1705408355; __utmc=223695111; __utmz=223695111.1705408355.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1705408355%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
}

for page in range(start_page,end_page+1):
    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20'.format((page - 1) * 20)#使用格式化字符串
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    content_dict = json.loads(content)
    for movies in content_dict:
        print(f"排名：{movies['rank']} 电影名：{movies['title']}")

print("爬取结束")

