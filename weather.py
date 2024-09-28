import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

<<<<<<< HEAD
def wea(c, k):
    t = dict()
    e = datetime.now().date().strftime('%Y%m%d')
    t['date'] = str(e[:4] + '/' + e[4:6] + '/' + e[6:])
    d = dict()
=======
def wea(crd, ke):
    dt = dict()
    de = datetime.now().date().strftime('%Y%m%d')
    dt['date'] = str(de[:4] + '/' + de[4:6] + '/' + de[6:])
    w_d = dict()
>>>>>>> origin/main

    for m in requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + k + '&dataType=json&base_date=' + e + '&base_time=0800&nx=' + c[0] + '&ny=' + c[1]).json().get('response').get('body').get('items')['item']:
        i = m['fcstValue']
        if m['category'] == 'TMP': d['tmp'] = i

        elif m['category'] == 'PTY':
            if i == '1': w = '비'
            elif i == '2': w = '비/눈'
            elif i == '3': w = '눈'
            elif i == '4': w = '소나기'
            else: w = '없음'

            d['code'] = i
            d['state'] = w
    t['weather'] = d
    
<<<<<<< HEAD
    return t
=======
    return dt
>>>>>>> origin/main
