with open('스타벅스일일매출.txt', 'r', encoding='utf-8') as file: # 다른 위치에 있다면 경로 지정
    for e in file:
        print(e, end='')
    print()

#%%
# 스타벅스 판매량 구하기
file_name = '스타벅스일일매출.txt'
espresso = []
americano = []
cafelatte = []
capuccino = []
dates = []

with open(file_name, 'r', encoding='utf-8') as file:
    header = file.readline().split() # 줄 바꿈 기준으로 한줄을 읽어 드림


    for e in file:
        data_list = e.split()
        dates.append(data_list[0])
        espresso.append(int(data_list[1])) # 10
        americano.append(int(data_list[2])) # 50
        cafelatte.append(int(data_list[3])) # 45
        capuccino.append(int(data_list[4])) # 20

# 제목 / 전체 판매량 / 일 평균 판매량
print('제목\t\t 전체 판매량\t\t 일평균 판매량')
print('-' * 38)
print(f'{header[1]:5}  {sum(espresso):>8}  {sum(espresso) / len(espresso):>15.2f}')
print(f'{header[2]:5}  {sum(americano):>8}  {sum(americano) / len(americano):>15.2f}')
print(f'{header[3]:5}  {sum(cafelatte):>8}  {sum(cafelatte) / len(cafelatte):>15.2f}')
print(f'{header[4]:5}  {sum(capuccino):>8}  {sum(capuccino) / len(capuccino):>15.2f}')
print()

# 1. 각 메뉴별 전체 판매량
def total_sales_func():
    print('-' * 25)
    print('각 메뉴별 전체 판매량')
    print('-' * 25)
    print('메뉴명\t\t전체 판매량')
    print('-' * 25)
    print(f'{header[1]:5}\t\t{sum(espresso)}')
    print(f'{header[2]:5}\t\t{sum(americano)}')
    print(f'{header[3]:5}\t\t{sum(cafelatte)}')
    print(f'{header[4]:5}\t\t{sum(capuccino)}')




# 2. 각 메뉴별 일 평균 판매량
def avg_sales_func():
    print('-' * 25)
    print('각 메뉴별 일 평균 판매량')
    print('-' * 25)
    print('메뉴명\t\t일 평균 판매량')
    print('-' * 25)
    print(f'{header[1]:5}\t\t{sum(espresso) / len(espresso):.2f}')
    print(f'{header[2]:5}\t\t{sum(americano) / len(americano):.2f}')
    print(f'{header[3]:5}\t\t{sum(cafelatte) / len(cafelatte):.2f}')
    print(f'{header[4]:5}\t\t{sum(capuccino)/ len(capuccino):.2f}')




# 3. 판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    menu_sales = {
        header[1] : sum(espresso),
        header[2] : sum(americano),
        header[3] : sum(cafelatte),
        header[4] : sum(capuccino)
    }

    most_sold_menu = max(menu_sales, key=menu_sales.get)
    print('-' * 25)
    print(f'판매량이 가장 높은 메뉴 : {most_sold_menu}, 총 {menu_sales[most_sold_menu]} 잔')
    print('-' * 25)





# 4. 판매량이 가장 적은 메뉴 구하기
def least_sold_menu_func():
    menu_sales = {
        header[1]: sum(espresso),
        header[2]: sum(americano),
        header[3]: sum(cafelatte),
        header[4]: sum(capuccino)
    }

    least_sold_menu = min(menu_sales, key=menu_sales.get)

    print('-' * 25)
    print(f'판매량이 가장 낮은 메뉴 : {least_sold_menu}, 총 {menu_sales[least_sold_menu]} 잔')
    print('-' * 25)



# 5. 판매량이 가장 많은 날짜 구하기
def most_sales_date_func():
    dates_sales = {}

    for i in range(len(dates)):
        dates_sales[dates[i]] = (
            espresso[i] + americano[i] + cafelatte[i] + capuccino[i]
        )


    most_sales_date = max(dates_sales, key=dates_sales.get)
    print('-' * 25)
    print(f'판매량이 가장 많은 날짜 : {most_sales_date}, 총 {dates_sales[most_sales_date]} 잔')
    print('-' * 25)



# 6. 반복문으로 구성된 메뉴 만들기

print('-' * 50)
print('[1. 각 메뉴별 전체 판매량]')
print('[2. 각 메뉴별 일 평균 판매량]')
print('[3. 판매량이 가장 높은 메뉴 구하기]')
print('[4. 판매량이 가장 적은 메뉴 구하기]')
print('[5. 판매량이 가장 많은 날짜 구하기]')
print('[0. 종료]')
print('-' * 50)

while True:
    menu_num = input('메뉴 번호를 입력하세요 : ')

    if not menu_num.isdigit():
        print('잘못 입력하셨습니다.')
        continue

    menu_num = int(menu_num)

    if menu_num == 1:
        total_sales_func()
    elif menu_num == 2:
        avg_sales_func()
    elif menu_num == 3:
        most_sold_menu_func()
    elif menu_num == 4:
        least_sold_menu_func()
    elif menu_num == 5:
        most_sales_date_func()
    elif menu_num == 0:
        print('종료합니다.')
        break
    else:
        print('없는 메뉴 번호 입니다.')
        continue
