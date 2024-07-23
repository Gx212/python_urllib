import socket
import struct
import math
import numpy as np
HOST = "192.168.130.128"    # The remote host
PORT = 30003        # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

dic= {'MessageSize': 'i', 'Time': 'd', 'q target': '6d', 'qd target': '6d', 'qdd target': '6d','I target': '6d',
      'M target': '6d', 'q actual': '6d', 'qd actual': '6d', 'I actual': '6d', 'I control': '6d',
      'Tool vector actual': '6d', 'TCP speed actual': '6d', 'TCP force': '6d', 'Tool vector target': '6d',
      'TCP speed target': '6d', 'Digital input bits': 'd', 'Motor temperatures': '6d', 'Controller Timer': 'd',
      'Test value': 'd', 'Robot Mode': 'd', 'Joint Modes': '6d', 'Safety Mode': 'd', 'empty1': '6d', 'Tool Accelerometer values': '3d',
      'empty2': '6d', 'Speed scaling': 'd', 'Linear momentum norm': 'd', 'SoftwareOnly': 'd', 'softwareOnly2': 'd', 'V main': 'd',
      'V robot': 'd', 'I robot': 'd', 'V actual': '6d', 'Digital outputs': 'd', 'Program state': 'd', 'Elbow position': '3d', 'Elbow velocity': '3d'}

data = s.recv(1108)
names=[]
ii=range(len(dic))#创建一个dic长度的正数列表
for key,i in zip(dic,ii):#zip 将dic和ii对应元素打包成一个个元组，返回这些元组组成的列表，遍历这些列表
    fmt_size=struct.calcsize(dic[key])#struct.calcsize(fmt)，是struct模块中的一个函数，用于计算给定格式符(fmt)所代表的结构体字节数
    data1,data=data[0:fmt_size],data[fmt_size:]
    fmt="!"+dic[key]#首位为！，即为大端模式标准对齐方式
    names.append(struct.unpack(fmt, data1))
    dic[key]=dic[key],struct.unpack(fmt, data1)
# print(names)
a=dic["Tool vector actual"]
# a2=np.array(a[1])
print(a)