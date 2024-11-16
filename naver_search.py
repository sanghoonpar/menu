import os, requests
from dotenv import load_dotenv 
load_dotenv()

def search_restaurant(add, f):
    res = []
    while len(res) <= 1:
        req = requests.get("https://openapi.naver.com/v1/search/local.json", headers = {"X-Naver-Client-Id": os.environ.get("n_cli_id"), "X-Naver-Client-Secret": os.environ.get("n_cli_secret")}, params = {"query": f"{add} {f} 맛집", "display": 10, "start": 1}).json().get("items")
        if len(req) >= 2:
            res.append(req[0])
            res.append(req[1])
    for i in range(len(res) - 1):
        if res[0] == res[1]: res.remove(res[0])
    
    return res