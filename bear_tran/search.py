# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import asyncio
import threading
import time
import time
from API import Wc_youdao,Wc_baidu1,Wc_google,Wc_Tencent,Wc_ciba,Wc_xiaoniu,Wc_Bing
# 接收POST请求数据
def search_post(request):
    ctx ={}
    yd = ''
    bd = ''
    gg = ''
    tx = ''
    cb = ''
    xn = ''
    wr = ''
    if request.POST:
        vlue = request.POST['q']
        print(request.POST)
        Language = request.POST['language'];

        if len(vlue) > 0:
            if 'youdao' in request.POST:
                results = Wc_youdao.youdao(vlue)
            if 'baidu' in request.POST:
                results = Wc_baidu1.baidu(vlue, Language)
            elif 'google' in request.POST:
                results = Wc_google.google(vlue, Language)
            elif 'ciba' in request.POST:
                results = Wc_ciba.ciba(vlue)
            elif 'tencent' in request.POST:
                results = Wc_Tencent.tencent(vlue)
            elif 'xiaoniu' in request.POST:
                results = Wc_xiaoniu.xiaoniu(vlue,Language)
            elif 'bing' in request.POST:
                results = Wc_Bing.bing(vlue, Language)
            elif 'all' in request.POST:
                threads = []
                threads.append(threading.Thread(target=Wc_youdao.youdao(vlue)))
                threads.append(threading.Thread(target=Wc_baidu1.baidu(vlue, Language)))
                threads.append(threading.Thread(target=Wc_google.google(vlue, Language)))
                threads.append(threading.Thread(target= Wc_Tencent.tencent(vlue)))
                threads.append(threading.Thread(target=Wc_xiaoniu.xiaoniu(vlue,Language)))
                threads.append(threading.Thread(target=Wc_Bing.bing(vlue, Language)))
                for t in threads:
                    t.setDaemon(True)
                    t.start()
                results = threads[1]
                # async def to_do_something(i):
                #     print('第{}个任务：任务启动...'.format(i))
                #     yd = Wc_youdao.youdao(vlue)
                #     ba = Wc_baidu1.baidu(vlue, Language)
                #     gg = Wc_google.google(vlue, Language)
                #     cb = Wc_ciba.ciba(vlue)
                #     tx = Wc_Tencent.tencent(vlue)
                #     xn = Wc_xiaoniu.xiaoniu(vlue,Language)
                #     wr = Wc_Bing.bing(vlue,Language)
                #     # 遇到耗时的操作，await就会使任务挂起，继续去完成下一个任务
                #     await asyncio.sleep(i)
                #     print('第{}个任务：任务完成！'.format(i))
                #
                # # 定义第2个协程，用于通知任务进行状态
                # async def mission_running():
                #     print('任务正在执行...')
                # start = time.time()
                # # 创建一个循环
                # loop = asyncio.new_event_loop()
                # asyncio.set_event_loop(loop)
                # # 创建一个任务盒子tasks，包含了3个需要完成的任务
                # tasks = [asyncio.ensure_future(to_do_something(1)),
                #          asyncio.ensure_future(to_do_something(2)),
                #          asyncio.ensure_future(to_do_something(3)),
                #          asyncio.ensure_future(to_do_something(4)),
                #          asyncio.ensure_future(to_do_something(5)),
                #          asyncio.ensure_future(to_do_something(6)),
                #          asyncio.ensure_future(to_do_something(7)),
                #          asyncio.ensure_future(mission_running())]
                # # tasks接入loop中开始运行
                # loop.run_until_complete(asyncio.wait(tasks))
                # end = time.time()
                #
                # print(end - start)
                # # results =    "有道："+ Wc_youdao.youdao(vlue) + '\n\n' \
                # #            + "百度：" + Wc_baidu1.baidu(vlue, Language) + '\n\n' \
                # #            + "谷歌：" + Wc_google.google(vlue, Language) + '\n\n' \
                # #            + "词霸：" + Wc_ciba.ciba(vlue) + '\n\n' \
                # #            + "腾讯：" + Wc_Tencent.tencent(vlue) + '\n\n'\
                # #            + "小牛：" + Wc_xiaoniu.xiaoniu(vlue,Language)+ '\n\n'\
                # #            + "微软：" + Wc_Bing.bing(vlue,Language)
                # results = yd + bd + gg + cb + tx + xn + wr
            ctx['rlt'] = results
            ctx['vlue'] = vlue
    return render(request, "post.html", ctx)
