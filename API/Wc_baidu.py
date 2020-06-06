import json
import re
import execjs
import js2py
import requests


class baidu_translate():
    def __init__(self):
        self.GET_URL = 'https://fanyi.baidu.com/?aldtype=16047#zh/en/'
        self.POST_URL = 'https://fanyi.baidu.com/v2transapi'

        self.GET_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'Referer': 'https://fanyi.baidu.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'cookie': 'BAIDUID=A1228CA32EDDDBD89BB45766E31428C2:FG=1; BIDUPSID=A1228CA32EDDDBD89BB45766E31428C2; PSTM=1568278626; BDUSS=VmSDZibGF-WGdiMHNFaWp4eGdIRjBqMi11eEs1NlpIZUFxOHlzUkMtbn5xNmxkRVFBQUFBJCQAAAAAAAAAAAEAAAB60AFOYmVhcsO0w7Tf1WdvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8egl3~HoJddn; BDSFRCVID=BM8OJeC62w3k1Wcw9gMnhLz6Z2yCrITTH6aoCtLVy5woyGaz0rnPEG0PeU8g0Ku-TzZpogKKKmOTH1IF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nCagc9aJ5nJDoCbMT_Dxnbeq0gLf7rhj5ztDQwoM8bQpP-HJ7J3MKhLlbLWRCJqP0O2tjQKl0MLPbWbb0xyn_VMM3beMnMBMniamOnaIjY3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFlDjLbjTcXeaRf-b-HHjn03RrebRrMeJOdq4bohjPYXH79BtQmJJrfobkhQbObbJ3Eh47d26KlDlrmbfcnQg-q3R7nbpR4JD56hnrn-JTQKxTT0x-jLITPVn0MW-KVS-cLK-nJyUPUhtnnBToA3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CcJ-J8XhI06D5rP; delPer=0; PSINO=6; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; locale=zh; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1570672869; H_PS_PSSID=1465_21117_29720_29568_29220; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1570687871; __yjsv5_shitong=1.0_7_089672d14e623c496acd4a3bf0b219ba09bd_300_1570687868489_113.251.168.182_9b8f8b1f; yjs_js_security_passport=6e5dffc8e3ca04dfb258d8187a6de83fa4229b87_1570687869_js; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
        }
        self.POST_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'X-Requested-With': 'XMLHttpRequest',
            'cookie': 'BAIDUID=A1228CA32EDDDBD89BB45766E31428C2:FG=1; BIDUPSID=A1228CA32EDDDBD89BB45766E31428C2; PSTM=1568278626; BDUSS=VmSDZibGF-WGdiMHNFaWp4eGdIRjBqMi11eEs1NlpIZUFxOHlzUkMtbn5xNmxkRVFBQUFBJCQAAAAAAAAAAAEAAAB60AFOYmVhcsO0w7Tf1WdvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8egl3~HoJddn; BDSFRCVID=BM8OJeC62w3k1Wcw9gMnhLz6Z2yCrITTH6aoCtLVy5woyGaz0rnPEG0PeU8g0Ku-TzZpogKKKmOTH1IF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nCagc9aJ5nJDoCbMT_Dxnbeq0gLf7rhj5ztDQwoM8bQpP-HJ7J3MKhLlbLWRCJqP0O2tjQKl0MLPbWbb0xyn_VMM3beMnMBMniamOnaIjY3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFlDjLbjTcXeaRf-b-HHjn03RrebRrMeJOdq4bohjPYXH79BtQmJJrfobkhQbObbJ3Eh47d26KlDlrmbfcnQg-q3R7nbpR4JD56hnrn-JTQKxTT0x-jLITPVn0MW-KVS-cLK-nJyUPUhtnnBToA3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CcJ-J8XhI06D5rP; delPer=0; PSINO=6; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; locale=zh; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1570672869; H_PS_PSSID=1465_21117_29720_29568_29220; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1570687871; __yjsv5_shitong=1.0_7_089672d14e623c496acd4a3bf0b219ba09bd_300_1570687868489_113.251.168.182_9b8f8b1f; yjs_js_security_passport=6e5dffc8e3ca04dfb258d8187a6de83fa4229b87_1570687869_js; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',

        }

        self._session = requests.session()
        self._data = {
            # 'from': str_type,
            # 'to': result_type,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            # 'query': '',  # 要翻译的词或句, 变项
            # 'sign': '',  # Ajax(js) 加密, 变项
            # 'token': '',  # 不变项
        }
        # 可以直接拿浏览器上的 token, 因为 token 是不变的
        self._get_token()
    def get_str_type(self):
        """获得被翻译的文字类型"""
        data = {
            'query': self._query
        }
        # print(data)
        response = requests.post(self.POST_URL, data=data, headers=self.POST_HEADERS)
        # xxx=response.content.decode()
        # print(xxx)
        str_type = json.loads(response.content.decode())['query']

        for ch in str_type.encode('utf-8').decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return 'zn'
        return  'en'
    def get_result_type(self, str_type):
        """判断翻译的文字类型"""
        # 中译英
        if str_type == 'zh':
            result_type = 'en'
        # 外译中
        else:
            result_type = 'zh'
        return result_type
    def _get_token(self):
        response = self._session.get(self.GET_URL, headers=self.GET_HEADERS)
        html = response.text
        li = re.search(r"<script>\s*window\[\'common\'\] = ([\s\S]*?)</script>", html)
        token = re.search(r"token: \'([a-zA-Z0-9]+)\',", li.group(1))
        self._data['token'] = token.group(1)

    def _get_sign(self):
        # 将 使用 js 加密的函数 copy 到 baidu_translate.js 文件中
        # 然后使用 execjs 执行
        with open('API/baiduFanyi.js') as fp:
            sign = execjs.compile(fp.read()).call('e', self._query)
            self._data['sign'] = sign

    def translate(self, query):
        self._query = query
        self._data['query'] = self._query
        self._get_sign()
        # 获得被翻译的文字类型
        str_type = self.get_str_type()
        # 判断翻译的文字类型
        x=self.get_result_type(str_type)
        self._data['from'] =str_type
        self._data['to'] = x
        print(self._data)
        response = self._session.post(self.POST_URL, data=self._data, headers=self.POST_HEADERS)
        content = response.content.decode()
        dict_data = json.loads(content)
        print(dict_data)
        ret = dict_data['trans_result']['data'][0]['dst'] +'\n'
        # print(ret)
        return (ret)


def baidu(content):
    trans = baidu_translate()
    return trans.translate(content)
