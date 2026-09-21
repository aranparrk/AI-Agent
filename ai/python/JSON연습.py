# JSON(JavaScript Object Notation)은 데이터를 저장하고 교환하는 데 널리 사용되는 경략 텍스트 형식 입니다.
# - 파이썬은 json 기본 라이브러리를 통해 사용 가능
# - 경량 텍스트 포맷
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 API 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용

import json

# 파이썬 객체를 json으로 직렬화
# 회원 정보 (이름, 주소, 나이, 성별, 포지션, 전화번호 2개) => 딕셔너리
# 회원 정보가 10개인 리스트 => 리스트

members = [
    {
        'name': '안유진',
        'addr': '대전시',
        'age' : 23,
        'gender': '여성',
        'position': '리더',
        'phone': ['010-1234-1234', ['010-1234-5678']]
    },
    {
        'name': '장원영',
        'addr': '서울시',
        'age': 22,
        'gender': '여성',
        'position': '센터, 서브보컬, 서브래퍼',
        'phone': ['010-6666-7777', ['010-8888-9999']]
    },
    {
        'name': '최우식',
        'addr': '수원시',
        'age': 30,
        'gender': '남성',
        'position': '메인보컬',
        'phone': ['010-7878-7878', ['010-6464-6464']]
    },
    {
        'name': '전현무',
        'addr': '부산광역시',
        'age': 50,
        'gender': '남성',
        'position': '메인댄서',
        'phone': ['010-2222-1111', ['010-3535-4545']]
    },
    {
        'name': '정원이',
        'addr': '거제시',
        'age': 23,
        'gender': '여성',
        'position': '메인보컬',
        'phone': ['010-5555-6666', ['010-7777-7878']]
    }
]

# Python 객체를 JSON으로 직렬화
json_str =json.dumps(members, ensure_ascii=False, indent=4)
print(json_str)

# JSON을 -> Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print('-' * 50)

for e in obj:
    print(e)

print('-' * 50)

# 파일로 저장 하기
# with는 파일을 자동으로 닫아 줌
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(members, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)