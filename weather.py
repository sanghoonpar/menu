import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(crd, key):
    d = dict()
    d_t = datetime.now().date().strftime("%Y%m%d")
    d["date"] = str(d_t[:4] + "/" + d_t[4:6] + "/" + d_t[6:])
    w_d = dict()
    for m in requests.get("http://apis.d.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst", {"serviceKey": key, "dType": "json", "base_date": d_t, "base_time": "0800", "nx": crd[0], "ny": crd[1]}).json().get("response").get("body").get("items")["item"]:
        i = m["fcstValue"]
        if m["category"] == "TMP": w_d["tmp"] = i

        elif m["category"] == "PTY":
            if i == "1": w_s = "비"
            elif i == "2": w_s = "비/눈"
            elif i == "3": w_s = "눈"
            elif i == "4": w_s = "소나기"
            else: w_s = "없음"

            w_d["code"] = i
            w_d["state"] = w_s
    d["weather"] = w_d
    return d