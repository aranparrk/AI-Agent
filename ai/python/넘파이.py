# NumPy (Numerical Python)는 파이썬에서 수치 계산과 과학적 연산을 위한 핵심 라이브러리 입니다.
# - 데이터의 언어는 '숫자와' '행렬'이며, 이를 효율적으로 처리하기 위해 NumPy를 사용
# - 빅데이터 환경에서 파이썬 기본 리스트로 반복문(for)를 돌리는 것은 매우 느립니다.
# - NumPy의 벡터화 연산을 쓰면 수백만 개의 데이터를 순식간에 처리할 수 있습니다.
# - 대규모 다차원 배열 처리
# - 고속 수학 연산 지원
# - 머신러닝, 딥러닝, 데이터 분석에서 필수적으로 사용 됨

import numpy as np # 일반적으로 np라는 별칭을 부여해 사용 함

# 기본 배열 생성
data = [0, 1, 2, 3, 4, 5]
a1 = np.array(data) # 리스트를 넘파이 배열로 만듦
print(a1)

data2 = [0, 1, 2, 3, 4,.4, 5.14, 6.75] # 하나의 타입으로 통일 됨
a2 = np.array(data2)
print(a2) # 실수

# 문자열, 실수, 정수를 포함하는 배열을 만들어서 출력 결과 확인 해보기
data3 = ['가', '나', 1, 2, 3, 4.5, 5.18]
a3 = np.array(data3)
print(a3) # 문자열

# 속성 확인
x = np.array([0.1, 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 요소의 데이터 타입 반환

# 특정 범위의 배열 생성
a4 = np.arange(0, 10, 2) # 0 ~ 10미만 간격은 2
print(a4)

# 1 ~ 100까지, 간격은 3
a5 = np.arange(1, 101, 3)
print(a5)

# 0 ~ 50미만, 간격은 5
a6 = np.arange(0, 50, 5)
print(a6)

# 2차원 배열 생성
a7 = np.arange(12).reshape(4, 3)
print(a7)
print(a7.shape)

# 동일한 간격으로 데이터 생성
a8 = np.linspace(1, 10, 10)
print(a8)

print('-' * 50)
# 실습문제
# NumPy 기초 실습

# 1. 리스트 [10, 20, 30, 40, 50]을 NumPy 배열로 만들어 arr1에 저장하고, 배열과 type(arr1)을 출력하세요.
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
print(type(arr1))

# 2. np.array([True, 1, 2])의 출력 결과와 dtype은 무엇일까요?
np1 = np.array([True, 1, 2])
print(np1)
print(np1.dtype)

# 3. 2행 3열 배열 [[1, 2, 3], [4, 5, 6]]을 만들고 shape와 dtype을 출력하세요.
np2 = np.arange(1, 7).reshape(2, 3)
print(np2)
print(np2.shape)
print(np2.dtype)

# 4. np.arange()를 사용해 2부터 20까지(20 포함) 짝수 배열을 만드세요.
np3 = np.arange(2, 21, 2)
print(np3)

# 5. np.arange()를 사용해 [10 9 8 7 6 5 4 3 2 1]을 만드세요.
np4 = np.arange(10, 0, -1)
print(np4)

# 6. np.aragne()로 0부터 1미만까지 0.1 간격의 배열을 만들고, 요소가 몇 개인지 출력 결과로 확인하세요.
np5 = np.arange(0, 1, 0.1)
print(np5)
print(len(np5))