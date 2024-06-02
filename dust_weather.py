import xml.etree.ElementTree as elemTree, requests

def dust_weather(data, ser_key):

    dust_data = dict()
    dust_data['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(ser_key) + 'serviceKey=' + ser_key + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}

    if dust_data.get('pm10').get('value') <= 30: pm10_state = '좋음'
    elif dust_data.get('pm10').get('value') <= 80: pm10_state = '보통'
    elif dust_data.get('pm10').get('value') <= 150: pm10_state = '나쁨'
    else: pm10_state = '매우나쁨'

    if dust_data.get('pm10').get('value') > 60: dust_code = '1'
    else: dust_code = '0'

    dust_data.get('pm10')['state'] = pm10_state
    dust_data['code'] = dust_code
    data['dust'] = dust_data
    
    return data