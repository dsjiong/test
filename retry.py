from time import sleep

from Setting.Retry import *
from Setting.Base import *
import unittest


@Retry(max_n=20)
class cf(unittest.TestCase, information):

    @unittest.skip("for subAccount")
    def test_vote(self):
        """表决"""
        cunInfo = information().getorgInfo(self.villageHeaders)
        assetName = cunInfo['organizationName'] + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '表决测试'
        resource = self.saveAssetResource(assetName)
        voteUser = 110
        print("01资产登记")

        # 表决出让
        getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = '/api/admin/v1/assetProjectCloud/cloudTS4Most'
        data = {
            "cloudDetailBase4MostVo": {
                "assetId": asstInfo['assetId'],
                "sysOrganizationId": cunInfo["sysOrganizationId"],
                "sysOrganizationName": cunInfo["organizationName"],
                "assetName": assetName,
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
                "province": cunInfo["province"],
                "provinceId": cunInfo["provinceId"],
                "city": cunInfo["city"],
                "cityId": cunInfo["cityId"],
                "area": cunInfo["area"],
                "areaId": cunInfo["areaId"],
                "street": cunInfo["street"],
                "streetId": cunInfo["streetId"],
                "assetAddress": cunInfo["address"],
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
                "assetGroupCode": asstInfo["assetGroupCodeLevel3"],
                "assetProjectId": None,
                "tradeTypeName": "出售",
                "projectTypeName": asstInfo["assetGroupLevel3Name"],
                "voteType": "0",  # 云表决类型  0=立项表决 1=遴选表决 2=拟定意向人表决
                "tradeMode": "01",  # 项目模式
                "tradeType": "03",  # 项目类别
                "organizationId": cunInfo["sysOrganizationId"],
                "organizationName": cunInfo["organizationName"],
                "contact": getsysuser['fullName'],
                "phone": getsysuser['phone'],
                "projectName": assetName,
                "projectType": asstInfo["assetGroupCodeLevel3"],
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
                "payTradeEarnestMoney": 1,
                "tradeEarnestMoney": 1,
                "floorPrice": 16888,
                "assetDeliverDay": 5,
                "progressiveIncrease": 0,  # 是否递增付款金额 0=否 1=是
                "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
                "progressiveIncreaseAmount": None,  # 每次递增固定金额
                "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
                "progressiveIncreaseMonth": None,  # 每n个月递增一次
                "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
                "rentFree": None,  # 是否免租期
                "rentFreePeriod": None,
                "floorPriceUnit": None,  # 租金收取方式 0=月 1=季 2=半年 3=年 4=一次性
                "projectStartDate": (datetime.date.today()).strftime('%Y-%m-%d'),
                "projectEndDate": (datetime.date.today() + datetime.timedelta(days=365)).strftime('%Y-%m-%d'),
                "projectTradeYear": "1年",
                "perpetualAssignment": "false"  # 是否永久转让
            },
            "cloudVotedRule": {
                "voteUser": voteUser,  # 有表决成员要求 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表
                "voteContinueDays": 5,  # 截止日期天数，测试可调整
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
        print('02发起表决')
        self.assertEqual(req["message"], '操作成功1')

    # @unittest.skip("for subAccount")
    def test_auction(self):
        """公开竞价"""
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"][0:3]
        assetName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '竞价测试'

        """资产登记"""
        print(assetName)
        resource = self.saveAssetResource(assetName)
        print("*" * 10, resource, "*" * 10)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

        # 立项申请-出租
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/assetProject/saveProjectApply"
        data = {
            "tradeMode": "01",
            "tradeType": "01",
            "organizationId": cunInfo["sysOrganizationId"],
            "organizationName": cunInfo["organizationName"],
            "provinceId": cunInfo["provinceId"],
            "province": cunInfo["province"],
            "cityId": cunInfo["cityId"],
            "city": cunInfo["city"],
            "areaId": cunInfo["areaId"],
            "area": cunInfo["area"],
            "streetId": cunInfo["streetId"],
            "street": cunInfo["street"],
            "address": cunInfo["address"],
            "contact": getsysuser['fullName'],
            "phone": getsysuser['phone'],
            "projectName": assetName,
            "projectType": asstInfo['assetGroupCodeLevel3'],
            "projectTypeName": asstInfo['assetGroupLevel3Name'],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防情况说明",
            "remarkOther": "其他重要情况说明",
            "remarkOtherClause": "合同其他条款",
            "remarkTaxation": "税费承担说明",
            "remark": "备注",
            "detailParamList": [{
                "assetId": asstInfo['assetId'],
                "sysOrganizationId": cunInfo["sysOrganizationId"],
                "sysOrganizationName": cunInfo["organizationName"],
                "assetName": assetName,
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
                "province": cunInfo["province"],
                "provinceId": cunInfo["provinceId"],
                "city": cunInfo["city"],
                "cityId": cunInfo["cityId"],
                "area": cunInfo["area"],
                "areaId": cunInfo["areaId"],
                "street": cunInfo["street"],
                "streetId": cunInfo["streetId"],
                "assetAddress": cunInfo["address"],
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
                "assetGroupCode": asstInfo['assetGroupCodeLevel3'],
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
            "auditMaterialsSaveParams": [],
            "enrollType": 0,
            "blacklistEnter": "false",
            "priorityOriginalLessee": "false",
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 9168,
            "minBidRange": 10000,
            "maxBidRange": 100000,
            "assetDeliverDay": 5,
            "progressiveIncrease": "false",  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": "",  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": '',  # 每次递增固定金额
            "progressiveIncreaseStartMonth": '',  # 从第n个月开始递增
            "progressiveIncreaseMonth": '',  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",  # 是否有免租期
            "rentFreePeriod": None,  # 免租天数
            "rentCollectMethod": '3',  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],  # 租赁开始时间
            "projectEndDate": str(datetime.datetime.now() + datetime.timedelta(days=520))[0:19],  # 租赁开始时间
            "projectTradeYear": "1年5个月5天",
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
        req = self.audit(assetName,status=11)
        print("03立项审核", req)
        self.assertEqual(req["message"], '操作成功1')

    # @unittest.skip("for subAccount")
    def test_small(self):
        """小额交易"""
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getSysUser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"][0:3]
        assetName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '小额测试'

        """资产登记"""
        print(assetName)
        resource = self.saveAssetResource(assetName)
        print("*" * 10, resource, "*" * 10)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

        """小额申请"""
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/smallTrade/smallApply"
        data = {
            "tradeMode": "03",
            "tradeType": "03",
            "organizationId": cunInfo["sysOrganizationId"],
            "organizationName": cunInfo["organizationName"],
            "provinceId": cunInfo["provinceId"],
            "province": cunInfo["province"],
            "cityId": cunInfo["cityId"],
            "city": cunInfo["city"],
            "areaId": cunInfo["areaId"],
            "area": cunInfo["area"],
            "streetId": cunInfo["streetId"],
            "street": cunInfo["street"],
            "address": cunInfo["address"],
            "contact": getSysUser['fullName'],
            "phone": getSysUser['phone'],
            "projectName": assetName,
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
                    "sysOrganizationId": cunInfo["sysOrganizationId"],
                    "sysOrganizationName": cunInfo["organizationName"],
                    "assetName": assetName,
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
                    "purposeExplain": asstInfo["assetGroupLevel3Name"],
                    "province": cunInfo["province"],
                    "provinceId": cunInfo["provinceId"],
                    "city": cunInfo["city"],
                    "cityId": cunInfo["cityId"],
                    "area": cunInfo["area"],
                    "areaId": cunInfo["areaId"],
                    "street": cunInfo["street"],
                    "streetId": cunInfo["streetId"],
                    "assetAddress": cunInfo["address"],
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
                    "assetGroupCode": asstInfo["assetGroupCodeLevel3"],
                    "assetProjectId": None,
                }
            ],
            "priorityOriginalLessee": "false",
            "payTradeEarnestMoney": 'true',
            "tradeEarnestMoney": 1,
            "floorPrice": 30000,
            "assetDeliverDay": 5,
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
        audit = self.audit(assetName, mode='03', status=11)
        print("03立项审核", audit)
        self.assertEqual(audit["message"], '操作成功1')

    # @unittest.skip("for subAccount")
    def test_consult(self):
        """公开协商"""
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getSysUser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"][0:3]
        assetName = projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '遴选测试'

        """资产登记"""
        print(assetName)
        resource = self.saveAssetResource(assetName)
        print("*" * 10, resource, "*" * 10)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

        """发布遴选公告"""
        # 利用资产名称查询资产信息
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/openConsult/selectApply"
        data = {
            "tradeMode": "02",
            "tradeType": "03",
            "organizationId": cunInfo["sysOrganizationId"],
            "organizationName": cunInfo["organizationName"],
            "provinceId": cunInfo["provinceId"],
            "province": cunInfo["province"],
            "cityId": cunInfo["cityId"],
            "city": cunInfo["city"],
            "areaId": cunInfo["areaId"],
            "area": cunInfo["area"],
            "streetId": cunInfo["streetId"],
            "street": cunInfo["street"],
            "address": cunInfo["address"],
            "contact": getSysUser['fullName'],
            "phone": getSysUser['phone'],
            "projectName": projectName,
            "projectType": asstInfo["assetGroupCodeLevel3"],
            "projectTypeName": asstInfo["assetGroupLevel3Name"],
            "remarkIndustryRequire": "行业要求",
            "remarkFireControl": "消防要求",
            "remarkOther": None,
            "remarkOtherClause": None,
            "remarkTaxation": None,
            "remark": None,
            "detailParamList": [
                {
                    "assetId": asstInfo['assetId'],
                    "sysOrganizationId": cunInfo["sysOrganizationId"],
                    "sysOrganizationName": cunInfo["organizationName"],
                    "assetName": assetName,
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
                    "purposeExplain": asstInfo["assetGroupLevel3Name"],
                    "province": cunInfo["province"],
                    "provinceId": cunInfo["provinceId"],
                    "city": cunInfo["city"],
                    "cityId": cunInfo["cityId"],
                    "area": cunInfo["area"],
                    "areaId": cunInfo["areaId"],
                    "street": cunInfo["street"],
                    "streetId": cunInfo["streetId"],
                    "assetAddress": cunInfo["address"],
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
                    "assetGroupCode": asstInfo["assetGroupCodeLevel3"],
                    "assetProjectId": None
                }
            ],
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 10000,
            "assetDeliverDay": 5,  # 合同签订X日之后交付资产
            "progressiveIncrease": 0,  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": None,  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": None,  # 每次递增固定金额
            "progressiveIncreaseStartMonth": None,  # 从第n个月开始递增
            "progressiveIncreaseMonth": None,  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",  # 是否有免租期
            "rentFreePeriod": None,  # 免租天数
            "rentCollectMethod": 0,  # 租金收取方式 0=按月 1=按季 2=按半年 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],
            "projectEndDate": str(datetime.datetime.now() + datetime.timedelta(days=20))[0:19],
            "projectTradeYear": "20天",
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
            "applyType": 1
        }
        req = self.post(url, data, self.villageHeaders)
        print("02发布遴选公告", req)
        self.assertEqual(req["message"], '操作成功')

        # 调用审核
        req = self.audit(projectName, mode='02', status=101)
        print("03遴选审核", req)
        self.assertEqual(req["message"], '操作成功1')

    @unittest.skip("for subAccount")
    def test_proposedVote(self):
        """拟定表决"""
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getUser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"][0:5]
        assetName = projectName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '遴选表决测试'
        voteUser = '000'  # 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表

        """创建资产"""
        print(assetName)
        resource = self.saveAssetResource(assetName)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

        """发起表决"""
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = '/api/admin/v1/assetProjectCloud/cloudTS4Most'
        data = {
            "cloudDetailBase4MostVo": {
                "assetId": asstInfo['assetId'],
                "sysOrganizationId": cunInfo["sysOrganizationId"],
                "sysOrganizationName": cunInfo["organizationName"],
                "assetName": assetName,
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
                "province": cunInfo["province"],
                "provinceId": cunInfo["provinceId"],
                "city": cunInfo["city"],
                "cityId": cunInfo["cityId"],
                "area": cunInfo["area"],
                "areaId": cunInfo["areaId"],
                "street": cunInfo["street"],
                "streetId": cunInfo["streetId"],
                "assetAddress": cunInfo["address"],
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
                "tradeTypeName": "出售",
                "projectTypeName": asstInfo["assetGroupLevel3Name"],
                "voteType": "1",  # 云表决类型  0=立项表决 1=遴选表决 2=拟定意向人表决
                "tradeMode": "02",  # 项目模式 01=公开竞价 02=公开协商 03=小额简易交易 04=续约交易
                "tradeType": "03",  # 项目类别 01=出租 02=出让 99=其它
                "organizationId": cunInfo["sysOrganizationId"],
                "organizationName": cunInfo["organizationName"],
                "contact": getUser['fullName'],
                "phone": getUser['phone'],
                "projectName": projectName,
                "projectType": asstInfo["assetGroupCodeLevel3"],
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
                "assetDeliverDay": 5,
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
                "voteUser": voteUser,  # 有表决成员要求 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表
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

        """循环登录表决"""
        path = '/api/user/v1/user/open/censusLoginByCode'
        url = '/api/admin/v1/vote/saveVoteInfo'
        # 获取表决id
        assetProjectCloudId = self.getCloudId(assetName, 1)
        # 通过voteUser成员要求类型查询登录手机号和村民总数
        censusData, total = self.search_phone(voteUser)
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

        """修改定时任务时间，提前执行工作流"""
        cqjy = self.connect('cqjy')
        cursor = cqjy.cursor()
        time = (datetime.datetime.now() + datetime.timedelta(seconds=10)).strftime('%Y-%m-%d %H:%M:%S')
        # 获取表决id
        assetProjectCloudId = self.getCloudId(assetName, 1)
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

        """查看表决结果公告"""
        noticeUrl = '/api/admin/v1/assetProjectCloud/getVotingNoticePage'
        noticeData = {
            "noticeName": assetName,
            "current": 1,
            "size": 10,
            "informationType": 1
        }
        Notice = self.post(noticeUrl, noticeData, self.villageHeaders)
        print('05查看表决结果公告', Notice['data']['records'][0]['url'])
        self.assertEqual(Notice['message'], '操作成功')

        """转立项"""
        voteListUrl = '/api/admin/v1/assetProjectCloud/getCloudVotedList'
        # voteStatus 0=待发布表决 1=表决中 2=表决通过 3=表决不通过 4=表决转立项 5=历史记录
        voteListData = {"assetName": assetName, "tradeMode": None, "current": 1, "size": 10, "voteStatus": 4}
        voteList = self.post(voteListUrl, voteListData, self.villageHeaders)['data']['records'][0]
        # 提交审核
        ulr = '/api/admin/v1/assetProjectCloud/submit'
        data = {
            "assetProjectId": voteList['assetProjectId'],
            "assetProjectCloudId": voteList["assetProjectCloudId"],
            "contractFiles": [{
                "fileName": "民主表决书.png",
                "fileUrl": "project/441702000000/202307/2870d13f-6cd6-4f43-8f9a-c6a3ea0f2857.png"
            }],
            "operateType": 3  # 操作类型 1=获取民主表决书 2=暂存 3=提交审核 4=提交
        }
        submit = self.post(ulr, data, self.villageHeaders)
        print('06表决提交', submit)
        self.assertEqual(submit['message'], '操作成功')

        """发起遴选公告"""
        assetProjectId = self.getProjectInfoPage(projectName)
        url = '/api/admin/v1/assetProject/submit'
        data = {
            "assetProjectId": assetProjectId,
            "organizationId": cunInfo["sysOrganizationId"],
            "projectStatus": 101,
            "taskId": None,
            "actType": "02"
        }
        submit = self.post(url, data, self.villageHeaders)
        print('07提交', submit)

        """遴选公告审核"""
        noticeAudit = self.audit(projectName, mode='02', status=101)
        print("08遴选审核", noticeAudit)
        self.assertEqual(noticeAudit["message"], '操作成功')

        """意向人申请"""
        # 先将付款账号改成工行
        projectId = self.getProjectInfoPage(projectName)
        idUrl = "/api/auction/v1/assetProjectAuditMaterials/getAssetProjectAuditMaterials"
        idData = {"assetProjectId": projectId}
        materialsId = self.post(idUrl, idData, self.userHeaders)['data'][0]['assetProjectAuditMaterialsId']
        url = '/api/auction/v1/assetProjectEnroll/saveAssetProjectEnroll'
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
        self.assertEqual(req["message"], '操作成功1')

    @unittest.skip("for test")
    def test_transactionVote(self):
        """事务表决"""
        cunInfo = information().getorgInfo(self.villageHeaders)
        getUser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"]
        transactionName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '就公共场地如何最大化使用事务表决测试'
        voteUser = '110'  # 000=所有成员 111=仅成员代表和户代表 110=仅成员代表 101=仅户代表
        print(transactionName)

        """发起事务表决"""
        address = cunInfo["province"] + cunInfo["city"] + cunInfo["area"] + cunInfo["address"]
        url = '/api/admin/v1/transactionVote/saveTransactionVote'
        data = {
            "voteUser": voteUser,
            "voteDay": 5,
            "transactionVoteProjectId": "",
            "voteType": 0,
            "organizationName": cunInfo["organizationName"],
            "organizationAddress": address,
            "contactUserName": getUser['fullName'],
            "contactPhone": getUser['phone'],
            "transactionName": transactionName,
            "htmlContent": "<p>中国人民大学公共管理学院党委书记孙柏瑛认为，《操作指引》的发布，对北京社区既有多层住宅加装电梯的条件与技术标准进行了明确规定，这将对北京加装电梯工作产生积极影响。《操作指引》一方面建立了加装电梯的规范流程和技术标准，指明了社区公共设施供给的安全要求；另一方面，电梯加装能够解决老年居民群体上下楼难题，提高老年人群体的社会福利与生活品质，有助于“老破小”社区基础设施的改善。</p>",
            "transactionVoteSelectionList": [{
                "remark": "当前表决需要在甲、乙、丙三人中选择一人，则新增3个选项，分别是甲、乙、丙当前表决需要在甲、乙、丙三人中选择一人",
                "selectionName": "甲"
            }, {
                "remark": "当前表决需要征求成员同意，则新增2个选项，分别是同意、拒绝",
                "selectionName": "乙"
            }, {
                "remark": "说明：",
                "selectionName": "丙"
            }],
            "operate": 1  # 0:临时保存，1：提交，2：重新发起
        }
        tVote = self.post(url, data, self.villageHeaders)
        print('01发起表决', tVote)
        self.assertEqual(tVote['message'], '操作成功')

        """获取表决详情进行表决
        pageUrl = '/api/admin/v1/transactionVote/getTransactionVotePage'
        pageData = {
            "current": 1,
            "size": 10,
            "queryType": 1,
            "transactionName": transactionName
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
            data = {"phone": phone, "code": "888888", "user_Type": 1}
            sessionid = self.login(data, path)  # 循环登录
            header = {"sessionid": sessionid, "Content-Type": "application/json", "channel": "census"}
            vote = self.post(voteUrl, voteData, header)  # 循环同意
        print('02表决同意', vote)
        self.assertEqual(vote['message'], '操作成功')"""


if __name__ == '__main__':
    unittest.main()
