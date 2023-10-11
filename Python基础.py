"""
矩阵乘法
"""
# 对应元素相乘
import numpy as np
m1=np.array([[1,2,3,4],[5,6,7,8]])
m2=np.array([[1,2,3,4],[5,6,7,8]])
print(m1*m2)
print(np.multiply(m1,m2))

# 矩阵乘法or内积
m1=np.array([[1,2,3,4],[5,6,7,8]])
m2=np.array([[1,2],[5,6],[7,8],[9,10]])
m3=np.array([1,2,3,4])
m4=np.array([5,6,7,8])
print(np.dot(m1,m2))
print(np.dot(m3,m4))
print(np.dot(m3,m4))



"""
Spyder 设置末班 路径：C:\Users\dell\Anaconda3\Lib\site-packages\spyder\plugins
"""

"""
np.random.shuffle(x) 
"""
现场修改序列，改变自身内容。（类似洗牌，打乱顺序）
np.random.permutation(x) 返回一个随机排列


"""
日期设置
"""
#时间戳
import time
s=time.time()
print(s)
# 转日期
time_array=time.localtime(s)
dt10=time.strftime('%Y-%m-%d %H:%M:%S',time_array)

#时间数组
time_array=time.localtime()
#日期格式(str)
dt=time.strftime('%Y-%m-%d %H:%M:%S',time_array)
dt1=time.strftime('%Y%m%d',time_array)
print(type(dt))
print('日期格式(str)',dt)
print('日期格式(str)',dt1)

#日期时间(datetime,date)
import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
print(type(today),type(yesterday))
#转换成日期格式(str)
today_str=datetime.date.strftime(today,'%Y-%m-%d')
print(today_str)

"""
异常值处理方法
"""
# _*_coding:utf-8 _*_
# @Time     :2019-07-01 11:07:09
# @Author   :
# @File     :
# @Software :
# @Comment  :
import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.randn(10,6))
# 生成区域随机数
df.iloc[1:3,1]=np.nan
df.iloc[5,3]=np.nan
df.iloc[7:9,5]=np.nan
# 判断是否存在缺失值
df.isnull()
# 存在缺失值行的数据
df[df.isnull().values==True]
# 存在缺失值列的数据
df.isnull().any()
# 滤除缺失值
    # 滤除缺失值（只要行存在缺失值即滤除该行）
df.dropna()
    # 滤除整行是缺失值的行
df.dropna(how='all')
    # 滤除整列是缺失值的列
df.dropna(how='all',axis=1)
# 填充缺失值
    # 不同列填充不同值
df.fillna({1:1,3:3})
    # 第2列notnull值填充为yes
df.loc[(df.loc[:,1].notnull()),1]='yes'
    # 第2列isnull值填充为no
df.loc[(df.loc[:,1].isnull()),1]='no'
    # 缺失值替换成0
df.fillna(0)
    # 缺失值以均值替换
df.fillna(df.mean())
    # 以前一个数据代替nan:method='pad'
df.fillna(method='pad')
    # 以后一个数据代替nan:method='bfill'
df.fillna(method='bfill')
    # 以插值法填充
df.interpolate()


"""
判断文件夹是否存在
"""
import datetime
import os

today=datetime.date.today()
yesterday=today-datetime.timedelta(days=0)
yesterday=datetime.date.strftime(yesterday,'%Y%m%d')
partPath="C:\\Users\\dell\\Desktop\\"
Path=partPath+str(yesterday)+".txt"
existFlag=os.path.exists(Path)
print(existFlag)

"""
日期时间格式转换
"""
#时间戳
import time
s=time.time()
print(s)

# 使用time
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

#时间数组
time_array=time.localtime()
#日期格式(str)
dt=time.strftime('%Y-%m-%d %H:%M:%S',time_array)
dt1=time.strftime('%Y%m%d',time_array)
print(type(dt))
print('日期格式(str)',dt)
print('日期格式(str)',dt1)

#日期时间(datetime,date)
import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
print(type(today),type(yesterday))
#转换成日期格式(str)
today_str=datetime.date.strftime(today,'%Y-%m-%d')
print(today_str)


"""
1 判断文件夹是否存在
"""
import datetime
import os

today=datetime.date.today()
yesterday=today-datetime.timedelta(days=0)
yesterday=datetime.date.strftime(yesterday,'%Y%m%d')
partPath="C:\\Users\\dell\\Desktop\\"
Path=partPath+str(yesterday)+".txt"
existFlag=os.path.exists(Path)
print(existFlag)

import time
import pandas as pd
import pymysql
import sqlalchemy
import numpy as np
import json
import datetime
import os


"""
标准化
"""
import pandas as pd
import numpy as np
df=pd.DataFrame({'a':[1,2,3],'b':[5,6,7]})
df
x=df.apply(lambda df:(df-np.min(df))/(np.max(df)-np.min(df,axis=0)))
"""
     a    b
0  0.0  0.0
1  0.5  0.5
2  1.0  1.0
"""



"""
DataFrame的reset_index()函数用法：
"""
df.reset_index() #将会将原来的索引index作为新的一列
 index	A	B	C
0	0	1	2	3
1	2	2	4	5
2	4	2	5	6
#############################
#使用drop参数设置去掉原索引
df.reset_index(drop=True)
    A	B	C
0	1	2	3
1	2	4	5
2	2	5	6



"""
DataFrame groupby  apply
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
    'key2' : ['one', 'two', 'one', 'two', 'one'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)})
# 1
grouped = df['data1'].groupby(df['key1']).mean()

# 2
for (k1,k2), group in df.groupby(['key1','key2']):
    print k1,k2
    print group

# 3
names.groupby(['year', 'sex']).apply(add_prop)



"""
train_test_split
"""
from sklearn.model_selection import train_test_split

from sklearn.cross_validation import train_test_split

"""
np.concatenate()  
pd.concat()
"""
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6]])
arr22=arr2.T
# 合并行
np.concatenate((arr1,arr2),axis=0)
# 类似合并列
np.concatenate((arr1,arr22),axis=1)

import pandas as pd
data1=pd.DataFrame(np.arange(0,16).reshape(4,4),columns=list('abcd'))
data2=[
  [4,1,5,7],
  [6,5,7,1],
  [9,9,123,129],
  [16,16,32,1]
]
data2 = pd.DataFrame(data2,columns = ['a','b','c','d'])
# 合并列
pd.concat([data1,data2],axis=1)
# 合并行
pd.concat([data1,data2],axis=0)


"""
DataFrame  isnull
"""
df.Column[df.Column.isnull()==False]


"""
pd.qcut & pd.cut
"""
import pandas as pd
import numpy as np
data=np.random.randn(1000)

# qcut样本分位数
    # 左开右闭
cats=pd.qcut(data,4)
print(cats)
    # 分组后的data区间
cats_=pd.qcut(data,[0,0.1,0.5,0.7,1])
print(cats_)
cats_count=pd.value_counts(cats)
print(cats_count)

# cut 分成指定组
catss=pd.cut(data,5)
print(catss)
    # 指定分组的上下限
bin=[-4,0,1,2,3]
catss_=pd.cut(data,bins=bin)
print(catss_)

df=pd.DataFrame({'data':data,'bucket':pd.cut(data,[-4,0,1,3])})
print(df)


"""
df.apply函数
"""
DataFrame.apply(func, axis=0, broadcast=False, raw=False, reduce=None, args=(), **kwds)
    这个函数需要自己实现，函数的传入参数根据axis来定，比如axis = 1，就会把一行数据作为Series的数据
结构传入给自己实现的函数中，我们在函数中实现对Series不同属性之间的计算，返回一个结果，则apply函数
会自动遍历每一行DataFrame的数据，最后将所有结果组合成一个Series数据结构并返回。
 df_final_1['abs_error']=df_final_1.apply(lambda row:abs(row['unit_actual_mean_price_tmp_standard']-row['actual_anticipate_profit_sum_standard']),axis=1)
 
"""
df 分组top
"""
def top(df,by_column='abs_error',n=1):
    return df.sort_values(by=by_column,ascending=True).head(n)

df_final_2=df_final_1.groupby('lst').apply(top)


"""
.read()、.readline() 和 .readlines()
"""
.read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
.readline() 和 .readlines() 之间的差异是后者一次读取整个文件

"""
定义MySQL类
"""
import pymysql
class Mysql:
    def __init__(self,database,host="localhost",user="root",password="052206",port=3306,charset='utf8'):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.database=database
        self.charset=charset
    def connect(self):
        self.cnn=pymysql.connect(database=self.database,
                                 host=self.host,
                                 user=self.user,
                                 password=self.password,
                                 port=self.port,
                                 charset=self.charset)
        self.cursor=self.cnn.cursor()

    def close(self):
        self.cursor.close()
        self.cnn.close()

    def exec(self,sql):
        """
        只能执行一个语句不能执行多个
        :param sql: 
        :return: 
        """
        try:
            self.connect()
            self.cursor.execute(sql)
        except:
            print('error')
        self.close()

    def exec_(self,sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.cnn.commit()
        except:
            self.cnn.rollback()
        self.close()
"""
os
"""
os.rmdir(path)# 只能删除空文件夹，否则报错
os.remove(path)# 只能删除文件，否则报错



"""
re
"""
不能在产品代码中链式调用search()和groups()
的原因。如果search()方法匹配不成功，也就是返回None，这
就不是返回的一个正则表达式匹配对象。它没有groups()方
法，所以调用None.groups()将会抛出一个异常

phonePattern = re.compile(r'^(\d{3})‐(\d{3})‐
(\d{4})‐(\d+)$')
phonePattern.search('800‐555‐1212‐1234')
# 匹配到则，返回元组
phonePattern.search('800‐555‐1212‐1234').groups

re 模块是正则表达式的Python实现。它有一个漂亮的函数
findall()，接受一个正则表达式和一个字符串作为参数，然后
找出字符串中出现该模式的所有地方。在这个例子里，模式匹
配的是数字序列。findall()函数返回所有匹配该模式的子字符
串的列表。  


Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36


"""
字典排序
"""
a={'a': 1, 'b': 0}
sorted(a.items(),key=lambda item:item[1])




"""
sys.stdin.readline()  input()
"""
import sys
print('Plase input your name: ')
name = sys.stdin.readline()
print('Hello ', name)

python3中使用sys.stdin.readline()可以实现标准输入，其中默认输入的格式是字符串，如果是int，float类型则需要强制转换。


"""
python中的operator.itemgetter函数
"""
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号
要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
import operator 
a=[0,1,2]
ope=operator.itemgetter(0) # 函数ope，获取对象的第0个域的值
b=ope(a)# 调用函数

ope=operator.itemgetter(1,0) # 获取对象的第1个域和第0个的值
b=ope(a)# 调用函数

sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])
a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(a, key=operator.itemgetter(1,2))



# itertools.groupby
friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
def height_class(h):
    if h>180:
        return 'tall'
    elif h<160:
        return 'short'
    else:
        return 'middle'
friends = sorted(friends,key = height_class)
for m,n in groupby(friends,key = height_class):
    print m
    print list(n)
	
	
"""
map  reduce 
"""
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
map(function, iterable, ...)

x=[1,2,3]
x_map=list(map(lambda x0:x0*2,x))

x_1=[1,2,4]
x_2=[4,5,6]
x_1_2=list(map(lambda x_10,x_20:x_10+x_20,x_1,x_2))

reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
reduce(function, iterable[, initializer])

from functools import reduce
x=[1,2,6]
x_map=reduce(lambda x0,x1:x0+x1,x)


"""
Python使用pywin32关闭窗口
"""
python写脚本的时候，遇到这么一个问题，笔者需要通过脚本去关闭一些窗口，比如关闭浏览器的窗口。这种关闭行为类似于手动去点叉关闭（比较温和，窗口程序可以有反应的时间），而不是强制地kill进程（比较暴力，但是导致窗口来不及进行一些处理就被关闭）。

笔者使用的方法是通过枚举当前可视的所有窗口，判断窗口的标题。例如要关闭Chrome，就判断窗口的标题是否含有“Chrome”，如果有，则将其关闭。这种方法可能会关闭一些其它的窗口，所以使用的时候要小心一点。但是优点是实现起来非常简单。
笔者使用的Python版本为3.4，需要额外使用一个pywin32来操纵windows平台的窗口。
Python代码：
import win32gui
from win32.lib import win32con
import time

def handle_window(hwnd, extra):

    if win32gui.IsWindowVisible(hwnd):

        if 'Chrome' in win32gui.GetWindowText(hwnd):

            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
if __name__ == '__main__':
    win32gui.EnumWindows(handle_window, None)
    time.sleep(5)
    # TODO If app didn't close, force close.
	
"""
sys.path
"""
sys.path是python的搜索模块的路径集，返回的结果是一个list
path[0]
此列表的第一项，path[0],在程序启动时初始化，是包含用来调用Python解释器的脚本的目录。如果脚本目录不可用（例如，如果解释器被交互式地调用，或者脚本是从标准输入读取的），path[0]是空字符串，它引导Python首先在当前目录中搜索模块。 
比如在C:User\chenxi3\Destop\Simplify中有一个testSysPath. py

import sys
print("\n".join(sys.path))
 
输出是：
C:\Users\chenxi3\Desktop\Simplify 
C:\Python27\DLLs 
C:\Python27\lib 
C:\Python27\lib\plat-win 
C:\Python27\lib\lib-tk 
C:\Python27 
C:\Python27\lib\site-packages

path[0] 是C:\Users\chenxi3\Desktop\Simplify，调用python解释器的脚本所在的目录。 其实就是存放需要运行的代码的路径

什么是python解释器？（下面是选取廖雪峰老师文章的总结）

当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。


"""
bat执行python脚本，执行多条命令
"""

1、新建一个txt文档，输入以下命令

@echo off
cmd /k python F:\Pycharm_Projection\Test\test2.py

2、将txt文档保存为.bat格式，然后双击运行即可

例如我要是想打开labelImg打标签工具：

@echo off
start python device_statistics_exporter_old.py d 2019 1 31> 2019-1-31五大指标.csv
start python device_statistics_exporter_old.py d 2019 1 30> 2019-1-30五大指标.csv
start python device_statistics_exporter_old.py d 2019 1 29> 2019-1-29五大指标.csv
exit


"""
正则表达式
"""
模式	描述
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a|b	匹配a或b
(re)	对正则表达式分组并记住匹配的文本
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)	匹配的独立模式，省去回溯。
\w	匹配字母数字及下划线
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。




"""
python中3种调用可执行文件.exe的方法
"""
方法一、os.system()  会保存可执行程序中的打印值和主函数的返回值，且会将执行过程中要打印的内容打印出来

import os  
main = "project1.exe"
r_v = os.system(main) 
print (r_v )
方法二、commands.getstatusoutput()  会保存可执行程序中的打印值和主函数的返回值，但不会将执行过程中要打印的内容打印出来

import subprocess  
import os  
main = "project1.exe"
if os.path.exists(main):  
    rc,out= subprocess.getstatusoutput(main)  
    print (rc)
    print ('*'*10)
    print (out)
方法三、popen()  会保存可执行程序中的打印值，但不会保存主函数的返回值，也但不会将执行过程中要打印的内容打印出来

import os
main = "project1.exe"
f = os.popen(main)    
data = f.readlines()    
f.close()    
print (data)
另外，上面提到的三种方式，实际上都是在python中执行命令，因此他们不只是用来执行可执行文件，也可以用来执行linux系统中别的指令。



python pip快速安装
pip install --index https://pypi.mirrors.ustc.edu.cn/simple/ pandas



python3下列代码会报上边的错
print("Response:", resp.text.decode('unicode_escape'))
response.text
'{"success":true,"listCount":207051,"list":[{"KeyNo":"fec4bc109643726db7b5762ca4c2104c","Name":"\\u6df1\\u5733\\u5e02\\u9f99\\u5c97\\u533a\\u5434\\u71d5\\u4e91\\u670d\\u88c5\\u767e\\u8d27\\u5e97","OperName":"\\u5434\\u71d5\\u4e91",
解决办法：
print("Response:", resp.text.encode('utf-8').decode('unicode_escape'))
中间加上.encode('utf-8')即可。
{"success":true,"listCount":207051,"list":[{"KeyNo":"fec4bc109643726db7b5762ca4c21
问题原因：
python3里面，字符串要先encode手动指定其为某一编码的字节码之后，才能decode解码。
————————————————
版权声明：本文为CSDN博主「请保持优秀。」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/IT_TIfarmer/java/article/details/90747496

"""
python实现Content-Type类型为application/x-www-form-urlencoded发送POST请求
"""
在实际编码的过程中经常遇到header的Content-Type的类型主要是application/json格式，我这里也没有考虑到与application/x-www-form-urlencoded区别还按照以前方式来写代码，每次请求都会提示"缺少必要参数"，我这里明明已经传入body数据为什么依然报错，所以回头查询下文档，发现Content-Type的类型为application/x-www-form-urlencoded时，body的格式不是json格式，所以会报错。

　　application/x-www-form-urlencoded属于比较常用的POST 提交数据的方式。浏览器的原生 form 表单，如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数据。
　　如果Content-Type 设置为 application/x-www-form-urlencoded；此时body提交的数据需要按照 k1=v1&k2=v2 的方式进行编码,然后进行提交，下面我们看看python代码如何实现。

# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 15:22
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : example.py
# @Software: PyCharm
import requests
import json
from urllib import parse

# 定义请求header
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'Key': '332213fa4a9d4288b5668ddd9'}
# 定义请求地址
url = "https://api.newrank.cn/api/sync/weibo/trend"
# 通过字典方式定义请求body
FormData = {"from": '2018-07-18 16:00:00', "to": '2018-07-18 18:00:00', "page": 1, "size": 1}
# 字典转换k1=v1 & k2=v2 模式
data = parse.urlencode(FormData)
# 请求方式
content = requests.post(url=url, headers=HEADERS, data=data).text
content = json.loads(content)
print(content)



xlrd.biffh.XLRDError: Excel xlsx file; not supported:
指定打开引擎 xlsx=pd.read_excel(r"C:\Users\W\Desktop\text_pd.xlsx",engine='openpyxl')


## 
xlsx_2_pivot=pd.pivot_table(
    df,
    index= ["城市","日期"], 
    columns= ["航空公司","航线"],
    values= ["出票数量","登机人数"]
    aggfunc= sum
    )

# 将multiindex变成colums
xlsx_2_pivot.reset_index(inplace=True)


## 百分比转换 
f1 = lambda x:'%.2f%%' % (x*100)
## 应用到列
result["金额占比"] = result["金额占比"].apply(f1)
