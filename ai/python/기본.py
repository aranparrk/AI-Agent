star = '='

# 기본적인 출력 구문, 줄이 끝날 때 ;(세미콜론)이 없음
print("안녕하세요. 파이썬 입니다.")

print(star * 50)

# 문자와 문자열을 구분하지 않음, "", '' 모두 문자열로 간주 함
print('안녕하세요. 파이썬 입니다.')

print(star * 50)
print(100 + 200)
print("100" + "200")

name = "곰돌이"
age = 23
addr = "충남 천안시"
print(star * 50)

print('당신의 이름은 ' + name)
# 출력 구간에서 정수를 문자열로 변경해서 출력
print('나이는 ' + str(age) + '이고 주소는' + addr + '입니다')
print(star * 50)

print(f'{name}은 {age}살 이고 {addr}에서 삽니다.')
print(star * 50)

# 변수 사용하기
# - 값을 저장하기 위해 메모리 공간을 확보하는 것
# - 파이썬은 상수가 없음
# - 동적 타입의 언어이므로 변수만 따로 선언 불가
# 변수를 포함한 식별자(변수, 함수, 클래스 등) 작성 규칙
# - 예약어 사용 불가
# - 특수문자 _(언더바)만 가능
# - 숫자는 사용할 수 있으나, 숫자로 시작할 수 없음
# - 공백 불가
# - 네이밍 규칙은 snake case 사용
tax_rate = 0.10
member_info = '회원정보'

# 성별과 직업 출력해보기
gender = '여자'
job = '삐에로'

print(f'안녕하세요. 제 이름은 {name}이고, 성별은 {gender}입니다. 직업은 {job}입니다. 잘 부탁드립니다.')
print(star * 50)

# 이름, 전화번호, 주소, 성별, 나이, 국어, 영어, 수학 성적을 대입받기
name = '아란'
phone_number = '010-1234-1234'
addr = '경기도 수원시'
gender = '여자'
age = 33
korean = 100
english = 60
math = 80

print(f'이름 : {name}')
print(f'전화번호 : {phone_number}')
print(f'주소 : {addr}')
print(f'성별 : {gender}')
print(f'나이 : {age}')
print(f'국어 : {korean}')
print(f'영어 : {english}')
print(f'수학 : {math}')
print(star * 50)

# 이름, 전화번호, 주소, 성별, 나이, 총점, 평균을 출력 하기
print(f'이름 : {name}')
print(f'전화번호 : {phone_number}')
print(f'주소 : {addr}')
print(f'성별 : {gender}')
print(f'나이 : {age}')
total_score = korean + english +math
average_score = total_score / 3
print(f'총점 : {total_score}')
print(f'평균 : {average_score}')

# 한 줄 주석

'''
범위 주석
'''

print(star * 50)
age = 18

if age > 18:
    print('성인입니다.')
else:
    print('미성년자 입니다.')