# 회원정보를 입력 받아서 출력하는 예제 진행
#
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다. (남성과 여성으로 출력)
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한 번에 출력 한다

name = input('이름 입력 : ')

while True:
    age = int(input('나이 입력 : '))
    if 0 < age < 200:
        break
    else:
        print('다시 입력하세요')

while True:
    gender = input('성별 입력 : ').upper()
    if gender == 'M':
        gender_name = '남성'
        break
    elif gender == 'F':
        gender_name = '여성'
        break
    else:
        print('다시 입력하세요')

while True:
    job = int(input('직업 입력 : '))
    if job == 1:
        job_name = '학생'
        break
    elif job == 2:
        job_name = '회사원'
        break
    elif job == 3:
        job_name = '주부'
        break
    elif job == 4:
        job_name = '무직'
        break
    else:
        print('다시 입력하세요')

print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'성별 : {gender_name}')
print(f'직업 : {job_name}')

#%%
# 짝수 / 홀수 개수 세기
# 정수를 하나씩 계속 입력받다가, -1이 입력되면 반복을 종료합니다. 그동안 입력받은 숫자 중 짝수의 개수와 홀수의 개수를 각각 출력하세요.
# while과 break 사용
even = 0
odd = 0

while True:
    num = int(input('정수를 입력하세요 : '))

    if num == -1:
        break

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'짝수 개수 : {even}, 홀수 개수 : {odd}')

#%%
# 구구단 중 특정 단만 출력하기
# 2~9 사이의 정수를 입력하세요: 3

dan = int(input('단을 입력하세요. : '))

print(f'{dan}단 시작!')
for i in range(1, 10):
    print(f'{dan} X {i} = {dan * i}')