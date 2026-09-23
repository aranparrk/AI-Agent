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

# 특정 숫자로 채워진 배열
a8 = np.zeros(10)
print(a8)
a9 = np.zeros((3, 4))
print(a9)

a10 = np.ones(10)
print(a10)

a11 = np.eye(4) # 4 x 4
print(a11)

# 배열의 데이터 타입
a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a13)
print(a13.dtype) # <U8의 의미는 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 의미

num_a13 = a13.astype(float) # 문자열을 실수 타입으로 변환
print(num_a13)

a14 = np.array(['1', '3', '5', '7', '9'])
num_a14 = a14.astype(int) # 문자열을 정수 타입으로 전환
print(num_a14)

# 난수 배열의 생성
# rand() : 0 ~ 1 미만의 실수로 난수 배열을 생성
a15 = np.random.rand(2, 3)
print(a15)
a16 = np.random.rand(2, 3, 4)
print(a16)

# randint() : 지정된 범위에 해당하는 정수로 난수 배열을 생성
a17 = np.random.randint(10, size=(5, 4)) # 0 ~ 9 사이의 난수를 5행 4열로 생성
print(a17)

# 실습문제 2
# 1. 0으로 채워진 요소 5개짜리 1차원 배열을 만들고, 배열과 dtype을 출력하세요.
np6 = np.zeros(5)
print(np6)
print(np6.dtype)

# 2. 0으로 채워진 3행 5열 배열을 만들고 shape를 출력하세요.
np7 = np.zeros((3, 5))
print(np7)
print(np7.shape)

# 3. 1로 채워진 2행 4열 배열을 만든 뒤, astype()을 사용해 정수형으로 변환하여 출력하세요.
np8 = np.ones((2, 4))
num_np8 = np8.astype(int)
print(num_np8)

# 4. np.eye()로 5 x 5 배열을 만들어 출력하고, 이런 형태의 행렬을 무엇이라고 부르는지, dtype은 무엇인지 확인하세요.
np8 = np.eye(5)
print(np8)
print(np8.dtype)

# 5. 배열 np.array(['10', '20, '30', '40'])의 dtype을 출력한 뒤, 정수형으로 변환하고 변환 후의 dtype도 출력하세요.
np9 = np.array(['10', '20', '30', '40'])
print(np9.dtype)
num_np9 = np9.astype(int)
print(num_np9)

# 6. 0 ~ 1 미만의 실수 난수로 4행 3열 배열을 만들고 shape를 출력하세요.
np10 = np.random.rand(4, 3)
print(np10.shape)

# 7. np.random.randint()를 사용해 주사위를 10번 던진 결과(1 ~ 6)를 1차원 배열로 만드세요.
np11 = np.random.randint(1,7, size=10)
print(np11)

# 8. 0 ~ 99 사이의 정수 난수 12개를 1차원 배열로 만든 뒤, 다음을 순서대로 수행하세요.
np12 = np.random.randint(0, 100, size=12)
print(np12)
