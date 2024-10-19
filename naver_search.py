import os, requests, random
from dotenv import load_dotenv 
load_dotenv()

r = []
def s_r(l, f):
    q = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ l + ' ' + f + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')
    if q != []:
        r.append(q[0])
        r.append(q[1])
    else: 
        f2 = random.sample('김치찌개, 짜장면, 삼겹살, 치킨, 국밥'.split(', '), 1)[0]
        q = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ l + ' ' + f2 + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')
        r.append(q[0])
        r.append(q[1])
    for i in range(len(r) - 1):
        if r[0] == r[1]: r.remove(r[0])
    if len(r) >= 3:
        if r[0] == r[2]: r.remove(r[0])
    if len(r) >= 3: 
        if r[1] == r[2]: r.remove(r[1])

    return r