import requests.sessions
import re
import execjs
class BaiDuFanYi():
 def __init__(self):
    self.homeUrl = "https://fanyi.baidu.com/"
    self.transUrl = "https://fanyi.baidu.com/v2transapi"
    self.headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            # "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"
            # "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)"
            # "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)"
            # "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)"
            # "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"
            # "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"
            # "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
            # "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    }
    self.gtk = None
    self.token = None
    self.s = requests.Session()
    self.get_params()
    self.get_params()
 def get_sign(self, query_string):
        JS_CODE = """
         function a(r, o) {
         for (var t = 0; t < o.length - 2; t += 3) {
         var a = o.charAt(t + 2);
         a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
         a = "+" === o.charAt(t + 1) ? r >>> a: r << a,
         r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
         }
         return r
         }
         var C = null;
         var token = function(r, _gtk) {
         var o = r.length;
         o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substring(r.length, r.length - 10));
         var t = void 0,
         t = null !== C ? C: (C = _gtk || "") || "";
         for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {
         var m = r.charCodeAt(g);
         128 > m ? d[f++] = m: (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)), d[f++] = m >> 18 | 240, d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224, d[f++] = m >> 6 & 63 | 128), d[f++] = 63 & m | 128)
         }
         for (var S = h,
         u = "+-a^+6",
         l = "+-3^+b+-f",
         s = 0; s < d.length; s++) S += d[s],
         S = a(S, u);
         return S = a(S, l),
         S ^= i,
         0 > S && (S = (2147483647 & S) + 2147483648),
         S %= 1e6,
         S.toString() + "." + (S ^ h)
         }
         """
        with open('baidu.js') as fp:
            sign = execjs.compile(fp.read()).call('e', self._query)
            self._data['sign'] = sign
            return sign.call('token', query_string, self.gtk)
 def get_params(self):
    r = self.s.get(self.homeUrl, headers=self.headers)
    self.gtk = re.findall(r"window.gtk = '(.*?)';", r.text)[0]
    self.token = re.findall(r"token: '(.*?)',", r.text)[0]
 def translate(self, query_string):
    sign = self.get_sign(query_string)
    data = {
        'from': 'en',
         'to': 'zh',
         'query': query_string,
         'simple_means_flag': 3,
         'sign': sign,
         'token': self.token,
    }
    res = self.s.post(url=self.transUrl, data=data, headers=self.headers)
    return res.json()['trans_result']['data'][0]['dst']
if __name__ == '__main__':
    words = input("请输入原文:\n")
    mydict = BaiDuFanYi()
    print(f"翻译结果是：\n{mydict.translate(words)}")