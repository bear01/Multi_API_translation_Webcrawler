
#导入requests模块
import requests
import urllib.parse
class Xiaoniu(object):
    def __init__(self):

        self.headers={
        'Accept': 'application / json, text / plain, * / *',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN,zh;q = 0.9,en;q = 0.8',
        'Connection': 'keep - alive',
        'Host': 'test.niutrans.com',
        'Origin': 'https: // niutrans.com',
        'Referer': 'https: // niutrans.com / Trans',
        'Sec - Fetch - Mode': 'cors',
        'Sec - Fetch - Site': 'same - site',
        'User - Agent': 'Mozilla / 5.0(WindowsNT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
        }
        self.url = 'https://test.niutrans.vip/NiuTransServer/testtrans'

    def translate(self, from_lan, to_lan, text):
        data = {
            'from' : from_lan,
            'src_text': text,
            'to' : to_lan
        }
        url = self.url
        url+='?from='+from_lan+'&to='+to_lan+'&src_text='
        url+=urllib.parse.quote(data['src_text'])
        #print(url)
        result = requests.get(url=url,headers=self.headers)
        print(result.json())
        if result != None:
            return result.json()['tgt_text']


def xiaoniu(text,len):
        niu = Xiaoniu()
        if (len == 'zh'):
            return (niu.translate('zh','en',text))
        if (len == 'en'):
            return (niu.translate('en','zh',text))
