import urllib.request
import urllib.parse
import time
import random
import hashlib
import json
from bs4 import BeautifulSoup
from colorama import init,Fore

def youdao(content):
    # 解决反爬机制
    u = 'fanyideskweb'
    d = content
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    f = str(int(time.time()*1000) + random.randint(1,10))  # 时间戳
    c= 'rY0D^0\'nM0}g5Mm1z%1G4'
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()   # md5加密，生成一个随机数
    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    data = {}
    # data 有道翻译数据表单
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = f  # salt 与 sign 反爬机制 ，每次都会变化 salt就是时间戳
    data['sign'] = sign # 使用的是u + d + f + c的md5的值。
    data['ts'] = '1551506287219'
    data['bv'] = '97ba7c7fb78632ae9b11dcf6be726aee'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'False'

    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,data=data,headers=head, method='POST')
    response  = urllib.request.urlopen(request)
    line = json.load(response)  # 将得到的字符串转换成json格式
    text=''
    for x in line['translateResult']:
        text += x[0]['tgt']
    return text