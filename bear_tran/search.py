# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from API import Wc_youdao,Wc_baidu1,Wc_google,Wc_jinshanciba,Wc_Tencent
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        vlue = request.POST['q']
        print(request.POST)
        Language = request.POST['language'];
        # if(Language=='en'):
        #     Language = 1;
        # else:
        #     Language = 0;
        # if 'en' in request.POST:
        #     Language = 'en' ;
        # if 'zn' in request.POST:
        #     Language = 0;

        if len(vlue) > 0:
            if 'youdao' in request.POST:
                results = Wc_youdao.youdao(vlue, Language)
            elif 'baidu' in request.POST:
                results = Wc_baidu1.baidu(vlue, Language)
            elif 'google' in request.POST:
                results = Wc_google.google(vlue, Language)
            elif 'tencent' in request.POST:
                results = Wc_Tencent.tencent(vlue, Language)
            elif 'other' in request.POST:
                results = '其他翻译工具正在探索中，目前只有有道、百度、谷歌、腾讯翻译可以使用'
            elif 'all' in request.POST:
                results = "有道："+Wc_youdao.youdao(vlue, Language) + '\n\n'+"百度："+Wc_baidu1.baidu(vlue, Language) + '\n\n' +'谷歌：'+ Wc_google.google(vlue, Language)+'\n\n'+ '腾讯：'+ Wc_Tencent.tencent(vlue, Language)
            ctx['rlt'] = results
            ctx['vlue'] = vlue
            print(Language)
    return render(request, "post.html", ctx)
