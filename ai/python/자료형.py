#%%
# 자료형(Data Type)은 데이터를 저장하는 방식과 연산할 수 있는 방법을 정의하는 데이터의 형태를 의미
# Python에서는 변수를 선언할 때 자료형을 명시하지 않아도 되며, 값이 할당될 때 자동으로 자료형이 결정
from traceback import print_tb

text = '안녕하세요. 파이썬 입니다.'
text = 100
text = 3.14
text = True
print(type(text))

#%%
# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음, "", '', """""", ''''''
text1 = '안녕하세요. 파이썬 입니다.'
print(text1)
print(text1[0])
print(text1[7:10]) # 슬라이싱
print(text1 + '!!!!!!!!')
print(text1 * 3)

#%%
# 숫자형(Number) : 정수, 실수, 복소수형이 있음, 사칙연산 가능
num1 = 10.1
num2 = 4.0
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

#%%
# 불리언(Boolean) : 참과 거짓 두가지의 값만 가짐
age = int(input('나이를 입력하세요. : '))
is_adult = False
if age > 18:
    is_adult = True
else:
    is_adult = False

print(bool(1))      # True
print(bool(-1))     # True
print(bool(0))      # False
print(bool(''))     # False
print(bool(' '))    # True
print(bool(None))   # False

#%%
# 형변환 : 데이터를 다른 자료형으로 변환할 때 사용
print('100' + str(200))
print(int('100') + 200)
