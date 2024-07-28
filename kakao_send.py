# -*- coding: utf-8 -*-
import urllib, json, requests

def send(tk, lc, res, dt):

    suc = 0
    text = f'''\
    위치 정보 : {lc}
    날씨 정보 ({dt['date']})
    기온 : {dt['weather']['tmp']}
    기우  : {dt['weather']['state']}
    미세먼지 : {dt['dust']['pm10']['value']} {dt['dust']['pm10']['state']}
    '''

    def li(url): return {'web_url': url, 'mobile_web_url': url}
    def req(): return requests.post(url = url, data = dat, headers = {'Authorization': 'Bearer ' + {'access_token' : tk}.get('access_token'), 'scope':'talk_message'}).json()
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    wea = li('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨')
    dat = {'template_object' : json.dumps({'object_type': 'text', 'text': text, 'link': wea, 'button_title': '날씨 상세보기'})}

    if req().get('result_code') == 0: suc += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req()))

    ct = []

    for place in res:
        tt = place.get('title').replace('<b>','').replace('</b>','')
        if place.get('telephone'): tt = tt, '\ntel) ', place.get('telephone')
        ct.append({'title': '[' + place.get('category') + '] ' + tt, 'description': ''.join(place.get('address').split()[1:]), 'image_url': 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill', 'image_width': 50, 'image_height': 50, 'link': li('https://search.naver.com/search.naver?query=' + urllib.parse.quote(place.get('address') + '' + tt))})

    dat = {'template_object' : json.dumps({'object_type' : 'list', 'header_title' : '현재 날씨에 따른 음식 추천', 'header_link' : wea, 'contents' : ct, 'buttons' : [{'title' : '날씨 상세보기', 'link' : wea}]})}
    if req().get('result_code') == 0: suc += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req()))

    return suc