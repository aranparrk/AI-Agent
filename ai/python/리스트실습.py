# 3개의 햄버거와 2개의 음료의 가격을 입력 받아 제일 싼 세트 메뉴의 가격 구하기(50원 할인)
# - 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료들 중 싼 음료의 가격을 합산하고 여기서 50원 할인

price = list(map(int, input('가격을 입력하세요. : ').split()))

set_price = min(price[:3]) + min(price[3:]) - 50

print(f'햄버거 세트 가격은 {set_price}원 입니다.')

#%%
# 리스트 순회하기 : 5대의 자동차 이름을 입력 받음
# - 범위기반 for문으로 순회해서 출력 : for i in range()
# - 시퀀스 for문으로 순회해서 출력 for e in 시퀀스
# - 오름차순, 내림차순 출력


cars = list(input('자동차 5대를 입력하세요 : ').split())

# 범위 기반 for문: 오름차순
ascending_cars = sorted(cars)

print('오름차순 : ', end='')
for i in range(len(ascending_cars)):
    print(ascending_cars[i], end=' ')

print()

# 시퀀스 for문: 내림차순
descending_cars = sorted(cars, reverse=True)

print('내림차순 : ', end='')
for car in descending_cars:
    print(car, end=' ')