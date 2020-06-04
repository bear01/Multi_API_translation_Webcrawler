  
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from colorama import init,Fore

def jinshan(content):
    url1 = 'http://fy.iciba.com/?trans='
    url = url1 + 'nihao' # 屏蔽特殊的字符、比如如果url里面的空格！url里面是不允许出现空格的，quote_plus更先进一些，可以编码
    response = urllib.request.urlopen(url) # 发送请求 类型<class 'http.client.HTTPResponse'>
    print(url)
    html = response.read() # 得到一个html格式对象（字符串）
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)

    tag_soup = soup.find(class_='trans_result')
    print(tag_soup)
    # for tag in tag_soup.find_all("span"):
         # print(tag.get_text())
    #     print("_____________")
    # if tag_soup == None: # 防止输入的单词没有释义
    #     print(Fore.GREEN + '输入的单词不存在，重新输入.')
    # else:
        #print(tag_soup)
        # meanings = tag_soup.find_all(class_='clearfix')
        # text12=tag_soup.find_all("span")
        # print(text12)
        # for tag in tag_soup.find_all("span"):
        #     print(tag.get_text())
        #     print("_____________")
            # return tag.get_text()
        # translation = meanings[3].get_text()
        # return translation.strip()
        # for i in range(len(text12)):
        #     translation = text12[i].get_text() # 获取文本内容 print(translation.strip()) # 去掉字符串开头和结尾的空行
        #     return (translation.strip())
            