import random

def menu_choose(d):

    if d.get("weather").get("code") != "0": w = 1
    elif d.get("dust").get("code") == "1":  w = 2
    else: w = 3

    if w == 1: f = random.sample("부대찌개, 칼국수, 수제비, 짬뽕, 김치부침개, 파전, 김치찌개".split(", "), 3)
    elif w == 2: f = random.sample("고등어조림, 미역국, 마늘장아찌, 녹차, 오이냉국".split(", "), 3)
    else: f = random.sample("된장찌개, 짜장면, 삼겹살, 치킨, 국밥, 떡볶이".split(", "), 3)

    return f