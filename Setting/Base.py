import pymysql
import datetime
from time import sleep
from Setting.Publics import *

urllib3.disable_warnings()


class information(public):
    header = public().get_header()
    villageHeaders = header[0]
    auditHeaders = header[1]
    userHeaders = header[2]

    # 数据库
    def connect(self, database):
        mysql = pymysql.connect(host='39.108.128.154',
                                port=3307,
                                user='b2bwings',
                                password='b2bwings666!',
                                database=database)
        print('连接成功', mysql)
        return mysql

    """# 更改工行付款账号
    def update(self):
        mysql = self.connect('cqjy-user')
        cur = mysql.cursor()
        # print('name=' + self.name)
        sql1 = "SELECT phone FROM t_user_info WHERE earnest_money_pay_account_name = " \
               "'42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002'"
        cur.execute(sql1)
        rest = cur.fetchone()[0]
        account = datetime.datetime.now().strftime('%y%m%d%H%M%S')
        sql2 = "UPDATE t_user_info SET earnest_money_pay_account_name = " + account + " WHERE earnest_money_pay_account_name = '42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002'"
        # print(sql2)
        sql3 = "UPDATE t_user_info SET earnest_money_pay_account_name = " \
               "'42443581a7a4fa0390894082d45bcfec0d3570b7d5a4706913302487d2083002' WHERE phone = \"" + self.name + "\""
        # print(sql3)
        if rest == self.name:
            print("执行修改")
        elif rest is None:
            cur.execute(sql2)
            cur.execute(sql3)
        else:
            print("当前帐号" + rest)
            cur.execute(sql2)
            cur.execute(sql3)
            print("执行修改")
        try:
            mysql.commit()
        except Exception as e:
            mysql.rollback()
        cur.close()
        mysql.close()"""

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

    def getOrganizationAndParentInfo(self, header):
        sysOrganizationId = self.getorgInfo(header)['sysOrganizationId']
        url = '/api/admin/v1/investmentAttraction/getOrganizationAndParentInfo'
        data = {"organizationId": sysOrganizationId, "executiveLevel": 4}
        req = self.post(url, data, header)
        return req['data']

    # 资产分类groupId
    def getByParentId(self, parentId):
        url = '/api/admin/v1/assetGroup/getByParentId'
        data = {"parentId": parentId}
        response = self.post(url, data, self.villageHeaders)['data']
        return response

    # IT信息管理项目查询
    def getProjectInfoPage(self, projectName):
        url = "/api/admin/v1/assetProject/getProjectInfoPage"
        data = {"projectName": projectName, "current": 1, "size": 10}
        req = self.post(url, data, self.auditHeaders)
        return req["data"]["records"][0]["assetProjectId"]

    # 项目详情跟踪
    def getProjectManagementList(self, projectName):
        url = "/api/admin/v1/assetProject/getProjectManagementList"
        data = {"projectName": projectName, "current": 1, "size": 10, "actNode": 2}
        req = self.post(url, data, self.auditHeaders)
        return req["data"]["records"][0]

    # 资产登记
    def saveAssetResource(self, assetName):
        getorgInfo = self.getorgInfo(self.villageHeaders)
        url = "/api/admin/v1/assetInfoResource/saveAssetResource"
        # /api/admin/v1/assetInfoFixed/saveAssetFixed 经营性资产&非经营性资产
        data = {
            "assetCode": None,
            "sysOrganizationName": None,
            "assetName": assetName,
            "assetSelfCode": assetName,
            "assetSource": "自购",
            "recordDate": "2024-12-04",
            "landCertificateType": 1,
            "ownership": "1",
            "commonAsset": False,
            "commonAssetRate": 100,
            "billCount": None,
            "originVouchers": [],
            "remark": None,
            "assetWorth": "59990",
            "newAssetStatusStr": None,
            "newAssetStatus": "1",
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
            "purposeExplain": "耕地",
            "landOccupation": "5",
            "landOccupationUnit": 0,
            "videoUrl": None,
            "videoThumbnailUrl": None,
            "images": [
                "asset/440112000000/202306/86c1c80f-3f8a-4849-9330-3a6d18c42ad2.jpg",
                "asset/440112000000/202306/3682bf2c-1211-4b46-a386-2a35fdbc4dc8.png",
                "asset/441702000000/202307/c0a09fc8-d223-4071-ae89-b7a4f3c07ec3.jpg"
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
            "sysOrganizationId": getorgInfo["sysOrganizationId"],
        }
        req = self.post(url, data, self.villageHeaders)
        # print("创建资产", req)
        return req

    def projectEndDate(self, year=5, month=6, day=0):
        """获取项目结束日期"""
        url = '/api/admin/v1/assetProject/getProjectEndDate'
        data = {"startDate": str(datetime.datetime.now())[0:10], "year": year, "month": month, "day": day}
        req = self.post(url, data, self.villageHeaders)
        return req["data"]

    def applyData(self, assetName, Type="00"):
        """立项申请data参数调用函数，默认Type=00,出租无资质要求"""
        cunInfo = self.getorgInfo(self.villageHeaders)
        getSysUser = self.getSysUser(self.vPhone, self.villageHeaders)
        asstInfo = self.getChooseAssetList(assetName, cunInfo["sysOrganizationId"])
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
            "contact": getSysUser['fullName'],
            "phone": getSysUser['phone'],
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
                "assetAddress": asstInfo["assetAddress"],
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
            "enrollType": 0,  # 允许报名用户类型
            "blacklistEnter": "false",  # 是否禁止警示名单报名 0=否 1=是
            "priorityOriginalLessee": "false",  # 是否原承租方优先权 0=否 1=是
            "payTradeEarnestMoney": "true",
            "tradeEarnestMoney": 1,
            "floorPrice": 51688.88,
            "minBidRange": 10000,
            "maxBidRange": 900000,
            "assetDeliverDay": 1,
            "progressiveIncrease": "false",  # 是否递增付款金额 0=否 1=是
            "progressiveIncreaseWay": "",  # 递增方式 1=按比例递增 2=按固定金额递增
            "progressiveIncreaseAmount": '',  # 每次递增固定金额
            "progressiveIncreaseStartMonth": '',  # 从第n个月开始递增
            "progressiveIncreaseMonth": '',  # 每n个月递增一次
            "progressiveIncreaseIncrease": None,  # 每次递增幅度为上期缴纳租金的n百分比
            "rentFree": "false",  # 是否有免租期
            "rentFreePeriod": None,  # 免租天数
            "rentCollectMethod": '3',  # 租金收取方式 0=按月 1=按季 3=按年 4=一次性
            "projectStartDate": str(datetime.datetime.now() + datetime.timedelta(days=0))[0:10],  # 租赁开始时间,出售类型时间为空
            "projectEndDate": self.projectEndDate(), # 租赁开始时间,出售类型时间为空
            "projectTradeYear": "5年6月",
            "perpetualAssignment": "false",  # 是否永久出让 0=否 1=是
            "repostAssetProject": "false",  # 流拍是否自动挂牌
            "contractExpirationDate": 1,
            "isSubmit": 1,
            "taskId": None,
            "delivery": "按现状交付",
            "agent": "false"
        }
        if Type == "00":
            # 出租不变
            pass
        elif Type == "01":
            # 出租+资格
            data["requires"] = 'true'
            data["auditMaterialsSaveParams"] = [{"materialsName": "身份证", "remark": "备注"}]
        elif Type == "10":
            # 出让
            data["tradeType"] = "02"
        elif Type == "11":
            # 出让+资格
            data["tradeType"] = "02"
            data["requires"] = 'true'
            data["auditMaterialsSaveParams"] = [{"materialsName": "身份证", "remark": "备注"}]
        elif Type == "12":
            """永久出让"""
            data["tradeType"] = "02"
            data["projectEndDate"] = None
            data["projectTradeYear"] = "永久出让"
            data["perpetualAssignment"] = "true"
        elif Type == "20":
            # 出售
            data["tradeType"] = "03"
            del data["rentCollectMethod"], data["projectStartDate"], data["projectEndDate"], data["projectTradeYear"]
        elif Type == "21":
            # 出售+资格
            data["tradeType"] = "03"
            data["requires"] = 'true'
            del data["rentCollectMethod"], data["projectStartDate"], data["projectEndDate"], data["projectTradeYear"]
            data["auditMaterialsSaveParams"] = [{"materialsName": "身份证", "remark": "备注"}]
        return data

    # 资产选择列表,增加Id避免接口多次调用
    def getChooseAssetList(self, assetName, Id=None):
        url = '/api/admin/v1/asset/getChooseAssetList'
        data = {
            "sysOrganizationId": Id,
            "current": 1,
            "size": 10,
            "type": 0,
            "assetName": assetName
        }
        return self.post(url, data, self.villageHeaders)['data']['records'][0]

    # 审核、发布工作流项目列表  默认mode=01公开竞价；status=20待发布交易公告；tradeType=01出租
    def getActivitiPage(self, mode="01", status=20, projectName=None):
        url = "/api/admin/v1/activiti/getActivitiPage"
        data = {"current": 1, "size": 10, "tradeMode": mode, "projectStatusList": [status],
                "projectName": projectName}
        req = self.post(url, data, self.auditHeaders)
        return req['data']['records'][0]

    # 项目查询->审核
    def audit(self, projectName, mode='01', status=20):
        # 根据projectName查询项目任务id等信息,mode默认01代表公开竞价审核列表，status默认20是发布公告查询列表
        proejctInfo = self.getActivitiPage(mode, status, projectName=projectName)
        print(proejctInfo["assetProjectId"])
        tradeNo = proejctInfo['tradeNo']
        # 审核
        url = '/api/admin/v1/activiti/activitiInstance'
        data = {"assetProjectId": proejctInfo["assetProjectId"],
                "taskId": proejctInfo["taskId"],
                "businessKey": proejctInfo["businessKey"],
                "status": 1, "annotation": "通过"}
        self.setSubAccount(tradeNo, projectName)
        return self.post(url, data, self.auditHeaders)

    def setSubAccount(self, trade_no, projectName):
        """测试环境手动生成子账号"""
        mysql = self.connect("cqjy-account")  # 连接数据库
        cursor = mysql.cursor()  # 建立游标
        time = (datetime.datetime.now()).strftime('%Y%m%d%H%M%S')
        time1 = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        sql = ("INSERT INTO `cqjy-account`.`t_sub_account`(`sub_account_id`, `app_id`, `app_name`, `sub_app_id`, "
               "`sub_account_no`, `sub_account_name`, `sub_req_no`, `organization_name`, `organization_id`, "
               "`main_account_no`, `account_bank_code`, `main_account_name`, `open_bank_name`,  `project_trade_no`, "
               "`auth_code`, `account_status`, `gmt_create`, `project_name`) "
               "VALUES (" + time + ", 'gdnccqjy', '广东省农村产权流转交易管理服务平台', '100000', '95588" + time + "', "
               "'八赏冒乐蹬饥符曾绍亥猴睹崎等佑', \'" + time + "\', '清远市清新区集体资产交易中心', 1531213778436427778, "
               "'3602023929200100926', '102', '八赏冒乐蹬饥符曾绍亥猴睹崎等佑', "
               "'中国工商银行广州支行',  \'" + trade_no + "\', \'" + time + "\', '00', '" + time1 + "', '" + projectName +
               "');")
        print(sql)
        cursor.execute(sql)
        try:
            mysql.commit()
        except Exception as e:
            mysql.rollback()
        cursor.close()
        mysql.close()

    def getEarenstMoneyForPortal(self, projectName, payerAccountNo):
        """查看保证金子账号并缴纳后查询"""
        mysql = self.connect("cqjy")
        cursor = mysql.cursor()
        time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        # 查询子账号
        assetProjectId = self.getProjectInfoPage(projectName)
        url1 = "/api/auction/v1/assetProjectEnroll/getEarnestMoneyInfo"
        data1 = {"assetProjectId": assetProjectId}
        req1 = self.post(url1, data1, self.userHeaders)["data"]
        # 缴纳保证金
        # url2 = "/api/account/v1/counterRecord/open/simulationAddMoney"
        # data2 = {"subAccountNo": req1["mainAccountNo"], "payerAccountNo": '3602019309200000266', "amount": 1}
        # req2 = self.post(url2, data2, self.auditHeaders)
        sql = ("UPDATE cqjy.t_asset_project_enroll SET system_feedback_status = 1, pay_earnest_money_date = '" + time +
               "', pay_earnest_money = 1 WHERE asset_project_id = " + assetProjectId + " ;")
        # if req2["message"] != "操作成功":
        cursor.execute(sql)
        try:
            mysql.commit()
        except Exception as e:
            mysql.rollback()
        cursor.close()
        mysql.close()
        # 查询保证金
        url = "/api/auction/v1/assetProjectEnroll/getEarenstMoneyForPortal"
        data = {"assetProjectId": assetProjectId}
        req = public().post(url, data, self.userHeaders)
        return req

    def getEnrollAuditProjectDetail(self, projectId):
        """意向人审核列表"""
        url = "/api/admin/v1/assetProject/getEnrollAuditProjectDetail"
        data = {"assetProjectId": projectId, "current": 1, "size": 10}
        req = self.post(url, data, self.auditHeaders)
        return req["data"]["records"][0]["assetProjectEnrollId"]

    def uploadContract(self, projectName, trade=None):
        """查询项目id，No"""
        project = self.getProjectManagementList(projectName)
        url = '/api/admin/v1/assetProjectContract/saveAssetProjectContract'
        data = {
            "type": 1,
            "assetProjectId": project["assetProjectId"],
            "tradeNo": project["tradeNo"],
            "contractNo": project["tradeNo"],
            "contractStartDate": str(datetime.datetime.now() + datetime.timedelta(days=1))[0:10],
            "contractYear": 5,
            "contractMonth": 6,
            "contractDay": 0,
            "contractEndDate": self.projectEndDate(),
            "payDateUnit": 4,
            "firstPayDate": str(datetime.datetime.now() + datetime.timedelta(days=1))[0:10],
            "payDays": 0,
            "paymentDays": 0,
            "idCardBackFile": "ZW5jcnlwdC9jb250cmFjdC80NDE3MDQwMDAwMDAvMjAyNDExL2Y1MDFlM2MzLWY0MzEtNGQwMi05YjE1LTE2MGQ0OTU1MzI4NC5wbmc=",
            "idCardFrontFile": "ZW5jcnlwdC9jb250cmFjdC80NDE3MDQwMDAwMDAvMjAyNDExLzk2ZGM2ZWYwLWE5MjYtNGZjMS04MjkwLWU0NjY4ODUyMTVkMC5wbmc=",
            "files": [{
                "fileName": "1.png",
                "fileUrl": "contract/441802000000/202311/20028cc3-734b-4e0d-a043-f85a89921fe4.png"
            }],
            "clinchAmount": 5168,
            "contractSignDate": str(datetime.datetime.now())[0:10],
            "contractSignPlace": "科华街251号",
            "tradeType": "02",
            "ourOwnProportion": 100,
            "totalPrice": "5168.00",
            "contractName": project["projectName"]
        }
        if trade == '20':
            del data['contractStartDate'], data['contractYear'], data['contractMonth'], data['contractDay'], (
                data)['contractEndDate'], data['payDateUnit']
            return data
        return self.post(url, data, self.villageHeaders)

    def activitiInstance(self, projectName):
        """合同审核"""
        project = self.getProjectManagementList(projectName)
        url = '/api/admin/v1/activiti/activitiInstance'
        data = {"actNode": "contractFirstInstance", "assetProjectId": project["assetProjectId"],
                "businessKey": project["businessKey"], "status": 1, "annotation": "通过"}
        return self.post(url, data, self.auditHeaders)

    def search_notice(self, assetName):
        """查询成交公告"""
        url = '/api/admin/v1/assetInformation/getPostInfoPageList'
        data = {"informationTitle": assetName, "current": 1, "size": 10, "informationType": 3}
        return self.post(url, data, self.auditHeaders)

    def getCloudId(self, assetName, status):
        """查询表决id"""
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

    def search_phone(self, voteUser):
        """根据表决传的用户身份确定data"""
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

    def getHistoryPageList(self, projectName):
        """招标立项历史记录查询"""
        url = "/api/admin/v1/smallProject/getHistoryPageList"
        data = {
            "current": 1,
            "size": 10,
            "projectName": projectName
        }
        response = self.post(url, data, self.auditHeaders)["data"]["records"][0]
        return response

    def getEnrollPageList(self, projectName, legal=""):
        """指定中标人列表"""
        smallProjectId = self.getHistoryPageList(projectName)['smallProjectId']
        url = '/api/admin/v1/smallProjectWin/getEnrollPageList'
        data = {
            "current": 1,
            "size": 10,
            "legalRepresentative": legal,  # 默认为空，传值查询对应法人名称
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
