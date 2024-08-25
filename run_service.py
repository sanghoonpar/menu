from menu_choose import m_c
from weather import weather
from dust_weather import d_w
from kakao_send import send
from geopy import geocoders
from naver_search import search_res
from dotenv import load_dotenv
import requests, os
load_dotenv()
ke =  os.environ.get('ser_key')
def serve_code(location, token, crd, ke): 
    data = d_w(weather(crd, ke), ke)
    return send(token, location, search_res(location, m_c(data)), data)

def g_t(code, client_id, redirect_uri): return requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'code': code}).json().get('access_token')

def g_a(lat_lng):
    
    for i in range(len(str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', '))):
        address = str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', ')[i]
        if '동' in address: return address

def serve_code1(location, token, food, crd): return send(token, location, search_res(location, food), d_w(weather(crd)[0], weather(crd)[1]))