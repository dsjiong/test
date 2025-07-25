import unittest
import time
from Setting.Base import *
from dateutil.relativedelta import relativedelta


from Setting.CustomSkip import *


# @stop_on_failure
class testOpenConsult(unittest.TestCase, information):

    @classmethod
    # 获取机构信息
    def setUpClass(self) -> None:
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getSysUser = information().getSysUser(self.vPhone, self.villageHeaders)
        self.projectName = self.assetName = information().getorgInfo(self.villageHeaders)["organizationName"][0:3] + \
                                            (datetime.datetime.now()).strftime('%y%m%d%H%M%S') + '协商测试'

    def test_01(self):
        """资产登记"""
        print(self.assetName)
        resource = self.saveAssetResource(self.assetName)
        print("*" * 10, resource, "*" * 10)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

    def test_02(self):
        """发布遴选公告"""
        # 利用资产名称查询资产信息
        asstInfo = self.getChooseAssetList(self.assetName, self.cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/openConsult/selectApply"
        data = {
            "tradeMode": "02",
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
            "contact": self.getSysUser['fullName'],
            "phone": self.getSysUser['phone'],
            "projectName": self.projectName,
            "projectType": asstInfo['assetGroupCodeLevel3'],
            "projectTypeName": asstInfo['assetGroupLevel3Name'],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防说明",
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
                    "assetCode": asstInfo['assetCode'],
                    "assetStatus": asstInfo['assetStatus'],
                    "assetNature": asstInfo['assetNature'],
                    "assetType": asstInfo["assetType"],
                    "assetTypeName": asstInfo["assetTypeName"],
                    "assetCategory": asstInfo['assetCategory'],
                    "assetCategoryName": asstInfo['assetCategoryName'],
                    "disposalMethod": asstInfo['disposalMethod'],
                    "acquiredDate": asstInfo['acquiredDate'],
                    "purpose": asstInfo['purpose'],
                    "purposeExplain": asstInfo['purposeExplain'],
                    "provinceId": self.cunInfo["provinceId"],
                    "province": self.cunInfo["province"],
                    "cityId": self.cunInfo["cityId"],
                    "city": self.cunInfo["city"],
                    "areaId": self.cunInfo["areaId"],
                    "area": self.cunInfo["area"],
                    "streetId": self.cunInfo["streetId"],
                    "street": self.cunInfo["street"],
                    "assetAddress": self.cunInfo["address"],
                    "originalValue": None,
                    "buildArea": asstInfo['buildArea'],
                    "buildAreaUnit": asstInfo['buildAreaUnit'],
                    "landOccupation": asstInfo['landOccupation'],
                    "landOccupationUnit": asstInfo['landOccupationUnit'],
                    "mainPicture": asstInfo['mainPicture'],
                    "temporaryAssets": 0,
                    "contractEndDate": None,
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
                    "assetGroupCode": asstInfo['assetGroupCodeLevel3'],
                    "assetProjectId": None
                }
            ],
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 6666,
            "assetDeliverDay": 1,  # 合同签订X日之后交付资产
            "progressiveIncrease": None,  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": None,  # 每次递增固定金额
            "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
            "progressiveIncreaseMonth": None,  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",  # 是否有免租期
            "rentFreePeriod": None,  # 免租天数
            "rentCollectMethod": 0,  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now())[0:10],
            "projectEndDate": self.projectEndDate(month=0),
            "projectTradeYear": "5年",
            "perpetualAssignment": "false",
            "repostAssetProject": "false",
            "fileSaveParams": [
                {
                    "fileType": 1,
                    "fileUrl": "project/440111000000/202303/4234d96b-762c-4dc8-b15d-44a71175163f.png"
                },
                {
                    "fileType": 2,
                    "fileUrl": "project/440111000000/202303/fbc67d84-92f0-4fe0-95b0-4ed8a28e5796.doc"
                }
            ],
            "requires": "false",
            "remarkCondition": "无",
            "auditMaterialsSaveParams": [],
            "enrollType": 0,
            "blacklistEnter": "false",
            "isSubmit": 1,
            "taskId": None,
            "applyType": 1,
            "delivery": "按现状交付"
        }
        req = self.post(url, data, self.villageHeaders)
        print("02发布遴选公告", req)
        self.assertEqual(req["message"], '操作成功')

    def test_03(self):
        """遴选审核"""
        req = self.audit(self.projectName, mode='02', status=101)
        print("03遴选审核", req)
        self.assertEqual(req["message"], '操作成功')

    def test_04(self):
        """意向人申请"""
        projectId = self.getProjectInfoPage(self.projectName)
        url = '/api/auction/v1/assetProjectEnroll/saveAssetProjectEnroll'
        data = {"assetProjectId": projectId, "files": []}
        req = self.post(url, data, self.userHeaders)
        print("04意向人申请", req)
        sleep(80)
        self.assertEqual(req["message"], '操作成功')

    def test_05(self):
        """转立项"""
        # 获取projectId
        projectId = self.getProjectInfoPage(self.projectName)
        # 获取项目assetProjectEnrollId
        url1 = '/api/admin/v1/assetProject/getProjectDetail'
        data1 = {"assetProjectId": projectId, "type": ""}
        req1 = self.post(url1, data1, self.villageHeaders)
        # 转立项申请
        url2 = '/api/admin/v1/openConsult/auditSelectEnroll'
        data2 = {"assetProjectId": projectId,
                 "assetProjectEnrollId": req1["data"]["enrollInfo"][0]["assetProjectEnrollId"], "type": 0,
                 "remark": None}
        req2 = self.post(url2, data2, self.villageHeaders)
        # 获取遴选申请详情
        url3 = '/api/admin/v1/assetProject/getProjectDetail'
        data3 = {"assetProjectId": projectId, "type": ""}
        req3 = self.post(url3, data3, self.villageHeaders)
        # 获取assetProjectSchemeConsultId
        url4 = '/api/admin/v1/assetProject/getProjectApply'
        data4 = {"assetProjectId": projectId, "type": ""}
        req4 = self.post(url4, data4, self.villageHeaders)
        # 遴选转申请
        url = '/api/admin/v1/openConsult/selectApply'
        data = {
            "assetProjectOtherId": req3['data']['projectOther']['assetProjectOtherId'],
            "assetProjectId": projectId,
            "remarkCondition": "无",
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防说明",
            "remarkOther": None,
            "remarkOtherClause": None,
            "remarkTaxation": None,
            "remark": None,
            "gmtCreate": req3['data']['projectOther']['gmtCreate'],
            "gmtModified": req3['data']['projectOther']['gmtModified'],
            "createUserId": req3['data']['projectOther']['createUserId'],
            "modifiedUserId": None,
            "organizationName": self.cunInfo['organizationName'],
            "organizationId": self.cunInfo['sysOrganizationId'],
            "projectName": self.projectName,
            "htmlContent": None,
            "projectAmount": 66666,
            "projectAmountUnit": "元/月",
            "projectType": req3["data"]['assetProject']['projectType'],
            "projectNo": req3["data"]['assetProject']['projectNo'],
            "originalProjectNo": None,
            "tradeNo": req3["data"]['assetProject']['tradeNo'],
            "businessKey": req3["data"]['assetProject']['businessKey'],
            "tradeType": req3["data"]['assetProject']['tradeType'],
            "tradeMode": req3["data"]['assetProject']['tradeMode'],
            "projectStatus": req3["data"]['assetProject']['projectStatus'],
            "initiateDate": req3["data"]['assetProject']['initiateDate'],
            "passDate": req3["data"]['assetProject']['passDate'],
            "auctionStartDate": None,
            "auctionEndDate": None,
            "publicStartDate": None,
            "publicEndDate": None,
            "enrollStartDate": None,
            "enrollEndDate": None,
            "contractUploadDate": None,
            "contractDeadlineDate": None,
            "examineDeadlineDate": None,
            "provinceId": self.cunInfo["provinceId"],
            "province": self.cunInfo["province"],
            "cityId": self.cunInfo["cityId"],
            "city": self.cunInfo["city"],
            "areaId": self.cunInfo["areaId"],
            "area": self.cunInfo["area"],
            "streetId": self.cunInfo["streetId"],
            "street": self.cunInfo["street"],
            "address": self.cunInfo["address"],
            "contact": self.getSysUser['fullName'],
            "phone": self.getSysUser['phone'],
            "auctionUserName": "测试邓",
            "auctionUserId": None,
            "contactPhone": None,
            "auctionPrice": None,
            "legalIdCard": None,
            "auctionDate": None,
            "rentCollectMethod": 0,  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": req3["data"]['assetProject']['projectStartDate'],
            "projectEndDate": req3["data"]['assetProject']['projectEndDate'],
            "projectTradeYear": req3["data"]['assetProject']['projectTradeYear'],
            "createUserName": req3["data"]['assetProject']['createUserName'],
            "requires": False,
            "projectCloseType": None,
            "initOrganizationId": self.cunInfo['sysOrganizationId'],
            "initOrganizationName": self.cunInfo['organizationName'],
            "initUserId": self.cunInfo['sysUserId'],
            "initUserName": "joe",
            "complaintCall": "020-88888888",
            "complaintEmail": "",
            "mainPicture": "asset/441702000000/202305/b2d129b7-2362-4eb3-b33a-7cee89199050.jpg",
            "appKey": None,
            "detailUrl": None,
            "detailUrlType": None,
            "assetType": None,
            "assetTypeName": None,
            "assetCategory": None,
            "assetCategoryName": None,
            "tradeReleaseDate": None,
            "checkCode": req3["data"]['assetProject']['checkCode'],
            "showTestData": req3["data"]['assetProject']['showTestData'],
            "contactIdx": req3["data"]['assetProject']['contactIdx'],
            "phoneIdx": req3["data"]['assetProject']['phoneIdx'],
            "contactPhoneIdx": None,
            "legalIdCardIdx": None,
            "tradeOrganizationId": self.auditInfo['sysOrganizationId'],
            "tradeOrganizationName": self.auditInfo['sysOrganizationId'],
            "tradeOrganizationAddress": "广东省阳江市江城区城东街道农科路22之1号",
            "tradeOrganizationUserName": "黄先生",
            "tradeOrganizationUserPhone": "13751964421",
            "tradeCode": "Z01",
            "provinceCode": "440000000000",
            "cityCode": "441700000000",
            "areaCode": "441702000000",
            "streetCode": "441702006000",
            "assetProjectCloud": False,
            "sevenDayStatus": 0,
            "isOrganizationActTimerConfig": None,
            "assetInformationId": None,
            "projectStatusText": None,
            "applicantsCount": 0,
            "perpetualAssignment": False,
            "projectTypeName": req3['data']['assetProject']['projectTypeName'],
            "assetGroupCode": req3['data']['assetProject']['assetGroupCode'],
            "assetGroupName": req3['data']['assetProject']['assetGroupName'],
            "flowAssetProjectId": None,
            "contractExpirationDate": 10,
            "assetProjectSchemeConsultId": req4["data"]["scheme"]["assetProjectSchemeConsultId"],
            "blacklistEnter": True,
            "enrollType": 0,
            "payTradeEarnestMoney": True,
            "tradeEarnestMoney": req3["data"]['projectScheme']['tradeEarnestMoney'],
            "floorPrice": req3["data"]['projectScheme']['floorPrice'],
            "floorPriceUnit": req3["data"]['projectScheme']['floorPriceUnit'],
            "assetDeliverDay": req3["data"]['projectScheme']['assetDeliverDay'],
            "progressiveIncrease": False,
            "progressiveIncreaseWay": None,
            "progressiveIncreaseStartMonth": None,
            "progressiveIncreaseMonth": None,
            "progressiveIncreaseIncrease": None,
            "progressiveIncreaseAmount": None,
            "rentFree": False,
            "rentFreePeriod": None,
            "detailParamList": [{
                "assetProjectDetailId": req4["data"]['details']['assetProjectDetailId'],
                "assetProjectId": projectId,
                "sysOrganizationId": self.cunInfo['sysOrganizationId'],
                "sysOrganizationName": self.cunInfo['sysOrganizationId'],
                "assetId": req3["data"]['assetDetails'][0]['assetId'],
                "assetType": None,
                "assetTypeName": None,
                "assetCategory": None,
                "assetCategoryName": None,
                "assetNature": None,
                "assetCode": req3["data"]['assetDetails'][0]['assetCode'],
                "assetName": req3["data"]['assetDetails'][0]['assetName'],
                "purpose": None,
                "purposeExplain": req3['data']['assetDetails'][0]['purposeExplain'],
                "originalValue": req3['data']['assetDetails'][0]['originalValue'],
                "buildArea": req3['data']['assetDetails'][0]['buildArea'],
                "buildAreaUnit": req3['data']['assetDetails'][0]['buildAreaUnit'],
                "landOccupation": req3['data']['assetDetails'][0]['landOccupation'],
                "landOccupationUnit": req3['data']['assetDetails'][0]['landOccupationUnit'],
                "threeCapitalsOwnershipNo": None,
                "sharedArea": None,
                "sharedAreaUnit": None,
                "unitNo": None,
                "provinceId": self.cunInfo["provinceId"],
                "province": self.cunInfo["province"],
                "cityId": self.cunInfo["cityId"],
                "city": self.cunInfo["city"],
                "areaId": self.cunInfo["areaId"],
                "area": self.cunInfo["area"],
                "streetId": self.cunInfo["streetId"],
                "street": self.cunInfo["street"],
                "assetAddress": self.cunInfo["address"],
                "gmtCreate": req3['data']['projectScheme']['gmtCreate'],
                "createUserId": req3['data']['projectScheme']['createUserId'],
                "gmtModified": req3['data']['projectScheme']['gmtModified'],
                "modifiedUserId": None,
                "videoUrl": None,
                "videoThumbnailUrl": None,
                "provinceCode": None,
                "cityCode": None,
                "areaCode": None,
                "streetCode": None,
                "mainPicture": req3['data']['assetDetails'][0]['mainPicture'],
                "images": req3['data']['assetDetails'][0]['images'],
                "assetGroupCode": req3['data']['assetDetails'][0]['assetGroupCode'],
                "assetGroupLevel1Name": None,
                "assetGroupLevel2Name": None,
                "assetGroupLevel3Name": None,
                "assetGroupLevel4Name": None,
                "assetGroupLevel5Name": None
            }],
            "fileSaveParams": [{
                "fileType": 1,
                "fileUrl": "project/440882000000/202303/3999f135-0ec2-4406-82b0-142299509a21.jpg"
            }, {
                "fileType": 2,
                "fileUrl": "project/440882000000/202303/926c6fe0-652d-4cdd-ba88-02cacfa4e7c9.doc"
            }],
            "auditMaterialsSaveParams": [],
            "confirmedPrice": 6666,
            "isSubmit": 1,
            "taskId": None,
            "agent": "false",
            "delivery": "按现状交付",
            "applyType": 2
        }
        req = self.post(url, data, self.villageHeaders)
        print('05指定意向人并转立项申请', req)
        self.assertEqual(req["message"], '操作成功')

    def test_07(self):
        """立项审核"""
        req = self.audit(self.projectName, mode='02', status=11)
        self.assertEqual(req["message"], '操作成功')
        print('07立项审核', req)

    def test_08(self):
        """意向人同意"""
        project = self.getProjectManagementList(self.projectName)
        url = '/api/auction/v1/openConsult/intentConfirm'
        data = {"assetProjectId": project['assetProjectId'],
                "businessKey": project['businessKey'], "status": 1, "annotation": ""}
        req = self.post(url, data, self.userHeaders)
        print('08意向人同意', req)
        self.assertEqual(req["message"], '操作成功')

    def test_09(self):
        """缴纳保证金并查询"""
        req = self.getEarenstMoneyForPortal(self.projectName, 3602019309200000266)
        print('09查询保证金', req)
        self.assertEqual(req["message"], '操作成功')
        time.sleep(300)

    def test_10(self):
        """上传合同"""
        req = self.uploadContract(self.projectName)
        print("10上传合同", req)
        self.assertEqual(req["message"], '操作成功')

    def test_11(self):
        """合同审核"""
        req = self.activitiInstance(self.projectName)
        print("11合同审核", req)
        self.assertEqual(req["message"], '操作成功')

    def test_12(self):
        """查询成交公告"""
        req = self.search_notice(self.assetName)
        print("12查询成交公告", req)
        self.assertEqual(req["data"]["records"][0]["projectName"], self.projectName)

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
