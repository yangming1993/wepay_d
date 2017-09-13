#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/12
'''
import hashlib
import random
import xml.etree.ElementTree as ET
import requests

class UnifiedOrder_pub():
    '''
    参数信息
    需要设置固定部分通知地址notify_url

    '''
    params = {}
    def __init__(self):
        #固定部分
        self.params["appid"] = "wx38e042863be96f89"  # 公众账号ID
        self.params["mch_id"] = "1481746222" # 商户号
        self.URL = "https://api.mch.weixin.qq.com/pay/unifiedorder" #请求地址
        self.KEY = "P7QEnRab93joT7FOe0CScMz0YQYVoL3f" #密钥
        self.params["trade_type"] = "NATIVE" # 交易类型
        self.params["notify_url"] = "http://www.weixin.qq.com/wxpay/pay.php" # 通知地址

        #生成部分
        self.params["nonce_str"] = ""  # 随机字符串
        self.params["sign"] = ""  # 签名

        #填入部分
        self.params["body"] = "" # 商品描述
        self.params["detail"] = "" # 商品详情 F
        self.params["attach"] = "" # 附加数据 F
        self.params["out_trade_no"] = "" # 商户订单号
        self.params["total_fee"] = "" # 总金额
        self.params["spbill_create_ip"] = ""  # 终端IP

        # self.params["time_start"] = ""  # 交易起始时间 F
        # self.params["time_expire"] = "" # 交易结束时间 F
        # self.params["goods_tag"] = "" # 订单优惠标记 F
        # self.params["product_id"] = "" # 商品ID F
        # self.params["limit_pay"] = "" # 指定支付方式 F
        # self.params["openid"] = "" # 用户标识 F
        # self.params["sub_openid"] = "" # 用户子标识 F
        # self.params["scene_info"] = "" # 场景信息 F
        # self.params["fee_type"] = "CNY" # 币种类型 F
        # self.params["sub_mch_id"] = "1483743352" # 子商户号
        # self.params["device_info"] = ""  # 设备号 F
        # self.params["sign_type"] = "MD5" # 签名类型 F
        # self.params["sub_appid"] = "" # 子商户公众账号ID F

    def gen_sign(self,params, key):
        """
        签名生成函数
        :param params: 参数，dict 对象
        :param key: API 密钥
        :return: sign string
        """
        param_list = []
        for k in sorted(params.keys()):
            v = params.get(k)
            if not v:
                # 参数的值为空不参与签名
                continue
            param_list.append('{0}={1}'.format(k, v))
        # 在最后拼接 key
        param_list.append('key={}'.format(key))
        # 用 & 连接各 k-v 对，然后对字符串进行 MD5 运算
        h = hashlib.md5()
        h.update('&'.join(param_list))
        return h.hexdigest()

    def createRdStr(self,length=32):
        """产生随机字符串，不长于32位"""
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        strs = []
        for x in range(length):
            strs.append(chars[random.randrange(0, len(chars))])
        return "".join(strs)

    def dictToXml(self, arr):
        """将dict转xml"""
        xml = ["<xml>"]
        for k, v in arr.iteritems():
            if v.isdigit():
                xml.append("<{0}>{1}</{0}>".format(k, v))
            else:
                xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
        xml.append("</xml>")
        return "".join(xml)

    def xmlToDit(self, xml):
        """将xml转为dit"""
        return dict((child.tag, child.text) for child in ET.fromstring(xml))

    def createPayment(self,client_ip,
                      credit_recharge,
                      out_trade_no="2217752501201408053253368018",
                      body="NATIVE扫码支付"):
        '''

        :param client_ip: 用户id
        :param credit_recharge: 价格，单位为分
        :param out_trade_no: 32个字符内，只能是数字、大小写字母_-|*@
        :param body: 商品简单描述
        :return: 支付url
        '''
        self.params["spbill_create_ip"] = client_ip
        self.params["total_fee"] = credit_recharge
        self.params["out_trade_no"] = out_trade_no
        self.params["body"] = body
        self.params["nonce_str"] = self.createRdStr()
        self.params["sign"] = self.gen_sign(self.params,self.KEY)
        xmls = self.dictToXml(self.params)
        x = requests.post(self.URL,data=xmls)
        return self.xmlToDit(x.content)['code_url']

B = UnifiedOrder_pub()
print B.createPayment("192.168.1.68","1")
