"""1.input输入"""
# name = input("请告诉我你是谁：")
# print("原来你是%s" %name)

"""2.input输入的类型"""
# passkey = input("请告诉我你的银行卡密码：")
# print("你的银行卡密码是：%s" %type(passkey))
# print("你的银行卡密码是：%d" %passkey) #输出错误，input输入的是一个str类型

"""3.数据类型转换"""
# passkey = int(input("请输入你的密码："))
# print("你的密码原来是：%d" %passkey)

"""4.布尔类型和逻辑判断"""
# bool_1 = True
# bool_2  = False
# print(f"bool_1的变量内容是{bool_1},类型是{type(bool_1)} bool_2的变量内容是{bool_2},类型是{type(bool_2)}")

# name_1 = 'guoxin'
# name_2 = '聪明人'
# print(f"{name_1}是{name_2}是{name_1 == name_2}")

"""5.条件判断语句"""
# age = 18
# if age >= 18:
#     print(f"{age}岁已经成年了")
# else:
#     print(f"{age}岁还是未成年")

# age = int(input("你的年龄："))
# if age >= 18:
#     print("你已经成年，愉快玩耍吧！")
# elif (age >= 15 and age < 18):
#     print("你未成年，但是可以游玩规定项目")
# else:
#     print("抱歉，你不能进行游玩")

"""6.循环语句"""
# i = 0
# sum = 0
# while i < 100:
#     i+=1
#     sum+=i
#
# print(sum)

# import random
# num = random.randint(1,100)
#
# Flag = True
# while Flag:
#     guess_num = int(input("输入猜测的数字："))
#     if guess_num == num:
#         print("猜对了")
#         Flag = False
#     elif guess_num > num:
#         print("猜大了")
#     elif guess_num < num:
#         print("猜小了")

# print("你是谁？",end='')  print输出不换行
# print("我是扫把帚")

# i = 1
# j = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t",end='')
#         j+=1
#     print("\n")
#     i+=1
#

"""7.for循环"""
# name = '郭鑫'
# for x in name:
#     print(x)
#

# name = "akjhgdiha9geoiahdshadsg"
# count = 0
# for x in name:
#     if x == 'a':
#         count+=1
# print(count)

"""8.range语句"""
# 语法1
# num = 5
# for i in range(num):#0-num的数字序列
#     print(i)
#

# 语法2
# num = 5
# for i in range(2,num):#2-num数字序列
#     print(i)

# 语法3
# num = 8
# for i in range(2,num,2):#2-num,数字之间间隔2，同样不包含num
#     print(i)

# num = 100
# cout = 0
# for i in range(2,num,2):
#     cout+=1
#
# print(cout)

# num = 100
# count = 0
# for i in range(1,100):
#     if (i % 2) == 0:
#         count+=1
#
# print(count)

"""9.函数"""
# def print_hi():
#     print("hi,i am guoxin")

# def check():
#     print("欢迎来到这个美丽的世界\n请出示你的身份证表明身份")
# check()

"""函数传入参数"""
# def add_num(a,b):
#     result = a + b
#     return result
#
# x = int(input())
# y = int(input())
#
# num = add_num(x,y)
# print(f"{num}")

"""返回参数None"""
# def print_woord():
#     print("hello world")
#
# word = print_woord()
# print(f"{word}")
# print(type(word))

# name = None
# for i in range(1,10):
#     if i % 2 == 0:
#         name = 1
#
# print(type(name))

"""函数文档"""
# def num_add(x,y):
#     """
#     add函数可以实现两数相加的功能（x,y）
#     :param x: 参数1
#     :param y: 参数2
#     :return: 返回数字1和数字2的和
#     """
#     result = x + y
#     return result
#
#
# num_add(a,b)

"""10.数据容器"""
# name_list = ['郭鑫','李好',123]
#
# for i in name_list:
#     print(f"{i}的数据类型是{type(i)}")

"""10.1.数据容器之列表"""
# name_list = [[1,2,3],[4,5,6]]#列表的嵌套和列表下标索引
# for i in name_list:
#     print(i[1])
"""下标索引"""
# num_list = [1,2,3,4,5,6]
# name_list = [['郭鑫','妈妈','爸爸','姐姐'],['小明','小红','小军','小芳']]
# print(num_list[1])
# print(name_list[1][-3])

"""index方法查找元素下标"""
# num_list = [1,2,3,4,5,6]
# print(num_list.index(2))

"""修改列表指定元素内容"""
# num_list = [1,2,3,4,5,6]
# num_list[2] = '大坏蛋'
# print(num_list[2])

"""插入指定元素到指定位置"""
# name_list = ['myboy','mygirl','myson','mydog','mymom']
# # name_list.insert(2,'bigbadguy')
# # print(name_list[2])
# # for i in name_list:
# #     print(i)

""""追加指定元素"""
# name_list = ['bigboy','smallboy','apple']
# name_list.append('hahaha')
# for i in name_list:
#     print(i)

"""追加指定列表"""
# name_1 = ['guoxin','is','a']
# name_2 = ['good','boy']
# name_1.extend(name_2)
# for i in name_1:
#     print(i+' ',end='')

"""del关键字和pop方法"""
# num_list = [1,2,3,4,5,6]
# del num_list[2]
# for i in num_list:
#     print(str(i)+' ',end='')
#
# print()
#
# del_num = num_list.pop(2)
# for i in num_list:
#     print(str(i)+' ',end='')
# print('\n'+str(del_num))

"""remove方法"""
# num_list = [1,2,3,1,4,5,6]
# num_list.remove(1)
#
# for i in num_list:
#     print(i)

"""clear方法"""
# num_list = [1,2,3,4,5]
# print("清空列表前：")
# for i in num_list:
#     print(str(i)+' ',end='')
# num_list.clear()
# print("\n清空列表后：")
# for i in num_list:
#     print(i)

"""count方法"""
# num_list = [1,2,3,4,1,2,3,7,8]
# num = num_list.count(1)
# num_list_len = len(num_list)
# print(num)
# print(num_list_len)

"""列表的遍历"""
# my_list = ['我是','大哥','你是','小弟']
# index = 0
# for i in my_list:
#     print(i,end='')

"""10.2数据容器之元组"""

# my_tuple = ('你好',2,"hello")
# p = tuple()#空元组的定义
#
# print(f"my_tuple的数据类型是{type(my_tuple)},内容是：{my_tuple}")
# print(f"p的数据类型是：{type(p)}")
#
# name_list = ['你好']
# name_tuple = ('你好')#单个元素的元组必须用逗号分隔一下，否则类型是str
# print(name_list)
# print(f"name_tuple的数据类型是{type(name_tuple)}")

"""元组的嵌套"""

# name_tuple = ('你是谁？','我是郭鑫',('不','你不是','我才是'))
# index = name_tuple.index('你是谁？')
# for i in range(3):
#     if i == 2:
#         for k in name_tuple[i]:
#             print(k,end='')
#         continue

#     print(name_tuple[i])

"""10。3字符串"""
# name = "hallo world"
# for i in name:
#     print(i,end='')

# name = "wodemingzishiguoxin"
# value = name[10]
# value_2 = name[-3]
# print(f"value的值是{value},value_2的值是{value_2}")

# name = "guoxin"
# print("name中 xin 的起始下标是%d" %name.index('xin'))
# 字符串中index方法也是适用的，注意输出格式化的时候中间没有 ‘，’

"""replace替换方法"""
# name = "郭星"
# new_name = name.replace("星","鑫")
# print(f"{name}替换后的名字是{new_name}")

"""split分割方法"""
# song = "today is good day"
# song_split_list = song.split(" ")
# print(f"{song}分割后的列表是{song_split_list},类型是{type(song_split_list)}")
# for i in song_split_list:
#     print(i)

"""strip规整操作"""
# name = " guoxin "
# new_name  = name.strip()
# print(new_name)
# print(name)

# name = "2121guoxin1111"
# new_name = name.strip("21")
# print(new_name)

# str =  "guoxinisahandsome"
# count = str.count('guoxin')
# len = len(str)
# print(f"str中 guoxin 出现了{count}次，总体长度是{len}")

"""10.4序列的切片操作"""
# number = [0,1,2,3,4,5,6,7]
# num_1 = number[0:3:2]
# name = ('g','u','o','x','i','n')
# name_1 = name[::-1]
# print(f"name_1的类型是{type(name_1)},它的内容是{name_1}")
# print(f"num_1的类型是{type(num_1)},它的内容是{num_1}")

"""10.5集合"""
# my_set = {"我","名字","是","郭鑫","郭鑫","是","我的","名字"}
# print(my_set)
# my_set.add("郭鑫")
# print(f"添加第一个元素后的内容是{my_set}")
# my_set.add("大郭鑫")
# print(f"添加第二个元素后的内容是{my_set}")
# my_set.remove("我")
# print(f"移除一个元素后的内容是{my_set}")
#
# for i in my_set:
#     print(i)

"""pop"""
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,3,5,7,9,11}
# num = set_1.pop()
# print(f"取出的数据类型是{type(num)},数据是{num}")

"""_difference/得到新集合"""
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,3,5,7,9,11}
# set = set_1.difference(set_2)
# print(set)

"""_difference_update/改变原集合"""
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,3,5,7,9,11}
# set_1.difference_update(set_2)
# print(set_1)

"""union/合并两个集合"""
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,3,5,7,9,11}
# set = set_1.union(set_2)
# print(set)

"""10.6字典"""
# my_dict = {
#     "郭鑫" : 100,
#     "小明" : 200,
#     "小红" : 300
# }
# print(f"my_dict的内容是{my_dict},它的类型是{type(my_dict)}")
# print(f"郭鑫的考试成绩是{my_dict['郭鑫']}")
#
# my_dict["郭鑫"] = 250
# my_dict["张三"] = 1234
# print(f"my_dict已经更新，更新后的的值是{my_dict['郭鑫']}")
# print("现在字典中的成绩有：")
# for i in my_dict:
#     print(f"{i}的成绩是{my_dict[i]}")

""".pop 移除元素"""
# name_1 = my_dict.pop("郭鑫")
# print(name_1)#已经将郭鑫从数据中取出

""".keys 得到字典全部key"""
# keys = my_dict.keys()
# for i in keys:
#     print(my_dict[i])
#
# num = len(my_dict)
# print(f"字典全部元素有{num}个")

"""max（） min（）"""
# my_dict = {
#     "郭鑫" : 100,
#     "小明" : 200,
#     "小红" : 300
# }
#
# num = [1,2,3,4,5,6]
#
# name = max(my_dict)
# max_num = max(num)
#
# print(name)
# print(max_num)

# num = [1,7,5,3,68,9,2,234]
# print(sorted(num,reverse=True))

"""字符串大小比较"""
# a = 'a'
# b = 'c'
#
# if a > b:
#     print("ture")
# else:
#     print("false")

"""11.1函数多返回值"""

# def my_return():
#     a = 'x'
#     b = 2
#     return a,b
#
# x,y = my_return()
# print(f"x的类型是{type(x)},y的类型是{type(y)}")

"""11.2函数多种参数"""


# def user_imformation(name, age, gender):
#     print(f"{name}的年龄是{age},Ta的性别是{gender}")
#
# # user_imformation("小明", 18, "男")
#
# user_imformation(name = "郭鑫",gender='女',age = 20)

# def user_imformation(*args):
#     print(args)
#
# user_imformation("你好的",19,"我的名字")

# def user_imformation(**kwargs):
#     print(kwargs)
# user_imformation(姓名 = "小明",年龄 = 20,sex = '女')


"""11.3函数参数作为参数传递"""
# def test_fun(compute):
#     result = compute(1,2)
#     print(result)
#
# def compute(x,y):
#     return x+y
#
# test_fun(compute)#函数作为参数传递

"""lambda匿名函数"""
# def test_fun(compute):
#     result = compute(1,2)
#     print(f"结果是{result}")
#
# test_fun(lambda x,y:x+y)

"""12文件"""
"""12.1文件编码"""
#常用UTF-8

"""12.2文件的读取"""
"""1)打开指定路径的文件"""
# f = open("C:/Users/86183/Desktop/python_code/python测试文本.txt",'r',encoding="UTF-8")#encoding是关键字传参
# print(f"类型是{type(f)}")

"""2)读取文件 read()和关闭文件"""
# print(f"读取十字节的内容:{f.read(10)}")
# print(f"{f.readlines()}")

# print(f"{f.readline()}" ,end="")
# print(f"{f.readline()}")

# with open("C:/Users/86183/Desktop/python_code/python测试文本.txt",'r',encoding="UTF-8") as f:
#     print(f"文件的内容是{f.read()}")

"""小练习：文件字符串统计"""
# f = open("C:/Users/86183/Desktop/python_code/python测试文本.txt","r",encoding="UTF-8")
##方法一
# txt_list = f.readlines()
# count = 0
# for txts in txt_list:
#     word_find_list = txts.strip('\n').split(' ')
#     count = count + word_find_list.count('itheima')
# print(count)

##方法二
# count = f.read().count('itheima')
# print(count)

"""10.3文件的写操作"""
# f = open("C:/Users/86183/Desktop/python_code/python写操作练习文本.txt",'w',encoding = "UTF-8")
# f.write("你好美丽的新世界-guoxin")
# f.flush()

"""10.4文件的追加"""
# f = open("C:/Users/86183/Desktop/python_code/python写操作练习文本.txt",'a',encoding = "UTF-8")
# f.write("\n哈哈，我今天心情不是很好得勒")
# f.close()

"""11python异常"""
"""捕获异常"""
# try:
#     fr = open("C:/Users/86183/Desktop/python_code/捕获异常.txt", 'r', encoding="UTF-8")
# except:
#     fr = open("C:/Users/86183/Desktop/python_code/捕获异常.txt", 'w', encoding="UTF-8")

"""12.python模块"""

"""import"""
# import time
# time.sleep(2)
# print("我是郭鑫")

"""from xx import xx"""
# from time import sleep
# print("你好")
# sleep(2)
# print("我也好")

"""from xx import *"""
from time import *  # *表示导入全部功能，和直接import区别，不需要 模块名. 调用，直接使用
# print("你是:")
# sleep(2)
# print("郭鑫")

"""import xx as tt"""
# import time as t
# print("hello")
# t.sleep(2)
# print("hello too")

"""from xx import xx as xx"""
# from time import sleep as sl
# print("你好")
# sl(2)
# print("我是你爸爸")

"""自定义模块"""
# from my_module_1 import test
# num = test(2,1)
# print(f"{num}")

"""__main__变量"""
# from my_module_1 import test

"""__all__变量"""
# from my_module_1 import *
# test_add("halo")

"""13.python的包"""
# from my_packbage.my_module_1 import my_pythonbag_fun_1
# my_pythonbag_fun_1()

# import my_packbage.my_module_1
# my_packbage.my_module_1.my_pythonbag_fun_1()

"""练习：自定义工具包"""
# from my_utils.str_util import str_reverse
# my_str = 'guoxin'
# my_new_str = str_reverse(my_str)
# print(my_new_str)

"""字符串的拼接"""
# str_2 = ['haha','你','被','骗','了','吧']
# new_str_1 = ''
# for i in str_2:
#     new_str_1 += i
# print(f"方法一，转换后的字符串{new_str_1}")
# print(f"方法二，转换后的字符串{''.join(str_2)}")

"""回顾：自定义工具包"""

# from my_utils import file_util #其中my_utils是软甲的包，必须使用from xxx import调用

"""14.json数据格式"""
# import json #导入json模块
# #准备一个python列表，列表中每一盒元素都是字典，将其转换成json数据
#
# data = [{"郭鑫":"男","18":18},{"小明":"女","19":23},{"小军":"男","18":22},{"都是":"大笨蛋","猪猪侠":22}]
#
# json_data = json.dumps(data,ensure_ascii=False)#中文显示
# print(f"json_data数据类型是：{type(json_data)},数据内容是:{json_data}")
#
# data2 = '[{"\u90ed\u946b": "\u7537", "18": 18}, {"\u5c0f\u660e": "\u5973", "19": 23}, {"\u5c0f\u519b": "\u7537", "18": 22}, {"\u90fd\u662f": "\u5927\u7b28\u86cb", "\u732a\u732a\u4fa0": 22}]'
# python_data = json.loads(data2)
# print(f"python_data数据类型是：{type(python_data)},数据内容是:{python_data}"

"""15.pyechars构建基础折线图"""
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts
#
#
# #创建一个折线图
# line = Line()
# #设置x、y坐标数据
# line.add_xaxis(["中国","美国","英国"])
# line.add_yaxis("GDP",[30,20,10])
#
# #全局配置项
# line.set_global_opts(
#     title_opts=TitleOpts()
# )
# #通过render方法将代码生成图像
# line.render()

"""16.python 爬虫基础"""

# file_path = 'C:/Users/86183/Desktop/python_code/python_爬虫.txt'#给定一个路径，创建一个txt文件
# content = "笔记一"
#
# with open(file_path,'w') as file:
#     file.write(content)#在文件中写入
# print("文件创建成功")


# import json
# file_path = "C:/Users/86183/Desktop/python_code/python测试文本.txt"
# name_list = ['张三','王老五']
# name_json = json.dumps(name_list)
# name_str = str(name_list)
# print(type(name_json))

# with open(file_path,'w') as file:
#     file.write(name_str)

"""列表的序列化"""
# file = open('file_test.txt','w')#创建一个文本
# name_list = ['张三','李四']
# json.dump(name_list,file)//序列化列表

"""列表的反序列化"""
#1.0
# file = open('file_test.txt','r')
# content = file.read()
# content_list = json.loads(content)
# print(type(content_list))
# print(content_list)

#2.0
# file = open('file_test.txt','r')
# # print(json.load(file))
# print(type(json.load(file)))










