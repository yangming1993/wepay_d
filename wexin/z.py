#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/12
'''

import common
para = {'APPID': "wx38e042863be96f89", 'APPSECRET' : "5b2f3f872ec1e78f98cd6329f9be6776"}
t = common.formatBizQueryParaMap(para, 1)
print(t)