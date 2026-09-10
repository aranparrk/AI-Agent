# for 문 : 정해진 범위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스 :
# for 변수 in range(시작값, 최종값, 증감값) :

ive = ['안유진', '장원영', '이서', '가을', '레이', '리즈']
for e in ive: # 시퀀스형 데이터를 자동으로 반복 수행하면서 값을 요소의 값을 복사하면서 수행
    print(e, end=" ")

print()

for i in range(len(ive)):
    ive[i] += '*'
    print(ive[i], end=" ")

print()

for e in ive: # 시퀀스형 데이터를 자동으로 반복 수행하면서 값을 요소의 값을 복사하면서 수행
    print(e, end=" ")

print()

for i in range(len(ive) - 1, -1, -1):
    print(ive[i], end=" ")

#%%
# 1 ~ 1000사이의 3의 배수 출력
cnt = 0
for i in range(1, 100 + 1):
    if i % 3 == 0:
        print(f'{i:3}', end=' ')
        cnt += 1
        if cnt >= 10:
            print()
            cnt = 0
#%%
# 입력 받은 숫자의 범위 내의 7의 배수를 출력.
# 한 줄에 10개씩 출력
# 정렬을 적용해 줄맞춤

num = int(input('숫자를 입력 하세요.'))

cnt = 0
for i in range(1, num +1):
    if i % 7 == 0:
        print(f'{i:5}', end=' ')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0

#%%

star = '*'

for i in range(1, 6):
    print(star * i)

#%%
# 입력 받은 문자열을 뒤집어 출력하기
# 입력 : abcdef => fedcba

text = input('문자열을 입력하세요 : ')

for i in range(len(text) - 1, -1, -1):
    print(text[i], end='')

#%%
# 입력 받은 문자열에서 대문자는 소문자로, 소문자는 대문자로

text = input('문자열을 입력하세요 : ')

for i in range(len(text)):
    if text[i].isupper():
        print(text[i].lower(), end='')
    elif text[i].islower():
        print(text[i].upper(), end='')

new_text = ''

for e in text :
    if e.isupper():
        new_text += e.lower()
    elif e.islower():
        new_text += e.upper()
    else:
        new_text += e

print(new_text)
#%%
# 정수값을 입력 받아 3의 배수, 5의 배수이면 값을 출력 1줄에 5개씩 출력
num = int(input('정수 입력 : '))

cnt = 0
for i in range(1, num + 1):
    if i % 3 == 0 or i %  5 == 0:
        print(f'{i:3}', end=' ')
        cnt += 1
        if cnt == 5:
            print()
            cnt = 0

#%%
# 이중 for문
# 입력 받은 수가 10이라면 10 * 10 행렬 출력

num = int(input('정수 입력 : '))

cnt = 0
for i in range(1, num + 1):
    for j in range(1, num + 1):
        cnt += 1
        print(f'{cnt:4}', end='')
    print()

#%%
# 단일 for문으로 변경해서 출력 해보기
# 반복문 범위를 num * num
# i % num == 0 : print()
num = int(input('정수 입력 : '))

for i in range(1, num * num + 1):
    print(f'{i:4}', end='')
    if i % num == 0:
        print()

#%%
# 선택한 구구단 출력하기
dan = int(input('단을 입력하세요. : '))

print(f'{dan}단 시작!')
for i in range(1, 10):
    print(f'{dan} X {i} = {dan * i}')

#%%
# 2 ~ 9단까지 구구단 출력하기

for i in range(2, 10):
    print(f'{i}단 시작')
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()