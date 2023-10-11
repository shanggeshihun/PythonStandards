"""
P1 001.爬虫前奏什么是网络爬虫
"""
1.通用爬虫:通用爬虫是搜索引擎抓取系统(百度、谷歌、搜狗等)的重要组成部分。主要是将互联网上的网页下载到本地，形成一个互联网内容的镜像备份。
2.聚焦爬虫:是面向特定需求的-种网络爬虫程序，他与通用院虫的区别在于:聚焦爬虫在实施网页抓取的时候会对内容进行筛选和处理，尽量保证只抓取与需求相关的网页信息。

"""
P2 002.爬虫前奏 HTTP协议介绍
"""
HTTP协议:全称是HyperText Transfer Protoco1 , 中文意思是超文本传输协议，是一种发布和接收HTML页面的方法。服务器端口号是80端口。
HTTPS协议:是HTTP协议的加密版本，在HTTP下加入了SSL层。服务器端口号是443端口。

url详解:
URL是Uniform Resource Locator 的简写，统-资源定位符。
一个URL由以下几部分组成:
schene://host:port/path/?query-stringexxxCanchor

●scheme:代表的是访问的协议，一般为http或者htts以及ftp 等。
●host:主机名，城名，比如www.baidu.com。
●port: 端口号。当你访问一个网站的时候，浏览器默认使用80端口。
●path:查找路径。比如: www.jianshu.com/trending/now ，后面的trending/now就是path。
●query-string: 查询字符串，比如: www.baidu.com/snd-python ，后面的wd=python 就是查询字符串。
●anchor:锚点，后台一般不用管，前端用来做页面定位的。
在测览器中请求一个url,浏览器会对这个uri进行-一个编码。除英文字母，数字和部分符号外，其他的全部使用百分号+十六进制码直进行编码。


"""
P3 003.爬虫前奏_抓包工具的使用网络请求
"""
常用的请求方法:
在Http协议中，定义了八种请求方法。这里介绍两种常用的请求方法，分别是get请求和post请求。
1. get请求: -般情况下，只从服务器获取数据下来，并不会对服务器资源产生任何影响的时候会使用get请求。
2. post请求:向服务器发送数据(登录)、上传文件等，会对服务器资源产生影响的时候会使用post 请求。
以上是在网站开发中常用的两种方法。并且一般情况下都会遵循使用的原则。但是有的网站和服务器为了做反爬虫机制，也经常会不按常理出牌，有可能一个应该使用get方法的请求就一定要改成 post请求，这个要视情况而定。

请求头常见参数:|
在http协议中，向服务器发送-一个请求，数据分为三部分，第一个是把数据放在url中，第二个是把数据放在body 中(在post 请求中)，第三个就是把数据放在hed中。这里介绍在网刚爬虫中经常会用到的一些请求头参数: 
1. User-Agent : 浏览器名称。这个在网络爬虫中经常会被使用到。请求-个网页的时候， 服务器通过这个梦数就可以知道这个请求是由哪种浏览器发送的。如果我们是通过爬虫发送请求，那么我们的User-Agent 就是Python ,这对于那些有反爬虫机制的网站来
说，可以轻易的判断你这个请求是爬虫。因此我们要经常设置这个值为-些浏览器的值， 来伪装我们的爬虫。
2. Referer :表明当前这个请求是从哪个url过来的。这个一般也可以用来做反化虫技术。如果不是从指定页面过来的,那么就不做相关的响应。
3. Cookie : http 协议是无状态的。也就是同一一个人发送了两次请求,服务器没有能力知道这两个请求是否来自同一个人。因此这时候就用cookie 来做标识。一般如果想要做登录后才能访问的网站，那么就需要发送cookie信息了。


常见响应状态码:
1. 200:请求正常，服务器正常的返回数据。
2. 301 :永久重定向。比如在访问www.jingong.com的时候会重定向到ww.jd.com
3. 302 :临时重定向。比如在访问一一个需要登录的页面的时候，而此时没有登录，那么就会重定向到登录页面。
4. 400 :请求的ur1在服务器上找不到。换句话说就是请求ur1错误。
5. 403 :服务器拒绝访问，权限不够。
6. 500 :服务器内部错误。可能是服务器出现bug了。



"""
P4 1_urlopen函数用法
"""
urllib库
urlli1b库是Python 中一个最基本的网络请求库。可以模拟浏览器的行为,向指定的服务器发送一个请求，并可以保存服务器返回的数据。

urlopen函数:
在Python3的ur1l1b库中，所有和网络请求相关的方法，都被集到urllb.request模块下面了,以先来看下urlopen 函数基本的
使用:
from ur11ib import request
resp中request.urlopen('http:/www.baidu.com')
print(resp.read())
实际上，使用刘览器访问百度，右键查看源代码。你会发现，跟我们刚才打印出来的数据是一样的。也就是说，上面的三行代码
就已经帮我们把百度的首页的全部代码爬下来了。一个基本的ur请求对应的python代码真的非常简单。
以下对urlopen 函数的进行详细讲解:
1. url :请求的url.
2. data :请求的data ,如果设置了这个值，那么将变成post请求。
3.返回值:返回值是一个htp.cilet.HTTPResponse 对象，这个对象是一-个类文件句柄对象
有read(site)、readline 、readlines 以及cetcode等方法。



"""
P5 2_urlretrieve函数用法函数用法
"""
urlretrieve函数:
这个函数可以方便的将网页上的一一个文件保存到本地。以下代码可以非常方便的将百度的首页下载到本地: .
from u11ib import request
request.urlretrleve( 'http://www.baidu.com/',"baidu .html')

"""
P6 3_参数编码和解码函数
"""
urlencode函数:
用浏览器发送请求的时候，如果url中包含了中文或者其他特殊字符，那么浏览器会自动的给我们进行编码。而如果使用代码发送请
求，那么就必须年动的进行编码，这时候就应该使用urlencode函数来实现。urlencose 可以把字典数据转换为URL 编码的數据。
示例代码如下:
from ur11ib import parse
data={'nase":"爬业基码","ereet":"he1lo wor10","age" :100}
qs= parse.urlencode(data)
print(qs)

from urllib import request
from urllib import parse
url= 'http://www.baidu.com/s'
params ={"wd" :"刘德华"}
gs=parse.urlencode(params)
url=url+"?"+qs
resp=request.urlopen(url)
print(resp.read())


parse_qs 函数:
可以将经过编码后的url参数进行解码。示例代码如下:
from ur11ib import parse
data={'nase":"爬业基码","ereet":"he1lo wor10","age" :100}
qs= parse.urlencode(data)
print(qs)
result=parse.parse_qs(qs)
print(result)

"""
P7 4urlparse和urlsplt函数用法
"""
urlparse和urlsplit:
有时候拿到一个url,想要对这个url中的各个组成部分进行分割，那么这时候就可以使用urlparse或者是urlsplit来进行分割。示
例代码如下:

from urllib import parse
url="http://www.baidu.com/s?wd=python&usernmae=abc#1"
result=parse.urlparse(url)
print(result)
print(result.scheme)
result1=parse.urlsplit(url)
print(result)
urlparse和urlsplit基本上是一模一样的。唯-不一样的地方
是，urlparse里面多了一个params属性，而urlspllt没有这个parans属性。


"""
P8 5实战-用Request爬取拉勾网职位信息
"""
request.Request类:
如果想要在请求的时候增加一些请求头(urlopen无请求头参数),那么就必须使用reuest.Request 类来实现。比如要增加一个Uuser-agent , 示例代码如
下:
from urllib import request
headers ={
"User-Agent": "Hozil1a/5.0 (Hindons NT 10.0; Hin64; x64) ApplelebKit/537.36 (KHTHL, like Gecko) Chrome/62.0.3202.94"
}
#请求类
req=request.Request("http://www.baidu.com/" ,headers=headers)
#发送请求
resp=request=urlopen(req)
print(resp.read())


from urllib import request
from urllib import parse
headers ={
"User-Agent": "Hozil1a/5.0 (Hindons NT 10.0; Hin64; x64) ApplelebKit/537.36 (KHTHL, like Gecko) Chrome/62.0.3202.94",
"refer":""
}
data={
'first' :'true'，
'pn': 1,
'kd : 'python'
}
#请求类
req=request.Request("http://www.baidu.com/" ,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='post')
#发送请求
resp=request=urlopen(req)
print(resp.read().decode('utf-8'))


"""
P75 11ajax介绍和爬取ajax数据的两种方式
"""
动态网页数据抓取
什么是AJAX:
AJAX (Asynchronouse JavaScript And XML)异步JavaScript和XML.过在后台与服务器进行少量数据交换，Ajax可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。传统的网页(不使用Ajax)如果需要更新内容,必须重戟整个网页页面.因为传统的在传输数据格式方面，使用的是XPL语法。因此叫做AJAX ,其实现在数据交互基本上都是
使用ISON 。使用AJAX加载的数据，即使使用了JS,将数据渲染到了浏览器中，在石证τ>查石网页源代码还是不能看到通过ajax加载
的数据,只能看到使用这个ur加载的html代码。

获取ajax数据的方式:
1.直接分析ajax调用的接口。然后通过代码请求这个接口。
2.使用Selenium+ chromedriver模拟浏览器行为获取数据。|

方式 优点 缺点
分析接口
直接可以请求到数据。不需要做一些解析工作，代码量少，性能高。 分析接口比较复杂, 特别是通过js混淆的接口，要有一定的js功底。容易被发现是爬虫。

selenium
直接模拟浏览器的行为。浏览器能请求到的，使用selenium也能请求到。爬虫更稳定。
代码量多,性能低。

"""
P76 12selenium + chromedriver安装和入门
"""
Selenium+chromedriver获取动态数据:
Selenlum相当于是一个机器人。可以模拟人类在浏览器上的一些行为，自动处理浏览器上的-些行为,比如点击，填充數据，删余cookie等。chromedriver 是一个驱动Chrome 浏览器的驱动程序，使用他才可以驱动浏览器。当然针对不同的浏览器有不同的driver.以下列出了不同划览器及其对应的driver:
1. Chrome: htp://sites. google .com/a/chromium. org/chromedriver/downloads
2. Firefox: htp://github com/milla/geckodriver/releases
3. Edge: https://developer microsoft. com/enus/microsoft edge/tools/webdriver/
4. Safarl: htp://webkit org/blog/6900/webriver-support-in-safar-10/

安装Selenium和chromedriver:
1.安装Selenlum : Selenlum 有很多语言的版本，有java. ruby、python等。我们下载python版本的就可以了。
pip insta1l seleniun
2.安装chromedriver :下载完成后，放到不需要权限的纯英文目录下就可以了。


"""
P77 13selenium关闭页面和浏览器
"""
selenium常用操作:
更多教程请参考: http://selenium-python.readthedocs lo/installation .html#introduction
关闭页面:
1. driver.close() :关闭当前页面。
2. driver.quit() :退出整个浏览器。

"""
P78 14selenium定位元素的方法详解
"""

1.如果只是想要解析网页中的数据，那么推荐将网页源代码扔给1xm1来解析。因为1xm1底层使用的是c语言，所以解析效率会更高。
2.如果是想要对元素进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法。


from selenium import webdriver
from lxml import etree
# driver_path=r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
html=driver.page_source
print (driver.page_source)
# driver.close()
# driver.quit()
# input_tag=driver.find_element_by_id('kw')
# input_tag=driver.find_element_by_name('wd')
# input_tag=driver.find_element_by_class_name('s_ipt')
input_tag=driver.find_element_by_xpath(r'//input[@id="kw"]')
input_tag.send_keys('python')
html=etree.HTML(html)

"""
P79 15selenium操作表 单元素
"""
常见的表单元素：
文本框input type='text/password/email/number' 'submit'

按钮 button、input[type='sbumit']

checkbox input='checkbox'

选项框下拉列表 select

操作表单元素:
1.操作输入框:分为两步。第一步:找到这个元素。第二步:使用send, keys(velue) , 将数据填充进去。示例代码如下:

# 操作输入框
from selenium import webdriver
import time
# driver_path=r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
input_tag=driver.find_element_by_id('kw')
# input_tag=driver.find_element_by_xpath(r'//input[@id="kw"]')
input_tag.send_keys('python')
time.sleep(3)
input_tag.clear()


2.操作checkbox:因为要选中checkbox 标签,在网页中是通过鼠标点击的。因此想要选中checkbox 标签，那么先选中这个标签，然后执行click 事件。示例代码如下:
# 操作checkbox(记住我)
from selenium import webdriver
import time
# driver_path=r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get('http://www.douban.com/')
remember_tag=driver.find_element_by_xpath('//input[@name="remember"]')
remember_tag.click()

3.选择select: select元素不能直接点击。因为点击后还需要选中元素。这时候selenium就专门为select标签提供了-个类selenium.webdriver support.ui.Select将获取到的元素当成参数传到这个类中，创建这个对象。以后就可以使用这个对象
进行选择了。示例代码加下:
from selenium.webdriver.support.ui import Select
#选中这个标签。然后使用select创建对象
selectTag=Select(driver.find.element_by_name("jumpHenu"))
#根据索引选择
selectTag.select_by_index(1)
#根据值这择
selectTag.select_by_value("http://www.95yueba.com")
#根据可视的文本选种
selectTag.select_by_visible_text("95秀客户端”)
#取消选中所有选项
selectTag.deselect_a11()

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://down.95you.com/')

from selenium.webdriver.support.ui import Select
#选中这个标签。然后使用select创建对象
selectTag=Select(driver.find_element_by_name("jumpMenu"))
#根据索引选择
selectTag.select_by_index(1)
#根据值这择
selectTag.select_by_value("http://m.95xiu.com/")
#根据可视的文本选种
selectTag.select_by_visible_text("95秀客户端")
#取消选中所有选项
selectTag.deselect_a11()

4.操作按钮:操作按钮有很多种方式。比如单击、右击、双击等。这里讲一一个最常用的。 就是点击。直接调用click函数就可以了。示例代码如下:
inputTag=driver.find_element_by_id('su')
inputTag.click()

"""
P80 16selenium行为链
"""
行为链:
有时候在页面中的操作可能要有很多步，那么这时候可以使用鼠标行为链类ActionChains来完成。比如现在要将鼠标移动到某个元素上并执行点击事件。那么示例代码如下: 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =webdriver.Chrome()
driver.get('https://www.baidu.com/')
input_tag =driver.find_element_by_id('kw')
submit_btn=driver.find_element_by_id('su')
actions=ActionChains(driver)
actions.move_to_element(input_tag)
actions.send_keys_to_element(input_tag, 'python')
actions.move_to_element(submit_btn)
actions.click(submit_btn)
actions .perform()


"""
P81 17selenium操作cookie
"""
Cookie操作:
1.获教所有的cookie :
for cookle in driver.get_cookies():
    print(cookie)
2根据cookie的key获取value:
value=driver.get_cookies(key)
3.最所有的cookie:
driver.delete_a11_cookies()
4.删除某个cookie:
driver.delete_cookie(key)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =webdriver.Chrome()
driver.get('https://www.baidu.com/')

for cookie in driver.get_cookies():
    print(cookie)
print('='*30)

driver.delete_cookie('PSTM')
print('='*30)

driver.delete_all_cookies()

"""
P82 18selenum的隐式等待和显式等待
"""
页面等待:

现在的网页越来越多采用了AJax技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom
元素还没出来，但是你的代码直接使用了这个WebElement,那么就会抛出NullPointer的异常。为了解决这个问题。所以Selenium提供了两种等待方式: 一种是隐式等待、一种是显式等待。
1.隐式等待:调用driver.implicitly_wait。那么在获取不可用的元素之前，会先等待10秒中的时间。示例代码如下:
driver=webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
eriver.get("https://www.douben.com/")

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)
driver.find_element_by_id('asdf')

2.显示等待:显示等待是表明某个条件成立后才执行获取元素的操作。也可以在等待的时候指定一个最大的时间， 如果超过这个时间那么就抛出一个异常。显示等待应该使用selenium.webdriver.support.excepted_ .conditions 期望的条件和selenium.webdriver.support.ui.WebDriverWait来配合完成。示例代码如下:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get('http://www.douban.com')
element=WebDriverWait(driver,18).until(
    EC.presence_of_element_located((By.ID,'form-email'))
)
print(element)


"""
P83 19selenium打开多窗口和切换窗口
"""
切换页面:
有时候窗口中有很多子tab页面。这时候肯定是需要进行切换的。selenium提供了一个叫做switch_to window来进行切换，具体切换到哪个页面，可以从driver.window_handles中找到。示例代码如下:
#打开一个新的页面
self.driver.execute_script("window.open('"+url+"')")
#切换到这个新的页面中
self.driver.switch_to_window(self.driver.window_handles[1])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.execute_script("window.open('https://www.douban.com')")
print(driver.current_url)
driver.switch_to_window(driver.window_handles[1])
#虽然在窗口中切换到了新的页面。但是driver中还没有切换。
#如果想要在代码中切换到新的页面，并且做些爬虫。
#那么应该使用driver.switch_to_windon来切换到指定的窗口
#从driver.window_handlers中取出具体第几个窗口_
#driver.window_handlers是一个列表，里面装的都是窗口句柄。
#他会按照打开页面的顺序来存储窗口的句柄。


"""
P84 20selenium使用代理ip
"""
设置代理ip:
有时候领繁爬取一些网页。服务器发现你是爬虫后会封掉你的ip地址。这时候我们可以更改代理ip.更改代理ip,不同的浏览器有不同
的实现方式。这里以Chrome浏觉器为例来讲解:

from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://115.223.2.114	:80" )
driver=webdriver.Chrome(options=options)
driver.get('http://httpbin.org/ip')


"""
P85 21selenium中的WebElement类补充
"""


"""
P86 22实战-selenium完美实现拉勾网列表页之爬虫解析 
"""
import json
import requests
# 您操作太频繁,请稍后再访问
def request_list_page():
    """
    :return:
    """
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers={
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    }
    data={
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    response=requests.post(url)
    print(response.text)

    

import json
import requests
import time
# 您操作太频繁,请稍后再访问
def request_list_page():
    """
    :return:
    """
    main_url='https://www.lagou.com/'
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data={
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    s = requests.Session()
    s.get(main_url,timeout=3)
    cookies=s.cookies
    print(cookies)
    response=s.post(url,headers=headers,data=data,cookies=cookies,timeout=5)
    print(response.text)
    
# 正常   
def request_list_page():
    """
    :return:
    """
    main_url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=/'
    s=requests.Session()
    s.get(main_url, timeout=3)
    cookies=s.cookies
    print(cookies)
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data={
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    response=s.post(url,headers=headers,data=data,cookies=cookies,timeout=5)
    print(response.text)

# 您操作太频繁,请稍后再访问，可正常(不能连续请求)    
def request_list_page():
    """
    :return:
    """
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data={
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    response=requests.post(url,headers=headers,data=data,timeout=5)
    print(response.text)
    
def main():
    request_list_page()

if __name__ == '__main__':
    main()

"""
24实战selenium完美实现拉勾网爬虫之跑通流程
"""

from selenium import webdriver
from lxml import etree
import time

class LagouSpider():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url='https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='
        self.positions=[]

    def run(self):
        self.driver.get(self.url)
        while True:
            source=self.driver.page_source
            # self.parse_list_page(source)
            # 爬完一页点击下一页
            next_bnt=self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
            time.sleep(2)
            if "pager_next pager_next_disabled" in next_bnt.get_attribute('class'):
                break
            else:
                next_bnt.click()
            time.sleep(1)

    def parse_list_page(self,source):
        html=etree.HTML(source)
        links=html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
            print(link)

    def request_detail_page(self,url):
        # driver未切换窗口，会覆盖原窗口
        self.driver.get(url)
        source=self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self,source):
        """
        解析详情页
        :param source:
        :return:
        """
        html=etree.HTML(source)
        position_name=html.xpath('//div[@class="job-name"]/h1/text()')[0]
        job_requests_span=html.xpath('//dd[@class="job_request"]//span')
        salary=job_requests_span[0].xpath('./text()')[0]
        city=''
        work_years=''
        education=''
        desc=''
        position={
            'name':position_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
            'desc':desc
        }
        print(position)
        self.positions.append(position)
if __name__ == '__main__':
    spider=LagouSpider()
    spider.run()