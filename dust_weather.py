import xml.etree.ElementTree as elemTree, requests

def dust_weather(data, key):
    dust_data = dict()
    dust_data["pm10"] = {"value" : float(elemTree.fromstring(requests.get("http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0"%(key) + "serviceKey=%s&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10"%{key}).text).find("body").find("items").find("item").findtext("pm10Value"))}
    dust_value = dust_data.get("pm10").get("value")
    if dust_value <= 30: pm10_state = "좋음"
    elif dust_value <= 80: pm10_state = "보통"
    elif dust_value <= 150: pm10_state = "나쁨"
    else: pm10_state = "매우나쁨"


    if dust_value > 60: code = "1"
    else: code = "0"

    dust_data.get("pm10")["state"] = pm10_state
    dust_data["code"] = code
    data["dust"] = dust_data
    
    return data