import random

def m_c(d):

    if d.get('weather').get('code') != '0': w = 1
    elif d.get('dust').get('code') == '1':  w = 2
    else: w = 3

    if w == 1: f = random.sample('부대찌개, 칼국수, 수제비, 짬뽕, 김치부침개, 파전, 김치찌개'.split(', '), 3)
    elif w == 2: f = random.sample('도라지, 미나리, 마늘, 녹차, 오이'.split(', '), 3)
    else: f = random.sample('타코야끼, 찜닭, 카레, 샌드위치'.split(', '), 3)

    return f