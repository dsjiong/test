import pymysql
import datetime
from time import sleep
from Setting.public import *


class ccBase(PublicService):
    """接口服务基类 (类名建议使用驼峰式命名)"""

    # 类变量命名推荐下划线格式[7](@ref)
    def search_org_list(self):
        url = '/api/core/v1/sysOrganization/getSysOrganizationPage'
        api_data = {
            "organizationName": "",
            "organizationUnitLevel": None,
            "sysOrganizationId": "1816405603320205313",
            "sysTenantId": "",
            "current": 1,
            "size": 50,
            "loginChannel": 2
        }
        list_response = self.post(url, api_data, 'cc')
        print(list_response)
        return list_response


if __name__ == '__main__':
    ccBase().search_org_list()
