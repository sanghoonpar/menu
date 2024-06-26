import xml.etree.ElementTree as elemTree, requests

def dust_weather(data, key):

    dust_data = dict()
    dust_data['pm10'] = {'value' : float(elemTree.fromstring(requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=xml&serviceKey=%s&ver=1.0'%(key) + 'serviceKey=' + key + '&dataType=json&dataGubun=HOUR&searchCondition=WEEK&itemCode=PM10').text).find('body').find('items').find('item').findtext('pm10Value'))}
    data_d = dust_data.get('pm10').get('value')
    if data_d <= 30: pm10_state = '좋음'
    elif data_d <= 80: pm10_state = '보통'
    elif data_d <= 150: pm10_state = '나쁨'
    else: pm10_state = '매우나쁨'

    if data_d > 60: dust_code = '1'
    else: dust_code = '0'

    dust_data.get('pm10')['state'] = pm10_state
    dust_data['code'] = dust_code
    data['dust'] = dust_data
    
    return data