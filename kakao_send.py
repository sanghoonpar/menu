# -*- coding: utf-8 -*-
import urllib, json, requests

def send(token, location, res, data):
    
    a = 0
    text = f'''\
    위치 정보 : {location}
    날씨 정보 ({data['date']})
    기온 : {data['weather']['tmp']}
    기우  : {data['weather']['state']}
    미세먼지 : {data['dust']['pm10']['value']} {data['dust']['pm10']['state']}
    '''

    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    wea = {'web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨', 'mobile_web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'}
    dat = {'template_object' : json.dumps({'object_type': 'text', 'text': text, 'link': wea, 'button_title': '날씨 상세보기'})}
    
    req = requests.post(url = url, data = dat, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json()
    if req.get('result_code') == 0: a += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req))

    contents = []

    for place in res: 
        title = place.get('title').replace('<b>','').replace('</b>','')
        if place.get('telephone'): title = place.get('title').replace('<b>','').replace('</b>',''), '\ntel) ', place.get('telephone')

        urlliB = 'https://search.naver.com/search.naver?query=' + urllib.parse.quote(place.get('address') + '' + title)
        
        contents.append({'title': '[' + place.get('category') + '] ' + title, 'description': ''.join(place.get('address').split()[1:]), 'image_url': 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill', 'image_width': 50, 'image_height': 50, 'link': {'web_url': urlliB, 'mobile_web_url': urlliB}})
    
    dat = {'template_object' : json.dumps({'object_type' : 'list', 'header_title' : '현재 날씨에 따른 음식 추천', 'header_link' : wea, 'contents' : contents, 'buttons' : [{'title' : '날씨 상세보기', 'link' : wea}]})}
    req = requests.post(url = url, data = dat, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json()
    if req.get('result_code') == 0: a += 1
    else: print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(req))
    
    return a