import requests
from . import HandleJs

def google(content):
    js = HandleJs.Py4Js()
    tk = js.getTk(content)    
    return translate(tk,content)    
def translate(tk,content):   
    if len(content) > 4891:    
        print("翻译的长度超过限制！！！")    
        return  

    param = {'tk': tk, 'q': content}

    # result = requests.get("""https://translate.google.cn/translate_a/single?client=webapp&
    #                         sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&
    #                         dt=rw&dt=rm&dt=ss&dt=t&dt=gt&otf=2&ssel=0&tsel=3&kc=1""", params=param)
    #返回的结果为Json，解析为一个嵌套列表
    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
                            &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
                            &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)
    # print(result.json())
    text=''
    data=result.json()[0]
    for vlue in data:
        if not vlue[0] is None:
            text+=vlue[0]
    return text
