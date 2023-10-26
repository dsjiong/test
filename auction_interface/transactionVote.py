import unittest
from Setting.Base import *


class Transaction(unittest.TestCase, information):
    @classmethod
    def setUpClass(cls):
        """使用机构名称作为项目名称，拼接时间"""
        cls.cunInfo = information().getorgInfo(cls.villageHeaders)
        cls.getUser = information().getSysUser(cls.vPhone, cls.villageHeaders)
        prefix = cls.cunInfo["organizationName"]
        cls.transactionName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '事务表决测试'
        cls.voteUser = '110'  # 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表
        print(cls.transactionName)

    def test_01(self):
        """发起事务表决"""
        address = self.cunInfo["province"] + self.cunInfo["city"] + self.cunInfo["area"] + self.cunInfo["address"]
        url = '/api/admin/v1/transactionVote/saveTransactionVote'
        data = {
            "voteUser": self.voteUser,
            "voteDay": 5,
            "transactionVoteProjectId": "",
            "voteType": 0,
            "organizationName": self.cunInfo["organizationName"],
            "organizationAddress": address,
            "contactUserName": self.getUser['fullName'],
            "contactPhone": self.getUser['phone'],
            "transactionName": self.transactionName,
            "htmlContent": "<p>中国人民大学公共管理学院党委书记孙柏瑛认为，《操作指引》的发布，对北京社区既有多层住宅加装电梯的条件与技术标准进行了明确规定，这将对北京加装电梯工作产生积极影响。《操作指引》一方面建立了加装电梯的规范流程和技术标准，指明了社区公共设施供给的安全要求；另一方面，电梯加装能够解决老年居民群体上下楼难题，提高老年人群体的社会福利与生活品质，有助于“老破小”社区基础设施的改善。</p>",
            "transactionVoteSelectionList": [{
                "remark": "当前表决需要在甲、乙、丙三人中选择一人，则新增3个选项，分别是甲、乙、丙",
                "selectionName": "甲"
            }, {
                "remark": "支持",
                "selectionName": "乙"
            },{
                "remark": "驳斥",
                "selectionName": "丙"
            }, {
                "remark": "反对",
                "selectionName": "丁"
            }, {
                "remark": "同意",
                "selectionName": "戊"
            }, {
                "remark": "赞成",
                "selectionName": "己"
            }, {
                "remark": "拒绝",
                "selectionName": "庚"
            }, {
                "remark": "否决",
                "selectionName": "辛"
            }, {
                "remark": "附议",
                "selectionName": "壬"
            }, {
                "remark": "再议",
                "selectionName": "癸"
            }, {
                "remark": "批准",
                "selectionName": "子"
            }, {
                "remark": "回绝",
                "selectionName": "丑"
            }, {
                "remark": "答应",
                "selectionName": "寅"
            }, {
                "remark": "禁止",
                "selectionName": "卯"
            }, {
                "remark": "容许",
                "selectionName": "辰"
            }, {
                "remark": "争辩",
                "selectionName": "巳"
            }],
            "operate": 1  # 0:临时保存，1：提交，2：重新发起
        }
        tVote = self.post(url, data, self.villageHeaders)
        print('01发起表决', tVote)
        self.assertEqual(tVote['message'], '操作成功')

    # @unittest.skip("暂时不需要表决")
    def test_02(self):
        """获取表决详情进行表决"""
        pageUrl = '/api/admin/v1/transactionVote/getTransactionVotePage'
        pageData = {
            "current": 1,
            "size": 10,
            "queryType": 1,
            "transactionName": self.transactionName
        }
        projectId = self.post(pageUrl, pageData, self.villageHeaders)['data']['records'][0]['transactionVoteProjectId']
        detailUrl = '/api/admin/v1/transactionVote/getTransactionVoteDetail'
        detailData = {"transactionVoteProjectId": projectId}
        detail = self.post(detailUrl, detailData, self.villageHeaders)
        selectionId = detail['data']['transactionVoteSelectionList'][0]['transactionVoteProjectSelectionId']
        # 获取表决手机号
        phoneUrl = '/api/admin/v1/transactionVote/getTransactionVoteRecordPage'
        phoneData = {"current": 1, "size": 100, "transactionVoteProjectId": projectId}
        req = self.post(phoneUrl, phoneData, self.villageHeaders)['data']
        total = int(req['total'])
        records = req['records']
        path = '/api/user/v1/user/open/censusLoginByCode'
        voteUrl = '/api/admin/v1/vote/saveTransactionVoteRecord'
        voteData = {"transactionVoteProjectId": projectId, "transactionVoteProjectSelectionId": selectionId}
        for x in range(total):
            phone = records[x]['phone']
            if phone == '13751964417':
                continue
            data = {"phone": phone, "code": "888888", "user_Type": 1}
            sessionid = self.login(data, path)  # 循环登录
            header = {"sessionid": sessionid, "Content-Type": "application/json", "channel": "census"}
            vote = self.post(voteUrl, voteData, header)  # 循环同意
        print('02表决同意', vote)
        self.assertEqual(vote['message'], '操作成功')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
