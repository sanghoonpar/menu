import os, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(crd):
    data = dict()
    data['date'] = str(datetime.now().date().strftime('%Y%m%d')[:4] + '/' + datetime.now().date().strftime('%Y%m%d')[4:6] + '/' + datetime.now().date().strftime('%Y%m%d')[6:])
    weather_data = dict()

    for item in requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + os.environ.get('ser_key') + '&dataType=json&base_date=' + datetime.now().date().strftime('%Y%m%d') + '&base_time=0800&nx=' + crd[0] + '&ny=' + crd[1]).json().get('response').get('body').get('items')['item']:

        if item['category'] == 'TMP': weather_data['tmp'] = item['fcstValue']

        elif item['category'] == 'PTY':
            if item['fcstValue'] == '1': weather_state = '비'
            elif item['fcstValue'] == '2': weather_state = '비/눈'
            elif item['fcstValue'] == '3': weather_state = '눈'
            elif item['fcstValue'] == '4': weather_state = '소나기'
            else: weather_state = '없음'

            weather_data['code'] = item['fcstValue']
            weather_data['state'] = weather_state

    data['weather'] = weather_data
    
    return [data, os.environ.get('ser_key')]