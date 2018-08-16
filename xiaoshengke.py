# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 22:42
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : xiaoshengke.py
# @Software: PyCharm
import json
from urllib import request

#获取每一页的数据
def get_one_page(url):
    respones = request.get(url = url)
    if respones.status_code == 200:
        return respones.text
    return None

#解析每一页的数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield{
            'data':item['time'].split(' ')[0],
            'nickname':item['nickname'],




        }

