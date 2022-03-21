import requests
from bs4 import BeautifulSoup
sese = requests.session()
r = sese.get('http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false'
             '&studentShowWjdc=false')
files = {
    'username': (None, '202008540021067'),
    'password': (None, '160135')
}
header = {
        'ttoken': '*/*',
        'province': 'gzip, deflate',
        'city': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'district': 'no-cache',
        'adcode': 'keep-alive',
        # 'Content-Length': '451',
        'longitude': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '',
        'Host': '',
        'Origin': '',
        'Pragma': 'no-cache',
        'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44',
        'X-Requested-With': 'XMLHttpRequest'

    }
proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
do = sese.post('http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do', files=files, proxies=proxies, verify=False)
if do.text == 'success':
    mainpage = sese.get('http://yiqing.ctgu.edu.cn/wx/health/toApply.do')
    soup =BeautifulSoup(mainpage.text, 'lxml')
    print(soup.find('input', {'name': 'ttoken'})['value'])