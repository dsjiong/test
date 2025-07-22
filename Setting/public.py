import os

import requests
import time
import json

import urllib3

urllib3.disable_warnings()
os.environ["http_proxy"] = 'http://192.168.123.99:28'
os.environ["https_proxy"] = 'http://192.168.123.99:28'


class PublicService:
    """接口服务基类 (类名建议使用驼峰式命名)"""
    ENV_URL_MAP = {
        'test_cq': 'https://cqjy-test.b2bwings.com',
        'uat_cq': 'https://cqjy-uat.b2bwings.com',
        'test_cc': 'https://cc-test.b2bwings.com',
        'uat_cc': 'https://cc-uat.b2bwings.com',
        'prod_cc': 'https://nccw.gdagri.gov.cn:8443'
    }   # 类变量命名推荐下划线格式[7](@ref)

    # 接口路径集中管理
    API_ENDPOINTS = {
        'admin_login': '/api/admin/v1/sysUser/open/loginByCode',
        'user_login': '/api/user/v1/user/open/loginByCode',
        'cc_login': '/api/core/v1/login/authentication'
    }

    # 村财组织选择集中管理
    ACCOUNT_ORGANIZATION = {
        # 五山
        'GX': {'account': 13751964417, 'sysOrganizationId': '1816405603320205313'},
        # 云浮
        'YF': {'account': 13812345678, 'sysOrganizationId': '1930460747057274882'},
        # 火箭
        'DKS': {'account': 18127845417, 'sysOrganizationId': '1810997833934704642'},
        # 晓婷
        'XT': {'account': 13543800003, 'sysOrganizationId': '1811208886614474753'}
    }

    # 登录凭证集中管理（建议加密存储敏感信息）
    CREDENTIALS = {
        'village': {"phone": 13751964424, "code": "888888"},
        'audit': {"phone": 13751964422, "code": "888888"},
        'user': {"phone": 13751964417, "code": "888888", "user_Type": 1},
        'cc': {"account": ACCOUNT_ORGANIZATION['XT']['account'],
               "sysOrganizationId": ACCOUNT_ORGANIZATION['XT']['sysOrganizationId'], "password": "Hxt123456",
               "check": 'false'}
    }

    def __init__(self, env='test_cc'):
        """初始化运行环境[4](@ref)"""
        self.base_url = self.ENV_URL_MAP.get(env, self.ENV_URL_MAP['test_cc'])
        self.session = requests.Session()  # 复用TCP连接提升性能
        self.headers_cache = {}  # 缓存已获取的headers

    def _request(self, method, url, data=None, headers=None, retries=3):
        """统一请求处理（增加headers参数）"""
        for attempt in range(retries):
            try:
                response = self.session.request(
                    method=method,
                    url=self.base_url + url,
                    headers=headers or {},  # 显式使用传入的headers
                    data=json.dumps(data),
                    verify=False,
                    timeout=(3.05, 27)
                )
                response.raise_for_status()
                return response.json() if response.content else {}
            except (requests.exceptions.RequestException, ValueError) as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                time.sleep(2 ** attempt)
        raise ConnectionError(f"API request failed after {retries} retries")

    def login(self, user_type):
        """增强版cc登录认证逻辑"""
        if user_type not in self.headers_cache:
            # 动态选择登录接口
            endpoint = self.API_ENDPOINTS.get(
                'admin_login' if user_type in ('village', 'audit') else
                'user_login' if user_type == 'user' else
                'cc_login'  # 专用cc登录接口
            )

            # 执行登录获取sessionid
            auth_data = self.CREDENTIALS[user_type]
            result = self._request('POST', endpoint, auth_data)

            # 构建动态headers
            if user_type == 'cc':
                self.headers_cache[user_type] = {
                    'token': result['data']['token'],
                    'Content-Type': 'application/json'
                }
            else:
                self.headers_cache[user_type] = {
                    'sessionid': result['data']['sessionid'],
                    'Content-Type': 'application/json',
                    'channel': 'admin' if user_type in ('village', 'audit') else None
                }
        return self.headers_cache[user_type]

    def post(self, endpoint, data, user_type='user'):
        """明确指定用户类型（解决headers混淆）"""
        # 强制要求指定user_type
        if user_type not in ('village', 'audit', 'user', 'cc'):
            raise ValueError("Invalid user_type. Allowed: village/audit/user")

        # 获取对应用户类型的headers
        headers = self.login(user_type)
        return self._request('POST', endpoint, data=data, headers=headers)


# 使用示例
if __name__ == '__main__':
    service = PublicService(env='test_cc')
    # 调用示例
    # headers = service.login(user_type='village')
    ulr = '/api/core/v1/personal/getPersonalInfo'
    data = {"loginChannel": 2}
    response = service.post(ulr, data, user_type='cc')
    print(response)
