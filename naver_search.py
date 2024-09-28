import os, requests
from dotenv import load_dotenv 
load_dotenv()

<<<<<<< HEAD
r = []
def s_r(l, f):
    q = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ l + ' ' + f + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')
    r.append(q[0])
    r.append(q[1])
    for i in range(len(r) - 1):
        if r[0] == r[1]: r.remove(r[0])
    if len(r) >= 3:
        if r[0] == r[2]: r.remove(r[0])
    if len(r) >= 3:
        if r[1] == r[2]: r.remove(r[1])
    return r
=======
res = []
def s_r(loc, listf):
    req = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ loc + ' ' + listf + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')
    res.append(req[0])
    res.append(req[1])
    # for food in listf:
    #     req = requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ loc + ' ' + food + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')

    #     if not req: print('검색 실패', food)

    #     else:
    #         res.append(req[0])

    #         if len(res) >= 3: break

    for i in range(len(res) - 1):
        if res[0] == res[1]: res.remove(res[0])
    if len(res) >= 3:
        if res[0] == res[2]: res.remove(res[0])
    if len(res) >= 3:
        if res[1] == res[2]: res.remove(res[1])
    return res
>>>>>>> origin/main
