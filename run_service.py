from weather import wea
from dust_weather import d_w
from kakao_send import send
from geopy import geocoders
from naver_search import s_r
from dotenv import load_dotenv
import requests
load_dotenv()

def g_t(code, client_id, redirect_uri): return requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': client_id, 'redirect_uri': redirect_uri, 'code': code}).json().get('access_token')

def g_a(lat_lng):
    
    for i in range(len(str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', '))):
        address = str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(lat_lng)).split(', ')[i]
        if '동' in address: return address

def s_c(location, token, food, wea): 
    return send(token, location, s_r(location, food), wea)

def weat(crd, ke): return d_w(wea(crd, ke), ke)