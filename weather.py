import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def weather(coordinate, key):
    data = dict()
    date_time = datetime.now().date().strftime("%Y%m%d")
    data["date"] = str(date_time[:4] + "/" + date_time[4:6] + "/" + date_time[6:])
    weather_data = dict()
    for m in requests.get("http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst", 
                          {"serviceKey": key, 
                           "dataType": "json", 
                           "base_date": date_time, 
                           "base_time": "0800", 
                           "nx": coordinate[0], 
                           "ny": coordinate[1]}).json().get("response").get("body").get("items")["item"]:
        i = m["fcstValue"]
        if m["category"] == "TMP": weather_data["tmp"] = i

        elif m["category"] == "PTY":
            if i == "1": weather_state = "비"
            elif i == "2": weather_state = "비/눈"
            elif i == "3": weather_state = "눈"
            elif i == "4": weather_state = "소나기"
            else: weather_state = "없음"

            weather_data["code"] = '1'
            weather_data["state"] = '비'
    data["weather"] = weather_data
    return data