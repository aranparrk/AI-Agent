#%%
# 10명의 성적에대한 총점, 평균, 최소 점수, 최대 점수 구하는 코드
# - 10명의 성적을 입력 받아 총점, 평균, 최소 점수, 최대 점수를 계산하는 코드 작성
# - 점수 입력은 공백 기준으로 연속

score = list(map(int, input('10명의 성적을 입력하세요. : ').split()))

total_score = sum(score)
avg_score = total_score / len(score)
min_score = min(score)
max_score = max(score)

print(f'총점 : {total_score}')
print(f'평균 : {avg_score}')
print(f'최소 점수 : {min_score}')
print(f'최대 점수 : {max_score}')

#%%
# 정수 n을 입력 받아 n * n 출력하기

n = int(input('숫자를 입력하세요 : '))

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt += 1
        print(f'{cnt:3}', end=' ')
    print()


#%%
# 중복 없는 로또 번호 생성하기
import random

lotto = set()

while len(lotto) < 6:
    lotto.add(random.randint(1, 45))

print(sorted(lotto))


#%%
# 영화표 예매하기
seats = [0] * 10
ticket_price = 12000

def show_seat():
    cnt = 0
    for i in range(len(seats)):
        if seats[i] == 1:
            print('[V]', end=' ')
            cnt += 1
        else :
            print('[ ]', end=' ')
            cnt += 1
        if cnt == 5:
            print()
            cnt = 0



def booking(num):

    if seats[num - 1] == 0:
        seats[num - 1] = 1
        print(f'{num}번 좌석 예매 되었습니다.')
    else:
        print('이미 예매 된 좌석이거나, 존재하지 않는 좌석 입니다.')

def total_sales():
    total = 0
    for i in seats:
        if i == 1:
            total += ticket_price

    print(f'총 판매금액 : {total}')


print('-' * 30)
print('[1] 예매하기')
print('[2] 종료하기')
print('-' * 30)

while True:
    menu_num = input('메뉴 번호를 입력해주세요.')

    if not menu_num.isdigit():
        print('메뉴 번호를 잘못 입력 하셨습니다.')
        continue

    menu_num = int(menu_num)

    if menu_num == 1:
        while True:
            show_seat()
            seat_num = input('원하시는 좌석 번호를 입력해주세요. 예매가 완료되면 Enter: ')

            if seat_num == '':
                break

            if not seat_num.isdigit():
                print('숫자를 입력해주세요.')
                continue

            seat_num = int(seat_num)

            booking(seat_num)
    elif menu_num == 2:
        print('예매를 종료합니다.')
        total_sales()
        break
    else:
        print('번호를 잘못 입력하셨습니다.')


#%%
# 커피 메뉴 만들기

menu_dic = {'americano' : ['coffee', 2000, '기본 커피입니다.'],
    'espresso' : ['coffee', 2500, '진한 커피입니다.'],
    'latte' : ['coffee', 4000, '우유가 들어 있는 커피'],
    'green tea' : ['tea', 4500, '녹차 입니다.'],
    'black tea' : ['tea', 4500, '홍차 입니다.']}

def print_menu():

    for i in menu_dic:
        print(f'{i:10} : {menu_dic[i][1]}원, {menu_dic[i][2]}')

def retrieve_menu(menu_name):
    menu_name = menu_name.lower()

    if menu_name in menu_dic:
        print(f'{menu_name:10} : {menu_dic[menu_name][1]}원, {menu_dic[menu_name][2]}')
    else:
        print('찾는 메뉴가 없습니다.')

def add_menu(menu_name, category, price, comment):
    while True:
        if menu_name in menu_dic:
            print('존재 하는 메뉴입니다.')
            continue
        else:
            menu_dic[menu_name] = [category, price, comment]
            print(f'{menu_name}이 추가 되었습니다.')
            break

def delete_menu(menu_name):
    while True:
        if menu_name in menu_dic:
            del menu_dic[menu_name]
            print(f'{menu_name}이 삭제 되었습니다.')
            break
        else :
            print('존재 하지 않는 메뉴 입니다.')
            continue

print('[1] 전체 메뉴 조회')
print('[2] 개별 메뉴 조회')
print('[3] 메뉴 추가')
print('[4] 메뉴 삭제')
print('[0] 종료')

while True:
    menu_num = int(input('메뉴 번호를 선택하세요.'))

    try:
        if menu_num == 1:
            print_menu()
        elif menu_num == 2:
            menu_name = input('찾는 메뉴를 입력하세요.')

            while True:
                if menu_name in menu_dic:
                    retrieve_menu(menu_name)
                    break
        elif menu_num == 3:
            menu_name = input('메뉴 이름을 입력하세요.')
            category = input('카테고리를 입력하세요.')
            price = input('가격을 입력하세요.')
            comment = input('설명을 입력하세요.')

            add_menu(menu_name, category, price, comment)

        elif menu_num == 4:
            menu_name = input('삭제할 메뉴를 입력하세요.')

            delete_menu(menu_name)
        elif menu_num == 0:
            print('종료합니다.')
            break
        else:
            print('잘못 입력 하셨습니다.')
            continue
    except ValueError:
        print('숫자를 입력하세요.')




