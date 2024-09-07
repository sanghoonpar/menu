import xml.etree.ElementTree as elemTree, requests

def d_w(dt, ke):

    u_d = dict()
    u_d['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(ke) + 'serviceKey=' + ke + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}
    d_d = u_d.get('pm10').get('value')
    if d_d <= 30: p_s = '좋음'
    elif d_d <= 80: p_s = '보통'
    elif d_d <= 150: p_s = '나쁨'
    else: p_s = '매우나쁨'

    if d_d > 60: d_c = '1'
    else: d_c = '0'

    u_d.get('pm10')['state'] = p_s
    u_d['code'] = d_c
    dt['dust'] = u_d
    
    return dt