"""urllib的get请求"""

# import urllib.request
#
# #（1）定义一个url，为你访问的网页
# url= 'http://www.baidu.com'
# #（2）模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(url)
# #（3）获取响应中的页面源码
# content = response.read() #read返回的字节形式的二进制数据
# content_str = content.decode('UTF-8')#decode（‘编码格式’），对应页面的编码格式，在网页源码中charset查看编码格式
# #（4）答打印数据
# print(content_str)
#

"""____________________________________________________________"""
import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# content = response.read()#字节读取
# content2 = response.readline()#按行读
# content3 = response.readlines()
# content4 = response.getcode()#读状态码
# content5 = response.geturl()#返回访问的url
content6  = response.getheaders()#获取状态信息
print(content6)


