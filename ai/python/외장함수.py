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



