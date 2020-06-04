# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from API import Wc_youdao,Wc_baidu,Wc_google,Wc_jinshanciba
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        vlue = request.POST['q']
        if len(vlue) > 0:
            if 'youdao' in request.POST:
                results = Wc_youdao.youdao(vlue)
            elif 'baidu' in request.POST:
                results = Wc_baidu.baidu(vlue)
            elif 'google' in request.POST:
                results = Wc_google.google(vlue)
            elif 'jinshan' in request.POST:
                # results = Wc_jinshanciba.jinshan(vlue)
                results = '金山词霸正在开发中，目前只有有道、百度、谷歌翻译可以使用'
            elif 'other' in request.POST:
                results = '其他翻译工具正在探索中，目前只有有道、百度、谷歌翻译可以使用'
            elif 'all' in request.POST:
                results = "有道："+Wc_youdao.youdao(vlue) + '\n' +"百度："+ Wc_baidu.baidu(vlue)+'谷歌：'+ Wc_google.google(vlue)
            ctx['rlt'] = results
            ctx['vlue'] = vlue
    return render(request, "post.html", ctx)
