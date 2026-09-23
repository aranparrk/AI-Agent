# 반복문 : 주어진 조건이 참인 동안 반복 수행 함
# while문 : 주로 반복횟수를 알 수 없을 때
# for문 : 반복 횟수가 정해져있을 때

n = int(input('정수 입력 : '))
total = 0 # 합계를 저장할 변수
while n > 0: # 반복문의 조건인 n의 값이 0보다 크면 참이므로 반복 수행
    total += n # total = total + n
    n -= 1 # n = n - 1, n의 값을 변경해서 반복문을 빠져나가게 함

for i in range(1, n + 1):
    total += i

print(f'합 : {total}')

#%%
# while문은 반복 횟수를 알 수 없을 때 사용하면 좋음
# 성별을 받는데 남성은 M. 여성은 F로 입력 받음, 잘못된 입력이면 계속 다시 입력 받음

while True: # 무한 반복문 이므로 탈출 조건 필요
    gender = input('성별을 입력하세요. : ').upper().strip()

    if gender == 'M' or gender == 'F':
        break
    print('성별을 잘못 입력하셨습니다.')

print(f'{'남성' if gender == 'M' else '여성'}')

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

while True:
    korean = int(input('국어 성적 : '))
    english = int(input('영어 성적 : '))
    math = int(input('수학 성적 : '))

    if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
        break
    print("성적이 잘못 입력 되었습니다.")

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



