import os, requests
from dotenv import load_dotenv 
load_dotenv()

def s_r(l, f):
    r = []
    while len(r) <= 1:
        q = requests.get("https://openapi.naver.com/v1/search/local.json", headers = {"X-Naver-Client-Id": os.environ.get('n_cli_id'), "X-Naver-Client-Secret": os.environ.get('n_cli_secret')}, params = {"query": f"{l} {f} 맛집", "display": 10, "start": 1}).json().get('items')
        if len(q) >= 2:
            r.append(q[0])
            r.append(q[1])
    for i in range(len(r) - 1):
        if r[0] == r[1]: r.remove(r[0])
    
    return r