import datetime
import json
import unittest

from Setting.CustomSkip import *

from time import sleep
from Setting.Base import *

# @stop_on_failure
class Tender(unittest.TestCase, information):

    @classmethod
    def setUpClass(cls):
        # 使用机构名称作为项目名称，拼接时间
        cls.corporatePhone = [18722222224, 13802965035, 13000000000]
        # cls.corporateName = ["供应链", "信巴迪", "百事通"]
        cls.defaultInfo = information().getDefaultInfo()
        prefix = cls.defaultInfo["organizationName"][0:5]
        cls.assetName = cls.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '小额工程测试'
        print(cls.projectName)

    def test_01(self):
        """招标申请"""
        url = "/api/admin/v1/smallProject/saveProjectApply"
        data = {
            "smallProjectId": None,
            "projectName": self.projectName,
            "organizationName": self.defaultInfo["organizationName"],
            "organizationId": self.defaultInfo["organizationId"],
            "organizationCode": self.defaultInfo["organizationCode"],
            "organizationAddress": self.defaultInfo["organizationProvince"] + self.defaultInfo["organizationCity"] +
                                   self.defaultInfo[
                                       "organizationArea"] + self.defaultInfo["organizationStreet"] + self.defaultInfo[
                                       "organizationAddress"],
            "areaOrganizationName": self.defaultInfo["areaOrganizationName"],
            "areaOrganizationId": self.defaultInfo["areaOrganizationId"],
            "areaOrganizationCode": "",
            "areaOrganizationAddress": self.defaultInfo["areaOrganizationProvince"] + self.defaultInfo[
                "areaOrganizationCity"] +
                                       self.defaultInfo["areaOrganizationArea"] + self.defaultInfo[
                                           "areaOrganizationStreet"] +
                                       self.defaultInfo["areaOrganizationAddress"],
            "tenderUserName": self.defaultInfo["tenderUserName"],
            "tenderUserPhone": self.defaultInfo["tenderUserPhone"],
            "approvalOrganization": self.defaultInfo["areaOrganizationName"],
            "approvalNumber": self.defaultInfo["areaOrganizationId"],
            "projectProvinceId": self.defaultInfo["organizationProvinceId"],
            "projectProvince": self.defaultInfo["organizationProvince"],
            "projectCityId": self.defaultInfo["organizationCityId"],
            "projectCity": self.defaultInfo["organizationCity"],
            "projectAreaId": self.defaultInfo["organizationAreaId"],
            "projectArea": self.defaultInfo["organizationArea"],
            "projectStreetId": self.defaultInfo["organizationStreetId"],
            "projectStreet": self.defaultInfo["organizationStreet"],
            "projectDetailAddress": self.defaultInfo["organizationAddress"],
            "areaOrganizationUser": self.defaultInfo["areaOrganizationUser"],
            "areaOrganizationPhone": self.defaultInfo["areaOrganizationPhone"],
            "tenderTypeName": "施工",
            "tenderTypeCode": "03",
            "projectTypeName": "房屋建筑工程",
            "projectTypeCode": "01",
            "projectIndustryCategoryCode": "E000000000",
            "projectIndustryCategoryName": "建筑业",
            "tenderMethod": "01",
            "projectContent": "施工",
            "tradeEarnestMoney": 1,
            "bidUserRequire": "资格要求：中国国籍法人+企业固定资产在xxxxxx以上，月流动资金在xxxxx以上",
            "standardPeriod": "100",
            "tenderPeriod": "10",
            "evaluateMethod": "01",
            "tenderPrice": 500000,
            "blacklistEnter": "1",
            "remark": " ",
            "moneySource": "中国银行",
            "projectRegionCode": "440111113000"
        }
        response = self.post(url, data, self.villageHeaders)
        print('01小额工程申请', response)
        self.assertEqual(response["message"], "操作成功")

    def test_02(self):
        """项目审核"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProjectAudit/audit"
        data = {
            "smallProjectId": smallProjectId,
            "status": 1,
            "auditKey": "activitiFirstInstance",  # activitiFirstInstance 初审
            "annotation": "通过"
        }
        response = self.post(url, data, self.auditHeaders)
        print("02立项审核")
        self.assertEqual(response["message"], "操作成功")

    @unittest.skip("不驳回，跳过")
    def test_rejected(self):
        """项目驳回"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProjectAudit/audit"
        data = {
            "smallProjectId": smallProjectId,
            "status": 0,
            "auditKey": "activitiFirstInstance",  # activitiFirstInstance 初审
            "annotation": "第一次驳回"
        }
        response = self.post(url, data, self.auditHeaders)
        print("驳回")
        self.assertEqual(response["message"], "操作成功")

    @unittest.skip("不重提，跳过")
    def test_reApply(self):
        """重提申请"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProject/saveProjectReApply"
        data = {
            "smallProjectId": smallProjectId,
            "projectName": projectName,
            "organizationName": self.defaultInfo["organizationName"],
            "organizationId": self.defaultInfo["organizationId"],
            "organizationCode": self.defaultInfo["organizationCode"],
            "organizationProvince": self.defaultInfo["organizationProvince"],
            "organizationProvinceCode": "",
            "organizationCity": self.defaultInfo["organizationCity"],
            "organizationCityCode": "",
            "organizationArea": self.defaultInfo["organizationArea"],
            "organizationAreaCode": "",
            "organizationStreet": self.defaultInfo["organizationStreet"],
            "organizationStreetCode": "",
            "organizationAddress": self.defaultInfo["organizationAddress"],
            "areaOrganizationName": self.defaultInfo["areaOrganizationName"],
            "areaOrganizationId": self.defaultInfo["areaOrganizationId"],
            "areaOrganizationCode": "",
            "areaOrganizationAddress": self.defaultInfo["areaOrganizationProvince"] + self.defaultInfo[
                "areaOrganizationCity"] +
                                       self.defaultInfo["areaOrganizationArea"] + self.defaultInfo[
                                           "areaOrganizationStreet"] +
                                       self.defaultInfo["areaOrganizationAddress"],
            "tenderUserName": self.defaultInfo["tenderUserName"],
            "tenderUserPhone": self.defaultInfo["tenderUserPhone"],
            "approvalOrganization": self.defaultInfo["areaOrganizationName"],
            "approvalNumber": self.defaultInfo["areaOrganizationId"],
            "projectProvinceId": self.defaultInfo["areaOrganizationProvinceId"],
            "projectProvince": self.defaultInfo["areaOrganizationProvince"],
            "projectCityId": self.defaultInfo["areaOrganizationProvinceId"],
            "projectCity": self.defaultInfo["areaOrganizationCity"],
            "projectAreaId": self.defaultInfo["areaOrganizationAreaId"],
            "projectArea": self.defaultInfo["areaOrganizationArea"],
            "projectStreetId": self.defaultInfo["areaOrganizationStreetId"],
            "projectStreet": self.defaultInfo["areaOrganizationStreet"],
            "projectDetailAddress": self.defaultInfo["organizationAddress"],
            "areaOrganizationUser": self.defaultInfo["areaOrganizationUser"],
            "areaOrganizationPhone": self.defaultInfo["areaOrganizationPhone"],
            "tenderTypeName": "施工",
            "tenderTypeCode": "03",
            "projectTypeName": "房屋建筑工程",
            "projectTypeCode": "01",
            "projectIndustryCategoryCode": "E000000000",
            "projectIndustryCategoryName": "建筑业",
            "tenderMethod": "01",
            "projectContent": "施工",
            "tradeEarnestMoney": 1,
            "bidUserRequire": "无",
            "standardPeriod": "100",
            "tenderPeriod": "10",
            "evaluateMethod": "01",
            "tenderPrice": 500000,
            "blacklistEnter": "0",
            "remark": "无",
            "moneySource": "招标",
            "projectRegionCode": "440111113000"
        }
        response = self.post(url, data, self.villageHeaders)
        print('小额工程重提', response)
        self.assertEqual(response["message"], "操作成功")

    def test_03(self):
        """发布公告"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProjectTrade/publicTrade"
        data = {
            "smallProjectId": smallProjectId,
            "publicStartDate": datetime.datetime.today().strftime('%Y-%m-%d'),
            "publicEndDate": (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            "enrollEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=enrollEndDate)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "tenderEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=tenderEndDate)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "auctionStartDate": (datetime.datetime.today() + datetime.timedelta(days=auctionStartDate)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "auctionSignStartDate": (datetime.datetime.now() + datetime.timedelta(minutes=15)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "auctionSignEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=20)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "evaluateStartDate": (datetime.datetime.now() + datetime.timedelta(minutes=25)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "evaluateSignStartDate": (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "evaluateSignEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=35)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "winPublicPeriod": 0
        }
        response = self.post(url, data, self.auditHeaders)
        print("03发布公告")
        self.assertEqual(response["message"], "操作成功")

    def test_04(self):
        """循环报名-缴纳保证金"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        path = '/api/user/v1/user/open/censusLoginByCode'
        enrollUrl = "/api/auction_interface/v1/smallProject/smallProjectEnroll"
        checkUrl = '/api/auction_interface/v1/smallProject/getSmallProjectEarenstMoneyForPortal'
        addMoneyurl = "/api/account/v1/counterRecord/open/simulationAddMoney"
        url = "/api/auction_interface/v1/assetProjectEnroll/getEarenstMoneyForPortal"
        enrolldata = {"smallProjectId": smallProjectId}
        mysql = self.connect('cqjy')
        cursor = mysql.cursor()
        i = 0
        for phone in self.corporatePhone:
            data = {"phone": phone, "code": "888888", "user_Type": 2}
            sessionid = self.login(data, path)  # 循环登录
            loginHeader = {"sessionid": sessionid, "Content-Type": "application/json"}  # 组装header
            enroll = self.post(enrollUrl, enrolldata, loginHeader)  # 报名
            print("报名")
            self.assertEqual(enroll["message"], "操作成功")
            # # 查询保证金
            # check = self.post(checkUrl, enrolldata, loginHeader)
            # print(check)
            # addMoneydata = {"subAccountNo": check["data"]["mainAccountNo"], "payerAccountNo": 3602019309200000266,
            #                 "amount": 1}
            # addMoney = self.post(addMoneyurl, addMoneydata, loginHeader)
            # print("缴纳保证金")
            current_time = str(datetime.datetime.now())[:-7]
            sqle = "UPDATE t_asset_project_enroll SET pay_earnest_money_date = \"" + current_time + "\", pay_earnest_money = 1, system_feedback_status = 1 WHERE asset_project_enroll_id = " + self.getEnrollPageList(
                self.projectName)[i]["assetProjectEnrollId"]
            cursor.execute(sqle)    # 循环修改保证金缴纳状态
            portal = self.post(url, enrolldata, loginHeader)
            print("查看保证金")
            i += 1
            cursor.close()
        mysql.close()
        self.assertEqual(portal["message"], "操作成功")

    def test_05(self):
        """中标人信息"""
        smallProjectId = self.getFirstAuditPageList(self.projectName)["smallProjectId"]
        project_enroll_id = self.getEnrollPageList(self.projectName)[1]["assetProjectEnrollId"]
        corporatorUrl = '/api/admin/v1/smallProjectWin/getEnrollDetail'
        corporatorData = {"enrollId": project_enroll_id}
        corporator = self.post(corporatorUrl, corporatorData, self.villageHeaders)["data"]
        """指定中标人"""
        url = '/api/admin/v1/smallProjectWin/decideWin'
        data = {
            "winReason": "综合评分得分最高",
            "winContact": corporator["contactPhone"],
            "winContactUser": corporator["legalRepresent"],
            "winId": corporator["bidUserId"],
            "winIdCard": corporator["legalPersonCode"],
            "winIdCardType": "49",
            "winName": corporator["legalPerson"],
            "smallProjectId": smallProjectId,
            "fileList": [{
                "fileName": "bf8590f3-e21e-46d0-98c2-44928b2df0b6.png",
                "fileUrl": "https://cqjy-test.b2bwings.com/obs/default/441702000000/202304/fa74dd1f-a9bb-4029-af96-bef7164e7804.png"
            }]
        }
        response = self.post(url, data, self.villageHeaders)
        print("指定中标人", response)

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == "__main__":
    imageKey = "contract/440111000000/202303/ea364b65-c361-48f5-88b3-02ad28633dd1.png"
    docKey = "project/440111000000/202303/db04edbd-482d-46ab-9151-446ce04e33b7.doc"
    unittest.main()
