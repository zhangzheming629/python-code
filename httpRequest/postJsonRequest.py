#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import urllib.request

def main():
    t = "f6aa60a8d4d4e5e6c413350fdaca59ee4aa973ca61cb28b73beee93e9ba80be5"
    url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(t)
    header = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    body = {
        "msgtype": "text",
        "text": {
        "content": "监控指标:content"
        },
        "at": {
           "isAtAll": 0
        }
    }
    print(body)
    data = json.dumps(body)
    data = bytes(data, 'utf8')
    request = urllib.request.Request(url,data = data,headers = header)
    response = urllib.request.urlopen(request)
    page = response.read().decode('utf-8')
    print(page)

if __name__ == "__main__":
        main()