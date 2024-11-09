import urllib, json, requests

def kakao_send(access_token, address, restaurants, data):

    result = 0
    datas = f"""\
    위치 정보 : {address}
    날씨 정보 ({data["date"]})
    기온 : {data["weather"]["tmp"]}
    기우  : {data["weather"]["state"]}
    미세먼지 : {data["dust"]["pm10"]["value"]} {data["dust"]["pm10"]["state"]}
    """
    def gather_url(url): return {"web_url": url, 
                      "mobile_web_url": url}
    
    def request(): return requests.post(url = url, 
                                  data = template, 
                                  headers = {"Authorization": "Bearer " + {"access_token" : access_token}.get("access_token" ), 
                                             "scope":"talk_message"}).json()
    
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    weather_link = gather_url("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨")
    template = {"template_object" : json.dumps({"object_type": "text", 
                                         "text": datas, 
                                         "link": weather_link, 
                                         "button_title": "날씨 상세보기"})}

    if request().get("result_code") == 0: result += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(request()))

    contents = []
    restaurants_list = []

    for restaurant in restaurants:
        restaurant_title = restaurant.get("title").replace("<b>", "").replace("<b>", "")
        restaurants_list.append(restaurant_title)
        if restaurant.get("telephone"): restaurant_title = restaurant_title, "\ntel) ", restaurant.get("telephone")
        contents.append({"title": "[" + restaurant.get("category") + "] " + restaurant_title, 
                  "description": "".join(restaurant.get("address").split()[1:]), 
                  "image_url": "https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill", 
                  "image_width": 50, "image_height": 50, 
                  "link": gather_url("https://search.naver.com/search.naver?query=" + urllib.parse.quote(restaurant.get("address") + "" + restaurant_title))})

    template = {"template_object" : json.dumps({"object_type" : "list", 
                                         "header_title" : "현재 날씨에 따른 음식 추천", 
                                         "header_link" : weather_link, 
                                         "contents" : contents, 
                                         "buttons" : [{"title" : "날씨 상세보기", 
                                                       "link" : weather_link}]})}
    if request().get("result_code") == 0: result += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(request()))

    return [result, restaurants_list, data["weather"]["state"], data["dust"]["pm10"]["value"], data["weather"]["tmp"]]