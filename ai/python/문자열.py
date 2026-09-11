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

#%%
# 대소문자 바꾸기 : upper()와 lower()
a = 'Hello Python Program..'
print(a.upper())
print(a.lower())

# isupper(), islower()
# 입력 받은 문자열에서 소문자는 대문자로 대문자는 소문자로 변경

text = input('문자열을 입력하세요 : ')

for i in range(len(text)):
    if text[i].isupper():
        print(text[i].lower(), end='')
    elif text[i].islower():
        print(text[i].upper(), end='')
    else:
        print(text[i], end='')

#%%
# 문자열 변경 : replace("", "")
input_str = 'Hello Python Program'
new_str = input_str.replace('Python', 'JavaScript')
print(new_str)

#%%
# 문자 갯수 세기 : count()
text = 'Google kakao naver openAI oole'

print(text.count('oo'))

#%%
# 문자열 길이 : len()
text = 'Hello World'
print(len(text))

#%%
# 문자열 찾기 : find()와 rfind(), 그리고 index()
# find() : 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 -1을 반환합니다.
# index() : 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 ValueError 예외를 발생시킵니다.

phrase = ('가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서')

print(phrase.find('가장'))
print(phrase.rfind('가장')) # 뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index('포기'))

print(phrase.find('나에게')) # 찾는 결과 없으면 -1

new_phrase = phrase.replace('가장', '나에게')

print(new_phrase.index('나에게')) # 해당 단어가 없으므로 에러가 발생 합니다.

print(new_phrase)

#%%
# 문자열 양옆의 공백제거
# - strip() : 양쪽 공백 제거
# - lstrip() : 왼쪽 공백 제거
# - rstrip() : 오른쪽 공백 제거

input_a = '''
    안녕하세요.
문자열 함수를 알아 봅니다.
    
'''

print(input_a.strip())
