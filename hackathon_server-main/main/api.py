# 라이브러리 import
import requests
import json
import pandas as pd
from urllib.parse import urlencode, unquote, quote_plus

# **** 본인 공공데이터 포털의 서비스 키 받아서 추가하기 ****
serviceKey = ''
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_space():
    # data1 불러오기
    url = "http://apis.data.go.kr/6280000/ICParkInfo/ParkingOperInfo"
    returnType="xml"
    numOfRows="10000"
    pageNo="1"
    ver = "1.0"
    queryParams = '?' + urlencode({quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('ver') : ver})
    response = requests.get(url + queryParams, verify=False)
    contents = response.text
    json_file = json.loads(contents)
    body = json_file['response']['body']['items']
         
    # data1 데이터 전처리
    df = pd.json_normalize(body)        
    df[df['addrDetail'] == '주소없음'] # 주소 위치 없는 거 제거
    df.loc[20,'addrDetail'] = '인천광역시 중구 우현로 28'
    df.loc[22,'addrDetail'] = '인천광역시 중구 하늘중앙로195번길 14'
    df.loc[369,'addrDetail'] = '인천광역시 연수구 연수동 587-4'
    df['name'] = df['addr1'] + ' ' + df['addr2'] + ' ' + df['addr3'] + ' ' + df['name'] 
    df['name'] = [i.replace('-', '') for i in df['name']]
    df.drop(columns = {'divCode', 'typeCode', 'landCode', 'addr1', 'addr2', 'addr3', 'addr4', 'addr5', 'addr6', 'zipcode'}, inplace = True)
    df['parkID'] = df['parkID'].astype('int')
    df['longitude'] = df['longitude'].astype('float')
    df['latitude'] = df['latitude'].astype('float')
    df['totalLots'] = df['totalLots'].astype('int')

    # data2 불러오기
    url1 = "http://apis.data.go.kr/6280000/ICParkInfo/ParkingCurrentInfo"
    returnType1="xml"
    numOfRows1="100"
    pageNo1="1"
    ver = "1.0"
    queryParams1 = '?' + urlencode({quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows1, quote_plus('pageNo') : pageNo1, quote_plus('ver') : ver})
    response1 = requests.get(url1 + queryParams1, verify=False)
    contents1 = response1.text
    json_file1 = json.loads(contents1)
    body1 = json_file1['response']['body']['items']

    # data2 데이터 전처리 
    df1 = pd.json_normalize(body1) 
    df1['parkID'] = df1['parkID'].astype('int')
    df1['totalSpace'] = df1['totalSpace'].astype('int')
    df1['remainingSpace'] = df1['remainingSpace'].astype('int')

    # data1, data2 병합
    df_tt = pd.merge(df, df1, on = 'parkID')
    df_tt.drop(columns = 'totalSpace', axis = 1, inplace = True)
    df_tt.rename(columns = {'longitude': 'lng', 'latitude':'lat', 'remainingSpace':'remain'}, inplace = True)

    # json으로 정리
    name = df_tt['name'].values.tolist()
    addrDetail = df_tt['addrDetail'].values.tolist()
    lng = df_tt['lng'].values.tolist()
    lat = df_tt['lat'].values.tolist()
    totalLots = df_tt['totalLots'].values.tolist()
    updateTime = df_tt['updateTime'].values.tolist()
    remain = df_tt['remain'].values.tolist()
    
    # dict 타입으로 변환
    data={}
    for a,b,c,d,e,f,g in zip(name,addrDetail, lng, lat, totalLots, updateTime, remain):
        b = b.replace("광역시 ", " ")

        data[a] = {"name": b, "lng": c, "lat": d, 'totalLots': e, 'updateTime':f, 'remain': g}
    return data