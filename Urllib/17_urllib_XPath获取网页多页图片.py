import urllib.request
from lxml import etree
#hippopx图片网的图片批量下载

#请求对象的定制,获取网页响应源码
def creat_request(page):
    if(page == 1):
        url = 'https://www.hippopx.com/zh/query?q=studio%20shot'
    else:
        #https://www.hippopx.com/en/query?q=studio%20shot&page=2
        url = f'https://www.hippopx.com/en/query?q=studio%20shot&page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url = url,headers= headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

#通过XPath锁定需要下载的图片的路径
def get_picture_link(html_content):
    tree = etree.HTML(html_content)
    src_result = tree.xpath("//li[contains(@itemprop, 'associatedMedia')]/descendant::img/@src")
    name_result = tree.xpath("//li[contains(@itemprop, 'associatedMedia')]/descendant::img/@title")

    # for i in range(len(src_result)):
    #     print(src_result[i],name_result[i])
    return src_result,name_result

#通过获取到的链接下载图片到指定路径
def download_pictures(src_result,name_result):
    for i in range(len(src_result)):
        urllib.request.urlretrieve(url=src_result[i],filename='./17_pictures/'+name_result[i]+'.jpg')

    print("下载完成")

if __name__ == '__main__':
    start_page = int(input("开始的页数："))
    end_page = int(input("结束的页数："))
    for page in range(start_page,end_page+1):
        src_result,name_result = get_picture_link(creat_request(page))
        # download_pictures(src_result,name_result)#下载函数，不要执行，内存不要啦！！





