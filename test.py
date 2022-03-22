import json

# userlist = {
#     '黄天星': {
#         'user': {
#             'username': (None, '202008540021067'),
#             'password': (None, '160135')
#         },
#         'msg': {
#             'ttoken': '',
#             'province': '湖北省',
#             'city': '宜昌市',
#             'district': '西陵区',
#             'adcode': '420502',
#             'longitude': '111',
#             'latitude': '31',
#             'sfqz': '否',
#             'sfys': '否',
#             'sfzy': '否',
#             'sfgl': '否',
#             'status': '1',
#             'szdz': '湖北省 宜昌市 西陵区',
#             'sjh': '17627067137',
#             'lxrxm': '黄天星',
#             'lxrsjh': '17627067137',
#             'sffr': '否',
#             'sffrAm': '否',
#             'sffrNoon': '否',
#             'sffrPm': '否',
#             'sffy': '否',
#             'sfgr': '否',
#             'qzglsj': '',
#             'qzgldd': '',
#             'glyy': '',
#             'mqzz': '',
#             'sffx': '否',
#             'qt': ''
#         }
#     },
#     '陈露露': {
#         'user': {
#             'username': (None, '202008120021001'),
#             'password': (None, '305321')
#         },
#         'msg': {
#             'ttoken': '',
#             'province': '湖北省',
#             'city': '宜昌市',
#             'district': '西陵区',
#             'adcode': '420502',
#             'longitude': '111',
#             'latitude': '31',
#             'sfqz': '否',
#             'sfys': '否',
#             'sfzy': '否',
#             'sfgl': '否',
#             'status': '1',
#             'szdz': '湖北省 宜昌市 西陵区',
#             'sjh': '15871577206',
#             'lxrxm': '陈露露',
#             'lxrsjh': '15871577206',
#             'sffr': '否',
#             'sffrAm': '否',
#             'sffrNoon': '否',
#             'sffrPm': '否',
#             'sffy': '否',
#             'sfgr': '否',
#             'qzglsj': '',
#             'qzgldd': '',
#             'glyy': '',
#             'mqzz': '',
#             'sffx': '否',
#             'qt': ''
#         }
#     }
# }
# with open('userfile.json', 'w', encoding='utf8') as f:
#     json.dump(userlist, f, indent=4, ensure_ascii=False, )
with open('userfile.json', 'r', encoding='utf-8') as f:
    uuserlist = json.load(f)
uuserlist['黄天星']['user']['username'] = tuple(uuserlist['黄天星']['user']['username'])
print(uuserlist['黄天星']['user'])
