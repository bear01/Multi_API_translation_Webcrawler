# post请求
import json

import requests


class King:
    def __init__(self, word):
        self.word = word
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        # 构造post请求的参数
        self.post_data = {
            'f': 'auto',
            't': 'auto',
            'w': self.word
        }

    # 发送请求
    def request_post(self):
        res = requests.post(url=self.url, headers=self.headers, data=self.post_data)
        # print(res.content.decode())
        return res.content.decode()

    # 解析数据
    @staticmethod
    def parse_data(data):
        dict_data = json.loads(data)
        if 'out' in dict_data['content']:
            print(dict_data['content']['out'])
            return dict_data['content']['out']
        elif 'word_mean' in dict_data['content']:
            print(dict_data['content']['word_mean'])
            return dict_data['content']['word_mean']

    def run(self):
        data = self.request_post()
        return self.parse_data(data)


# if __name__ == '__main__':
def ciba(text):
    king = King(text)
    return king.run()