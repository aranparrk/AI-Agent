# 판다스 : Pandas는 테이블 형태의 데이터를 쉽게 다룰 수 있도록 설계된 파이썬 데이터 분석 라이브러리
# - 데이터 전처리, 탐색, 변환 및 시각화 등의 작업에 널리 사용
# - 행과 열의 구조로 구성된 데이터를 직관적으로 다룰 수 있게 해줌
# - Series(1차원), DataFrame(2차원) 구조 지원
# - 다양한 데이터 파일(CSV, Excel, SQL, JSON 등) 불러오기 가능
# - 결축치 처리, 정렬, 그룹화, 필터링, 통계 분석 등 풍부한 기능 제공
# - 시계열 데이터 처리 기능 내장

# Series - 1차원 데이터 구조 : 리스트와 유사하지만, 각 데이터에 인덱스(라벨)가 붙음
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# DataFrame - 2차원 데이터 구조 : 여러 개의 Series가 모여 이루어짐. 행과 열을 가짐
data = {
    '이름': ['민지', '하니', '다니엘'],
    '수학': [95, 85, 75],
    '영어': [90, 85, 94]
}

df = pd.DataFrame(data)
print(df)

# 특정 행 및 열 추출
print(df['수학']) # 열 추출
print(df.loc[0]) # 행 추출
print(df.loc[1, '영어']) # 특정 행의 열 추출

# 새로운 열 및 행 추가
df['과학'] = [93, 89, 87] # 열 추가
df.loc[3] = ['혜인', 92, 89, 77]

print(df)

# 기본 연산
print(df['수학'].sum()) # 합계
print(df['수학'].mean()) # 평균
print(df['수학'].max()) # 최대값
print(df['수학'].min()) # 최소값

# 열추가
df['반'] = [1, 1, 2, 2]
print(df)

print(df.groupby('반')['수학'].mean())

#%%
import pandas as pd

# 1. CSV 파일을 불러와 데이터의 전체 행 개수를 출력하세요.
data = pd.read_csv('exam.csv')


print(len(data))
print()

# 2. 데이터프레임에서 특정 열('수학')만 선택하여 출력하세요.
print(data['math'])
print()

# 3. 데이터프레임에서 '수학'점수가 80점 이상인 학생만 필터링하세요.
print(data[data['math'] >= 80])
print()

# 4. '영어' 점수의 평균을 계산하여 출력하세요.
print(data['english'].mean())
print()

# 5. 데이터프레임을 새로운 CSV 파일로 저장하세요.
data.to_csv('filtered_exam.csv', index=False)
print()

# 6. 각 학급별 수학과 영어 점수의 평균을 동시에 구하세요.
print(data.groupby('nclass')[['math', 'english']].mean())
print()

# 7. 각 학급별 수학 점수의 최대값과 최소값을 동시에 구하세요.
print(data.groupby('nclass')['math'].agg(['max', 'min']))
print()

# 8. 다음 표의 내용을 데이터프레임으로 만들어서 출력
df = pd.DataFrame({
    '제품' : ['사과', '딸기', '수박'],
    '가격' : [1800, 1500, 3000],
    '판매량' : [24, 38, 13]
})

print(df)
print(f'평균 가격 : {df['가격'].mean()}')
print(f'평균 판매량 : {df['판매량'].mean()}')

print()