# 외장함수 : 파이썬에서 기본 제공, 단 import 해서 사용
# 랜덤 함수 : 난수 발생기
import random
# from random import randint

# randint(m, n) : 지정된 범위 안의 임의의 정수 생성
for i in range(20):
    print(f'{random.randint(1, 10)}', end=' ') # 1 ~ 10 사이의 임의의 값 생성
print()

# randrange(m, n, p)
for i in range(20):
    print(f'{random.randrange(1, 10, 2)}', end=' ') # 1 ~ 10 미만까지 임의의 값 생성
print()

#%%
import random
# 무인도 탈출 게임
# 두 개의 주사위를 굴려 같은 값이 나오면 '무인도를 탈출 했습니다. 탈출 시도 횟수, 두 개의 주사위 값'

cnt = 0
while True:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    print(f'주사위 값 : {dice_1}, {dice_2}')
    cnt += 1

    if dice_1 == dice_2:
        break

print(f'무인도를 탈출 했습니다.')
print(f'탈출횟수 시도 : {cnt}')

#%%
import random
# 로또 번호 생성 하기 (1 ~ 45 사이의 임의의 수 6개, 단, 중복되면 안 됨)

lotto = []

while len(lotto) < 6: # 중복되지 않은 번호가 6개가 되면 반복문 탈출
    number = random.randint(1, 45)
    if number not in lotto: # 생성된 난수가 로또 리스트에 포함 되어 있지 않으면,
        lotto.append(number) # 리스트의 마지막에 값 추가

print(sorted(lotto))
#%%
# 날짜 및 시간 관련 처리 모듈
from datetime import datetime
datetime.today()             # 운영체제로 부터 시간 가져 오기
datetime.today().year        # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기
datetime.today().hour        # 현재 시간 가져오기

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

#%%
# 오늘은 2024년 10월12일 토요일 10시31분 입니다.
# 현재 시간 가져 오기
# %Y : 4자리 연도
# %m : 2자리 월
# %d : 2자리 일
# %A : 요일 표시
# %H : 24시간 형식의 시간
# %M : 분 표시
now = datetime.now()
#원하는 출력 형식 만들기
formatted = now.strftime("오늘은 %Y년 %m월%d일 %A %H시%M분 입니다.")
print(formatted)

#%%
# 실습 1: 나의 생일까지 남은 일수 계산하기
# 오늘 날짜와 올해 생일(예: 12월 25일)까지 남은 일수를 계산해보세요
today = datetime.today()
birthday = datetime(today.year, 12, 25)  # 원하는 날짜로 변경
print(f"생일까지 남은 날: {(birthday - today).days}")

#%%
# 실습 2: 요일별 인사말 출력하기
# 오늘 요일에 따라 다른 메시지를 출력해보세요
# 월~금: "오늘은 평일입니다. 힘내세요!"
# 토, 일: "오늘은 주말입니다. 푹 쉬세요!"
weekday = today.weekday() # 월요일이 0 ~
if 0 <= weekday <= 4:
    print("오늘은 평일입니다. 힘내세요!")
else:
    print("오늘은 주말입니다. 푹 쉬세요!")

#%%
# 실습 3: 현재 시간대별 인사말 만들기
# 현재 시각(hour)에 따라 다른 인사말을 출력해보세요
# 06~11시: "좋은 아침입니다"
# 12~17시: "좋은 오후입니다"
# 18~22시: "좋은 저녁입니다"
# 그 외: "늦은 밤이네요, 얼른 주무세요"
hour = datetime.today().hour
if 0 <= hour <= 11:
    print("좋은 아침입니다")
elif 12 <= hour <= 17:
    print("좋은 오후 입니다.")
elif 18 <= hour <= 22:
    print("좋은 저녁 입니다.")
else:
    print("늦은 밤이네요, 얼른 주무세요")

#%%
# 실습 4: 원하는 형식으로 파일명 생성하기
# strftime을 활용해서 로그 파일명을 만들어보세요
# 예: "backup_20261014_1530.txt" 같은 형식
form = now.strftime("backup_%Y%m%d_%H%M.txt")
print(form)

#%%
# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(10))
print(math.ceil(100.01)) # 소수점 이하를 올림
print(math.floor(100.9)) # 소수점 이하를 내림

from simple_colors import *

print(green('hello'))
print(yellow('hello', 'bold'))
print(red('hello', ['bold', 'underlined']))

#%%
# 실습 문제 1: 가위바위보 승부 판정 (random)
# 컴퓨터가 random.randint로 가위(0)/바위(1)/보(2) 중 하나를 뽑고, 사용자가 입력한 값과 비교해서 승패를 판정하는 프로그램을 작성하세요.
# 무승부가 나오면 같은 값이 나올 때까지가 아니라,
# 무승부 횟수를 세어 "총 N번 만에 승부가 났습니다"를 출력하도록 반복문을 구성해보세요.
# 힌트: 무인도 탈출 게임의 while True + cnt 패턴 재사용
# 출력 예시: 무승부! 다시 도전합니다... → 당신의 승리! 총 3번 만에 승부가 났습니다.
choices = ["가위", "바위", "보"]
user = int(input("가위(0) 바위(1) 보(2) 중 선택: "))
cnt = 0

while True:
    computer = random.randint(0, 2)
    cnt += 1

    if user == computer:
        print(f"무승부!!! {choices[user]} 다시 도전 합니다.")
        continue

    # 승패판정
    if (user - computer) % 3 == 1:
        print(f"컴퓨터: {choices[computer]} -> 당신의 승리! 총 {cnt}번 만에 승부가 났습니다.")
    else:
        print(f"컴퓨터: {choices[computer]} -> 당신의 패배! 총 {cnt}번 만에 승부가 났습니다.")
    break

#%%
# 실습 문제 2: 로그인 시도 시간 기록기 (datetime + math)
# 사용자가 로그인을 시도할 때마다 현재 시각을 strftime으로 "%Y-%m-%d %H:%M:%S" 형식으로 출력하고,
# 최초 로그인 시각부터 현재까지 경과된 시간을 초 단위로 계산해서 math.floor로 소수점을 버린 정수 초로 출력하세요.
# (같은 코드 안에서 time.sleep으로 몇 초 지연을 준 뒤 두 번째 시각을 구해 차이를 계산하면 됩니다.)
# 힌트: (now2 - now1).total_seconds() 결과에 math.floor 적용
# 출력 예시: 로그인 시각: 2026-09-14 10:31:05 → 2번째 접속까지 경과 시간: 12초



