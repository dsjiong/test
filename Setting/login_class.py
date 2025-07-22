import requests


class loginHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def data(self, phone=None, user_type=None):
        data = {"phone": phone, "code": "888888", "userType": user_type}
        return data

    def visit(self, method, url=None, params=None, data=None, json=None, headers=None, **kwargs):
        headers = {"Content-Type": "application/json"}
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, verify=False,
                                    **kwargs).json()
