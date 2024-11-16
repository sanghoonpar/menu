import xml.etree.ElementTree as elemTree, requests

def dust_weather(data, key):
    d_d = dict()
    d_d["pm10"] = {"value" : float(elemTree.fromstring(requests.get("http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0"%(key) + "serviceKey=%s&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10"%{key}).text).find("body").find("items").find("item").findtext("pm10Value"))}
    d_v = d_d.get("pm10").get("value")
    if d_v <= 30: p_s = "좋음"
    elif d_v <= 80: p_s = "보통"
    elif d_v <= 150: p_s = "나쁨"
    else: p_s = "매우나쁨"


    if d_v > 60: code = "1"
    else: code = "0"

    d_d.get("pm10")["state"] = p_s
    d_d["code"] = code
    data["dust"] = d_d
    
    return data