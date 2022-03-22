import json
import sys

import requests
from bs4 import BeautifulSoup


def login(name, user):
    msg = user['msg']
    sengkey = user['sendkey']
    user['user']['username'] = tuple(user['user']['username'])
    user['user']['password'] = tuple(user['user']['password'])
    sese = requests.session()
    sese.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) '
                                       'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 '
                                       'MQQBrowser/8.9 Mobile Safari/537.36'})
    try:
        r = sese.get('http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false'
                     '&studentShowWjdc=false')
    except:
        print('请求失败')
        return
    try:
        do = sese.post('http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do', files=user['user'])
    except:
        print('请求失败')
        return
    if do.text == 'success':
        mainpage = sese.get('http://yiqing.ctgu.edu.cn/wx/health/main.do')
        soup_main = BeautifulSoup(mainpage.text, 'lxml')
        find_status = soup_main.find(string='今日已上报')
        if find_status == None:
            print('今日未上报')
            try:
                toApply = sese.get('http://yiqing.ctgu.edu.cn/wx/health/toApply.do')
            except:
                print('请求toApply.do页面失败')
                sys.exit(0)
            soup = BeautifulSoup(toApply.text, 'lxml')
            ttoken = soup.find('input', {'name': 'ttoken'})['value']
            msg['ttoken'] = ttoken
            print(msg['ttoken'])
            try:
                res = sese.post('http://yiqing.ctgu.edu.cn/wx/health/saveApply.do', data=msg,
                                verify=False)

            except:
                print('saveapply.do页面请求失败')
                sendmessage('陈露露 上报失败！', sengkey)
                return
            sendmessage('陈露露 上报成功！', sengkey)

        else:
            rest = name + ' ' + find_status
            print(rest)
            sendmessage(rest, sengkey)


def main():
    with open('userconfig.json', 'r', encoding='utf-8') as f:
        uuserlist = json.load(f)
    for name, user in uuserlist.items():
        login(name, user)


def sendmessage(message, sendkey):
    if sendkey == '':
        return
    url = 'https://sctapi.ftqq.com/' + sendkey + '.send?title='
    try:
        send = requests.get(url + message)
    except:
        return


if __name__ == '__main__':
    main()
