#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests, json
import datetime
import time

def send_msg(content):
  """艾特全部，并发送指定信息"""
  data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list":["@all"]}})
  r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
  print(r.json)

if __name__ == '__main__':
  wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=054fe1ed-7c2e-404d-a336-3dc1de065d24"  # 测试机器人1号
  send_message = "今天你订餐了吗！"
  send_msg(send_message)