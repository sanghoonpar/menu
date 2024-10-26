from weather import wea
from dust_weather import d_w
from kakao_send import send
from geopy import geocoders
from naver_search import s_r
from dotenv import load_dotenv
import requests
load_dotenv()

def g_t(c, c_i, r_u): return requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': c_i, 'redirect_uri': r_u, 'code': c}).json().get('access_token')

def g_a(crd): return str(geocoders.Nominatim(user_agent = 'South Korea', timeout = None).reverse(crd)).split(', ')[3]

def s_c(l, t, f, w): return send(t, l, s_r(l, f), w)

def weat(c, k1, k2): return d_w(wea(c, k1), k2)