from Setting.public import *
import random


class xiuGai(PublicService):
    def search_org_list(self):
        url = '/api/core/v1/sysOrganization/getSysOrganizationPage'
        api_data = {
            "organizationName": "",
            "organizationUnitLevel": None,
            "sysOrganizationId": "1811208886614474753",
            "sysTenantId": "",
            "current": 1,
            "size": 50,
            "loginChannel": 2
        }
        list_response = self.post(url, api_data, 'cc')
        # print(list_response)
        return list_response

    def generate_unified_credit_code(self):
        # 基础字符集（排除易混淆字符 I/O/Z/S/V）
        base_chars = "0123456789ABCDEFGHJKLMNPQRTUWXY"
        weights = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]

        # 1. 登记管理部门代码（第1位）：9=工商
        code = "N"
        # 2. 机构类别代码（第2位）：1-3随机
        code += str(random.randint(1, 2))
        # 3. 行政区划码（第3-8位）：6位随机数字
        code += ''.join(str(random.randint(0, 9)) for _ in range(6))
        # 4. 主体标识码（第9-16位）：8位随机字符
        code += ''.join(random.choice(base_chars) for _ in range(8))

        # 5. 计算校验码（第17-18位）
        total = sum(base_chars.index(char) * weights[i] for i, char in enumerate(code))
        check_code = base_chars[31 - (total % 31)]

        print(code + check_code)
        return code + check_code

    def check_credit_code(self):
        org_id = self.search_org_list()['data']['records']
        # print(org_id[34])
        for x in range(34):
            if not org_id[x]['creditCode'].startswith('N') or len(org_id[x]['creditCode']) < 18:
                # print(org_id[x]['creditCode'])
                organizationId = org_id[x]['sysOrganizationId']
                remark = org_id[x]['creditCode']
                detail_url = '/api/core/v1/sysOrganization/getSysOrganizationDetail'
                detail_data = {
                    "sysOrganizationId": organizationId,
                    "loginChannel": 2
                }
                detail = self.post(detail_url, detail_data, 'cc')['data']
                update_url = '/api/core/v1/sysOrganization/updateSysOrganization'
                update_data = {
                    "province": detail['province'],
                    "provinceCode": detail['provinceCode'],
                    "area": detail['area'],
                    "areaCode": detail['areaCode'],
                    "city": detail['city'],
                    "cityCode": detail['cityCode'],
                    "street": detail['street'],
                    "streetCode": detail['streetCode'],
                    "village": detail['village'],
                    "villageCode": detail['villageCode'],
                    "creditCode": self.generate_unified_credit_code(),
                    "organizationName": detail['organizationName'],
                    "organizationType": detail['organizationType'],
                    "organizationUnitLevel": detail['organizationUnitLevel'],
                    "parentId": detail['parentId'],
                    "remark": remark,
                    "sort": detail['sort'],
                    "sysTenantId": detail['sysTenantId'],
                    "tenantName": detail['tenantName'],
                    "sysOrganizationId": detail['sysOrganizationId'],
                    "parentOrganizationName": detail['parentOrganizationName'],
                    "organizationTypeText": detail['organizationTypeText'],
                    "organizationUnitLevelText": detail['organizationUnitLevelText'],
                    "loginChannel": 2
                }
                self.post(update_url, update_data, 'cc')


if __name__ == '__main__':
    xiuGai().check_credit_code()
