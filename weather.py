import os, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(crd):
    data = dict()
    date = datetime.now().date().strftime('%Y%m%d')
    data['date'] = str(date[:4] + '/' + date[4:6] + '/' + date[6:])
    weather_data = dict()

    for item in requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + os.environ.get('ser_key') + '&dataType=json&base_date=' + date + '&base_time=0800&nx=' + crd[0] + '&ny=' + crd[1]).json().get('response').get('body').get('items')['item']:
        itemf = item['fcstValue']
        if item['category'] == 'TMP': weather_data['tmp'] = itemf

        elif item['category'] == 'PTY':
            if itemf == '1': weather_state = '비'
            elif itemf == '2': weather_state = '비/눈'
            elif itemf == '3': weather_state = '눈'
            elif itemf == '4': weather_state = '소나기'
            else: weather_state = '없음'

            weather_data['code'] = itemf
            weather_data['state'] = weather_state

    data['weather'] = weather_data
    
    return [data, os.environ.get('ser_key')]