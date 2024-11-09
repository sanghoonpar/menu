from weather import weather
from dust_weather import dust_weather
from kakao_send import kakao_send
from geopy import geocoders
from naver_search import search_restaurant
from dotenv import load_dotenv
import requests
load_dotenv()

def get_access_token(code, client_id, redirect_uri): 
    return requests.post("https://kauth.kakao.com/oauth/token", 
                         data = {"grant_type": "authorization_code", 
                                 "client_id": client_id, 
                                 "redirect_uri": redirect_uri, 
                                 "code": code}).json().get("access_token")

def get_address(coordinate): 
    return list(reversed(str(geocoders.Nominatim(user_agent = "South Korea", 
                                                 timeout = None).reverse(coordinate)).split(", ")))[4]

def run_service(address, access_token, food, data): 
    return kakao_send(access_token, address, search_restaurant(address, food), data)

def select_menu(coordinate, key1, key2): 
    return dust_weather(weather(coordinate, key1), key2)