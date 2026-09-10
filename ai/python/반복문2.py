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