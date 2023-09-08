"""
a2w6MN2TzhY5c6Oh  aliyun
用户登录手机号：13751964417  # 15521289224  法人手机号 13802965035   工行手机号 18902284540   # 13535550504
对应付款帐号：     2                               4                        工行：3602019309200000266

测试帐号
地区                        后台村集体帐号                             镇                                         县
黄埔凤美小区                  13751964412、13751964415              13751964411                               13751964410
江高测试村集体                13750000006、13750000007              13750000004、13750000005                   13750000001、13750000002
梅南村民委员会                13750000125、13750000126              13750000027                                13750000010
南口村民委员会                13750000123                           13750000025                                13750000010
雁洋村民委员会                13750000124                           13750000026                                13750000010
南上村民委员会                13750000120                           13750000011
南下村民委员会（未激活）        13750000121                           13750000011
小黄村民委员会                13750000122                           13750000011
湖寮镇黎家坪                  13750000042                           13750000041                               13750000040
松口镇石盘村                  13750000012                           13750000011                               13750000010
阳江                        13751964423、13751964424               13751964422、13751964425                 13751964421、13751964426
"""

import requests, urllib3, json, os

# cert_file = '/path/to/certificate.pem'
urllib3.disable_warnings()
os.environ["http_proxy"] = 'http://192.168.123.177:28'
os.environ["https_proxy"] = 'http://192.168.123.177:28'


class public:
    host = 'https://cqjy-test.b2bwings.com'
    uatHost = 'https://cqjy-uat.b2bwings.com'
    admin = '/api/admin/v1/sysUser/open/loginByCode'
    user = '/api/user/v1/user/open/loginByCode'
    # census = '/api/user/v1/user/open/censusLoginByCode'
    vPhone = 13751964424
    villagePhone = {"phone": vPhone, "code": "888888"}
    aPhone = 13751964426
    auditPhone = {"phone": aPhone, "code": "888888"}
    uPhone = 13751964417
    userPhone = {"phone": uPhone, "code": "888888", "user_Type": 1}
    '''
    用户登录手机号：13751964417  #袁 13535550504 # 15521289224  法人手机号 13802965035   工行手机号18902284540   郑组长 17346642256
    对应付款帐号：     2               4        3602019309200000266
    '''

    # 登录接口
    def login(self, data, path):
        url = self.host + path
        header = {"Content-Type": "application/json"}
        js = requests.post(url=url, headers=header, data=json.dumps(data), verify=False).json()
        return js["data"]["sessionid"]

    # 根据login获取不同sessionId组装header
    def getSessionId(self):
        village = {"sessionid": self.login(self.villagePhone, self.admin), "Content-Type": "application/json",
                   "channel": "admin"}
        audit = {"sessionid": self.login(self.auditPhone, self.admin), "Content-Type": "application/json",
                 "channel": "admin"}
        user = {"sessionid": self.login(self.userPhone, self.user), "Content-Type": "application/json"}
        headers = [village, audit, user]
        # print(headers)
        return headers

    # 封装post，header带上
    def post(self, url, data, header):
        # header = self.getSessionId()
        return requests.post(url=self.host + url, headers=header, data=json.dumps(data), verify=False).json()


if __name__ == '__main__':
    pass
