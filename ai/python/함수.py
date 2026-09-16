# 함수(function)는 코드의 특정 블록을 하나의 이름으로 묶어둔 것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면 재사용성, 가독성, 유지보수성을 높일 수 있음
# 함수는 반드시 생성 이후 호출을 해야 실행 됨
# def 키워드 사용
# 일반적으로 식별자뒤에() 소괄호가 있으면 함수

# 함수의 재사용 : 매개변수는 존재하고, 반환값이 없음
def name_card(name, addr, phone):
    print(f'주소 : {addr}')
    print(f'전화번호 : {phone}')
    print(f'이름 : {name}')
    print('-' * 30)

name_card('안유진', '서울시 강남구 역삼동', '010-1234-1234')
name_card('장원영', '서울시 강남구 삼성동', '010-1234-9999')
name_card('가을', '서울시 권선구 권선동', '010-1234-1111')

#%%
# 매개변수 O, 반환값 X
# 1-1 이름(name), 나이(age), 취미(hobby)를 매개변수로 받아서 아래 형식으로 출력하는 함수 intro_card()를 작성하시오.

def intro_card(name, age, hobby):
    print(f'이름 : {name}, 나이 : {age}, 취미 : {hobby}')

intro_card('장원영', 23, '필라테스')
intro_card('안유진', 24, '복싱')
intro_card('리즈', 23, '태권도')

#%%
# 1-2 과목명(subject)과 점수(score)를 매개변수로 받아 "수학 점수 : 90점"
# 형식으로 출력하는 함수 print_score()를 작성하고, 서로 다른 3개 과목으로 호출해보시오.

def print_score(subject, score):
    print(f'{subject} 점수 : {score}점')

print_score('수학', 90)
print_score('과학', 80)
print_score('영어', 75)

#%%
# 매개변수 O, 반환값 O
# 2-1 두 정수를 입력 받아 큰 수를 반환하는 함수 get_max(a, b)를 작성하시오. (if문 사용)

def get_max(a, b):
    if a > b :
        return a
    return b

print(get_max(1, 11))
print(get_max(15, 11))
print(get_max(7, 13))
print(get_max(1, 1))

#%%
# 2-2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수 circle_area(r)를 작성하시오. (원주율은 3.14 사용)
def circle_area(r):
    return 3.14 * r * r

print(circle_area(5))

#%%
# 2-3 정수를 입력받아 짝수면 "짝수", 홀수면 "홀수"를 반환하는 함수 check_even_odd(num)을 작성하시오.
def check_even_odd(num):
    if num % 2 == 0:
        return '짝수'
    return '홀수'

print(check_even_odd(5))
print(check_even_odd(6))
print(check_even_odd(7))

#%%
# 기본값 인자 : 함수 선언 시 매개 변수에 대한 기본값의 정의
# - 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출
def profile(name, age=0, job='무직', addr='대한민국'):
    print(f'이름 : {name}')
    print(f'나이 : {age}')
    print(f'직업 : {job}')
    print(f'주소 : {addr}')

profile('안유진', 23, '아이돌','대전시' )
profile('장원영', 22, '아이돌' )
profile('이서', 20 )