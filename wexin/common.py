#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/12
'''

import random
from urllib import quote
from config import WxPayConf_pub
import hashlib

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

def getSign(obj):
    """生成签名"""
    #签名步骤一：按字典序排序参数,formatBizQueryParaMap已做
    String = formatBizQueryParaMap(obj, False)
    #签名步骤二：在string后加入KEY
    String = "{0}&key={1}".format(String,WxPayConf_pub.KEY)
    #签名步骤三：MD5加密
    String = hashlib.md5(String).hexdigest()
    #签名步骤四：所有字符转为大写
    result_ = String.upper()
    return result_
