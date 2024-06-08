# -*- coding: utf-8 -*-
import urllib, json, requests

def send(token, location, res, data):

    suc = 0
    text = f'''\
    위치 정보 : {location}
    날씨 정보 ({data['date']})
    기온 : {data['weather']['tmp']}
    기우  : {data['weather']['state']}
    미세먼지 : {data['dust']['pm10']['value']} {data['dust']['pm10']['state']}
    '''

    def li(url): return {'web_url': url, 'mobile_web_url': url}
    def req(a, b, c): return requests.post(url = a, data = b, headers = {'Authorization': 'Bearer ' + {'access_token' : c}.get('access_token'), 'scope':'talk_message'}).json()
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    wea = li('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨')
    dat = {'template_object' : json.dumps({'object_type': 'text', 'text': text, 'link': wea, 'button_title': '날씨 상세보기'})}

    if req(url, dat, token).get('result_code') == 0: suc += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req(url, dat, token)))

    contents = []

    for place in res:
        title = place.get('title').replace('<b>','').replace('</b>','')
        if place.get('telephone'): title = title, '\ntel) ', place.get('telephone')
        urlliB = 'https://search.naver.com/search.naver?query=' + urllib.parse.quote(place.get('address') + '' + title)
        contents.append({'title': '[' + place.get('category') + '] ' + title, 'description': ''.join(place.get('address').split()[1:]), 'image_url': 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill', 'image_width': 50, 'image_height': 50, 'link': li(urlliB)})

    dat = {'template_object' : json.dumps({'object_type' : 'list', 'header_title' : '현재 날씨에 따른 음식 추천', 'header_link' : wea, 'contents' : contents, 'buttons' : [{'title' : '날씨 상세보기', 'link' : wea}]})}
    if req(url, dat, token).get('result_code') == 0: suc += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req(url, dat, token)))

    return suc