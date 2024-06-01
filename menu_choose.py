import random

def menu_choose(data):

    if data.get('weather').get('code') != '0': weather_state = 1
    elif data.get('dust').get('code') == '1':  weather_state = 2
    else: weather_state = 3

    if weather_state == 1: foods_list = random.sample('부대찌개, 아구찜, 해물탕, 칼국수, 수제비, 짬뽕, 우동, 추어탕, 국밥, 김치부침개, 두부김치, 파전, 선지해장국'.split(', '), 3)
    elif weather_state == 2: foods_list = random.sample('콩나물국밥, 고등어, 굴, 쌀국수, 마라탕, 미나리'.split(', '), 3)
    else: foods_list = random.sample('한식, 중식, 양식, 일식'.split(', '), 3)

    return foods_list