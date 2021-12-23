#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib.request



def main():
    response = urllib.request.urlopen('https://www.baidu.com')
    print("查看 response 的返回类型：",type(response))
    print("查看反应地址信息: ",response)
    print("查看头部信息1(http header)：\n",response.info())
    print("查看头部信息2(http header)：\n",response.getheaders())
    print("输出头部属性信息：",response.getheader("Server"))
    print("查看响应状态信息1(http status)：\n",response.status)
    print("查看响应状态信息2(http status)：\n",response.getcode())
    print("查看响应 url 地址：\n",response.geturl())
    page = response.read()
    print("输出网页源码:",page.decode('utf-8'))
    print(page)

if __name__ == "__main__":
        main()