import os, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(crd):
    data = dict()
    date = datetime.now().date().strftime('%Y%m%d')
    data['date'] = str(date[:4] + '/' + date[4:6] + '/' + date[6:])
    w_d = dict()

    for item in requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + os.environ.get('ser_key') + '&dataType=json&base_date=' + date + '&base_time=0800&nx=' + crd[0] + '&ny=' + crd[1]).json().get('response').get('body').get('items')['item']:
        it = item['fcstValue']
        if item['category'] == 'TMP': w_d['tmp'] = it

        elif item['category'] == 'PTY':
            if it == '1': w_s = '비'
            elif it == '2': w_s = '비/눈'
            elif it == '3': w_s = '눈'
            elif it == '4': w_s = '소나기'
            else: w_s = '없음'

            w_d['code'] = it
            w_d['state'] = w_s

    data['weather'] = w_d
    
    return [data, os.environ.get('ser_key')]