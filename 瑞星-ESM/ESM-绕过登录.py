import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def exp_check(url):
    try:
        path = "/ESM/API/RAVServices/login.aspx"
        rsp = requests.get(url=url + path,headers=headers,verify=False)
        if rsp.status_code == 200 :
            return 1
        else:
            return 2
    except:
        return 3

def exp_others(url):
    try:
        path = "/ESM/API/RAVServices/login.aspx"
        rsp = requests.get(url=url + path,headers=headers,verify=False)
        if rsp.status_code == 200 :
            return ("绕过登录的接口如下：\r\n"
                    +url+path
                                        )
    except:
        return 3
    