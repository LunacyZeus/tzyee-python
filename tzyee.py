# -*- coding: utf-8 -*-
#天知易云计费 for VPNmod
"""
所有支付类型

ICBC	工商银行
ABC	农业银行
CCB	建设银行
BOC	中国银行
CMB	招商银行
BCCB	北京银行
BOCO	交通银行
CIB	兴业银行
NJCB	南京银行
CMBC	民生银行
CEB	光大银行
PINGANBANK	平安银行
CBHB	渤海银行
HKBEA	东亚银行
NBCB	宁波银行
CTTIC	中信银行
GDB	广发银行
SHB	上海银行
SPDB	上海浦东发展银行
PSBS	中国邮政
HXB	华夏银行
BJRCB	北京农村商业银行
SRCB	上海农商银行
SDB	深圳发展银行
CZB	浙江稠州商业银行
ALIPAY	支付宝
ALIPAYSCAN	支付宝扫码
TENPAY	财付通
WEIXIN	微信 ok
QQ	QQ钱包
ALIPAYWAP	支付宝Wap ok
TENPAYWAP	财付通Wap
WEIXINWAP	微信Wap ok
QQWAP	QQ钱包Wap
BANKWAP	中国银联手机支付
SHORTCUT	PC快捷支付
default	天知易聚合收银台{所有渠道}
WEIXINJSAPI	微信公众号支付{微信内置浏览器用}
"""

class tzyee(object):
    partner=""
    key=""
    callbackurl=""#下行异步通知地址
    hrefbackurl=""#下行同步通知地址
    
    def __init__(self,banktype="",paymoney="",ordernumber="",attach=""):#初始化,接受参数
        self.banktype=banktype#通道类型 ALIPAYSCAN 支付宝 WEIXIN 微信 QQ
        self.paymoney=paymoney#金额
        self.ordernumber=ordernumber#商户订单号
        self.attach=attach#备注信息
        self.sign=""#接口签名,使用sign函数才会生成
        self.RequestUrl=""#请求地址

    def signkey(self):#进行签名
        import hashlib
        m = hashlib.md5()
        encodestr='partner=%s&banktype=%s&paymoney=%s&ordernumber=%s&callbackurl=%s%s'%(self.partner,self.banktype,self.paymoney,self.ordernumber,self.callbackurl,self.key)
        m.update(encodestr)
        self.sign=m.hexdigest()
        self.RequestUrl='https://tzyee.com/Pay.aspx?partner=%s&banktype=%s&paymoney=%s&ordernumber=%s&callbackurl=%s&hrefbackurl=%s&attach=%s&sign=%s'%(self.partner,self.banktype,self.paymoney,self.ordernumber,self.callbackurl,self.hrefbackurl,self.attach,self.sign)
     
    def Validcallback(self,ordernumber,orderstatus,paymoney,sign):#效验订单
        import hashlib
        m = hashlib.md5()
        encodestr='partner=%s&ordernumber=%s&orderstatus=%s&paymoney=%s%s'%(self.partner,ordernumber,orderstatus,paymoney,self.key)
        m.update(encodestr)
        if sign!=m.hexdigest():
            return False
        
        return True
