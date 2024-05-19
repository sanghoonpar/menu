# -*- coding: utf-8 -*-
import urllib, json, requests

def send(token, location, res, data):
    a = 0
    print(data)
    #날씨 정보 만들기 
    text = f'''\
    위치 정보 : {location}
    날씨 정보 ({data['date']})
    기온 : {data['weather']['tmp']}
    기우  : {data['weather']['state']}
    미세먼지 : {data['dust']['pm10']['value']} {data['dust']['pm10']['state']}
    '''

    #카카오톡 보내기
    
    if requests.post(url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send', data = {'template_object' : json.dumps({'object_type': 'text', 'text': text, 'link': {'web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨', 'mobile_web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'}, 'button_title': '날씨 상세보기'})}, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json().get('result_code') == 0:
        a += 1
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', 
              str(requests.post(url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send', data = {'template_object' : json.dumps({'object_type': 'text', 'text': text, 'link': {'web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨', 'mobile_web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'}, 'button_title': '날씨 상세보기'})}, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json()))

    #리스트 템플릿 형식 만들기
    contents = []
    template = {'object_type' : 'list', 'header_title' : '현재 날씨에 따른 음식 추천', 'header_link' : {'web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨', 'mobile_web_url' : 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'}, 'contents' : contents, 'buttons' : [{'title' : '날씨 정보 상세보기', 'link' : {'web_url': 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨', 'mobile_web_url' : 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'}}]}

    #contents 만들기
    for place in res:
        title = place.get('title').replace('<b>','').replace('</b>','')

    #전화번호가 있다면 제목과 함께 넣어줍니다.
        if place.get('telephone'):
            title = place.get('title').replace('<b>','').replace('</b>',''), '\ntel) ', place.get('telephone')

    #카카오톡 리스트 템플릿 형식에 맞춰줍니다.
        contents.append({'title': '[' + place.get('category') + '] ' + title, 'description': ''.join(place.get('address').split()[1:]), 'image_url': 'https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill', 'image_width': 50, 'image_height': 50, 'link': {'web_url': 'https://search.naver.com/search.naver?query=' + urllib.parse.quote(place.get('address') + '' + place.get('title').replace('<b>','').replace('</b>','')), 'mobile_web_url': 'https://search.naver.com/search.naver?query=' + urllib.parse.quote(place.get('address') + '' + place.get('title').replace('<b>','').replace('</b>',''))}})

    # 카카오톡 보내기
    if requests.post(url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send', data = {'template_object' : json.dumps(template)}, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json().get('result_code') == 0:
        a += 1
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ', str(requests.post(url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send', data = {'template_object' : json.dumps(template)}, headers = {'Authorization': 'Bearer ' + {'access_token' : token}.get('access_token'), 'scope':'talk_message'}).json()))
    return a