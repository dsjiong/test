from time import sleep
from Setting.Base import *
from Setting.CustomSkip import *


@stop_on_failure
class Auction(unittest.TestCase, information):

    # 获取机构信息
    @classmethod
    def setUpClass(self):
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        self.enroll = 3
        self.startDate = 7
        self.endDate = 11
        prefix = information().getorgInfo(self.villageHeaders)["organizationName"][0:5]
        projectType = '竞价测试'
        self.assetName = self.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + projectType

    def test_01(self,):
        """资产登记"""
        print(self.assetName)
        resource = self.saveAssetResource(self.assetName)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

    # 立项申请-出租
    def test_02(self):
        assetId = self.getAssetPageList(self.assetName)
        asstInfo = self.getChooseAssetList(self.assetName, self.cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/assetProject/saveProjectApply"
        data = {
            "tradeMode": "01",
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
            "projectName": self.assetName,
            "projectType": asstInfo['assetGroupCodeLevel3'],
            "projectTypeName": asstInfo['assetGroupLevel3Name'],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防情况说明",
            "remarkOther": "其他重要情况说明",
            "remarkOtherClause": "合同其他条款",
            "remarkTaxation": "税费承担说明",
            "remark": "备注",
            "detailParamList": [{
                "assetId": assetId['assetId'],
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
                "purposeExplain": asstInfo["purposeExplain"],
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
                "landOccupation": asstInfo['landOccupation'],
                "landOccupationUnit": asstInfo['landOccupationUnit'],
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
                "assetGroupCode": "Z010100",
                "assetProjectId": None
            }],
            "fileSaveParams": [{
                "fileType": 1,
                "fileUrl": "project/441702000000/202307/38625b13-5963-48d2-a6ef-ef1144dcf3e1.png"
            }, {
                "fileType": 2,
                "fileUrl": "project/441702000000/202307/0cc60767-d50b-4523-b212-daa2ceff3e71.doc"
            }],
            "requires": "false",
            "remarkCondition": "无",
            "auditMaterialsSaveParams": [
                # {
                #     "materialsName": "材料1",
                #     "remark": "备注"
                # }
            ],
            "enrollType": 0,
            "blacklistEnter": "false",
            "priorityOriginalLessee": "false",
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 16888,
            "minBidRange": 10000,
            "maxBidRange": 100000,
            "assetDeliverDay": None,
            "progressiveIncrease": "false",  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": "",  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": '',  # 每次递增固定金额
            "progressiveIncreaseStartMonth": '',  # 从第n个月开始递增
            "progressiveIncreaseMonth": '',  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",  # 是否有免租期
            "rentFreePeriod": None,  # 免租天数
            "rentCollectMethod": '4',  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],  # 租赁开始时间
            "projectEndDate": str(datetime.datetime.now() + datetime.timedelta(days=30))[0:19],  # 租赁开始时间
            "projectTradeYear": "30天",
            "perpetualAssignment": "false",
            "repostAssetProject": "false",  # 流拍是否自动挂牌
            "contractExpirationDate": 10,
            "isSubmit": 1,
            "taskId": None
        }
        req = self.post(url, data, self.villageHeaders)
        print("02立项申请", req)
        self.assertEqual(req["message"], '操作成功')

    # 调用Base类方法立项审核
    def test_03(self):
        req = self.audit(self.assetName, status=11)
        print("03立项审核", req)
        self.assertEqual(req["message"], '操作成功')

    @skip_dependent("test_03")
    def test_04(self):
        """发布交易公告"""
        assetProjectId = self.getProjectInfoPage(self.assetName)
        url1 = "/api/admin/v1/sysUiaUser/getPersonalMessage"
        data1 = {"assetProjectId": assetProjectId, "type": ""}
        req1 = self.post(url1, data1, self.auditHeaders)
        # 详情
        url2 = "/api/admin/v1/assetProject/getProjectDetail"
        data2 = {"assetProjectId": assetProjectId, "type": ""}
        req2 = self.post(url2, data2, self.auditHeaders)
        # return {"contact": req["data"]["assetProject"]["contact"], "phone": req["data"]["assetProject"]["phone"]}
        # 发布交易公告
        getActivitiPage = self.getActivitiPage(projectName=self.assetName)
        taskId = getActivitiPage['taskId']
        businessKey = getActivitiPage['businessKey']
        url = "/api/admin/v1/assetInformation/saveAssetInformation"
        data = {
            "taskId": taskId,
            "businessKey": businessKey,
            "assetProjectId": assetProjectId,
            "auctionStartDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.startDate))[0:19],
            "auctionEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.endDate))[0:19],
            "contact": req2["data"]["assetProject"]["contact"],
            "phone": req2["data"]["assetProject"]['phone'],
            "earnestMoneyPayEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.enroll))[0:19],
            "enrollEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.enroll))[0:19],
            "extendSecond": 180,
            "maxExtend": 999,
            "resultPostPeriod": 5,
            "contractDeadlinePeriod": 10,
            "releaseUser": req1["data"]["name"],
            "sysOrganizationId": self.auditInfo["sysOrganizationId"],
            "releaseOrganizationName": self.auditInfo["organizationName"],
            "releaseDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],
            "publicStartDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "publicEndDate": (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"),
            "informationTitle": self.assetName + "交易公告",
            "projectName": self.assetName
        }
        req = self.post(url, data, self.auditHeaders)
        print("04发布交易公告", req)
        self.assertEqual(req["message"], '操作成功')

    def test_05(self):
        up = information().update()
        print("05修改个人付款账号")

    def test_06(self):
        """报名"""
        assetProjectId = self.getProjectInfoPage(self.assetName)
        url1 = "/api/auction_interface/v1/assetProjectAuditMaterials/getAssetProjectAuditMaterials"
        data1 = {"assetProjectId": assetProjectId}
        req1 = self.post(url1, data1, self.userHeaders)
        print("06报名-下一步", req1)
        # 报名-确定
        url = "/api/auction_interface/v1/assetProjectEnroll/saveAssetProjectEnroll"
        data = {
            "assetProjectId": assetProjectId  # ,
            # "files": [
            #     {
            #         "assetProjectAuditMaterialsId": req1["data"][0]["assetProjectAuditMaterialsId"],
            #         "fileUrl": "cqjy/000000/202211/679e7a2c-2b1f-439a-a11c-104d6134b3fb.jpg"
            #     }
            # ]
        }
        req = self.post(url, data, self.userHeaders)
        print("07报名-确定", req)
        self.assertEqual(req["message"], '操作成功')

    def test_07(self):
        """缴纳保证金并查看"""
        req = self.getEarenstMoneyForPortal(self.assetName, 3602019309200000266)
        print("08查看交易详情", req)
        self.assertEqual(req["message"], '操作成功')
        # sleep((self.earnestMoneyPayEndDate * 60) + 5)
        sleep(430)

    # 资格审核-审核
    # def test_08(self):
    #     assetProjectEnrollId = self.getEnrollAuditProjectDetail(self.assetName)
    #     url = "/api/admin/v1/assetProjectEnroll/audit"
    #     data = {"assetProjectEnrollId": assetProjectEnrollId, "type": 0, "remark": "通过"}
    #     req = self.post(url, data, self.auditHeaders)
    #     print("09资格审核-审核", req)
    #     self.assertEqual(req["message"], '操作成功')

    def test_08(self):
        """出价"""
        assetProjectId = self.getProjectInfoPage(self.assetName)
        url1 = "/api/auction_interface/v1/auctions/open/getAuctionPageList"
        data1 = {"projectName": self.assetName, "tradeMode": "01", "current": 1, "size": 16, "isShowPushData": 1,
                 "isShowTestData": "0"}
        req1 = self.post(url1, data1, self.userHeaders)['data']['records'][0]
        url2 = "/api/auction_interface/v1/auctions/auction_interface"
        data2 = {"assetProjectId": assetProjectId, "assetProjectAuctionId": req1["assetProjectAuctionId"],
                 "offerAPrice": 16888}
        req2 = self.post(url2, data2, self.userHeaders)
        print("09出价", req2)
        self.assertEqual(req2["message"], '操作成功')
        sleep(370)

    def test_09(self):
        """上传合同"""
        req = self.uploadContract(self.assetName)
        print("10上传合同", req)
        self.assertEqual(req["message"], '操作成功')

    def test_10(self):
        """合同审核"""
        req = self.activitiInstance(self.assetName)
        print("11合同审核", req)
        self.assertEqual(req["message"], '操作成功')

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main(failfast=True)
