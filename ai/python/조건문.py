# 제어문 : 프로그램의 흐름을 제어하는데 사용
# - 조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행 (if문, 3항연산자)
# - 반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행 (while문, for문)

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

