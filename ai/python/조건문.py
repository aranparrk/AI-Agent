# 제어문 : 프로그램의 흐름을 제어하는데 사용
# - 조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행 (if문, 3항연산자)
# - 반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행 (while문, for문)
from 표준입력 import avg_score

num = int(input('정수 입력 : '))

# 양수 / 음수 구분 하기
if num >= 0:
    print(f'{num}은 양수 입니다.')
else:
    print(f'{num}은 음수 입니다.')

#%%
# 홀수 / 짝수 구분하기
num = int(input('숫자 입력 : '))

if num % 2 == 0:
    print(f'{num}은 짝수입니다.')
else:
    print(f'{num}은 홀수입니다.')

#%%
# M이면 남성, F면 여성, 그외는 잘못 입력
gender = input('성별 입력 :').upper()

if gender == 'M':
    print('남성')
elif gender == 'F':
    print('여성')
else:
    print('잘못 입력')

#%%
# 학생의 이름, 국어, 영어, 수학 성적을 입력 받음
# 각각의 성적이 0 ~ 100 사이가 아니면 성적이 잘못 입력 되었습니다. 출력 후 종료
# 성적이 정상 입력 되었다면, 총점과 평균 구하기
# 평균이 90점 이상이면 이름과 등급 A
# 평균이 80점 이상이면 이름과 등급 B
# 평균이 70점 이상이면 이름과 등급 C
# 평균이 60점 이상이면 이름과 등급 D
# 나머지는 이름과 등급 F

name = input('이름 : ')
korean = int(input('국어 성적 : '))
english = int(input('영어 성적 : '))
math = int(input('수학 성적 : '))

if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
    total_score = korean + english + math
    avg_score = total_score / 3
    if avg_score >= 90:
        grade = 'A'
    elif avg_score >= 80:
        grade = 'B'
    elif avg_score >= 70:
        grade = 'C'
    elif avg_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f'총점 : {total_score} 평균 :{avg_score:.2f}')
    print(f'{name}, {grade}등급')
else:
    print("성적이 잘못 입력 되었습니다.")


#%%
# 계절을 영문으로 입력 받아 계절에 맞는 문구 출력하기
# spring, summer, fall, autumn, winter 입력 받아서 계절에 맞는 문구 출력
# 단, 비교의 편의를 위해 입력 받은 문자열은 대문자로 변환해서 비교하기

season = input('계절을 입력하세요. : ').upper().strip()

if season == 'SPRING':
    print('봄')
elif season == 'SUMMER':
    print('여름')
elif season == 'FALL' or season == 'AUTUMN':
    print('가을')
elif season == 'WINTER':
    print('겨울')
else:
    print('잘못 입력 하셨습니다.')

#%%
# [실습 문제] 자판기 만들기 (조건문만 사용)
#
# 아래 메뉴를 참고하여 자판기 프로그램을 작성하시오.
#
# 1. 콜라 - 1100원
# 2. 사이다 - 1000원
# 3. 커피 - 700원
# 4. 생수 - 600원
#
# [처리 조건]
# 1) 사용자로부터 구매할 음료 번호(1~4)를 입력 받는다.
# 2) 메뉴에 없는 번호를 입력하면 "존재하지 않는 메뉴입니다." 출력 후 종료한다.
# 3) 올바른 번호를 입력했다면, 선택한 음료의 이름과 가격을 안내하고
#    투입할 금액을 입력 받는다.
# 4) 투입한 금액이 음료 가격보다 적으면
#    "금액이 부족합니다. 000원이 부족합니다."를 출력하고 종료한다.
#    (부족한 금액이 정확히 계산되어 출력되어야 함)
# 5) 투입한 금액이 음료 가격 이상이면
#    "000가 나왔습니다. 잔돈 000원을 거슬러 드립니다."를 출력한다.
#    (거스름돈이 정확히 계산되어 출력되어야 함)
#
# 반복문(while, for), 딕셔너리는 사용하지 말고 조건문(if/elif/else)만으로 작성할 것

print('[ 메뉴 ]')
print('1. 콜라 - 1100원')
print('2. 사이다 - 1000원')
print('3. 커피 - 700원')
print('4. 생수 - 600원')
drink_num = int(input('구매할 음료 번호를 입력하세요. (1~4) : '))

if drink_num == 1:
    drink_name = '콜라'
    price = 1100
elif drink_num == 2:
    drink_name = '사이다'
    price = 1000
elif drink_num == 3:
    drink_name = '커피'
    price = 700
elif drink_num == 4:
    drink_name = '생수'
    price = 600
else:
    drink_num = '없음'
    price = 0

if drink_num == '없음':
    print('존재하지 않는 메뉴 입니다.')
else:
    print(f'{drink_name}을 선택하셨습니다. 가격은 {price}원 입니다.')

    money = int(input('금액을 투입하세요 : '))

    if price > money:
        print(f'금액이 부족합니다. {price - money}원 부족합니다.')
    else:
        print(f'{drink_name} 나왔습니다. 잔돈 {money - price}원을 거슬러 드립니다.')

#%%
# [실습 문제]
# 주간 근무 : 10320원
# 야간 근무 : 주간 시급 * 1.5
#
# - 주간근무[1], 야간근무[2]를 입력하세요 :
# - 근무 시간을 입력해 주세요 :
# - 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.

work_shift = int(input('주간근무[1], 야간근무[2]를 입력하세요 : '))
work_hours = int(input('근무 시간을 입력해 주세요 : '))

day_wage = 10320
night_wage = day_wage * 1.5

if work_shift == 1:
    work_type = '주간'
    pay = day_wage * work_hours
elif work_shift == 2:
    work_type = '야간'
    pay = night_wage * work_hours
else:
    work_type = '없음'
    pay = 0

if work_type == '없음':
    print('잘못 입력 하셨습니다.')
else:
    print(f'{work_hours}시간 동안 근무한 {work_type} 급여는 {pay:,.0f}원 입니다.')