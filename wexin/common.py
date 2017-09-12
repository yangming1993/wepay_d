#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/12
'''

import random


def createNoncestr(length=32):
    """产生随机字符串，不长于32位"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    strs = []
    for x in range(length):
        strs.append(chars[random.randrange(0, len(chars))])
    return "".join(strs)