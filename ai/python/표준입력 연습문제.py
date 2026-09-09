#%%
# "이름과 주소 입력 : " 안내 문구로 이름과 주소를 공백으로 구분해서 한 번에 입력 받고 (split() 활용), 두 값을 각각 출력하세요.
name, addr = input('이름과 주소 입력 : ').split(' ')

print(f'이름 : {name}')
print(f'주소 : {addr}')

#%%
# "시:분:초 : " 안내 문구로 "14:5:9" 형태의 시간을 클론(:) 기준으로 입력받아 map(int, ....) 정수 변환한 뒤,
# 각 자리를 2자리 폭에 0으로 채워서 출력하세요.
time = list(map(int, input('시:분:초 : ').split(':')))

print(f'{time[0]:02}:{time[1]:02}:{time[2]:02}')

#%%
# "국어 영어 수학 : " 안내 문구로 세 과목 점수를 공백 기준으로 한 번에 입력 받아 (map(int, input().split())) 평균을 구하고,
# 평균이 60점 이상이면 "합격", 아니면 "불합격"을 삼항 연산자로 함께 출력하세요.

korean, english, math = map(int, input("국어 영어 수학 : ").split(' '))

avg = (korean + english + math) / 3

print(f'결과 : {'합격' if avg >= 60 else '불합격'}')