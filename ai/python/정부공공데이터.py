import requests # HTTP로 서버의 데이터를 수신하기 위해서 사용
import json     # 정부기관 공공데이터를 JSON형태로 수신 받기 위함
import datetime # 시간 정보를 구하기 위해서
import os
from dotenv import load_dotenv

# .env 파일 불러오기
load_dotenv()

API_KEY = os.getenv('API_KEY')

if API_KEY is None:
    raise ValueError('.env 파일에서 API_KEY를 찾지 못했습니다.')

# 요청 주소의 URL 지정
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 날짜 및 시간 설정
now = datetime.datetime.now()

# 년월일 정보를 추출하기 위해서 포맷 형식을 지정, base_date : 20240121
date = now.strftime("%Y%m%d")

# 시간 정보를 추출하기 위해서 포맷 형식을 지정, base_time : 0622
if now.minute < 30:
    now = now - datetime.timedelta(minutes=30)
    time = now.strftime("%H%M")
else:
    time = now.strftime("%H%M")

# 예보 지점 좌표 (서울 강남구 역삼동)
nx_val = 62
ny_val = 126

# 한 페이지에 포함된 결과수
num_of_rows = 6
# 페이지 번호
page_no = 1
# 응답 데이터 형식 지정
data_type = 'JSON'

req_parameter = {'serviceKey' : API_KEY,
                 'pageNo': page_no,
                 'numOfRows': num_of_rows,
                 'dataType' : data_type,
                 'base_date' : date,
                 'base_time' : time,
                 'nx' : nx_val,
                 'ny' : ny_val
}

# 요청 및 응답 : 서버로 부터 데이터를 수신 받기 때문에 예외 처리가 필요
response = ''
try:
    response = requests.get(url, params=req_parameter)
except requests.exceptions.RequestException as e:
    print(f'날짜 정보 가져 오기 오류 : {e}')

# JSON 형태로 응답받은 데이터를 딕셔너리로 변환 (역직렬화)
dict_date = response.json()
print(json.dumps(dict_date, indent=2))

# 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
weather_items = dict_date['response']['body']['items']['item']

for weather_item in weather_items:
    obsrValue = weather_item['obsrValue']
    category = weather_item['category']

    if category == 'T1H':
        print(f'[현재 기온 : {obsrValue}도]')
    elif category == 'REH':
        print(f'[현재 습도 : {obsrValue}퍼]')
    elif category == 'RN1':
        print(f'[1시간 강수량 : {obsrValue}mm]')