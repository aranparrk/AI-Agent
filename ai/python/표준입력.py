# 표준입력이란? 콘솔로부터 사용자의 입력을 받음
# - 기본적으로 문자열로 반환되며, 다른 데이터형으로 변환하려면 형변환 함수 사용해야 함

# 이름(문자열), 나이(정수), 성별(문자열), 주소(문자열), 평균(실수) 입력 받아 출력 해보기
name = input('이름 입력 : ')
age = int(input('나이 입력 : ')) # 문자열로 입력 받은 나이를 정수로 반환
gender = input('성별 입력 : ').upper() # 대문자로 반환
addr = input('주소 입력 : ')
avg = float(input('평균 입력 : '))
print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'성별 : {'남성' if gender == 'M' else '여성'}')
print(f'주소 : {addr}')
print(f'평균 : {avg:.2f}')


# 국어, 영어, 수학 성적을 입력 받아, 총점과 평균으로 입력
kor = int(input('국어 입력 : '))
eng = int(input('영어 입력 : '))
math = int(input('수학 입력 : '))

total_score = kor + eng + math
avg_score = total_score / 3

print(f'총점 : {total_score}')
print(f'평균 : {avg_score:.2f}')

score = list(map(int, input('국어 영어 수학 : ').split()))

print(score)

# 시간을 24제로 예) 23:56:45 입력 받아 12시간 제로 변환해서 11시 56분 45초 형태로 출력하기
# split(':')
hour, minute, sec = input('24시간 시:분:초 > ').split(':')

hour = int(hour)
minute = int(minute)
sec = int(sec)

if hour == 12:
    print(f'오후{hour:02}시{minute:02}분{sec:02}초') # 2자리를 차지하는데 앞에 값이 없으면 0으로 채워라
elif hour > 12:
    hour -= 12 # hour = hour - 12
    print(f'오후{hour:02}시{minute:02}분{sec:02}초')
else:
    print(f'오전{hour:02}시{minute:02}분{sec:02}초')

