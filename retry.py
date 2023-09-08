from Setting.Retry import *
from Setting.Base import *
import unittest


@Retry(max_n=10, func_prefix='test_004')
class cf(unittest.TestCase, information):

    # 创建资产
    def test_001(self):
        cunInfo = information().getorgInfo(self.villageHeaders)
        assetName = cunInfo['organizationName'] + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '表决测试'
        resource = self.saveAssetResource(assetName)
        voteUser = 110
        print("01资产登记")

        # 表决出让
        getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        assetId = self.getAssetPageList(assetName)
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = '/api/admin/v1/assetProjectCloud/cloudTS4Most'
        data = {
            "cloudDetailBase4MostVo": {
                "assetId": assetId['assetId'],
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
                "tradeTypeName": "出租",
                "projectTypeName": asstInfo["assetGroupLevel3Name"],
                "voteType": "0",  # 云表决类型  0=立项表决 1=遴选表决 2=拟定意向人表决
                "tradeMode": "03",  # 项目模式
                "tradeType": "02",  # 项目类别
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
                "assetDeliverDay": "12",
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

    def test_002(self):
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
        assetId = self.getAssetPageList(assetName)
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
                "assetId": assetId['assetId'],
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
            "auditMaterialsSaveParams": [],
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
        req = self.audit(assetName)
        print("03立项审核", req)
        self.assertEqual(req["message"], '操作成功')

    def test_003(self):
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
        prefix = cunInfo["organizationName"][0:3]
        assetName = prefix + (datetime.datetime.now()).strftime('%m%d%H%M%S') + '小额测试'

        """资产登记"""
        print(assetName)
        resource = self.saveAssetResource(assetName)
        print("*" * 10, resource, "*" * 10)
        print("01资产登记")
        self.assertEqual(resource["message"], '操作成功')

        """小额申请"""
        assetId = self.getAssetPageList(assetName)
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
        url = "/api/admin/v1/smallTrade/smallApply"
        data = {
            "tradeMode": "03",
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
                    "acquiredDate": (
                        (datetime.date.today() + datetime.timedelta(days=-30)).strftime('%Y-%m-%d {}')).format(
                        '00:00:00'),
                    "purpose": asstInfo['purpose'],
                    "purposeExplain": asstInfo["assetGroupLevel5Name"],
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
        audit = self.audit(assetName, mode='03', status=11)
        print("03立项审核", audit)
        self.assertEqual(audit["message"], '操作成功1')

    def test_004(self):
        # 使用机构名称作为项目名称，拼接时间
        cunInfo = information().getorgInfo(self.villageHeaders)
        getsysuser = information().getSysUser(self.vPhone, self.villageHeaders)
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
        assetInfo = self.getAssetPageList(assetName)
        url = "/api/admin/v1/openConsult/selectApply"
        data = {
            "tradeMode": "02",
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
            "contact": "林縡",
            "phone": "13751964412",
            "projectName": projectName,
            "projectType": "Z010100",
            "projectTypeName": "耕地",
            "remarkIndustryRequire": "无",
            "remarkFireControl": "无",
            "remarkOther": None,
            "remarkOtherClause": None,
            "remarkTaxation": None,
            "remark": None,
            "detailParamList": [
                {
                    "assetId": assetInfo['assetId'],
                    "sysOrganizationId": cunInfo["sysOrganizationId"],
                    "sysOrganizationName": cunInfo["organizationName"],
                    "assetName": assetName,
                    "assetCode": "1Z0000002656",
                    "assetStatus": 0,
                    "assetNature": None,
                    "assetType": None,
                    "assetTypeName": None,
                    "assetCategory": None,
                    "assetCategoryName": None,
                    "disposalMethod": None,
                    "acquiredDate": (datetime.datetime.today() + datetime.timedelta(days=-100)).strftime('%y-%m-%d'),
                    "purpose": None,
                    "purposeExplain": "无",
                    "provinceId": cunInfo["provinceId"],
                    "province": cunInfo["province"],
                    "cityId": cunInfo["cityId"],
                    "city": cunInfo["city"],
                    "areaId": cunInfo["areaId"],
                    "area": cunInfo["area"],
                    "streetId": cunInfo["streetId"],
                    "street": cunInfo["street"],
                    "assetAddress": cunInfo["address"],
                    "originalValue": None,
                    "buildArea": None,
                    "buildAreaUnit": None,
                    "landOccupation": 6.66,
                    "landOccupationUnit": 0,
                    "mainPicture": "default/440111000000/202302/6852cd89-4ff1-45a3-beaf-0530efa03471.jpg",
                    "temporaryAssets": 0,
                    "contractEndDate": None,
                    "assetGroupCodeLevel1": "Z000000",
                    "assetGroupCodeLevel2": "Z010000",
                    "assetGroupCodeLevel3": "Z010100",
                    "assetGroupCodeLevel4": "",
                    "assetGroupCodeLevel5": "",
                    "assetGroupLevel1Name": "资源性资产",
                    "assetGroupLevel2Name": "农用地",
                    "assetGroupLevel3Name": "耕地",
                    "assetGroupLevel4Name": "",
                    "assetGroupLevel5Name": "",
                    "oriUserName": None,
                    "oriUserType": None,
                    "oriIdCardType": None,
                    "oriIdCardNo": None,
                    "assetGroupCode": "Z010100",
                    "assetProjectId": None
                }
            ],
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 10000,
            "assetDeliverDay": "",  # 合同签订X日之后交付资产
            "progressiveIncrease": 1,  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": 2,  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": 5000,  # 每次递增固定金额
            "progressiveIncreaseStartMonth": 3,  # 从第n个月开始递增
            "progressiveIncreaseMonth": 1,  # 每n个月递增一次
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


if __name__ == '__main__':
    unittest.main()
