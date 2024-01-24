from Setting.CustomSkip import *
from Setting.Base import *


# @stop_on_failure
class Tender(unittest.TestCase, information):

    @classmethod
    def setUpClass(cls):
        # 使用机构名称作为项目名称，拼接时间
        cls.mysql = information().connect('cqjy')
        cls.cursor = cls.mysql.cursor()
        cls.corporatePhone = [18722222224, 13802965035, 13000000000]
        cls.corporateName = ["测试供应链", "测试信巴迪", "测试百事通"]
        cls.defaultInfo = information().getDefaultInfo()
        prefix = cls.defaultInfo["organizationName"][0:3]
        cls.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '小额工程测试'

    def test_01(self):
        """招标申请"""
        print(self.projectName)
        url = "/api/admin/v1/smallProject/saveProjectApply"
        data = {
            "smallProjectId": None,
            "projectName": self.projectName,
            "organizationName": self.defaultInfo["organizationName"],
            "organizationId": self.defaultInfo["organizationId"],
            "organizationCode": self.defaultInfo["organizationCode"],
            "organizationAddress": self.defaultInfo["organizationProvince"] + self.defaultInfo["organizationCity"] +
               self.defaultInfo["organizationArea"] + self.defaultInfo["organizationStreet"] +
               self.defaultInfo["organizationAddress"],
            "areaOrganizationName": self.defaultInfo["areaOrganizationName"],
            "areaOrganizationId": self.defaultInfo["areaOrganizationId"],
            "areaOrganizationCode": "",
            "areaOrganizationAddress": self.defaultInfo["areaOrganizationProvince"] + self.defaultInfo[
                "areaOrganizationCity"] + self.defaultInfo["areaOrganizationArea"] + self.defaultInfo[
                "areaOrganizationStreet"] + self.defaultInfo["areaOrganizationAddress"],
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
        print('01小额工程申请')
        self.assertEqual(response["message"], "操作成功")

    def test_02(self):
        """项目审核"""
        pageList = self.getHistoryPageList(self.projectName)
        smallProjectId = pageList["smallProjectId"]
        tradeNo = pageList['projectTradeNo']
        self.setSubAccount(tradeNo, self.projectName)
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
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
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
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProject/saveProjectReApply"
        data = {
            "smallProjectId": smallProjectId,
            "projectName": self.projectName,
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
                "areaOrganizationCity"] + self.defaultInfo["areaOrganizationArea"] + self.defaultInfo[
                                           "areaOrganizationStreet"] + self.defaultInfo["areaOrganizationAddress"],
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
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
        url = "/api/admin/v1/smallProjectTrade/publicTrade"
        data = {
            "smallProjectId": smallProjectId,
            "publicStartDate": datetime.datetime.today().strftime('%Y-%m-%d'),
            "publicEndDate": (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            "enrollEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "tenderEndDate": (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            "auctionStartDate": (datetime.datetime.today() + datetime.timedelta(days=15)).strftime(
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
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
        path = '/api/user/v1/user/open/loginByCode'
        enrollUrl = "/api/auction/v1/smallProject/smallProjectEnroll"
        enrollData = {"smallProjectId": smallProjectId}
        for phone in self.corporatePhone:
            data = {"phone": phone, "code": "888888", "user_Type": 2}
            sessionid = self.login(data, path)  # 循环登录获取token
            loginHeader = {"sessionid": sessionid, "Content-Type": "application/json"}  # 组装header
            enroll = self.post(enrollUrl, enrollData, loginHeader)  # 报名
        print("报名")
        current_time = str(datetime.datetime.now())[:-7]
        sqle = ("UPDATE t_asset_project_enroll SET pay_earnest_money_date = \"" + current_time +
                "\", pay_earnest_money = 1, system_feedback_status = 1 WHERE small_project_id = " + smallProjectId)
        print(sqle)
        self.cursor.execute(sqle)  # 修改保证金缴纳状态
        try:
            self.mysql.commit()
        except Exception as e:
            self.mysql.rollback()
        self.cursor.close()
        self.mysql.close()
        self.assertEqual(enroll["message"], "操作成功")

    def test_05(self):
        """查看保证金"""
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
        path = '/api/user/v1/user/open/loginByCode'
        url = "/api/auction/v1/smallProject/queryByEarnestMoney"
        i = 0
        for phone in self.corporatePhone:
            project_enroll_id = self.getEnrollPageList(self.projectName, self.corporateName[i])[0]["assetProjectEnrollId"]
            enrolldata = {"smallProjectId": smallProjectId, "assetProjectEnrollId": project_enroll_id}
            data = {"phone": phone, "code": "888888", "user_Type": 2}
            sessionid = self.login(data, path)  # 循环登录获取token
            loginHeader = {"sessionid": sessionid, "Content-Type": "application/json"}  # 组装header
            portal = self.post(url, enrolldata, loginHeader)
            i = i + 1
        print("查看保证金")
        self.assertEqual(portal["message"], "操作成功")
        sleep(200)

    def test_06(self):
        """中标人信息"""
        smallProjectId = self.getHistoryPageList(self.projectName)["smallProjectId"]
        project_enroll_id = self.getEnrollPageList(self.projectName)[1]["assetProjectEnrollId"]
        corporateUrl = '/api/admin/v1/smallProjectWin/getEnrollDetail'
        corporationData = {"enrollId": project_enroll_id}
        corporate = self.post(corporateUrl, corporationData, self.villageHeaders)["data"]
        """指定中标人"""
        url = '/api/admin/v1/smallProjectWin/decideWin'
        data = {
            "winReason": "综合评分得分最高",
            "winContact": corporate["contactPhone"],
            "winContactUser": corporate["legalRepresent"],
            "winId": corporate["bidUserId"],
            "winIdCard": corporate["legalPersonCode"],
            "winIdCardType": "49",
            "winName": corporate["legalPerson"],
            "smallProjectId": smallProjectId,
            "winMoney": 5168,
            "fileList": [{
                "fileName": "bf8590f3-e21e-46d0-98c2-44928b2df0b6.png",
                "fileUrl": "https://cqjy-test.b2bwings.com/obs/default/441702000000/202304/fa74dd1f-a9bb-4029-af96-bef7164e7804.png"
            }]
        }
        response = self.post(url, data, self.villageHeaders)
        print("指定中标人", response)
        self.assertEqual(response['message'], "操作成功")

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
