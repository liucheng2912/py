import requests
import json
import urllib.request
import urllib.error
import time
import re


def jenkins(result):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=054fe1ed-7c2e-404d-a336-3dc1de065d24'
    if result == 1:
        con = {"msgtype": "text", "text": {"content": "" + wk + "未能成功构建"}, }
    else:
        con = {"msgtype": "text", "text": {
            "content": "测试用例：" + result[4] + "\r\n构建结果:" + result[0] + "\r\n总用例：" + result[1] + "  通过:" + result[
                2] + "  失败:" + result[3] + ""}, }
    jd = json.dumps(con).encode('utf-8')

    req = urllib.request.Request(url, jd)

    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)

if __name__ == '__main__':
    wk = "test"
    jenkins(1)