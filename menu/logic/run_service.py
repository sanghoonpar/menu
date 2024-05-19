from data.menu_choose import menu_choose
from data.weather import weather
from data.dust_weather import dust_weather
from service.kakao_send import send
from geopy.geocoders import Nominatim
from service.naver_search import search_res
import requests

def serve_code(location, token, crd):
    return send(token, location, search_res(location, menu_choose(dust_weather(weather(crd)[0], weather(crd)[1]))), dust_weather(weather(crd)[0], weather(crd)[1]))

def get_token(code, client_id, redirect_uri):
    return requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'code': code}).json().get('access_token')

def get_address(lat_lng):
    for i in range(len(str(Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', '))):
        if '동' in str(Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', ')[i]:
            return str(Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', ')[i]