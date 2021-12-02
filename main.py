import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'
}

origin_url = "https://www.zhihu.com";
url2 = "https://www.zhihu.com/question/452834742/answer/1819593409"
urlbaidu = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=hello&fenlei=256&rsv_pq=d4b177c10005863d&rsv_t=5410wKgjJcTBqQ4GpIAB7swXE136lC04nw19PwP76RsThMQQpuh6N4khhW4&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=hello&rsp=6&inputT=1118&rsv_sug4=1118"
urlmaishuren = "https://www.maishuren.com/log/1.log";
rs = requests.get(url2, headers = headers)
print(rs.status_code)
