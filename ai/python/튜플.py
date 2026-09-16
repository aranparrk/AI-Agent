# 파이썬에서 튜플(Tuple)은 변경할 수 없는(immutable) 시퀀스 자료형입니다. 튜플은 여러 개의 요소를 저장하고,
# 각 요소에는 인덱스를 통해 접근 할 수 있습니다. 튜플은 괄호(())를 사용하여 정의하며, 각 요소는 쉼표(,)로 구분됩니다.

ls = [1, 2, 3]
tp1 = (1, 2, 3)
tp2 = 1, 2, 3
ts = 1
ts2 = '1'
ts3 = 1,

print(type(ls))
print(type(tp1))
print(type(tp2))
print(type(ts))
print(type(ts2))
print(type(ts3))

#%%
member = '안유진', 23, '대전시', True # 패킹
name, age, addr, is_adult = member # 언팩킹

def get_name_card(name, phone):
    position = f'{name} 수석연구원'
    addr = '서울시 강남구'
    phone = f'082+{phone}'

    return position, addr, phone

result = get_name_card('박아란', '1234-5678')

print(result)

#%%
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 중복제거
s3 = {1, 2, 3, 4, 5, 6, 2, 3, 4, 5}
print(s3)

# 교집합
print(s1.intersection(s2))

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

#%%
import random

numbers = set()

while True:
    number = random.randint(1, 45)
    numbers.add(number)
    if len(numbers) == 6: break

print(sorted(numbers))