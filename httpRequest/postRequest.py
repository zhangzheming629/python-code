#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib.request



def main():
    url = 'https://httpbin.org/post'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Referer': 'https://httpbin.org/post',
        'Connection': 'keep-alive'
        }
    # 模拟表单提交
    dict = {
        'name':'MIka',
        'old:':18
    }
    data = urllib.parse.urlencode(dict).encode('utf-8')
    req = urllib.request.Request(url = url,data = data,headers = headers)
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    print(page)

def hello():
    print("hello nightingale")

if __name__ == "__main__":
        main()