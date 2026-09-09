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
