import xml.etree.ElementTree as elemTree, requests

<<<<<<< HEAD
def d_w(t, k):

    u = dict()
    u['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(k) + 'serviceKey=' + k + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}
    d = u.get('pm10').get('value')
    if d <= 30: p = '좋음'
    elif d <= 80: p = '보통'
    elif d <= 150: p = '나쁨'
    else: p = '매우나쁨'
=======
<<<<<<< HEAD
def d_w(t, k):

    u = dict()
    u['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(k) + 'serviceKey=' + k + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}
    d = u.get('pm10').get('value')
    if d <= 30: p = '좋음'
    elif d <= 80: p = '보통'
    elif d <= 150: p = '나쁨'
    else: p = '매우나쁨'
=======
def d_w(dt, ke):

    u_d = dict()
    u_d['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(ke) + 'serviceKey=' + ke + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}
    d_d = u_d.get('pm10').get('value')
    if d_d <= 30: p_s = '좋음'
    elif d_d <= 80: p_s = '보통'
    elif d_d <= 150: p_s = '나쁨'
    else: p_s = '매우나쁨'
>>>>>>> origin/main
>>>>>>> 9981c73c5a82b5eba295c67f006e6e4fa3185d73

    if d > 60: c = '1'
    else: c = '0'

    u.get('pm10')['state'] = p
    u['code'] = c
    t['dust'] = u
    
    return t