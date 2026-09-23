### 🧪 실습 문제: JSON 직렬화/역직렬화 — 도서 관리 프로그램

#### 📌 학습 목표
# - Python 객체(dict, list)를 JSON으로 직렬화(`json.dumps`, `json.dump`)할 수 있다.
# - JSON 문자열/파일을 Python 객체로 역직렬화(`json.loads`, `json.load`)할 수 있다.
# - `ensure_ascii`, `indent` 옵션의 역할을 이해한다.
# - 파일 입출력(`with open`)과 JSON 모듈을 함께 활용할 수 있다.

#### 📖 문제 설명

# 아래 조건에 맞는 **도서 관리 프로그램**을 작성하세요.

#### ✅ 요구사항

import json

# **1단계. 데이터 구성**

# - 도서 정보를 담는 딕셔너리를 최소 5개 만들어 리스트로 구성하세요.
# - 각 도서는 다음 필드를 포함해야 합니다.
#    - `title` (문자열)
#    - `author` (문자열)
#    - `publisher` (문자열)
#    - `year` (정수)
#    - `price` (정수)
#    - `genre` (문자열 2개로 구성된 리스트)

books = [
    {
        'title': '파이썬 기초',
        'author': '김개발',
        'publisher': '코딩출판사',
        'year': 2024,
        'price': 25000,
        'genre': ['프로그래밍', '교육']
    },
    {
        'title': '데이터베이스 입문',
        'author': '이데이터',
        'publisher': '한빛미디어',
        'year': 2023,
        'price': 28000,
        'genre': ['데이터베이스', '교육']
    },
    {
        'title': '웹 개발의 시작',
        'author': '박프론트',
        'publisher': '개발서적',
        'year': 2025,
        'price': 32000,
        'genre': ['웹 개발', '프로그래밍']
    },
    {
        'title': '인공지능과 미래',
        'author': '최인공',
        'publisher': '미래출판사',
        'year': 2022,
        'price': 30000,
        'genre': ['인공지능', '과학']
    },
    {
        'title': '알고리즘 문제 해결',
        'author': '정알고',
        'publisher': '코딩북스',
        'year': 2024,
        'price': 35000,
        'genre': ['알고리즘', '프로그래밍']
    }
]

# **2단계. 직렬화**

# - 위 리스트를 `json.dumps()`를 사용해 JSON 문자열로 변환하고 출력하세요.
# - 한글이 깨지지 않도록 옵션을 설정하고, 보기 좋게 들여쓰기 하세요.

json_date = json.dumps(books, ensure_ascii=False, indent=4)

# **3단계. 역직렬화**

# - 2단계에서 만든 JSON 문자열을 다시 Python 객체로 변환하세요.
# - `for`문을 사용해 각 도서 정보를 한 줄씩 출력하세요.

obj = json.loads(json_date)

for e in obj:
    print(e)

print('-' * 50)

# **4단계. 데이터 가공 (응용)**

# - 역직렬화한 데이터에서 **가격이 30,000원 이상인 책만** 필터링하세요.
# - 필터링한 결과를 `"제목 - 가격원"` 형식으로 출력하세요. (예: `클린 코드 - 33,000원`)

for e in obj:
    if e['price'] >= 30000:
        print(f'{e["title"]} - {e["price"]}원')

print('-' * 50)

# **5단계. 파일 저장 및 읽기**

# - 전체 도서 리스트를 `books.json` 파일로 저장하세요.
# - 저장한 파일을 다시 읽어서 출력하세요.

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

with open('books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)

print('-' * 50)


# **6단계. 심화 (선택)**

# - `books.json`을 읽은 후, 사용자로부터 저자 이름을 입력받아 해당 저자의 책만 출력하는 기능을 추가하세요.

author = input('저자 이름을 입력하세요 : ')

for i in data:
    if i['author'] == author:
        print(f'{i['title']} - {i['author']}')