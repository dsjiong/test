import pymysql
import datetime
from Setting.Publics import *

urllib3.disable_warnings()


class information(public):
    header = public().getSessionId()
    villageHeaders = header[0]
    auditHeaders = header[1]
    userHeaders = header[2]
    userPhone = public().uPhone
    name = ''
    if userPhone == 13751964417:
        name = '邓声炯'
    elif userPhone == 13535550504:
        name = '袁力思'
    else:
        name = '信巴迪'

    # 数据库
    def connect(self, database):
        mysql = pymysql.connect(host='39.108.128.154',
                                port=3307,
                                user='b2bwings',
                                password='b2bwings666!',
                                database=database)
        print('连接成功', mysql)
        return mysql

    # 更改工行付款帐号
    def update(self):
        mysql = self.connect('cqjy-user')
        cur = mysql.cursor()
        print('name=' + self.name)
        sql1 = "SELECT phone FROM t_user_info WHERE earnest_money_pay_account_name = " \
               "'42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002'"
        cur.execute(sql1)
        rest = cur.fetchone()[0]
        account = datetime.datetime.now().strftime('%y%m%d%H%M%S')
        sql2 = "UPDATE t_user_info SET earnest_money_pay_account_name = " + account + " WHERE earnest_money_pay_account_name = " \
               "'42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002'"
        # print(sql2)
        sql3 = "UPDATE t_user_info SET earnest_money_pay_account_name = " \
               "'42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002' WHERE phone = \"" + self.name + "\""
        # print(sql3)
        if rest == self.name:
            print(self.name + "的当前付款帐号为工行")
        elif rest is None:
            cur.execute(sql2)
            cur.execute(sql3)
            print(self.name + "的付款帐号已设为工行")
        else:
            print("当前帐号" + rest)
            cur.execute(sql2)
            # print("执行修改")
            cur.execute(sql3)
            print(self.name + "的付款帐号已修改为工行")
        try:
            mysql.commit()
        except Exception as e:
            mysql.rollback()
        cur.close()
        mysql.close()

    # 根据手机号获取账号成员信息
    def getSysUser(self, phone, header):
        url = "/api/admin/v1/sysUser/getSysUser"
        data = {"phone": phone, "current": 1, "size": 10}
        req = self.post(url, data, header)
        return req["data"]['records'][0]

    # 获取组织机构信息
    def getorgInfo(self, header):
        url = "/api/admin/v1/sysOrganization/getOrganizationRegion"
        req = self.post(url, {}, header)
        # print(req)
        return req["data"]

    # 资产分类groupId
    def getByParentId(self, parentId):
        url = '/api/admin/v1/assetGroup/getByParentId'
        data = {"parentId": parentId}
        req = self.post(url, data, self.villageHeaders)
        return req['data'][0]

    # IT信息管理项目查询
    def getProjectInfoPage(self, projectName):
        url = "/api/admin/v1/assetProject/getProjectInfoPage"
        data = {"projectName": projectName, "current": 1, "size": 10}
        req = self.post(url, data, self.auditHeaders)
        # print(req)
        return req["data"]["records"][0]["assetProjectId"]

    # 项目详情跟踪
    def getProjectManagementList(self, projectName):
        url = "/api/admin/v1/assetProject/getProjectManagementList"
        data = {"projectName": projectName, "current": 1, "size": 10, "actNode": 2}
        req = self.post(url, data, self.auditHeaders)
        # print(req)
        return req["data"]["records"][0]

    # 资产登记
    def saveAssetResource(self, assetName):
        getorgInfo = self.getorgInfo(self.villageHeaders)
        url = "/api/admin/v1/assetInfoFixed/saveAssetFixed"
        data = {
            "assetCode": None,
            "sysOrganizationName": None,
            "assetName": assetName,
            "assetSelfCode": None,
            "remark": None,
            "threeCapitalsOwnershipNo": None,
            "provinceId": getorgInfo["provinceId"],
            "province": getorgInfo["province"],
            "cityId": getorgInfo["cityId"],
            "city": getorgInfo["city"],
            "areaId": getorgInfo["areaId"],
            "area": getorgInfo["area"],
            "streetId": getorgInfo["streetId"],
            "street": getorgInfo["street"],
            "address": getorgInfo["address"],
            "purpose": None,
            "purposeExplain": "厂房",
            "buildArea": "200",
            "buildAreaUnit": 1,
            "sharedArea": None,
            "sharedAreaUnit": 1,
            "acquiredDate": ((datetime.date.today() + datetime.timedelta(days=-30)).strftime('%Y-%m-%d {}')).format(
                '00:00:00'),
            "videoUrl": None,
            "videoThumbnailUrl": None,
            "images": [
                "asset/440112000000/202306/86c1c80f-3f8a-4849-9330-3a6d18c42ad2.jpg",
                "asset/440112000000/202306/3682bf2c-1211-4b46-a386-2a35fdbc4dc8.png",
                "asset/441702000000/202307/c0a09fc8-d223-4071-ae89-b7a4f3c07ec3.jpg"
            ],
            "safetyLevel": None,
            "weighCoefficient": None,
            "serviceLife": None,
            "twoFourAddress": None,
            "originalValue": None,
            "cumulativeDepreciation": None,
            "netWorth": None,
            "startDepreciationDate": None,
            "selfUse": None,
            "attribute": None,
            "developmentType": None,
            "developmentReason": None,
            "unitNo": None,
            "cadastreNo": None,
            "landNo": None,
            "adjunctiveResourceNo": None,
            "houseOwner": None,
            "floor": None,
            "buildStructure": None,
            "constructionProjectPlanningPermitNo": None,
            "fireSafetyNo": None,
            "startDate": None,
            "coordinate": None,
            "disposalMethod": None,
            "assetGroupCodeLevel1": "J000000",
            "assetGroupLevel1Name": "经营性资产",
            "assetGroupCodeLevel2": "J020000",
            "assetGroupLevel2Name": "经营性固定资产",
            "assetGroupCodeLevel3": "J020100",
            "assetGroupLevel3Name": "房屋建筑",
            "assetGroupCodeLevel4": "J020101",
            "assetGroupLevel4Name": "农业生产用房",
            "assetGroupCodeLevel5": "J02010101",
            "assetGroupLevel5Name": "厂房",
            "sysOrganizationId": getorgInfo["sysOrganizationId"],
        }
        req = self.post(url, data, self.villageHeaders)
        # print("创建资产", req)
        return req

    # 资产列表
    def getAssetPageList(self, assetName):
        url = '/api/admin/v1/asset/getAssetPageList'
        data = {"current": 1, "size": 10, "assetName": assetName}
        req = self.post(url, data, self.villageHeaders)
        # print(req)
        return req["data"]["records"][0]

    # 资产选择列表,增加Id避免接口多次调用
    def getChooseAssetList(self, assetName, Id):
        url = '/api/admin/v1/asset/getChooseAssetList'
        data = {
            "sysOrganizationId": Id,
            "current": 1,
            "size": 10,
            "type": 0,
            "assetName": assetName
        }
        return self.post(url, data, self.villageHeaders)['data']['records'][0]

    # 审核、发布工作流项目列表  默认公开竞价和待发布交易公告
    def getActivitiPage(self, mode="01", status=20, projectName=None):
        url = "/api/admin/v1/activiti/getActivitiPage"
        data = {"current": 1, "size": 10, "tradeMode": mode, "projectStatusList": [status], "projectName": projectName}
        req = self.post(url, data, self.auditHeaders)
        return req['data']['records'][0]

    # 项目查询->审核
    def audit(self, projectName, mode='01', status=20):
        # 根据projectName查询项目任务id等信息,mode默认01代表公开竞价审核列表，status默认20是发布公告查询列表
        proejctInfo = self.getActivitiPage(mode, status, projectName=projectName)
        print(proejctInfo["assetProjectId"])
        # 审核
        url = '/api/admin/v1/activiti/activitiInstance'
        data = {"assetProjectId": proejctInfo["assetProjectId"],
                "taskId": proejctInfo["taskId"],
                "businessKey": proejctInfo["businessKey"],
                "status": 1, "annotation": "通过"}
        return self.post(url, data, self.auditHeaders)

    # 查看保证金子账号并缴纳后查询
    def getEarenstMoneyForPortal(self, projectName, payerAccountNo):
        # 查询子账号
        assetProjectId = self.getProjectInfoPage(projectName)
        url1 = "/api/auction_interface/v1/assetProjectEnroll/getEarnestMoneyInfo"
        data1 = {"assetProjectId": assetProjectId}
        req1 = self.post(url1, data1, self.userHeaders)["data"]
        # 缴纳保证金
        url2 = "/api/account/v1/counterRecord/open/simulationAddMoney"
        data2 = {"subAccountNo": req1["mainAccountNo"], "payerAccountNo": payerAccountNo, "amount": 1}
        req2 = self.post(url2, data2, self.userHeaders)
        # 查询保证金
        url = "/api/auction_interface/v1/assetProjectEnroll/getEarenstMoneyForPortal"
        data = {"assetProjectId": assetProjectId}
        req = public().post(url, data, self.userHeaders)
        return req

    # 意向人审核列表
    def getEnrollAuditProjectDetail(self, projectName):
        url = "/api/admin/v1/assetProject/getEnrollAuditProjectDetail"
        data = {"projectName": projectName, "current": 1, "size": 10}
        req = self.post(url, data, self.auditHeaders)
        return req["data"]["records"][0]["assetProjectEnrollId"]

    # 上传合同
    def uploadContract(self, projectName):
        # 查询项目id，No
        project = self.getProjectManagementList(projectName)
        url = '/api/admin/v1/assetProjectContract/saveAssetProjectContract'
        data = {
            "type": 1,
            "assetProjectId": project["assetProjectId"],
            "tradeNo": project["tradeNo"],
            "contractStartDate": str(datetime.datetime.now())[0:10],
            "contractYear": 0,
            "contractMonth": 0,
            "contractDay": 10,
            "contractEndDate": str(datetime.datetime.now() + datetime.timedelta(days=10))[0:19],
            "payDateUnit": 0,
            "firstPayDate": str(datetime.datetime.now())[0:10],
            "payDays": 2,
            "paymentDays": 0,
            "idCardBackFile": "ZW5jcnlwdC9jb250cmFjdC80NDA4ODIwMDAwMDAvMjAyMzAzLzcxNDAxN2IxLWZjNTMtNDUxYy1hOTgwLTdkNWQ2ODU0NDljNy5qcGc=",
            "idCardFrontFile": "ZW5jcnlwdC9jb250cmFjdC80NDA4ODIwMDAwMDAvMjAyMzAzLzBhNzE3NzRkLTVlNDUtNGNhYi1hZTFlLTQ1MzdhYWQ2MWRiZi5qcGc=",
            "files": [{
                "fileName": "1.doc",
                "fileUrl": "contract/440882000000/202303/20638259-7605-4e62-815e-93b2c2e26846.doc"
            }]}
        # print(data)
        return self.post(url, data, self.villageHeaders)

    # 合同审核
    def activitiInstance(self, projectName):
        project = self.getProjectManagementList(projectName)
        url = '/api/admin/v1/activiti/activitiInstance'
        data = {"actNode": "contractFirstInstance", "assetProjectId": project["assetProjectId"],
                "businessKey": project["businessKey"], "status": 1, "annotation": "通过"}
        return self.post(url, data, self.auditHeaders)

    # 查询成交公告
    def search_notice(self, assetName):
        url = '/api/admin/v1/assetInformation/getPostInfoPageList'
        data = {"informationTitle": assetName, "current": 1, "size": 10, "informationType": 3}
        return self.post(url, data, self.auditHeaders)

    def getCloudId(self, assetName, status):
        # 查询表决id
        url = '/api/admin/v1/assetProjectCloud/getCloudVotedList'
        data = {
            "assetName": assetName,
            "tradeMode": None,
            "current": 1,
            "size": 10,
            "voteStatus": status
        }
        req = self.post(url, data, self.villageHeaders)
        # print(req['data']['records'][0]['assetProjectCloudId'])
        return req['data']['records'][0]['assetProjectCloudId']

    # 根据表决传的用户身份确定data,
    def search_phone(self, voteUser):
        url = '/api/user/v1/censusRegister/getCensusRegister'
        delegate = {}
        if voteUser == '000':  # 000=所有成员
            delegate = {"censusRegisterStatus": 1, "current": 1, "size": 100, "ageType": 1}
            censusPhone = self.post(url, delegate, self.villageHeaders)
            total = int(censusPhone['data']['total'])  # 方便下个登录接口取值
            # print(censusPhone)
            return censusPhone['data']['records'], total
        elif voteUser == '110':  # 110=仅成员代表
            delegate = {"censusRegisterStatus": 1, "current": 1, "size": 100, "isUserDelegate": 1, "ageType": 1}
            censusPhone = self.post(url, delegate, self.villageHeaders)
            total = int(censusPhone['data']['total'])
            # print(censusPhone)
            return censusPhone['data']['records'], total
        elif voteUser == '101':  # 101=仅户代表
            delegate = {"censusRegisterStatus": 1, "current": 1, "size": 100, "isParentDelegate": 1, "ageType": 1}
            censusPhone = self.post(url, delegate, self.villageHeaders)
            total = int(censusPhone['data']['total'])
            # print(censusPhone)
            return censusPhone['data']['records'], total
        else:  # 111=仅成员代表和户代表
            delegate1 = {"censusRegisterStatus": 1, "current": 1, "size": 100, "isUserDelegate": 1, "ageType": 1}
            delegate2 = {"censusRegisterStatus": 1, "current": 1, "size": 100, "isParentDelegate": 1, "ageType": 1}
            censusPhone1 = self.post(url, delegate1, self.villageHeaders)
            censusPhone2 = self.post(url, delegate2, self.villageHeaders)
            total1 = censusPhone1['data']['total']
            total2 = censusPhone2['data']['total']
            total = int(total1) + int(total2)
            censusPhone = list(censusPhone1['data']['records']) + list(censusPhone2['data']['records'])
            # print(censusPhone)
            return censusPhone, total

    def getDefaultInfo(self):
        """招标获取组织机构信息"""
        url = "/api/admin/v1/smallProject/getDefaultInfo"
        data = {}
        response = self.post(url, data, self.villageHeaders)
        return response["data"]

    def getFirstAuditPageList(self, projectName):
        """查询招标项目流程信息"""
        url = "/api/admin/v1/smallProjectAudit/getFirstAuditPageList"
        data = {
            "current": 1,
            "size": 10,
            "projectName": projectName
        }
        response = self.post(url, data, self.auditHeaders)
        return response["data"]["records"][0]

    def getEnrollPageList(self, projectName):
        """指定中标人列表"""
        smallProjectId = self.getFirstAuditPageList(projectName)["smallProjectId"]
        url = '/api/admin/v1/smallProjectWin/getEnrollPageList'
        data = {
            "current": 1,
            "size": 10,
            "smallProjectId": smallProjectId
        }
        response = self.post(url, data, self.villageHeaders)
        return response["data"]["records"]

    def getIntentionInfo(self, projectName, voteRound=1, old=None):
        """获取遴选云表决意向人信息"""
        idUrl = '/api/admin/v1/assetProjectCloud/getPreIntentionVoteProjectPage'
        idData = {"current": 1, "size": 10, "voteRound": voteRound, "projectName": projectName}
        assetProjectId = self.post(idUrl, idData, self.villageHeaders)['data']['records'][0]['assetProjectId']
        pageUrl = '/api/admin/v1/assetProjectCloud/getIntentionPage'
        pageData = {
            "current": 1,
            "size": 10,
            "voteRound": voteRound,
            "assetProjectId": assetProjectId
        }
        EnrollId = self.post(pageUrl, pageData, self.villageHeaders)['data']['records'][0]['assetProjectEnrollId']
        infoUrl = '/api/admin/v1/assetProjectCloud/getVoteIntentionDetail'
        infoData = {"assetProjectEnrollId": EnrollId, "voteRound": voteRound,
                    "oldAssetProjectCloudId": old}
        info = self.post(infoUrl, infoData, self.villageHeaders)
        return info['data']


if __name__ == '__main__':
    pass
