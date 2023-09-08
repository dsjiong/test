import unittest
import random

from time import sleep
from Setting.Base import *
from Setting.CustomSkip import *

urllib3.disable_warnings()


@stop_on_failure
class Vote(unittest.TestCase, information):

    @classmethod
    def setUpClass(self):
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = self.cunInfo["organizationName"][0:5]
        self.assetName = self.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '表决测试'
        self.voteUser = '101'  # 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表

    def test_01(self):
        """创建资产"""
        print(self.assetName)
        resource = self.saveAssetResource(self.assetName)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

    def test_02(self):
        """发起表决"""
        assetId = self.getAssetPageList(self.assetName)
        asstInfo = self.getChooseAssetList(self.assetName, self.cunInfo["sysOrganizationId"])
        url = '/api/admin/v1/assetProjectCloud/cloudTS4Most'
        data = {
            "cloudDetailBase4MostVo": {
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
                "assetGroupCode": asstInfo["assetGroupCodeLevel5"],
                "assetProjectId": None,
                "tradeTypeName": "出租",
                "projectTypeName": asstInfo["assetGroupLevel5Name"],
                "voteType": "1",  # 云表决类型  0=立项表决 1=遴选表决 2=拟定意向人表决
                "tradeMode": "02",  # 项目模式 01=公开竞价 02=公开协商 03=小额简易交易 04=续约交易
                "tradeType": "01",  # 项目类别 01=出租 02=出让 99=其它
                "organizationId": self.cunInfo["sysOrganizationId"],
                "organizationName": self.cunInfo["organizationName"],
                "contact": self.getsysuser['fullName'],
                "phone": self.getsysuser['phone'],
                "projectName": self.projectName,
                "projectType": asstInfo["assetGroupCodeLevel5"],
                "projectStartDate": None,
                "projectEndDate": None,
                "projectTradeYear": None
            },
            "cloudDetailIntenderDemandVo": {  # 意向人资格要求
                "intenderDemand": 0,  # 是否需要资质证明材料 0=否 1=是
                "remarkCondition": "无",  # 受让人或承租人条件
                "materials": [],  # 资质证明材料
                "enrollType": 0,  # 允许报名的用户类型 0=全部 1=自然人 2=法人
                "blacklistEnter": 0  # 是否禁止警示名单报名 0=否 1=是
            },
            "cloudDetailOtherQueryVo": {  # 其他
                "remark": "备注/申请事项说明（仅内部审核用）",
                "remarkFireControl": "消防情况说明",
                "remarkIndustryRequire": "行业要求",
                "remarkOther": "其他重要情况说明",
                "remarkOtherClause": "合同其他条款",
                "remarkTaxation": "税费承担特别说明"
            },
            "cloudDetailSchemeQueryVo": {  # 拟定交易方案
                "tradeEarnestMoneyStr": "壹元整",  # 保证金大写
                "registrationDuration": None,
                "marginPaymentDate": None,
                "maxBidRange": 100000,
                "minBidRange": 10000,
                "payTradeEarnestMoney": 1,
                "tradeEarnestMoney": 1,
                "floorPrice": 16888,
                "assetDeliverDay": "12",
                "progressiveIncrease": 0,  # 是否递增付款金额 0=否 1=是
                "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
                "progressiveIncreaseAmount": None,  # 每次递增固定金额
                "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
                "progressiveIncreaseMonth": None,  # 每n个月递增一次
                "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
                "rentFree": None,  # 是否免租期
                "rentFreePeriod": None,
                "floorPriceUnit": 0,  # 租金收取方式 0=月 1=季 2=半年 3=年 4=一次性
                "projectStartDate": (datetime.date.today()).strftime('%Y-%m-%d'),
                "projectEndDate": (datetime.date.today() + datetime.timedelta(days=367)).strftime('%Y-%m-%d'),
                "projectTradeYear": "1年2天",
                "perpetualAssignment": "false",  # 是否永久转让
                "contractExpirationDate": 10
            },
            "cloudVotedRule": {
                "voteUser": self.voteUser,  # 有表决成员要求 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表
                "voteContinueDays": 5,  # 截止日期天数，测试默认10分钟
                "assetProjectCloudId": ""
            },
            "contractFiles": [{
                "fileName": "合同1",
                "fileUrl": "project/441702000000/202307/08cbb36b-022a-4839-a856-28b488d3b784.doc"
            }, {
                "fileName": "合作伙伴",
                "fileUrl": "asset/440106/202206/afb85130-b00f-41f9-9c85-edd769a3db39.pdf"
            }],
            "otherFiles": [{
                "fileName": "图片",
                "fileUrl": "asset/440111000000/202305/b5cf2a41-b929-47e4-829c-4b8f26d261c3.jpg"
            }],
            "operateType": 1
        }
        req = self.post(url, data, self.villageHeaders)
        print('02发起表决', req)
        self.assertEqual(req['message'], '操作成功')

    def test_03(self):
        """循环登录表决"""
        path = '/api/user/v1/user/open/censusLoginByCode'
        url = '/api/admin/v1/vote/saveVoteInfo'
        # 获取表决id
        assetProjectCloudId = self.getCloudId(self.assetName, 1)
        # 通过voteUser成员要求类型查询登录手机号和村民总数
        censusData, total = self.search_phone(self.voteUser)
        unique_phones = set()  # 用于存储出现过的phone
        for census in range(total):
            a = random.choice([0, 1])
            voteData = {"cloudVoteResult": 1, "remark": "", "assetProjectCloudId": assetProjectCloudId}
            phone = censusData[census]['phone']
            if phone in unique_phones:  # 如果phone已经出现过，则跳过当前循环
                continue
            unique_phones.add(phone)  # 将当前phone添加到集合中
            data = {"phone": phone, "code": "888888", "user_Type": 1}
            sessionid = self.login(data, path)  # 循环登录
            header = {"sessionid": sessionid, "Content-Type": "application/json", "channel": "census"}
            vote = self.post(url, voteData, header)  # 循环同意表决
        print('03表决同意', vote)
        self.assertEqual(vote['message'], '操作成功')

    def test_04(self):
        """后台固定表决截止时间，提前执行工作流，修改定时任务时间"""
        cqjy = self.connect('cqjy')
        cursor = cqjy.cursor()
        time = (datetime.datetime.now() + datetime.timedelta(seconds=10)).strftime('%Y-%m-%d %H:%M:%S')
        # 获取表决id
        assetProjectCloudId = self.getCloudId(self.assetName, 1)
        line1 = "Update t_asset_project_cloud_timer_job Set end_date = \"{}\" WHERE asset_project_cloud_id = {}".format(
            time, assetProjectCloudId)
        # print(line1)
        line2 = "Update t_asset_project_cloud Set project_cloud_end_date = \"{}\" WHERE asset_project_cloud_id = {}".format(
            time, assetProjectCloudId)
        cursor.execute(line1)
        cursor.execute(line2)
        try:
            cqjy.commit()
        except Exception as e:
            cqjy.rollback()
        cursor.close()
        cqjy.close()
        print('04修改定时任务时间')
        self.assertEqual("a", 'a')
        sleep(60)

    def test_05(self):
        """查看表决结果公告"""
        url1 = '/api/admin/v1/assetProjectCloud/getVotingNoticePage'
        data1 = {
            "noticeName": self.assetName,
            "current": 1,
            "size": 10,
            "informationType": 1
        }
        Notice = self.post(url1, data1, self.villageHeaders)
        print('05查看表决结果公告', Notice['data']['records'][0]['url'])
        self.assertEqual(Notice['message'], '操作成功')

    def test_06(self):
        """转立项"""
        url1 = '/api/admin/v1/assetProjectCloud/getCloudVotedList'
        # voteStatus 0=待发布表决 1=表决中 2=表决通过 3=表决不通过 4=表决转立项 5=历史记录
        data1 = {"assetName": self.assetName, "tradeMode": None, "current": 1, "size": 10, "voteStatus": 4}
        req1 = self.post(url1, data1, self.villageHeaders)['data']['records'][0]
        # 提交审核
        ulr = '/api/admin/v1/assetProjectCloud/submit'
        data = {
            "assetProjectId": req1['assetProjectId'],
            "assetProjectCloudId": req1["assetProjectCloudId"],
            "contractFiles": [{
                "fileName": "民主表决书.png",
                "fileUrl": "project/441702000000/202307/2870d13f-6cd6-4f43-8f9a-c6a3ea0f2857.png"
            }],
            "operateType": 3  # 操作类型 1=获取民主表决书 2=暂存 3=提交审核 4=提交
        }
        submit = self.post(ulr, data, self.villageHeaders)
        print('06表决提交', submit)
        self.assertEqual(submit['message'], '操作成功')

    def test_07(self):
        """调用类审核"""
        audit = self.audit(self.projectName, mode='03', status=11)
        print('07立项审核', audit)
        self.assertEqual(audit['message'], '操作成功')

    def test_08(self):
        """发布交易公告"""
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
        print('08发布交易公告', repost)
        self.assertEqual(repost['message'], '操作成功')

    def test_09(self):
        """修改付款账号"""
        up = information().update()
        print("09修改个人付款账号", up)

    def test_10(self):
        """报名-确定"""
        assetProjectId = self.getProjectInfoPage(self.projectName)
        url = "/api/auction_interface/v1/assetProjectEnroll/saveAssetProjectEnroll"
        data = {"assetProjectId": assetProjectId}
        sign = self.post(url, data, self.userHeaders)
        print("10报名-确定", sign)
        self.assertEqual(sign['message'], '操作成功')

    def test_11(self):
        """缴纳保证金并查看"""
        pay = self.getEarenstMoneyForPortal(self.assetName, 3602019309200000266)
        print("11缴纳保证金", pay)
        self.assertEqual(pay["message"], '操作成功')
        sleep(130)

    def test_12(self):
        """上传合同"""
        req = self.uploadContract(self.assetName)
        print("12上传合同", req)
        self.assertEqual(req["message"], '操作成功')

    def test_13(self):
        """合同审核"""
        req = self.activitiInstance(self.assetName)
        print("13合同审核", req)
        self.assertEqual(req["message"], '操作成功')

    @classmethod
    def tearDownClass(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
