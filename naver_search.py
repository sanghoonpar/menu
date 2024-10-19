import os, requests, random
from dotenv import load_dotenv 
load_dotenv()

r = []
def s_r(l, f):
    while len(r) <= 1:
        q = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ l + ' ' + f + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')
        print(q)
        if len(q) >= 2:
            r.append(q[0])
            r.append(q[1])
    for i in range(len(r) - 1):
        if r[0] == r[1]: r.remove(r[0])
    if len(r) >= 3:
        if r[0] == r[2]: r.remove(r[0])
    if len(r) >= 3: 
        if r[1] == r[2]: r.remove(r[1])

    return r