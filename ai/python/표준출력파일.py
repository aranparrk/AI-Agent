# 정수 출력
print('=======[정수 출력]=======')
print(30)
age = 23
print('나이 : ' + str(age))
print(f'나이 : {age}') # f-string 방식으로 출력
print('나이 :',age)

# 실수 출력
print('=======[실수 출력]=======')
avg = 76.6667
print(f'성적 : {avg:.2f}')

# 문자열 출력
print('=======[문자열 출력]=======')
name = '곰돌이사육사'
print('이름 : ' + name)
print(f'이름 : {name}')

# 리스트 출력 : 파이썬은 기본적으로 배열이 없고 리스트로 연속된 데이터를 관리함
print('=======[리스트 출력]=======')
score = [99, 88, 77]
print(f'성적 : {score[0]}')

# 여러 줄 출력
print('=======[여러줄 출력]=======')
print(
    '''
동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리 나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전 하세
    '''
)

# 줄 바꿈 문자 확인
print('=======[줄바꿈 출력]=======')
print('동해물과 백두산이 마르고 닳도록 하느님이\n\n\n\n')
print('보우하사 우리나라 만세')

# \t \"
print('=======[탭 출력]=======')
print('apple\tbanana\tgrape')

# 제어문자, escape sequence : \n, \t, \r, \\, \b
print('=======[제어문자 출력]=======')
print('동해물과\t백두산이\n마르고 닳도록\b 하느님이\n\n\n\n')
print('보우하사 \n우리나라 \\만세')

print('안녕하세요. "장원영"님 환영합니다.')

print("안녕하세요. \"장원영\"님 환영합니다.")

print("딸기\r바나나\r키위")



# import sys
# import time
#
# total_time = 100  # 총 실행 시간 100ms
# steps = 100
# sleep_time = total_time / steps  # 한 단계당 대기 시간
#
# for i in range(1, steps + 1):
#     print(f"\r진행률 : {i}% 입니다.", end="", flush=True)  # end=""로 줄바꿈 방지, flush=True로 즉시 출력
#     time.sleep(sleep_time)
#
# print()  # 최종 줄 바꿈

print('파이썬')
print('파' + '이' + '썬')
print('파''이''썬')
print('파','이','썬', sep='')

# end : 문자열을 출력하고 난 다음의 동작, 기본값이 줄바꿈 (\n)
# sep : 문자열 사이에서 콤마를 만나면 동작, 기본값이 스페이스
print('=============================')
print('life is shot', end=' & ')
print('you',  'need',  'python', sep = '\n')

# 정렬과 포맷지정
# < : 왼쪽 정렬
# > : 오른쪽 정렬
# ^ : 중앙 정렬
print('=========[정렬과 포맷지정]=========')
num1 = 10
num2 = 100
num3 = 1000

print(f'|{num1:^5}|')
print(f'|{num2:^5}|')
print(f'|{num3:^6}|')

# 소수점 이하 출력
print('========[소수점 이하 출력]========')
PI = 3.141592
print(f'{PI:.2f}')

# 다양한 출력 스타일
name = '박아란'
age = 23
gender = 'M'
job = '개발자'
addr = '충남 천안시'

# 파이썬 스타일, 가장 최근에 추가된 방식(f-string), 3.6 이후
# f와 {}로 사용합니다.
print('===== 파이썬 스타일 =====')
print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'성별 : {gender}')
print(f'직업 : {job}')
print(f'주소 : {addr}\n')

print('===== 자바 스타일 =====')
print('이름 : ' + name)
print('나이 : ' + str(age))
print('성별 : ' + gender)
print('직업 : ' + job)
print('주소 : ' + addr)

# 1. \n, \t 사용하여 아래와 같은 형태로 자기소개를 한 줄의 print() 문으로 출력하세요.
# 이름:   김민준
# 직업:   백엔드 개발자

print('===== 문제1 =====')
print('이름:\t김민준\n직업:\t백엔드 개발자')
print()

# 2. 따옴표 출력하기
# "오늘도 좋은 하루 되세요!"라고 인사했습니다.
print('===== 문제2 =====')
print('"오늘도 좋은 하루 되세요!"라고 인사했습니다.')
print()

# 3. \r 커서 이동 확인하기
# - 사과 바나나 키위를 연속 입력해서 키위만 나오도록 출력하기
print('===== 문제3 =====')
print('사과', '바나나', '\r키위')
print()

# 4. "010", "1234", "5678" 세 문자열을 sep="-" 옵션을 사용해서 아래와 같이 출력하세요.
# 010-1234-5678
print('===== 문제4 =====')
print('010', '1234', '5678', sep='-')
print()

# 5. 아래 세 개의 print()문을 각각 작성하되, end 옵션을 이용해 최종적으로 한 줄의 문장이 되도록 만드세요.
# 결과: 파이썬은 재밌있다.
print('===== 문제5 =====')
print('결과:', end=' ')
print('파이썬은', end=' ')
print('재미있다.')
print()

# 6. 두 가지 스타일로 자기소개 출력하기
# 이름(name), 나이(age), 직업(job) 변수를 출력
print('===== 문제6 =====')
name = '박아란'
age = 23
job = '학생'

print('-- 파이썬 스타일 --')
print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'직업 : {job}')

print('-- 자바 스타일 --')
print('이름 : ' + name)
print('나이 : ' + str(age))
print('직업 : ' + job)
print()

# 7. 정렬로 표 만들기
# num1 = 7, num2 = 42, num3 = 365 세 변수를 각각 너비 6칸으로 가운데 정렬(^) 하여 아래와 같이 출력하세요.
num1 = 7
num2 = 42
num3 = 365
print('===== 문제7 =====')
print(f'|{num1:^6}|')
print(f'|{num2:^6}|')
print(f'|{num3:^6}|')
print()

# 8. 원의 반지름 r = 5를 이용해 원의 넓이(3.14159 * r * r)를 구한 뒤, 폭 10칸, 오른쪽 정렬, 소숫점 둘째 자리까지 출력하세요.
# 넓이:        78.54
r = 5
pi = 3.14159
area = pi * r * r

print('===== 문제8 =====')
print(f'넓이 : {area:>10.2f}')

print()