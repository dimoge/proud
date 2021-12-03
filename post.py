import requests
import configparser

# gerrit登录接口 POST payload:From-Data

# 头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
    'Host': 'sellercentral.amazon.com',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# gerrit登录接口
url_gerrit_login = "http://192.168.87.190/gerrit/login"

# gerrit登录参数
login_param = {
    "username": "guohao0323",
    "password": "WWW.baidu.com323"
}

response = requests.post(url_gerrit_login, data=login_param, headers=headers)
print(response.status_code)
print(response.text)
