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