import urllib, json, requests

def send(a, b, c, d):

    e = 0
    f = f"""\
    위치 정보 : {b}
    날씨 정보 ({d["date"]})
    기온 : {d["weather"]["tmp"]}
    기우  : {d["weather"]["state"]}
    미세먼지 : {d["dust"]["pm10"]["value"]} {d["dust"]["pm10"]["state"]}
    """
    def n(g): return {"web_url": g, "mobile_web_url": g}
    def o(): return requests.post(url = g, 
                                  data = i, 
                                  headers = {"Authorization": "Bearer " + {"access_token" : a}.get("access_token" ), 
                                             "scope":"talk_message"}).json()
    g = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    h = n("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨")
    i = {"template_object" : json.dumps({"object_type": "text", 
                                         "text": f, 
                                         "link": h, 
                                         "button_title": "날씨 상세보기"})}

    if o().get("result_code") == 0: e += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(o()))

    j = []
    k = []

    for l in c:
        m = l.get("title").replace("<b> ", "").replace("<b> ", "")
        k.append(m)
        if l.get("telephone"): m = m, "\ntel) ", l.get("telephone")
        j.append({"title": "[" + l.get("category") + "] " + m, 
                  "description": "".join(l.get("address").split()[1:]), 
                  "image_url": "https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill", 
                  "image_width": 50, "image_height": 50, 
                  "link": n("https://search.naver.com/search.naver?query=" + urllib.parse.quote(l.get("address") + "" + m))})

    i = {"template_object" : json.dumps({"object_type" : "list", 
                                         "header_title" : "현재 날씨에 따른 음식 추천", 
                                         "header_link" : h, 
                                         "contents" : j, 
                                         "buttons" : [{"title" : "날씨 상세보기", 
                                                       "link" : h}]})}
    if o().get("result_code") == 0: e += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(o()))

    return [e, k, d["weather"]["state"], d["dust"]["pm10"]["value"], d["weather"]["tmp"]]