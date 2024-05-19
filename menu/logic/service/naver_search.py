import os, requests
from dotenv import load_dotenv 
load_dotenv()

res = []
def search_res(location, foods_list):
    for food in foods_list:

        if not requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ location + ' ' + food + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items'):
            print('검색 실패')

        if requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ location + ' ' + food + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items'):
            res.append(requests.get('https://openapi.naver.com/v1/search/local.json?', params = 'sort=comment&query='+ location + ' ' + food + ' 맛집&display=5', headers = {'X-Naver-Client-Id' : os.environ.get('n_cli_id'), 'X-Naver-Client-Secret' : os.environ.get('n_cli_secret')}).json().get('items')[0])
            
            if len(res) >= 3:
                break
        for i in range(len(res) - 1):
            if res[0] == res[1]:
                res.remove(res[0])

    return res