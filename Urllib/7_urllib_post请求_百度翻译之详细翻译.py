"""第二种反爬机制，需要提供cookie"""
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
#其中cookie最重要，第二种反爬机制，cookie
headers = {
        # 'Accept': '*/*',
        # # 'Accept-Encoding': 'gzip, deflate, br',                 #编码方式一定注释掉
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Acs-Token': '1705057661905_1705136702722_15YJKNLZYh5dkF7IgElz9yYgtQ5OD8T4oHu2I37g/BNvD8n4byCt+2wT5rfyc0q/QRGJMNyMixgeiTQloXT1z4GKI3iEF/OuBF3OzyDh9rOVV5vXbAPrhh4NXW3+W4aMpJE7E7DuHzPUv+n07MqLRXVbRUsOgeJnUPlf92QyumpSoRtP+7Yth+XEAVnS2KEGhhvWD16hBoU22sB5McHTzAH58+zWZYs9xfS7Gp4YkTI798360P/44EzUCfDyC/MiJbDiSHf7vGO4IoHZT0HEN5kAXHiS4xHXSc01NZozOs8RqbQ/1id570oJzpmgulAddSlXIwZGqhrMAoDJhj9yXwxff81v5zqawu4drfJALWRlMdc/1hUSnEycPR0+AOgy1t5YBtmEu1QXKy9EGiEsTblmAxJLD1rU6qzfMWVh0d4SZlNi+xcy8OLq0ryxarkDahVhV+ifXM5RRid5FEmUgwrYNaEe5MfGUSJ7pWJu1vU=',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '151',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BIDUPSID=216F248235DA54791265266B79C1C364; PSTM=1678803627; BAIDUID=E083A15AB1CC195175CDA97A6F170F94:FG=1; BDUSS=RoSGpWb1UyMjVsVFh1MGY0dUtFeDA2dlZ5Y0Z5VFpwRlN3cDVqbkY3aFRESkJsSVFBQUFBJCQAAAAAAAAAAAEAAAC2JWv40KHWvcz1Q2FsbQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFN~aGVTf2hlSU; BDUSS_BFESS=RoSGpWb1UyMjVsVFh1MGY0dUtFeDA2dlZ5Y0Z5VFpwRlN3cDVqbkY3aFRESkJsSVFBQUFBJCQAAAAAAAAAAAEAAAC2JWv40KHWvcz1Q2FsbQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFN~aGVTf2hlSU; H_PS_PSSID=39997_39919_40026_40044_39939; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=2gal8g0181810g00858001810mdqqv1iq4g3p1s; delPer=0; PSINO=6; ZFY=6kIkEkH6yWAhlBrVxZ8b2Oqas1ZK5FIxKFOm1SUtCOc:C; BAIDUID_BFESS=E083A15AB1CC195175CDA97A6F170F94:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1705132157; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1705132415; ab_sr=1.0.1_YmNmYmQxNzhiMmY3MDgzYThlYTYzNzk0Yzg5MTQxMjAwNGY0NTdlOThhMzUyOTZmNzA0YWQ1ZDMwM2U3MzcxMzYzMGYxZWYyMTI3NWI2NGJlMjkzNmE3OWY1NGQ3NmM3MjlkOTUxNzU3ZjkwZTVjZTc1YzIwNjZjNjNjNDFlYjlmYTA5OTdjN2NlMDA2ZGViZDQ3MGJkYmE5MGMxNWIwNjA3NGJkNjhlZDBlYzI3ZTY0YTAxNTk4ZDc4Y2IyY2Yx',
        # 'Host': 'fanyi.baidu.com',
        # 'Origin': 'https://fanyi.baidu.com',
        # 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'moon',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '22215.308726',
    'token': '1959cf9ee218386fa08e577835c4781d',
    'domain': 'common',
    'ts': '1705136702697',
}

data = urllib.parse.urlencode(data).encode('utf-8')#将data转换成字节
request = urllib.request.Request(url = url,data = data,headers = headers)#请求对象的定制
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(json.loads(content))

