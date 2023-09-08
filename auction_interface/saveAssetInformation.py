import unittest
import Setting.Base
from Setting.Base import *
from Setting.CustomSkip import *

@stop_on_failure
class MyTestCase(unittest.TestCase, information):

    @ classmethod
    def setUpClass(self) -> None:
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        getActivitiPage = information().getActivitiPage()
        self.releaseUser = information().getSysUser(self.vPhone, self.villageHeaders)
        self.taskId = getActivitiPage['taskId']
        self.businessKey = getActivitiPage['businessKey']
        self.assetProjectId = getActivitiPage['assetProjectId']
        self.projectName = getActivitiPage['projectName']
        print(self.projectName, '+', self.assetProjectId)
        self.earnestMoneyPayEndDate = 5
        self.auctionStartDate = 10
        self.auctionEndDate = 15

    # 获取项目详情
    def test_getProjectDetail(self):
        url = "/api/admin/v1/assetProject/getProjectDetail"
        data = {"assetProjectId": self.assetProjectId, "type": ""}
        req = public().post(url, data, self.auditHeaders)
        self.assertEqual(req["message"], '操作成功')
        return {"contact": req["data"]["assetProject"]["contact"], "phone": req["data"]["assetProject"]["phone"]}

    # 发布交易公告
    def test_pushNotice(self):
        url = "/api/admin/v1/assetInformation/saveAssetInformation"
        data = {
            "taskId": self.taskId,
            "businessKey": self.businessKey,
            "assetProjectId": self.assetProjectId,
            "auctionStartDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.auctionStartDate))[0:19],
            "auctionEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.auctionEndDate))[0:19],
            "contact": self.test_getProjectDetail()['contact'],
            "phone": self.test_getProjectDetail()['phone'],
            "earnestMoneyPayEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.earnestMoneyPayEndDate))[
                                      0:19],
            "enrollEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=self.earnestMoneyPayEndDate))[0:19],
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

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
