import os
import urllib3
from time import sleep

import datetime
import json
import requests

from Setting import login_class

urllib3.disable_warnings()
os.environ["http_proxy"] = 'http://192.168.123.83:8888'
os.environ["https_proxy"] = 'http://192.168.123.83:8888'


# ---------------获取账号信息----------------
def getVillageInfo(sessionId):
    url = test_host + "/api/admin/v1/sysOrganization/getOrganizationRegion"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId}
    data = {}
    response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    # print(response)
    return response["data"]


# ------------------------------ 获取用户信息-----------------
def getSysUser(phone):
    url = test_host + "/api/admin/v1/sysUser/getSysUser"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {"phone": phone, "current": 1, "size": 10}
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    return re["data"]['records'][0]


# ------------------------------ 创建资产-----------------
def saveAssetResource():
    url = test_host + "/api/admin/v1/assetInfoResource/saveAssetResource"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {
        "assetCode": None,
        "sysOrganizationName": None,
        "assetName": assetName,
        "assetSelfCode": None,
        "remark": None,
        "threeCapitalsOwnershipNo": None,
        "provinceId": villageInfo["provinceId"],
        "province": villageInfo["province"],
        "cityId": villageInfo["cityId"],
        "city": villageInfo["city"],
        "areaId": villageInfo["areaId"],
        "area": villageInfo["area"],
        "streetId": villageInfo["streetId"],
        "street": villageInfo["street"],
        "address": villageInfo["address"],
        "purpose": None,
        "purposeExplain": "耕地",
        "landOccupation": "26",
        "landOccupationUnit": 0,
        "videoUrl": None,
        "videoThumbnailUrl": None,
        "images": [
            "default\/440111000000\/202303\/13eefde2-0728-4e62-8deb-3e3a6c897404.jpg"
        ],
        "developmentType": None,
        "developmentReason": None,
        "unitNo": None,
        "cadastreNo": None,
        "landNo": None,
        "adjunctiveResourceNo": None,
        "attribute": None,
        "landUsufructNo": None,
        "landUser": None,
        "landOwnershipNo": None,
        "landOwner": None,
        "startDate": None,
        "selfUse": None,
        "coordinate": None,
        "disposalMethod": None,
        "assetGroupCodeLevel1": "Z000000",
        "assetGroupLevel1Name": "资源性资产",
        "assetGroupCodeLevel2": "Z010000",
        "assetGroupLevel2Name": "农用地",
        "assetGroupCodeLevel3": "Z010100",
        "assetGroupLevel3Name": "耕地",
        "assetGroupCodeLevel4": "",
        "assetGroupLevel4Name": "",
        "assetGroupCodeLevel5": "",
        "assetGroupLevel5Name": "",
        "sysOrganizationId": villageInfo["sysOrganizationId"],
    }
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("创建资产", re)
    return re["data"]


# ---------------资产列表----------------
'''def getAssetPageList():
    url = test_host + "/api/admin/v1/asset/getAssetPageList"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {
        "assetName": assetName,
        "current": 1,
        "size": 10
    }
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("查看资产", re)
    return (re["data"]["records"][0]["assetId"])'''


# ------------------------------立项申请-出租---------------------------------------------------------------
def saveProjectApply(assetId):
    url = test_host + "/api/admin/v1/assetProject/saveProjectApply"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {
        "tradeMode": "01",
        "tradeType": "01",
        "organizationId": villageInfo["sysOrganizationId"],
        "organizationName": villageInfo["organizationName"],
        "provinceId": villageInfo["provinceId"],
        "province": villageInfo["province"],
        "cityId": villageInfo["cityId"],
        "city": villageInfo["city"],
        "areaId": villageInfo["areaId"],
        "area": villageInfo["area"],
        "streetId": villageInfo["streetId"],
        "street": villageInfo["street"],
        "address": villageInfo["address"],
        "contact": sysUser['fullName'],
        "phone": sysUser['phone'],
        "projectName": projectName,
        "projectType": "Z010100",
        "projectTypeName": "耕地",
        "remarkIndustryRequire": "接口测试",
        "remarkFireControl": "接口测试",
        "remarkOther": None,
        "remarkOtherClause": None,
        "remarkTaxation": None,
        "remark": None,
        "detailParamList": [
            {
                "assetId": assetId,
                "sysOrganizationId": villageInfo["sysOrganizationId"],
                "sysOrganizationName": villageInfo["organizationName"],
                "assetName": assetName,
                "assetCode": "1019362",
                "assetStatus": 0,
                "assetNature": None,
                "assetType": "",
                "assetTypeName": "",
                "assetCategory": None,
                "assetCategoryName": None,
                "disposalMethod": None,
                "acquiredDate": None,
                "purpose": None,
                "purposeExplain": "耕地",
                "province": villageInfo["province"],
                "provinceId": villageInfo["provinceId"],
                "city": villageInfo["city"],
                "cityId": villageInfo["cityId"],
                "area": villageInfo["area"],
                "areaId": villageInfo["areaId"],
                "street": villageInfo["street"],
                "streetId": villageInfo["streetId"],
                "assetAddress": villageInfo["address"],
                "originalValue": None,
                "buildArea": None,
                "buildAreaUnit": None,
                "landOccupation": "26",
                "landOccupationUnit": 0,
                "mainPicture": "default\/440111000000\/202303\/13eefde2-0728-4e62-8deb-3e3a6c897404.jpg",
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
                "assetGroupCode": "Z010100",
                "assetProjectId": None
            }
        ],
        "priorityOriginalLessee": "false",
        "payTradeEarnestMoney": 'true',
        "tradeEarnestMoney": 1,
        "floorPrice": 30000,
        "minBidRange": 100,
        "maxBidRange": 500,
        "assetDeliverDay": "15",
        "progressiveIncrease": "true",  # 是否递增付款金额 0=否 1=是
        "progressiveIncreaseWay": "2",  # 递增方式 1=按比例递增 2=按固定金额递增
        "progressiveIncreaseAmount": '100',  # 每次递增固定金额
        "progressiveIncreaseStartMonth": '13',  # 从第n个月开始递增
        "progressiveIncreaseMonth": 12,  # 每n个月递增一次
        "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
        "rentFree": "true",
        "rentFreePeriod": '15',
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
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("立项申请", re)


# ---------查询项目流程信息-------------
def getMyTaskPage():
    url = test_host + "/api/admin/v1/activiti/getMyTaskPage"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionid_sp}
    data = {"projectName": projectName, "current": 1, "size": 10, "type": 1, "sortField": 8}
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    return re["data"]["records"][0]


# ------------------立项审核------------------
def activitiInstance():
    url = test_host + "/api/admin/v1/activiti/activitiInstance"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionid_sp}
    data = {"assetProjectId": myTaskPage["assetProjectId"], "taskId": myTaskPage["taskId"],
            "businessKey": myTaskPage["businessKey"], "status": 1, "annotation": "通过"}
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("立项审核", re)


# ------------------个人信息------------------
def getPersonalMessage(sessionid_sp):
    url = test_host + "/api/admin/v1/sysUiaUser/getPersonalMessage"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionid_sp}
    data = {"assetProjectId": myTaskPage["assetProjectId"], "type": ""}
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    return (re["data"]["name"])


# ------------------发布交易公告------------------
def saveAssetInformation(earnestMoneyPayEndDate, auctionStartDate, auctionEndDate):
    url = test_host + "/api/admin/v1/assetInformation/saveAssetInformation"
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionid_sp}
    data = {
        "taskId": getMyTaskPage()["taskId"],
        "businessKey": getMyTaskPage()["businessKey"],
        "assetProjectId": myTaskPage["assetProjectId"],
        "auctionStartDate": str(datetime.datetime.now() + datetime.timedelta(minutes=auctionStartDate))[0:19],
        "auctionEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=auctionEndDate))[0:19],
        "contact": sysUser["fullName"],
        "phone": sysUser["phone"],
        "earnestMoneyPayEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=earnestMoneyPayEndDate))[
                                  0:19],
        "enrollEndDate": str(datetime.datetime.now() + datetime.timedelta(minutes=earnestMoneyPayEndDate))[0:19],
        "extendSecond": 180,
        "maxExtend": 999,
        "resultPostPeriod": 5,
        "contractDeadlinePeriod": 10,
        "releaseUser": getPersonalMessage(sessionid_sp),
        "sysOrganizationId": centerInfo["sysOrganizationId"],
        "releaseOrganizationName": centerInfo["organizationName"],
        "releaseDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:19],
        "publicStartDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "publicEndDate": (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"),
        "informationTitle": projectName + "交易公告",
        "projectName": projectName
    }
    re = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("发布交易公告", re)


# ------------------------重提检查------------------------
def checkProjectAsset():
    url = test_host + '/api/admin/v1/assetProject/checkProjectAsset'
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {"assetProjectId": myTaskPage["assetProjectId"]}
    response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("重提检查是否通过", response)


# --------------------------项目详情-------------------------
def getProjectApply():
    url = test_host + '/api/admin/v1/assetProject/getProjectApply'
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {"assetProjectId": myTaskPage["assetProjectId"], "type": 3, "newProjectType": "0"}
    response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    # print("项目申请详情", response["data"])
    return response["data"]


# ------------------ 重提申请 ------------------
def reSaveProjectApply():
    url = test_host + '/api/admin/v1/assetProject/saveProjectApply'
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionId_C}
    data = {
        "assetProjectOtherId": "null",
        "assetProjectId": "null",
        "remarkCondition": "无",
        "remarkIndustryRequire": "无",
        "remarkFireControl": "无",
        "remarkOther": "null",
        "remarkOtherClause": "null",
        "remarkTaxation": "null",
        "remark": "null",
        "gmtCreate": "null",
        "gmtModified": "null",
        "createUserId": "null",
        "modifiedUserId": "null",
        "organizationName": villageInfo["organizationName"],
        "organizationId": villageInfo["sysOrganizationId"],
        "projectName": contractName,
        "htmlContent": "null",
        "projectAmount": 30000,
        "projectAmountUnit": "元/月",
        "projectType": "Z010100",
        "projectNo": "null",
        "originalProjectNo": projectApply["project"]["projectNo"],
        "tradeNo": "null",
        "businessKey": "null",
        "tradeType": "01",
        "tradeMode": "01",
        "projectStatus": 3,
        "initiateDate": "null",
        "passDate": projectApply["project"]["passDate"],
        "auctionStartDate": "null",
        "auctionEndDate": "null",
        "publicStartDate": "null",
        "publicEndDate": "null",
        "enrollStartDate": "null",
        "enrollEndDate": "null",
        "contractUploadDate": "null",
        "contractDeadlineDate": "null",
        "examineDeadlineDate": "null",
        "province": villageInfo["province"],
        "provinceId": villageInfo["provinceId"],
        "city": villageInfo["city"],
        "cityId": villageInfo["cityId"],
        "area": villageInfo["area"],
        "areaId": villageInfo["areaId"],
        "street": villageInfo["street"],
        "streetId": villageInfo["streetId"],
        "address": villageInfo["address"],
        "contact": projectApply["project"]["contact"],
        "phone": projectApply["project"]["phone"],
        "auctionUserName": "null",
        "auctionUserId": "null",
        "contactPhone": "null",
        "auctionPrice": "null",
        "legalIdCard": "null",
        "auctionDate": "null",
        "rentCollectMethod": 0,
        # "${__timeShift(yyyy-MM-dd'T'hh:mm:ss.SSS'Z',,P1D,,)}"
        "projectStartDate": (datetime.date.today() + datetime.timedelta(days=1)).strftime(
            '%Y-%m-%d{}%H:%M:%S.%f').format('T')[:-3] + 'Z',
        # "${__timeShift(yyyy-MM-dd,,P20D,,)}"
        "projectEndDate": (datetime.date.today() + datetime.timedelta(days=29)).strftime('%Y-%m-%d'),
        "projectTradeYear": "29天",
        "createUserName": "6f4ede90f61acfd5809f11b16cee83a0",
        "requires": "false",
        "projectCloseType": "null",
        "initOrganizationId": "null",
        "initOrganizationName": "null",
        "initUserId": "null",
        "initUserName": "null",
        "complaintCall": "020-86546357",
        "complaintEmail": "",
        "mainPicture": "default/440111000000/202303/ed3aa6fd-d5c5-4ba1-90dc-5a9174e51009.jpg",
        "appKey": "null",
        "detailUrl": "null",
        "detailUrlType": "null",
        "assetType": "null",
        "assetTypeName": "null",
        "assetCategory": "null",
        "assetCategoryName": "null",
        "tradeReleaseDate": projectApply["project"]["tradeReleaseDate"],
        "checkCode": projectApply["project"]["checkCode"],
        "showTestData": 0,
        "contactIdx": projectApply["project"]["contactIdx"],
        "phoneIdx": projectApply["project"]["phoneIdx"],
        "contactPhoneIdx": "null",
        "legalIdCardIdx": "null",
        "tradeOrganizationId": "1625419005632319489",
        "tradeOrganizationName": "广州市白云区农业农村局",
        "tradeOrganizationAddress": "广东省广州市白云区江高镇江村古楼街27号",
        "tradeOrganizationUserName": "江鱼儿",
        "tradeOrganizationUserPhone": "13750000001",
        "tradeCode": projectApply["project"]["tradeCode"],
        "provinceCode": "440000000000",
        "cityCode": "440100000000",
        "areaCode": "440111000000",
        "streetCode": "440111113000",
        "assetProjectCloud": "false",
        "sevenDayStatus": 1,
        "isOrganizationActTimerConfig": "null",
        "assetInformationId": "null",
        "projectStatusText": "null",
        "applicantsCount": 0,
        "perpetualAssignment": "false",
        "projectTypeName": "耕地",
        "assetGroupCode": "Z010100",
        "assetGroupName": "耕地",
        "flowAssetProjectId": "null",
        "assetProjectSchemeId": "null",
        "priorityOriginalLessee": "false",
        "blacklistEnter": "false",
        "enrollType": 0,
        "payTradeEarnestMoney": "true",
        "tradeEarnestMoney": 1,
        "floorPrice": 30000,
        "confirmedPrice": "null",
        "floorPriceUnit": 0,
        "minBidRange": 100,
        "maxBidRange": 500,
        "assetDeliverDay": "null",
        "progressiveIncrease": "null",
        "progressiveIncreaseWay": "null",
        "progressiveIncreaseStartMonth": "null",
        "progressiveIncreaseMonth": "null",
        "progressiveIncreaseIncrease": "null",
        "progressiveIncreaseAmount": "null",
        "rentFree": "false",
        "rentFreePeriod": "null",
        "registrationDuration": "null",
        "bidEndDay": "null",
        "userName": "null",
        "userType": "null",
        "idCardType": "null",
        "idCardNo": "null",
        "idCardNoIdx": "null",
        "repostAssetProject": "false",
        "detailParamList": [{
            "assetId": projectApply["details"]["assetId"],
            "sysOrganizationId": villageInfo["sysOrganizationId"],
            "sysOrganizationName": villageInfo["organizationName"],
            "assetName": contractName,
            "assetCode": projectApply["details"]["assetCode"],
            "assetStatus": 0,
            "assetNature": "null",
            "assetType": projectApply["details"]["assetType"],
            "assetTypeName": projectApply["details"]["assetTypeName"],
            "assetCategory": "null",
            "assetCategoryName": "null",
            "disposalMethod": "null",
            "acquiredDate": projectApply["details"]["acquiredDate"],
            "purpose": "null",
            "purposeExplain": "耕地",
            "province": villageInfo["province"],
            "provinceId": villageInfo["provinceId"],
            "city": villageInfo["city"],
            "cityId": villageInfo["cityId"],
            "area": villageInfo["area"],
            "areaId": villageInfo["areaId"],
            "street": villageInfo["street"],
            "streetId": villageInfo["streetId"],
            "assetAddress": villageInfo["address"],
            "originalValue": "null",
            "buildArea": "null",
            "buildAreaUnit": "null",
            "landOccupation": "26",
            "landOccupationUnit": "0",
            "mainPicture": "default/440111000000/202303/ed3aa6fd-d5c5-4ba1-90dc-5a9174e51009.jpg",
            "temporaryAssets": "null",
            "contractEndDate": "null",
            "assetGroupCodeLevel1": "Z000000",
            "assetGroupCodeLevel2": "Z010000",
            "assetGroupCodeLevel3": "Z010100",
            "assetGroupCodeLevel4": "null",
            "assetGroupCodeLevel5": "null",
            "assetGroupLevel1Name": "资源性资产",
            "assetGroupLevel2Name": "农用地",
            "assetGroupLevel3Name": "耕地",
            "assetGroupLevel4Name": "null",
            "assetGroupLevel5Name": "null",
            "oriUserName": "null",
            "oriUserType": "null",
            "oriIdCardType": "null",
            "oriIdCardNo": "null",
            "assetProjectId": myTaskPage["assetProjectId"],
            "assetGroupCode": "Z010100"
        }],
        "fileSaveParams": [{
            "fileType": 1,
            "fileUrl": "project/440111000000/202303/4234d96b-762c-4dc8-b15d-44a71175163f.png"
        }, {
            "fileType": 2,
            "fileUrl": "project/440111000000/202303/fbc67d84-92f0-4fe0-95b0-4ed8a28e5796.doc"
        }],
        "auditMaterialsSaveParams": [],
        "isGreyed": "true",
        "isSubmit": 1,
        "taskId": "null"
    }
    response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
    print("重提立项", response)


if __name__ == '__main__':
    test_host = 'https://cqjy-test.b2bwings.com'
    # test_host = 'https://cqjy-uat.b2bwings.com'
    loginAdmin_api = '/api/admin/v1/sysUser/open/loginByCode'
    loginAdmin_url = test_host + loginAdmin_api
    loginUser_api = '/api/user/v1/user/open/loginByCode'
    req = login_class.loginHandler()
    login_data_c = req.data(phone='13750000007')  # 村集体账号
    login_data_sp = req.data(phone='13750000002')  # 审批账号
    sessionId_C = req.visit("post", url=loginAdmin_url, data=json.dumps(login_data_c))["data"][
        "sessionid"]  # 村集体登录
    # print(sessionId_C)
    villageInfo = getVillageInfo(sessionId_C)  # 村集体信息
    time_mdhms = datetime.datetime.now().strftime('%m{}%d{}%H{}%M{}%S{}').format("月", "日", "时", "分", "秒")
    projectName = contractName = assetName = villageInfo["organizationName"][:-4] + time_mdhms
    print(projectName)
    sysUser = getSysUser('13750000007')
    saveProjectApply(saveAssetResource())  # 立项申请-出租
    sessionid_sp = req.visit("post", url=test_host + loginAdmin_api, data=json.dumps(login_data_sp))["data"][
        "sessionid"]  # 交易中心登录
    centerInfo = getVillageInfo(sessionid_sp)  # 交易中心信息
    myTaskPage = getMyTaskPage()  # 工作流信息
    print("assetProjectId:", myTaskPage["assetProjectId"])
    activitiInstance()  # 立项审核
    saveAssetInformation(1, 10, 15)  # 发布交易公告
    sleep(65)
    projectApply = getProjectApply()
    reSaveProjectApply()  # 重提立项
