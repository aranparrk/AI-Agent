# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음 (전부 문자열)
# "", '', """ """, ''' '''
from 기본 import gender
from 연산자 import birthyear

#%%
# 인덱싱과 슬라이싱
# 인덱싱은 인덱스로 원하는 값을 추출
text = '안녕하세요. 파이썬 입니다.'
word = '파이썬'

for i in range(len(text)):
    if text[i:i + len(word)] == word:
        print(i)

print(text[0])
print(text[7])
print(text[13])

#%% 슬라이싱
print(text[7:11])
print(text[::-1]) # 처음에서 마지막까지 역순으로 출력
print(text[:5])

#%%
# 주민등록번호를 입력 : 010222-3164414
# 생년월일 : 2001년 2월 22일
# 성별 : 남성
# 나이 :25살
from datetime import datetime
current_year = datetime.now().year

resident_registration_number = input('주민번호를 입력하세요 : ')
birth_year = ''
gender = resident_registration_number[7]

# 생년월일
year = resident_registration_number[0:2]
month = resident_registration_number[2:4]
day = resident_registration_number[4:6]

if gender == 1 or gender == 2:
    birth_year = '19' + year
elif gender == 3 or gender == 4:
    birth_year = '20' + year

# 성별
if gender == '1' or gender == '3':
    gender_type = '남자'
elif gender == '2' or gender == '4':
    gender_type = '여자'

# 나이
age = current_year - int(birth_year)

# 최종 결과
print(f'생년월일 : {birth_year}년 {month}월 {day}일')
print(f'성별 : {gender_type}')
print(f'나이 : {age}')
