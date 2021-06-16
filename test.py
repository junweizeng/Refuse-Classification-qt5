# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 20:28
# @Author  : zjw
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/vanishzeng/

import requests


if __name__ == '__main__':
    # request = requests.get("http://127.0.0.1:5000/upload")
    # print(request)
    # print(request.content)
    str = "玻璃垃圾 可回收垃圾"
    strs = str.split(" ")
    print(strs[0])
