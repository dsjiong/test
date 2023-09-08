import unittest
from time import sleep

from Setting.Base import *


class Intention(unittest.TestCase, information):

    @classmethod
    def setUpClass(self):
        # 使用机构名称作为项目名称，拼接时间
        self.cunInfo = information().getorgInfo(self.villageHeaders)
        self.auditInfo = information().getorgInfo(self.auditHeaders)
        self.getSysUser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = self.cunInfo["organizationName"][0:5]
        self.assetName = self.projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '遴选表决测试'
        self.voteUser = '000'  # 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表

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
                # "images": asstInfo['mainPicture'],
                # "assetGroupCode": asstInfo["assetGroupCodeLevel5"],
                "assetProjectId": None,
                "tradeTypeName": "出租",
                "projectTypeName": asstInfo["assetGroupLevel5Name"],
                "voteType": "1",  # 云表决类型  0=立项表决 1=遴选表决 2=拟定意向人表决
                "tradeMode": "02",  # 项目模式 01=公开竞价 02=公开协商 03=小额简易交易 04=续约交易
                "tradeType": "01",  # 项目类别 01=出租 02=出让 99=其它
                "organizationId": self.cunInfo["sysOrganizationId"],
                "organizationName": self.cunInfo["organizationName"],
                "contact": self.getSysUser['fullName'],
                "phone": self.getSysUser['phone'],
                "projectName": self.projectName,
                "projectType": asstInfo["assetGroupCodeLevel5"],
                "projectStartDate": None,
                "projectEndDate": None,
                "projectTradeYear": None
            },
            "cloudDetailIntenderDemandVo": {  # 意向人资格要求
                "intenderDemand": 1,  # 是否需要资质证明材料 0=否 1=是
                "remarkCondition": "1、袁2、力3、思",  # 受让人或承租人条件
                "materials": [{  # 资质证明材料
                    "materialsName": "袁",
                    "remark": "1"
                }],
                "enrollType": 0,  # 允许报名的用户类型 0=全部 1=自然人 2=法人
                "blacklistEnter": 0  # 是否禁止警示名单报名 0=否 1=是
            },
            "cloudDetailOtherQueryVo": {  # 其他
                "remark": None,  # "备注/申请事项说明（仅内部审核用）",
                "remarkFireControl": "消防情况说明",
                "remarkIndustryRequire": "行业要求",
                "remarkOther": None,  # "其他重要情况说明",
                "remarkOtherClause": None,  # "合同其他条款",
                "remarkTaxation": None,  # "税费承担特别说明"
            },
            "cloudDetailSchemeQueryVo": {  # 拟定交易方案
                "tradeEarnestMoneyStr": "壹元整",  # 保证金大写
                "registrationDuration": None,
                "marginPaymentDate": None,
                # "maxBidRange": 100000,
                # "minBidRange": 10000,
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
                "floorPriceUnit": 4,  # 租金收取方式 0=月 1=季 2=半年 3=年 4=一次性，出让要置空
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
            # a = random.choice([0, 1])
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
        """修改定时任务时间，提前执行工作流"""
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
        sleep(65)

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
        """发起遴选公告"""
        assetProjectId = self.getProjectInfoPage(self.projectName)
        url = '/api/admin/v1/assetProject/submit'
        data = {
            "assetProjectId": assetProjectId,
            "organizationId": self.cunInfo["sysOrganizationId"],
            "projectStatus": 101,
            "taskId": None,
            "actType": "02"
        }
        submit = self.post(url, data, self.villageHeaders)
        print('07提交', submit)

    def test_08(self):
        """遴选公告审核"""
        req = self.audit(self.projectName, mode='02', status=101)
        print("08遴选审核", req)
        self.assertEqual(req["message"], '操作成功')

    def test_09(self):
        """意向人申请"""
        # 先将付款账号改成工行
        self.update()
        projectId = self.getProjectInfoPage(self.projectName)
        idUrl = "/api/auction_interface/v1/assetProjectAuditMaterials/getAssetProjectAuditMaterials"
        idData = {"assetProjectId": projectId}
        materialsId = self.post(idUrl, idData, self.userHeaders)['data'][0]['assetProjectAuditMaterialsId']
        url = '/api/auction_interface/v1/assetProjectEnroll/saveAssetProjectEnroll'
        data = {
            "assetProjectId": projectId,
            "files": [{
                "assetProjectAuditMaterialsId": materialsId,
                "fileUrl": "cqjy/000000/202309/eb8c960f-6669-4edc-b932-71ab6b6e740d.jpg"
            }, {
                "assetProjectAuditMaterialsId": materialsId,
                "fileUrl": "cqjy/000000/202309/eb8c960f-6669-4edc-b932-71ab6b6e740d.jpg"
            }, {
                "assetProjectAuditMaterialsId": materialsId,
                "fileUrl": "cqjy/000000/202309/eb8c960f-6669-4edc-b932-71ab6b6e740d.jpg"
            }, {
                "assetProjectAuditMaterialsId": materialsId,
                "fileUrl": "cqjy/000000/202309/eb8c960f-6669-4edc-b932-71ab6b6e740d.jpg"
            }, {
                "assetProjectAuditMaterialsId": materialsId,
                "fileUrl": "cqjy/000000/202309/eb8c960f-6669-4edc-b932-71ab6b6e740d.jpg"
            }]
        }
        req = self.post(url, data, self.userHeaders)
        print("09意向人申请", req)
        self.assertEqual(req["message"], '操作成功')
        sleep(5)

    def test_10(self):
        """发起拟定意向人表决"""
        detail0 = self.getIntentionInfo(self.projectName)
        # detail1 = self.getIntentionInfo(1)
        voteUrl = '/api/admin/v1/assetProjectCloud/cloudTS4Most'
        voteData = {
            "cloudVotedRule": {
                "voteUser": self.voteUser,
                "voteContinueDays": 5,
                "assetProjectCloudId": "",
                "voteJoinUser": None,  # 100=上一轮前3名，101=上一轮前2名
                "votePassRequire": "100",  # 100=同意人数不少于应参与人数的2/3时，101=云表决结果中，同意人数较多的意向人
                "voteRound": "1"  # 表决轮次
            },
            "cloudDetailBase4MostVo": {
                "assetProjectId": detail0['assetProjectId'],
                "voteType": "2"
            },
            "cloudEnrollSchemeList": [{
                "userId": detail0['bidUserId'],
                "bidTypeText": detail0["bidTypeText"],
                "bidName": detail0["bidName"],
                "contactPhone": detail0["contactPhone"],
                "email": detail0["email"],
                "idcardType": detail0['legalIdCardType'],
                "legalIdCardTypeText": detail0["legalIdCardTypeText"],
                "legalIdCard": detail0["legalIdCard"],
                "city": detail0["city"],
                "province": detail0["province"],
                "legalName": None,
                "legalRepresentCodeTypeText": "",
                "legalRepresentCode": None,
                "floorPriceUnit": detail0['floorPriceUnit'],
                "rentCollectMethod": None,  # 承租方式，出让要置空
                "tradeType": detail0["tradeType"],
                "projectStartDate": detail0["projectStartDate"],
                "projectEndDate": detail0["projectEndDate"],
                "projectTradeYear": detail0["projectTradeYear"],
                "rentFree": detail0["rentFree"],
                "rentFreePeriod": detail0["rentFreePeriod"],
                "progressiveIncreaseWay": detail0["progressiveIncreaseWay"],
                "progressiveIncreaseStartMonth": detail0["progressiveIncreaseStartMonth"],
                "progressiveIncreaseMonth": detail0["progressiveIncreaseMonth"],
                "progressiveIncreaseIncrease": detail0["progressiveIncreaseIncrease"],
                "progressiveIncreaseAmount": detail0["progressiveIncreaseAmount"],
                "payTradeEarnestMoney": 1,
                "tradeEarnestMoney": detail0["tradeEarnestMoney"],
                "floorPrice": detail0["floorPrice"],
                "assetDeliverDay": detail0["assetDeliverDay"],
                "assetProjectEnrollId": detail0["assetProjectEnrollId"]
            }],
            "operateType": 1
        }
        vote = self.post(voteUrl, voteData, self.villageHeaders)
        print("10发起拟定意向人表决", vote)
        self.assertEqual(vote['message'], "操作成功")

    # @unittest.skip("test for vote")
    def test_11(self):
        """循环登录表决单个意向人"""
        path = '/api/user/v1/user/open/censusLoginByCode'
        url = '/api/admin/v1/vote/saveVoteInfo'
        # 获取表决id
        assetProjectCloudId = self.getCloudId(self.assetName, 5)
        detailUrl = '/api/admin/v1/vote/getVoteDetail'
        detailData = {"assetProjectCloudId": assetProjectCloudId, "tradeMode": "02"}
        # 通过voteUser成员要求类型查询登录手机号和村民总数
        censusData, total = self.search_phone(self.voteUser)
        unique_phones = set()  # 用于存储出现过的phone
        for census in range(total):
            # a = random.choice([0, 1])
            phone = censusData[census]['phone']
            if phone in unique_phones:  # 如果phone已经出现过，则跳过当前循环
                continue
            unique_phones.add(phone)  # 将当前phone添加到集合中
            data = {"phone": phone, "code": "888888", "user_Type": 1}
            sessionId = self.login(data, path)  # 循环登录
            header = {"sessionid": sessionId, "Content-Type": "application/json", "channel": "census"}  # 组装header
            schemeId = self.post(detailUrl, detailData, header)['data']['intentionList'][0][
                'assetProjectCloudEnrollSchemeId']  # 查询个人报名schemeID
            voteData = {"assetProjectCloudEnrollSchemeId": schemeId, "cloudVoteResult": 1, "remark": "",
                        "assetProjectCloudId": assetProjectCloudId}
            vote = self.post(url, voteData, header)  # 循环同意表决
        print('11表决同意', vote)
        self.assertEqual(vote['message'], '操作成功')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
