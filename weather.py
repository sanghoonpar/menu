import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(crd, key):
    dt = dict()
    d_t = datetime.now().date().strftime("%Y%m%d")
    dt["date"] = str(d_t[:4] + "/" + d_t[4:6] + "/" + d_t[6:])
    w_d = dict()
    for m in requests.get("http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst", 
                          {"serviceKey": key, 
                           "dataType": "json", 
                           "base_date": d_t, 
                           "base_time": "0800", 
                           "nx": crd[0], 
                           "ny": crd[1]}).json().get("response").get("body").get("items")["item"]:
        i = m["fcstValue"]
        if m["category"] == "TMP": w_d["tmp"] = i

        elif m["category"] == "PTY":
            if i == "1": weather_state = "비"
            elif i == "2": weather_state = "비/눈"
            elif i == "3": weather_state = "눈"
            elif i == "4": weather_state = "소나기"
            else: weather_state = "없음"

            w_d["code"] = i
            w_d["state"] = weather_state
    dt["weather"] = w_d
    return dt