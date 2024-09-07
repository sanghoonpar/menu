import os, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def wea(crd, ke):
    dt = dict()
    de = datetime.now().date().strftime('%Y%m%d')
    dt['date'] = str(de[:4] + '/' + de[4:6] + '/' + de[6:])
    w_d = dict()

    for im in requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + ke + '&dataType=json&base_date=' + de + '&base_time=0800&nx=' + crd[0] + '&ny=' + crd[1]).json().get('response').get('body').get('items')['item']:
        it = im['fcstValue']
        if im['category'] == 'TMP': w_d['tmp'] = it

        elif im['category'] == 'PTY':
            if it == '1': w_s = '비'
            elif it == '2': w_s = '비/눈'
            elif it == '3': w_s = '눈'
            elif it == '4': w_s = '소나기'
            else: w_s = '없음'

            w_d['code'] = it
            w_d['state'] = w_s
    dt['weather'] = w_d
    
    return dt