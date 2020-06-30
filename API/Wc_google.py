import requests
from . import HandleJs

def google(content,Language):
    js = HandleJs.Py4Js()
    tk = js.getTk(content)    
    return translate(tk,content,Language)
def translate(tk,content,Language):
    if len(content) > 4891:    
        print("翻译的长度超过限制！！！")    
        return
    param = {'tk': tk, 'q': content}
    # 中译英url
    # if(Langugae == 0):
    #     result = requests.get("""https://translate.google.cn/translate_a/single?client=webapp
    #                             &sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca
    #                             &dt=rw&dt=rm&dt=ss&dt=t&swap=1&otf=2&ssel=5&tsel=5&kc=1&""", params=param)
    # 英译中url
    if(Language == 'en'):
        result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
                                            &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
                                            &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""",params=param)
    # 中译英url
    else:
        result = requests.get("""https://translate.google.cn/translate_a/single?client=webapp
                                       &sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca
                                       &dt=rw&dt=rm&dt=ss&dt=t&swap=1&otf=2&ssel=5&tsel=5&kc=1&""", params=param)
    # print(result.json())
    text=''
    data=result.json()[0]
    for vlue in data:
        if not vlue[0] is None:
            text+=vlue[0]
    return text
