from Setting.Base import *


# ----------------------村集体获取信息----------------------
def getVillageInfo():
    url = "/api/admin/v1/sysOrganization/getOrganizationRegion"
    data = {}
    respone = public().post(url, data, sessionid_v)
    # print(respone)
    return respone["data"]


# ----------------------获取用户信息----------------------
def getSysUser(phone):
    url = "/api/admin/v1/sysUser/getSysUser"
    data = {"current": "1", "size": "10", "phone": phone}
    respone = public().post(url, data, sessionid_v)
    # print(re)
    return (respone["data"]["records"][0])


# ------------------------------ 创建资产-----------------
def saveAssetResource():
    url = "/api/admin/v1/assetInfoResource/saveAssetResource"
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
        "landOccupation": "10",
        "landOccupationUnit": 0,
        "videoUrl": None,
        "videoThumbnailUrl": None,
        "images": [
            "default/440111000000/202303/fd80f417-2b74-4a4e-901c-a92df17f39c8.jpg"
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
    respone = public().post(url, data, sessionid_v)
    print("创建资产", respone)
    return respone["data"]


# ------------------查看资产列表-----------------------
def getChooseAssetList():
    url = "/api/admin/v1/asset/getChooseAssetList"
    data = {
        "sysOrganizationId": villageInfo["sysOrganizationId"],
        "current": 1,
        "size": 10,
        "type": 0
    }
    respone = public().post(url, data, sessionid_v)
    # print(respone)
    return (respone["data"]["records"][0])


# ----------------------新增历史合同----------------------
def addContractHi():
    url = "/api/admin/v1/assetProjectExternalContractHi/saveContractHi"
    data = {
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
        "contact": Sysuser["fullName"],
        "phone": Sysuser["phone"],
        "contractName": contractName,
        "contractNo": contractName,
        "contractStartDate": (datetime.datetime.today() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d'),
        "contractEndDate": contractEndTime,
        "userType": userType,
        "userName": userName,
        "userPhone": userPhone,
        "idCardType": idCardType,
        "idCardNo": idcardNO,
        "assetId": chooseAssetList["assetId"],
        "assetCode": chooseAssetList["assetCode"],
        "assetName": chooseAssetList["assetName"],
        "assetType": chooseAssetList["assetType"],
        "buildArea": chooseAssetList["buildArea"],
        "buildAreaUnit": chooseAssetList["buildAreaUnit"],
        "landOccupation": chooseAssetList["landOccupation"],
        "landOccupationUnit": chooseAssetList["landOccupationUnit"],
        "adress": chooseAssetList["assetAddress"],
        "assetImage": "default/440111000000/202303/fd80f417-2b74-4a4e-901c-a92df17f39c8.jpg",
        "files": [
            {
                "fileName": "abc",
                "fileUrl": "default/440111000000/202303/fd80f417-2b74-4a4e-901c-a92df17f39c8.jpg"
            }
        ]
    }
    respone = public().post(url, data, sessionid_v)
    print("新增历史合同", respone)
    return respone


# ------------------线下合同(列表)------------------
def getPeriodPageList():
    url = "/api/admin/v1/assetProjectExternalContractHi/getPeriodPageList"
    data = {"current": 1, "size": 10}
    respone = public().post(url, data, sessionid_v)
    return (respone["data"]["records"][0])


# ------------------续约申请------------------
def renewalApply():
    url = "/api/admin/v1/renewalTrade/renewalApply"
    data = {
        "tradeMode": "04",
        "tradeType": "01",
        "projectStartDate": projectStartDate,
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
        "contact": (Sysuser)["fullName"],
        "phone": (Sysuser)["phone"],
        "projectName": contractName,
        "projectType": "Z010100",
        "projectTypeName": "耕地",
        "remarkIndustryRequire": "无",
        "remarkCondition": companyName,
        "remarkFireControl": "无",
        "remarkOther": "",
        "remarkOtherClause": "",
        "remarkTaxation": "",
        "remark": "",
        "detailParamList": [{
            "assetId": chooseAssetList["assetId"],
            "sysOrganizationId": villageInfo["sysOrganizationId"],
            "sysOrganizationName": villageInfo["organizationName"],
            "assetName": assetName,
            "assetCode": chooseAssetList["assetCode"],
            "assetStatus": 0,
            "assetNature": "",
            "assetType": "01",
            "assetTypeName": "资源类",
            "assetCategory": "",
            "assetCategoryName": "",
            "disposalMethod": "",
            "acquiredDate": None,
            "purpose": "",
            "purposeExplain": chooseAssetList["assetGroupLevel3Name"],
            "provinceId": villageInfo["provinceId"],
            "province": villageInfo["province"],
            "cityId": villageInfo["cityId"],
            "city": villageInfo["city"],
            "areaId": villageInfo["areaId"],
            "area": villageInfo["area"],
            "streetId": villageInfo["streetId"],
            "street": villageInfo["street"],
            "assetAddress": villageInfo["address"],
            "originalValue": "",
            "buildArea": "",
            "buildAreaUnit": "",
            "landOccupation": "10",
            "landOccupationUnit": "0",
            "mainPicture": "default/440111000000/202303/fd80f417-2b74-4a4e-901c-a92df17f39c8.jpg",
            "temporaryAssets": "",
            "contractEndDate": contractEndTime,
            "assetGroupCodeLevel1": chooseAssetList["assetGroupCodeLevel1"],
            "assetGroupCodeLevel2": chooseAssetList["assetGroupCodeLevel2"],
            "assetGroupCodeLevel3": chooseAssetList["assetGroupCodeLevel3"],
            "assetGroupCodeLevel4": chooseAssetList["assetGroupCodeLevel4"],
            "assetGroupCodeLevel5": chooseAssetList["assetGroupCodeLevel5"],
            "assetGroupLevel1Name": chooseAssetList["assetGroupLevel1Name"],
            "assetGroupLevel2Name": chooseAssetList["assetGroupLevel2Name"],
            "assetGroupLevel3Name": chooseAssetList["assetGroupLevel3Name"],
            "assetGroupLevel4Name": chooseAssetList["assetGroupLevel4Name"],
            "assetGroupLevel5Name": chooseAssetList["assetGroupLevel5Name"],
            "oriUserName": userName,
            "userPhone": userPhone,
            "oriUserType": userType,
            "oriIdCardType": idCardType,
            "oriIdCardNo": idcardNO,
            "assetGroupCode": chooseAssetList["assetGroupCodeLevel3"]
        }],
        "floorPrice": 6666,
        "assetDeliverDay": "",
        "progressiveIncrease": "",
        "progressiveIncreaseWay": "",
        "progressiveIncreaseAmount": "",
        "progressiveIncreaseStartMonth": "",
        "progressiveIncreaseMonth": "",
        "progressiveIncreaseIncrease": "",
        "rentFree": "false",
        "rentFreePeriod": "",
        "rentCollectMethod": 4,
        "projectEndDate": (datetime.datetime.now() + datetime.timedelta(days=56)).strftime('%Y-%m-%d'),
        "projectTradeYear": "1个月24天",
        "fileSaveParams": [
            {
                "fileType": 1,
                "fileUrl": imageKey
            },
            {
                "fileType": 2,
                "fileUrl": docKey
            }],
        "isSubmit": 1,
        "taskId": "",
        "perpetualAssignment": "false",
        "assetProjectId": "",
        "assetProjectOtherId": "",
        "assetProjectSchemeId": "",
        "businessKey": "",
        "tradeNo": "",
        "originalProjectNo": contractName,
        "projectNo": "",
        "assetId": chooseAssetList["assetId"]
    }

    respone = public().post(url, data, sessionid_v)
    print("续约申请", respone)
    return respone["data"]


# ------------------立项审核(列表)------------------
def getActivitiPage():
    url = "/api/admin/v1/activiti/getActivitiPage"
    data = {"current": 1, "size": 10, "projectStatusList": [11], "projectName": contractName, "sortField": 1}
    respone = public().post(url, data, sessionid_c)
    return (respone["data"]["records"][0])


# ------------------续约审核通过------------------
def activitiInstance():
    url = "/api/admin/v1/activiti/activitiInstance"
    data = {"assetProjectId": ActivitiPage["assetProjectId"], "taskId": ActivitiPage["taskId"],
            "businessKey": ActivitiPage["businessKey"], "status": 1, "annotation": "通过"}
    respone = public().post(url, data, sessionid_c)
    print("审核通过", respone)
    return respone


# ---------------------前台续约详情-----------------------------
def getRenewalTradeDetail():
    url = '/api/auction/v1/renewalTrade/open/getRenewalTradeDetail'
    data = {"assetProjectId": ActivitiPage["assetProjectId"]}
    respone = public().post(url, data, sessionid_user)
    return respone["data"]["businessKey"]


# ---------------------报名-确定-----------------------------
def saveAssetProjectEnroll():
    url = '/api/auction/v1/assetProjectEnroll/saveAssetProjectEnroll'
    data = {
        "assetProjectId": ActivitiPage["assetProjectId"],
        "businessKey": getRenewalTradeDetail(),
        "auctionPrice": "6666.00",
        "status": 1
    }
    respone = public().post(url, data, sessionid_user)
    print('报名', respone)


# ------------------项目详情------------------
def getProjectDetail():
    url = '/api/admin/v1/assetProject/getProjectDetail'
    header = {"Content-Type": "application/json", "channel": "admin", "sessionid": sessionid_v}
    data = {"assetProjectId": ActivitiPage["assetProjectId"], "type": ""}
    respone = public().post(url, data, sessionid_v)
    return respone["data"]["assetProject"]["tradeNo"]


# ------------------上传合同------------------
def saveProjectContract():
    url = '/api/admin/v1/assetProjectContract/saveAssetProjectContract'
    data = {
        "type": 1,
        "assetProjectId": ActivitiPage["assetProjectId"],
        "tradeNo": getProjectDetail(),
        "contractStartDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
        "contractYear": 0,
        "contractMonth": 0,
        "contractDay": 30,
        "contractEndDate": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d'),
        "payDateUnit": 0,
        "firstPayDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
        "payDays": 1,
        "paymentDays": 0,
        "idCardBackFile": "ZW5jcnlwdC9jb250cmFjdC80NDAxMTEwMDAwMDAvMjAyMzA0L2UxNzc5NWE2LTI4ZWQtNDc3MS04NWI2LTExZTJkMDAxMDYwNi5wbmc=",
        "idCardFrontFile": "ZW5jcnlwdC9jb250cmFjdC80NDAxMTEwMDAwMDAvMjAyMzA0LzI5Y2EyZjllLWY5ZGMtNGZlNC04Y2YyLTlkNDgwNjA3ZmY3ZC5wbmc=",
        "files": [
            {
                "fileName": "bf8590f3-e21e-46d0-98c2-44928b2df0b6.png",
                "fileUrl": "contract/440111000000/202304/e3997b05-8761-4458-9771-681fc0859e20.png"
            }
        ]
    }
    respone = public().post(url, data, sessionid_v)
    print("上传合同", respone)


# ---------查询项目流程信息-------------
def getMyTaskPage():
    url = "/api/admin/v1/activiti/getMyTaskPage"
    data = {"current": 1, "size": 10, "type": 1, "sortField": 8}
    respone = public().post(url, data, sessionid_c)
    return respone["data"]["records"][0]


# ------------------合同审核-----------------
def activitiInstanceht():
    url = "/api/admin/v1/activiti/activitiInstance"
    data = {"actNode": "contractFirstInstance", "assetProjectId": ActivitiPage["assetProjectId"],
            "businessKey": myTaskPage["businessKey"],
            "status": 1, "annotation": "通过"}
    respone = public().post(url, data, sessionid_c)
    print("合同审核", respone)


if __name__ == '__main__':
    headers = public().getSessionId()
    sessionid_v = headers[0]  # 村集体账号13210000012(工商)
    userName = "测试邓"   # 袁力思
    userPhone = 13751964417  # 13535550504
    idcardNO = 441422199303144030   # 440224199805052858
    userType = 1
    idCardType = 10
    companyName = "广州信巴迪信息科技有限公司"
    companyNo = '91440101331331509F'
    companyType = 2
    companyCardType = 49
    Sysuser = getSysUser("13751964424")  # 村集体信息13210000012(工商)
    villageInfo = getVillageInfo()
    imageKey = "contract/440111000000/202303/ea364b65-c361-48f5-88b3-02ad28633dd1.png"
    docKey = "project/440111000000/202303/db04edbd-482d-46ab-9151-446ce04e33b7.doc"
    time_mdhms = datetime.datetime.now().strftime('%m{}%d{}%H%M%S').format("月", "日")
    # contractName = assetName = villageInfo["organizationName"] + time_mdhms + '测试'
    contractName = assetName = time_mdhms + '续约测试'
    contractEndTime = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    saveAssetResource()  # 创建资产
    print(contractName)
    chooseAssetList = getChooseAssetList()
    addContractHi()  # 新建历史合同
    time_SSS = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] + 'Z'
    periodPageList = getPeriodPageList()
    projectStartDate = str((periodPageList["contractEndDate"]) + ' ' + time_SSS)
    renewalApply()  # 续约申请
    sessionid_c = headers[1]  # 审批账号13210000011
    ActivitiPage = getActivitiPage()
    print("assetProjectId:", ActivitiPage["assetProjectId"])
    activitiInstance()  # 审核通过
    sessionid_user = headers[2]  # userAccount
    saveAssetProjectEnroll()  # 意向人同意
    saveProjectContract()  # 上传合同
    myTaskPage = getMyTaskPage()
    activitiInstanceht()  #  合同审核