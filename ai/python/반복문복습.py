# while문
# for i in range(초기값, 최종값, 증감값)
# for e in sequence

n = int(input('정수 입력 : '))
total = 0


while n > 0:
    total += n
    n -= 1

for i in range(1, n + 1):
    total += i

while True:
    total += n
    n -= 1
    if n == 0: break

#%%
# 입력 받은 숫자의 합 구하기 (리스트)

score = list(map(int, (input('숫자 입력').split())))

sum = 0
for i in range(len(score)):
    sum += score[i]
    print(score[i], end=' ')

for e in score:
    sum += e

print(f'\n입력한 숫자의 합 : {sum}')

#%%
square = list(map(lambda a: a ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(square)

#%% 입력 받은 값을 역순으로 출력하기

num = list(map(int, input('숫자를 입력 하세요. : ').split()))

for i in range(len(num) - 1, -1, -1):
    print(num[i], end=' ')

#%%
# 별 100개 찍기
for i in range(10):
    print(f'|i = {i}|', end='')
    for j in range(10):
        print('*', end= ' ')
    print()

#%%
# 입력 : 5
# *
# **
# ***
# ****
# *****

# *****
# ****
# ***
# **
# *

star = int(input('숫자를 입력 하세요 : '))

for i in range(1, star + 1):
    print('*' * i)

for i in range(star, 0, -1):
    print('*' * i)

print()

for i in range(star):
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(star):
    for j in range(star - i):
        print('*', end=' ')
    print()

#%%
# continue : 반복문에서 아래의 문장을 수행하지 않고 반복문으로 이동

n = int(input('정수 입력 : '))
for i in range(1, n + 1):
    if i % 2 == 0: continue
    print(i)

#%%
# continue문을 이용해 3과 5의 배수를 제외하고 출력하기

n = int(input('정수 입력 : '))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0: continue
    print(i)