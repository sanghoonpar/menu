import os, requests
from dotenv import load_dotenv 
load_dotenv()

def search_restaurant(address, food):
    restaurants = []
    while len(restaurants) <= 1:
        request = requests.get("https://openapi.naver.com/v1/search/local.json", 
                         headers = {"X-Naver-Client-Id": os.environ.get("n_cli_id"), 
                                    "X-Naver-Client-Secret": os.environ.get("n_cli_secret")}, 
                                    params = {"query": f"{address} {food} 맛집", 
                                              "display": 10, "start": 1}).json().get("items")
        if len(request) >= 2:
            restaurants.append(request[0])
            restaurants.append(request[1])
    for i in range(len(restaurants) - 1):
        if restaurants[0] == restaurants[1]: restaurants.remove(restaurants[0])
    
    return restaurants