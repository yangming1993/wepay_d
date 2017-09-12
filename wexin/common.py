#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/12
'''

import random
from urllib.parse import quote

def createRdStr(length=32):
    """产生随机字符串，不长于32位"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    strs = []
    for x in range(length):
        strs.append(chars[random.randrange(0, len(chars))])
    return "".join(strs)

def formatBizQueryParaMap(paraMap, urlEncode):
    """格式化参数，签名过程需要使用"""
    slist = sorted(paraMap)
    buff = []
    for k in slist:
        v = quote(paraMap[k]) if urlEncode else paraMap[k]
        buff.append("{0}={1}".format(k, v))

    return "&".join(buff)
