#使用ajax的post请求肯德基官网的数据

import urllib.request
import urllib.parse

def creat_request(page):
    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    data = {
        'cname':'绵阳',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=base_url,headers=header,data=data)

    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open('kfc_'+ str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    for page in range(start_page,end_page+1):

        request = creat_request(page)

        content = get_content(request)

        down_load(page,content)

