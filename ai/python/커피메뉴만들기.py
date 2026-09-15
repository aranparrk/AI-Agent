# 기본 메뉴 추가
# {} 중괄호를 사용해 선언, 각 요소는 ,(쉼표)로 구분
# 키와 값은 :(콜론)으로 구분
# 딕셔너리 내부에 리스트를 가짐
menu = {
    'americano' : ['coffee', 2000, '기본 커피입니다.'],
    'espresso' : ['coffee', 2500, '진한 커피입니다.'],
    'latte' : ['coffee', 4000, '우유가 들어 있는 커피'],
    'green tea' : ['tea', 4500, '녹차 입니다.'],
    'black tea' : ['tea', 4500, '홍차 입니다.']
}

# 전체 메뉴 조회
def print_menu():
    for e in menu:
        print(f'{e} - {menu[e]}')

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(f'{name} - {menu[name]}')
    else:
        print('찾는 메뉴가 없습니다.')
        return

# 메뉴 추가
def add_menu(name, category, price, comment):
    if name not in menu:
        if not price.isdigit():
            print('숫자로 입력해주세요.')
            return
        price = int(price)
        menu[name] = [category, price, comment]
        print(f'{name} 메뉴가 추가 되었습니다.')
        return
    else:
        print(f'{name} 메뉴가 이미 존재합니다.')
        return

# 메뉴 삭제
def del_menu(name):
    if name in menu:
        del menu[name]
        print(f'{name} 메뉴가 삭제 되었습니다.')
        return
    else:
        print(f'{name} 메뉴는 존재하지 않습니다.')
        return

# 메뉴 수정
# 메뉴 수정
def update_menu(name, new_name, category, price, comment):
    if name not in menu:
        print(f'{name} 메뉴는 존재하지 않습니다.')
        return

    # 입력하지 않은 항목은 기존 값으로 설정
    if new_name == '':
        new_name = name

    if category == '':
        category = menu[name][0]

    if price == '':
        price = menu[name][1]
    else:
        if not price.isdigit():
            print('숫자로 입력 해주세요.')
            return
        price = int(price)

    if comment == '':
        comment = menu[name][2]

    # 변경하려는 이름이 이미 사용 중인지 검사
    if new_name != name and new_name in menu:
        print(f'{new_name} 메뉴가 이미 존재합니다.')
        return

    # 메뉴명이 달라졌을 때만 기존 키 삭제
    if new_name != name:
        del menu[name]

    menu[new_name] = [category, price, comment]
    print(f'{name} 메뉴가 수정되었습니다.')

# 전체 메뉴 만들기
# [1]전체 메뉴 보기 [2]개별 메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]메뉴 수정 [6] 종료하기

print('[1]전체 메뉴 보기')
print('[2]개별 메뉴 조회')
print('[3]메뉴 추가')
print('[4]메뉴 삭제')
print('[5]메뉴 수정')
print('[6]종료 하기')
print('-' * 30)

while True:
    menu_number = input('메뉴 번호를 입력하세요. : ')

    if not menu_number.isdigit():
        print('번호를 입력 해주세요.')
        continue

    menu_number = int(menu_number)

    if menu_number == 1:
        print_menu()
    elif menu_number == 2:
        menu_name = input('메뉴 명을 입력하세요 : ')
        get_menu(menu_name)
    elif menu_number == 3:
        menu_name_add = input('메뉴 명을 입력하세요 : ')
        menu_category = input('카테고리를 입력하세요 : ')
        menu_price = input('가격을 입력하세요 : ')
        menu_comment = input('설명을 입력하세요. : ')

        add_menu(menu_name_add, menu_category, menu_price, menu_comment)
    elif menu_number == 4:
        menu_name = input('메뉴 명을 입력하세요 : ')

        del_menu(menu_name)
    elif menu_number == 5:
        menu_name = input('수정할 메뉴명을 입력하세요 : ')
        new_menu_name = input('새 메뉴명을 입력하세요(변경하지 않으면 Enter) : ')
        menu_category = input('카테고리를 입력하세요 : ')
        menu_price = input('가격을 입력하세요 : ')
        menu_comment = input('설명을 입력하세요 : ')

        update_menu(menu_name, new_menu_name, menu_category, menu_price, menu_comment)
    elif menu_number == 6:
        print('종료 되었습니다.')
        break
    else:
        print('메뉴 번호를 잘못 입력하셨습니다.')