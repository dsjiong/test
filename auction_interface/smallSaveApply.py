from time import sleep
import unittest
from Setting.Base import *
from Setting.CustomSkip import skip_dependent

urllib3.disable_warnings()


class smallTrade(unittest.TestCase, information):

    @classmethod
    def setUpClass(self):
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = self.cunInfo["organizationName"][0:5]
        self.assetName = self.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '小额测试'

    # 创建资产
    def test_01(self):
        print(self.assetName)
        resource = self.saveAssetResource(self.assetName)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

    # 小额立项申请
    def test_02(self):
        assetId = self.getAssetPageList(self.assetName)
        asstInfo = self.getChooseAssetList(self.assetName, self.cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/smallTrade/smallApply"
        data = {
            "tradeMode": "03",
            "tradeType": "01",
            "organizationId": self.cunInfo["sysOrganizationId"],
            "organizationName": self.cunInfo["organizationName"],
            "provinceId": self.cunInfo["provinceId"],
            "province": self.cunInfo["province"],
            "cityId": self.cunInfo["cityId"],
            "city": self.cunInfo["city"],
            "areaId": self.cunInfo["areaId"],
            "area": self.cunInfo["area"],
            "streetId": self.cunInfo["streetId"],
            "street": self.cunInfo["street"],
            "address": self.cunInfo["address"],
            "contact": self.getsysuser['fullName'],
            "phone": self.getsysuser['phone'],
            "projectName": self.projectName,
            "projectType": asstInfo["assetGroupCodeLevel5"],
            "projectTypeName": asstInfo["assetGroupLevel5Name"],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防情况说明",
            "remarkOther": None,
            "remarkOtherClause": None,
            "remarkTaxation": None,
            "remark": None,
            "detailParamList": [
                {
                    "assetId": assetId['assetId'],
                    "sysOrganizationId": self.cunInfo["sysOrganizationId"],
                    "sysOrganizationName": self.cunInfo["organizationName"],
                    "assetName": self.assetName,
                    "assetCode": asstInfo["assetCode"],
                    "assetStatus": asstInfo["assetStatus"],
                    "assetNature": asstInfo["assetNature"],
                    "assetType": asstInfo["assetType"],
                    "assetTypeName": asstInfo["assetTypeName"],
                    "assetCategory": asstInfo['assetCategory'],
                    "assetCategoryName": asstInfo['assetCategoryName'],
                    "disposalMethod": asstInfo['disposalMethod'],
                    "acquiredDate": (
                        (datetime.date.today() + datetime.timedelta(days=-30)).strftime('%Y-%m-%d {}')).format(
                        '00:00:00'),
                    "purpose": asstInfo['purpose'],
                    "purposeExplain": asstInfo["assetGroupLevel5Name"],
                    "province": self.cunInfo["province"],
                    "provinceId": self.cunInfo["provinceId"],
                    "city": self.cunInfo["city"],
                    "cityId": self.cunInfo["cityId"],
                    "area": self.cunInfo["area"],
                    "areaId": self.cunInfo["areaId"],
                    "street": self.cunInfo["street"],
                    "streetId": self.cunInfo["streetId"],
                    "assetAddress": self.cunInfo["address"],
                    "originalValue": asstInfo['originalValue'],
                    "buildArea": asstInfo['buildArea'],
                    "buildAreaUnit": asstInfo['buildAreaUnit'],
                    "landOccupation": None,
                    "landOccupationUnit": None,
                    "mainPicture": asstInfo['mainPicture'],
                    "temporaryAssets": asstInfo['temporaryAssets'],
                    "contractEndDate": asstInfo['contractEndDate'],
                    "assetGroupCodeLevel1": asstInfo['assetGroupCodeLevel1'],
                    "assetGroupCodeLevel2": asstInfo['assetGroupCodeLevel2'],
                    "assetGroupCodeLevel3": asstInfo['assetGroupCodeLevel3'],
                    "assetGroupCodeLevel4": asstInfo['assetGroupCodeLevel4'],
                    "assetGroupCodeLevel5": asstInfo['assetGroupCodeLevel5'],
                    "assetGroupLevel1Name": asstInfo['assetGroupLevel1Name'],
                    "assetGroupLevel2Name": asstInfo['assetGroupLevel2Name'],
                    "assetGroupLevel3Name": asstInfo['assetGroupLevel3Name'],
                    "assetGroupLevel4Name": asstInfo['assetGroupLevel4Name'],
                    "assetGroupLevel5Name": asstInfo['assetGroupLevel5Name'],
                    "oriUserName": asstInfo['oriUserName'],
                    "oriUserType": asstInfo['oriUserType'],
                    "oriIdCardType": asstInfo['oriIdCardType'],
                    "oriIdCardNo": asstInfo['oriIdCardNo'],
                    "oriUserPhone": asstInfo['oriUserPhone'],
                    "assetGroupCode": asstInfo["assetGroupCodeLevel5"],
                    "assetProjectId": None,
                }
            ],
            "priorityOriginalLessee": "false",
            "payTradeEarnestMoney": 'true',
            "tradeEarnestMoney": 1,
            "floorPrice": 30000,
            "minBidRange": None,
            "maxBidRange": None,
            "assetDeliverDay": "15",
            "progressiveIncrease": "false",  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": None,  # 每次递增固定金额
            "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
            "progressiveIncreaseMonth": None,  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",
            "rentFreePeriod": None,
            "rentCollectMethod": 0,  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],  # 租赁开始时间
            "projectEndDate": str(datetime.datetime.now() + datetime.timedelta(days=23))[0:19],  # 租赁开始时间
            "projectTradeYear": "23天",
            "perpetualAssignment": "false",
            "repostAssetProject": "false",
            "fileSaveParams": [
                {
                    "fileType": 1,
                    "fileUrl": "project/441802000000/202301/361d7eb0-7a85-447d-8e9c-5263d36477b8.png"
                },
                {
                    "fileType": 2,
                    "fileUrl": "project/441802000000/202301/519f3e3b-a87e-4a49-be4a-cb9d2913c21a.doc"
                }
            ],
            "requires": "false",
            "remarkCondition": "无",
            "auditMaterialsSaveParams": [
            ],
            "enrollType": 0,
            "blacklistEnter": "true",
            "isSubmit": 1,
            "taskId": None
        }
        apply = self.post(url, data, self.villageHeaders)
        print("02小额申请", apply)
        self.assertEqual(apply['message'], '操作成功')

    # 立项审核
    def test_03(self):
        audit = self.audit(self.projectName, mode='03', status=11)
        print("03立项审核", audit)
        self.assertEqual(audit["message"], '操作成功')

    @skip_dependent("test_03")
    def test_04(self):
        """04发布交易公告"""
        projectInfo = self.getActivitiPage(mode='03', status=20, projectName=self.projectName)
        url = '/api/admin/v1/smallTrade/releasePost'
        data = {
            "taskId": projectInfo['taskId'],
            "businessKey": projectInfo['businessKey'],
            "assetProjectId": projectInfo['assetProjectId'],
            "informationTitle": self.projectName + "交易公告",
            "projectName": self.projectName,
            "publicStartDate": (datetime.date.today()).strftime('%Y-%m-%d'),
            "publicEndDate": (datetime.date.today()).strftime('%Y-%m-%d'),
            "resultPostPeriod": 5,
            "contractDeadlinePeriod": 10
        }
        repost = self.post(url, data, self.auditHeaders)
        print('04发布交易公告', repost)
        self.assertEqual(repost['message'], '操作成功')

    def test_05(self):
        """05修改个人付款账号"""
        up = information().update()
        print("05修改个人付款账号", up)

    def test_06(self):
        """06报名"""
        assetProjectId = self.getProjectInfoPage(self.projectName)
        url = "/api/auction_interface/v1/assetProjectEnroll/saveAssetProjectEnroll"
        data = {"assetProjectId": assetProjectId}
        sign = self.post(url, data, self.userHeaders)
        print("06报名-确定", sign)
        self.assertEqual(sign['message'], '操作成功')

    def test_07(self):
        """07查看交易详情"""
        pay = self.getEarenstMoneyForPortal(self.assetName, 3602019309200000266)
        print("07查看交易详情", pay)
        self.assertEqual(pay["message"], '操作成功')
        sleep(630)

    def test_08(self):
        """08上传合同"""
        req = self.uploadContract(self.assetName)
        print("08上传合同", req)
        self.assertEqual(req["message"], '操作成功')

    def test_09(self):
        """09合同审核"""
        req = self.activitiInstance(self.assetName)
        print("09合同审核", req)
        self.assertEqual(req["message"], '操作成功')

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
