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
        print(f'{name}, 평균 : {avg_score:.2f}점 A등급')
    elif avg_score >= 80:
        print(f'{name}, 평균 : {avg_score:.2f}점 B등급')
    elif avg_score >= 70:
        print(f'{name}, 평균 : {avg_score:.2f}점 C등급')
    elif avg_score >= 60:
        print(f'{name}, 평균 : {avg_score:.2f}점 D등급')
    else:
        print(f'{name}, 평균 : {avg_score:.2f}점 F등급')
else:
    print("성적이 잘못 입력 되었습니다.")


