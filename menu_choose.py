import random

def menu_choose(data):

    if data.get('weather').get('code') != '0': weather_state = 1
    elif data.get('dust').get('code') == '1':  weather_state = 2
    else: weather_state = 3

    if weather_state == 1: foods_list = random.sample('부대찌개, 칼국수, 수제비, 짬뽕, 김치부침개, 파전'.split(', '), 3)
    elif weather_state == 2: foods_list = random.sample('도라지, 미나리, 마늘, 녹차, 오이'.split(', '), 3)
    else: foods_list = random.sample('한식, 중식, 양식, 일식'.split(', '), 3)

    return foods_list