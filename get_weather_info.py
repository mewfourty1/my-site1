import requests
from pprint import pprint

from get_time import get_base
def get_info():
    url="http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    service_key="/RiLDbQOrX1DYkcfCT5/LyQYEKJ3G4If9ktXL8/B8o3aCQfi/S6D0g+OFjWQD+dZa2ru1Iwbasb9TV+IlJU0wA=="
    base_date,base_time = get_base()
    params ={'serviceKey' : service_key,
             'pageNo' : '1',
             'numOfRows' : '1000',
             'dataType' : 'JSON',
             'base_date' : base_date,
             'base_time' : base_time,
             'nx' : '89',
             'ny' : '90' }

    res= requests.get(url=url,params=params)

    res=res.json()
    _data = []
    data = res['response']['body']['items']['item']
    for d in data:
        _data.append((d['category'],d['obsrValue']))
    _data=_data[:4]
    code = {'PTY':'rain','REH':'humidity','RN1':'rainHour','T1H':'temperature'}
    rain_info = ['없음','비','비/눈','눈','','빗방울','빗방울눈날림','눈날림']


    weather_info = {}

    for c,v in _data:
        if c=='PTY':
            v=int(v)
            v=rain_info[int(v)]
        else:
            v=float(v)
        weather_info[code[c]] = v
    return weather_info

if __name__ =="__main__":
    info = get_info()
    print(info)