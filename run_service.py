from menu_choose import menu_choose 
from weather import weather
from dust_weather import dust_weather
from kakao_send import send
from geopy import geocoders
from naver_search import search_res
import requests

def serve_code(location, token, crd):
    
    d = dust_weather(weather(crd)[0], weather(crd)[1])
    return send(token, location, search_res(location, menu_choose(d)), d)

def get_token(code, client_id, redirect_uri): return requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'code': code}).json().get('access_token')

def get_address(lat_lng):
    
    for i in range(len(str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', '))):
        a = str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', ')[i]
        if '동' in a: return a