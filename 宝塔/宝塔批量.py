import requests

def exp_check(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    #扫描并输出存在漏洞的url
    url1= url+":888/pma"
    response = requests.get(url=url1,headers=header,timeout=5)
    try:
        if response.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url,cmd):
        pass