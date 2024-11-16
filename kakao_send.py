import urllib, json, requests

def kakao_send(a, b, c, d):

    e = 0
    dt = f"""\
    위치 정보 : {b}
    날씨 정보 ({d["date"]})
    기온 : {d["weather"]["tmp"]}
    기우  : {d["weather"]["state"]}
    미세먼지 : {d["dust"]["pm10"]["value"]} {d["dust"]["pm10"]["state"]}
    """
    def g_u(u): return {"web_url": u, "mobile_web_url": u}
    
    def req(): return requests.post(url = url, data = t, headers = {"Authorization": "Bearer " + {"access_token" : a}.get("access_token" ), "scope":"talk_message"}).json()
    
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    w_l = g_u("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨")
    t = {"template_object" : json.dumps({"object_type": "text", "text": dt, "link": w_l, "button_title": "날씨 상세보기"})}

    if req().get("result_code") == 0: e += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(req()))

    contents = []
    r_l = []

    for r in c:
        r_t = r.get("title").replace("<b>", "").replace("</b>", "")
        r_l.append(r_t)
        if r.get("telephone"): r_t = r_t, "\ntel) ", r.get("telephone")
        contents.append({"title": "[" + r.get("category") + "] " + r_t, 
            "description": "".join(r.get("address").split()[1:]), 
            "image_url": "https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill", 
            "image_width": 50, "image_height": 50, 
            "link": g_u("https://search.naver.com/search.naver?query=" + urllib.parse.quote(r.get("address") + "" + r_t))})

    t = {"template_object" : json.dumps({"object_type" : "list", "header_title" : "현재 날씨에 따른 음식 추천", "header_link" : w_l, "contents" : contents, "buttons" : [{"title" : "날씨 상세보기", "link" : w_l}]})}
    if req().get("result_code") == 0: e += 1
    else: print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ", str(req()))

    return [e, r_l, d["weather"]["state"], d["dust"]["pm10"]["value"], d["weather"]["tmp"]]