# import difflib
# import inspect
import json
import datetime
import requests
import urllib3

import Setting.Publics
from Setting.Base import *
import os
from functools import wraps

from Setting.CustomSkip import *

urllib3.disable_warnings()
test_host = "https://cqjy-test.b2bwings.com"
os.environ["http_proxy"] = 'http://192.168.123.177:28'
os.environ["https_proxy"] = 'http://192.168.123.177:28'

from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_future_date(date: datetime, months: int = 0, years: int = 0):
    """
    获取指定日期若干个月或若干年后的日期。

    参数:
    - date: 输入的初始日期 (datetime 类型)
    - months: 添加的月数 (默认为 0)
    - years: 添加的年数 (默认为 0)

    返回值:
    - 计算后的新日期 (datetime 类型)
    """
    future_date = date + relativedelta(months=months, years=years)
    return future_date


# 示例
current_date = datetime.now()  # 当前日期
one_month_later = get_future_date(current_date, months=1)
one_year_later = get_future_date(current_date, years=1)

print(f"当前日期: {str(current_date)[:10]}")
print(f"一个月后的日期: {one_month_later}")
print(f"一年后的日期: {one_year_later}")

'''
time_hms = datetime.datetime.now().strftime('%y%H:%M:%S')
time_sss = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] + 'Z'
# time_ss = datetime.utcnow().strftime('%H:%M:%S.%f')[:-3] + 'Z'
time_last = (datetime.datetime.now()+ datetime.timedelta(days=-30)).strftime('%Y-%m-%d %H:%M:%S')
print(time_hms)
print(time_sss)
print(time_last)
print(str(datetime.timedelta(days=25)))
'''

'''
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(i, 'x', j, '=', i*j, end='\t')
#     print('')
i = [1, 8, 0, 15, 200, 5]
for j in i:

    print(j)


time_hms = datetime.datetime.now().strftime('%H:%M:%S')
time_sss = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] + 'Z'
# time_ss = datetime.utcnow().strftime('%H:%M:%S.%f')[:-3] + 'Z'
time_last = (datetime.datetime.now()+ datetime.timedelta(days=-30)).strftime('%Y-%m-%d %H:%M:%S')
# print(time_hms)
# print(time_sss)
# print(time_last)
print(str(datetime.timedelta(days=25)))

print(50193.02+11200.04+12603.22+8286.15+34892.23+10228.71+19413.3+30923.77+28326.89+19324.31)

# ------------------查询入账流水-----------------
def queryInFlow():
    url = "https://cqjy-test.b2bwings.com/api/account/v1/counterRecord/open/queryInFlow"
    header = {}
    data = {
        "bankCode": "103",
        "subAccountNo": connect("\'凤凰二横路凤美小区03月21日160644\'")[4],
        "mainAccountNo": "44224201040008124",
        "mainAccountName": "清远市清新区集体资产交易中心测试",
        "projectTradeNo": connect("\'凤凰二横路凤美小区03月21日160644\'")[15],
        "startRow": "1",
        "endRow": "35",
        "authCode": connect("\'凤凰二横路凤美小区03月21日160644\'")[16]}
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("查询入账流水", re)
'''
# queryInFlow()

# # ------------------C端查询-----------------
# def queryFlowByName():
#     url = "https://cqjy-test.b2bwings.com/api/account/v1/counterRecord/open/queryFlowByName"
#     header = {}
#     data = [
#         "103",
#         "44224201040008124",
#         "清远市清新区集体资产交易中心测试",
#         rest[4],
#         str(datetime.datetime.now() + datetime.timedelta(days=0))[0:10],
#         "44224701040005947",
#         "姬洲试镉防古姬军甸李忠信",
#         "1",
#         rest[16]
#     ]
#     re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
#     print("C端查询流水", re)
# queryFlowByName()


"""resource = {"资源性资产": (1600008673008504834, 0, "Z000000"),
            "农用地": (1600008673084002305, 1600008673008504834, "Z010000")}
# 1600008673084002329     经营性资产     J000000
# 1600032507262603269     非经营性资产   F000000

def get_data(parentid=""):
    url = "/api/admin/v1/assetGroup/getByParentId"
    params = {"parentid": parentid}
    response = public().post(url, params, information().villageHeaders)
    print(type(response))
    return response["data"]


def find_code_by_name(name, data):
    codes = []
    for item in data:
        if item["assetGroupName"] == name:
            codes.append((item["assetGroupCode"], item["parentId"], item["assetGroupId"]))
            parentid = item["parentId"]
            while parentid:
                for item in data:
                    if item["assetGroupId"] == parentid:
                        codes.append((item["assetGroupCode"], item["parentId"]))
                        parentid = item["parentId"]
                        break
                else:
                    break
    return codes


# 测试调用接口并查找code和parentid
parentid = None  # 替换为实际的parentid，如果为空则传入None
data = get_data(parentid)
if data:
    name = "资源性资产"  # 替换为实际要查找的name
    codes = find_code_by_name(name, data)
    if codes:
        for code, parentid, assetGroupId in codes:
            print(f"name: {name}, code: {code}, parentid: {parentid}, assetGroupId:{assetGroupId}")
    else:
        print(f"未找到name为'{name}'的数据")"""

# target_name = "林木"
# target_index = None
#
# for i, item in enumerate(data):
#     if item["assetGroupName"] == target_name:
#         target_index = i
#         break
# print("目标位置：", target_index)
# print(data[target_index]['assetGroupCode'])


# 假设有一个包含重复值的列表

# my_list = [0, 2, 3, 2, 4, 5, 1, 3]
#
# # 创建一个空列表用于存储不重复的值
# unique_list = []
#
# # 使用for循环遍历原始列表
# for num in my_list:
#     # 如果当前值不在unique_list中，将其添加到unique_list中
#     if num not in unique_list:
#         unique_list.append(num)
#
# # 打印结果
# print(unique_list)


# 利用outcome存储的失败信息跳过用例
"""def customer(func):
    @wraps(func)
    def warppend(self):
        failures = str([fail[0] for fail in self._outcome.result.failures])
        if failures.find(func.__name__) == -1:
            raise unittest.SkipTest("{} is skipped".format(func.__name__))
        func(self)

    return warppend"""

# @skip_failed_cases("出现错误终止测试")
# class demo(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.word = "execute test"
#
#     def test_01(self):
#         print("execute test1")
#
#     # @skip_failed_cases("fail to skip")
#     def test_02(self):
#         print("execute test2")
#         self.assertEqual("execute test2", self.word)
#         # raise AssertionError
#
#     # @skip_dependent("test_02")
#     def test_03(self):
#         print("execute test3")
#         # print("failures=", str([fail[0] for fail in self._outcome.result.failures]))
#         self.assertEqual(1, 2)
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         pass
#
#
# if __name__ == '__main__':
#      unittest.main()


"""current_time = str(datetime.datetime.now())[:-7]
print(current_time)
i = 0
i += 1
print(i)
"""

'''
# inspect判定对象类型是否函数、方法、类等
if inspect.isclass(demo):
   print("object is class")
   functions = demo.__dict__
   # difflib 对比第一个参数相近的字符串后返回
   funclist = difflib.get_close_matches('test_', functions, 20, cutoff=0.7)
   print(funclist)
'''

"""文件流"""
# -*-coding:utf-8-*-
"""url = 'https://cqjy-test.b2bwings.com/api/file/v1/picture/uploadFileOnObs'
files = {'file': open('./115c.gif', 'rb')}  # 设置要被打开的文件
header = {"Accept": "*/*",
          "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
          "X-Requested-With": "XMLHttpRequest",
          "channel": "admin",
          "sessionid": "ab0e6d076d664a888b3fe5cbdccf25de"}
res = requests.post(url, headers=header, files=files, verify=False)  # 发送POST请求
print(res)
print(res.text)
print(res.content)"""

"""# coding=utf-8
import time
from splinter import Browser


def login_mail(url):
    browser = Browser(driver_name="edge")
    # 登录163邮箱
    browser.visit(url)
    # 输入账号和密码
    input_elements = browser.find_by_xpath('//*[@id="rc-tabs-0-panel-mail"]/div/form/div/input')
    # print(input_elements)
    input_elements.fill("dengshengjion@b2bwings.com")
    browser.find_by_xpath('//input[@type="password"]').fill('B2bwings')
    # 模拟单击登录按钮
    browser.find_by_xpath('//*[@id="rc-tabs-0-panel-mail"]/div/form/div/label/span[1]/input').click()
    browser.find_by_xpath('//*[@id="rc-tabs-0-panel-mail"]/div/form/div/button/span').click()
    time.sleep(5)
    # close the window of brower
    browser.quit()


if __name__ == '__main__':
    mail_addr = 'https://qiye.aliyun.com/login/oauth2/v2.0/login.json?referer=https%3A%2F%2Fqiye.aliyun.com&device_id=a3e7a9a8-787c-4c6c-b5fb-79dad0b20a54&response_type=code&state=7c01c518-e3bd-4c15-8d97-fc3138c61dde&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fqiye.aliyun.com%2Falimail%2Fauth%2FcallbackForCore&device_id_type=UUID&lang=zh_CN&client_id=legacy_webmail&code_challenge=eJDQZHPjWkIDhpL_nr82jcBSgBbefUifcqCvmOOX1RM'
    login_mail(mail_addr)
"""

# time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
# sub_account_no = "123"
# trade_no = "456"
# project_name = "abc"
# sql = ("INSERT INTO `cqjy-account`.`t_sub_account`(`sub_account_id`, `app_id`, `app_name`, `sub_app_id`, `sub_account_no`, "
#        "`sub_account_name`, `sub_req_no`, `organization_name`, `organization_id`,  `main_account_no`, "
#        "`account_bank_code`, `main_account_name`, `open_bank_name`,  `project_trade_no`, `auth_code`, "
#        "`account_status`, `project_name`) "
#        "VALUES (" + time + ", 'gdnccqjy', '广东省农村产权流转交易管理服务平台', '100000', '95588"+ time +"', '八赏冒乐蹬饥符曾绍亥猴睹崎等佑', "
#        "\'" + time + "\', '清远市清新区集体资产交易中心', 1531213778436427778, '3602023929200100926', '102', '八赏冒乐蹬饥符曾绍亥猴睹崎等佑', "
#        "'中国工商银行广州支行',  \'" + trade_no + "\', \'" + time + "\', '00', '" + project_name + "');")
#
# sql1 = "UPDATE cqjy.t_asset_project_enroll SET system_feedback_status = 1, pay_earnest_money_date = '" + time + "', pay_earnest_money = 1 WHERE asset_project_id = 1 ;"
#
# print(sql1)
