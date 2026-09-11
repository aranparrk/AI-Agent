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