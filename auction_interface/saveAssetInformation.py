import unittest
import Setting.Base
from Setting.Base import *
from Setting.CustomSkip import *


# @stop_on_failure
class MyTestCase(unittest.TestCase, information):

    @classmethod
    def setUpClass(self) -> None:
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        getActivitiPage = information().getActivitiPage(tradeType="03")
        self.releaseUser = information().getSysUser(self.vPhone, self.villageHeaders)
        self.taskId = getActivitiPage['taskId']
        self.businessKey = getActivitiPage['businessKey']
        self.assetProjectId = getActivitiPage['assetProjectId']
        self.projectName = getActivitiPage['projectName']
        self.enrollEndDate = 2
        self.auctionStartTime = 60
        self.auctionEndTime = 67

    # 获取项目详情
    def test_01(self):
        url = "/api/admin/v1/assetProject/getProjectDetail"
        data = {"assetProjectId": self.assetProjectId}
        req = public().post(url, data, self.auditHeaders)
        self.assertEqual(req["message"], '操作成功')
        return {"contact": req["data"]["assetProject"]["contact"], "phone": req["data"]["assetProject"]["phone"],
                "requires": req["data"]["assetProject"]["requires"]}

    # 发布交易公告
    def test_02(self):
        print(self.projectName, '+', self.assetProjectId)
        url = "/api/admin/v1/assetInformation/saveAssetInformation"
        data = {
            "taskId": self.taskId,
            "businessKey": self.businessKey,
            "assetProjectId": self.assetProjectId,
            "auctionStartDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.auctionStartTime))[0:19],
            "auctionEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.auctionEndTime))[0:19],
            "contact": self.test_01()['contact'],
            "phone": self.test_01()['phone'],
            "earnestMoneyPayEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.enrollEndDate))[
                                      0:19],
            "enrollEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.enrollEndDate))[0:19],
            "extendSecond": 180,
            "maxExtend": 999,
            "resultPostPeriod": 5,
            "contractDeadlinePeriod": 10,
            "releaseUser": self.releaseUser,
            "sysOrganizationId": self.auditInfo["sysOrganizationId"],
            "releaseOrganizationName": self.auditInfo["organizationName"],
            "releaseDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],
            "publicStartDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "publicEndDate": (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"),
            "informationTitle": self.projectName + "交易公告",
            "projectName": self.projectName
        }
        req = self.post(url, data, self.auditHeaders)
        print("发布交易公告", req)
        self.assertEqual(req["message"], '操作成功')  # add assertion here

    def test_03(self):
        """报名"""
        requires = self.test_01()['requires']
        url1 = "/api/auction/v1/assetProjectAuditMaterials/getAssetProjectAuditMaterials"
        data1 = {"assetProjectId": self.assetProjectId}
        req1 = self.post(url1, data1, self.userHeaders)
        print("报名-下一步", req1)
        # 报名-确定
        url = "/api/auction/v1/assetProjectEnroll/saveAssetProjectEnroll"
        # requires为true报名需要上传文件
        if requires:
            data = {
                "assetProjectId": self.assetProjectId,
                "files": [
                    {
                        "assetProjectAuditMaterialsId": req1["data"][0]["assetProjectAuditMaterialsId"],
                        "fileUrl": "cqjy/000000/202211/679e7a2c-2b1f-439a-a11c-104d6134b3fb.jpg"
                    }
                ]
            }
        else:
            data = {"assetProjectId": self.assetProjectId}
        req = self.post(url, data, self.userHeaders)
        print("报名-确定", req)
        self.assertEqual(req["message"], '操作成功')

    def test_04(self):
        """缴纳保证金并查看"""
        req = self.getEarenstMoneyForPortal(self.projectName, 3602019309200000266)
        print("查看交易详情", req)
        self.assertEqual(req["type"], '1')
        t1 = (self.enrollEndDate * 60) + 5
        sleep(int(t1))

    def test_05(self):
        """资格审核-审核"""
        if self.test_01()['requires']:
            assetProjectEnrollId = self.getEnrollAuditProjectDetail(self.assetProjectId)
            url = "/api/admin/v1/assetProjectEnroll/audit"
            data = {"assetProjectEnrollId": assetProjectEnrollId, "type": 0, "remark": "通过"}
            req = self.post(url, data, self.auditHeaders)
            print("手动审核")
        else:
            print("自动审核")
        t2 = (self.auctionStartTime - self.enrollEndDate) * 60 + 20
        sleep(int(t2))

    def test_06(self):
        """出价"""
        url1 = "/api/auction/v1/auctions/open/getAuctionPageList"
        data1 = {"projectName": self.projectName, "tradeMode": "01", "current": 1, "size": 16, "isShowPushData": 1,
                 "isShowTestData": "0"}
        req1 = self.post(url1, data1, self.userHeaders)['data']['records'][0]
        url2 = "/api/auction/v1/auctions/auction"
        data2 = {"assetProjectId": self.assetProjectId, "assetProjectAuctionId": req1["assetProjectAuctionId"],
                 "offerAPrice": req1['floorPrice']}
        req2 = self.post(url2, data2, self.userHeaders)
        print("出价", req2)
        self.assertEqual(req2["message"], '操作成功')

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
