import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'
}

origin_url = "https://www.zhihu.com";
url_douban = "https://www.douban.com"
url2 = "https://www.zhihu.com/question/452834742/answer/1819593409"
urlbaidu = "https://www.baidu.com"
urlmaishuren = "https://www.maishuren.com/log/1.log";
rs = requests.get(urlbaidu, headers = headers)
print(rs.status_code)
print(rs.headers)
