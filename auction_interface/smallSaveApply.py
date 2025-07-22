from Setting.Base import *
from Setting.CustomSkip import *
from Setting.Retry import *

urllib3.disable_warnings()


# @stop_on_failure
class smallTrade(unittest.TestCase, information):

    @classmethod
    def setUpClass(self):
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = self.cunInfo["organizationName"][0:5]
        time = (datetime.datetime.now()).strftime('%y%m%d%H%M%S')
        self.assetName = self.projectName = prefix + time + '小额出售测试'

    def test_01(self):
        """创建资产"""
        print(self.assetName)
        resource = self.saveAssetResource(self.assetName)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

    def test_02(self):
        """小额立项申请"""
        asstInfo = self.getChooseAssetList(self.assetName, self.cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/smallTrade/smallApply"
        data = {
            "tradeMode": "03",
            "tradeType": "03",
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
            "projectType": asstInfo["assetGroupCodeLevel3"],
            "projectTypeName": asstInfo["assetGroupLevel3Name"],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防情况说明",
            "remarkOther": None,
            "remarkOtherClause": None,
            "remarkTaxation": None,
            "remark": None,
            "detailParamList": [
                {
                    "assetId": asstInfo['assetId'],
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
                    "acquiredDate": asstInfo['acquiredDate'],
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
                    "assetGroupCode": asstInfo["assetGroupCodeLevel3"],
                    "assetProjectId": None,
                }
            ],
            "priorityOriginalLessee": "false",
            "payTradeEarnestMoney": 'true',
            "tradeEarnestMoney": 1,
            "floorPrice": 4168,
            "minBidRange": None,
            "maxBidRange": None,
            "assetDeliverDay": "5",
            "progressiveIncrease": "false",  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": None,  # 每次递增固定金额
            "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
            "progressiveIncreaseMonth": None,  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",
            "rentFreePeriod": None,
            # "rentCollectMethod": 0,  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            # "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],  # 租赁开始时间
            # "projectEndDate": str(datetime.datetime.now() + datetime.timedelta(days=23))[0:19],  # 租赁开始时间
            # "projectTradeYear": "23天",
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
            "agent": "false",
            "taskId": None
        }
        apply = self.post(url, data, self.villageHeaders)
        print("02小额申请", apply)
        self.assertEqual(apply['message'], '操作成功')

    def test_03(self):
        """立项审核"""
        audit = self.audit(self.projectName, mode='03', status=11)
        print("03立项审核", audit)
        self.assertEqual(audit["message"], '操作成功')

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

    @Retry(max_n=1)
    def test_05(self):
        """05报名"""
        assetProjectId = self.getProjectInfoPage(self.projectName)
        url = "/api/auction/v1/assetProjectEnroll/saveAssetProjectEnroll"
        data = {"assetProjectId": assetProjectId}
        sign = self.post(url, data, self.userHeaders)
        print("05报名-确定", sign)
        self.assertEqual(sign['message'], '操作成功')

    def test_06(self):
        """06缴纳保证金"""
        pay = self.getEarenstMoneyForPortal(self.assetName, 3602019309200000266)
        print("06缴纳保证金", pay)
        self.assertEqual(pay["message"], '操作成功')
        sleep(360)

    def test_07(self):
        """07上传合同"""
        req = self.uploadContract(self.assetName, trade="20")
        print("07上传合同", req)
        self.assertEqual(req["message"], '操作成功')

    def test_08(self):
        """08合同审核"""
        req = self.activitiInstance(self.assetName)
        print("08合同审核", req)
        self.assertEqual(req["message"], '操作成功')

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
