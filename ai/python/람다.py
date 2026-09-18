# 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 람다 함수를 이용에 익명의 함수를 만들 수 있음
# 람다 함수의 장점은 코드의 간결함, 메모리의 절약

def add(a,b):
    return a + b

print(add(10,20))

print(f'{ (lambda a, b: a + b)(1, 2)}')

def power(n):
    return n * n

out = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))

print(out)

#%%
# - 사용자로부터 좌석 번호를 입력받아 예매하는 시스템이다.
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

# 좌석 목록 및 티켓 가격
seats = [0] * 10
ticket_price = 12000


# 좌석 출력 함수
def print_seats():
    cnt = 0

    for i in range(len(seats)):
        if seats[i] == 0:
            print(f'[ ]', end=' ')
        else:
            print(f'[V]', end=' ')

        cnt += 1

        if cnt == 5:
            cnt = 0
            print()


# 좌석 선택 함수
def reserve_seat(num):
    if num < 1 or num > len(seats):
        print('존재하지 않는 좌석입니다.')

    elif seats[num - 1] == 1:
        print('이미 예약된 좌석입니다.')

    else:
        seats[num - 1] = 1
        print(f'{num}번 좌석이 예약되었습니다.')


# 판매 금액 계산 함수
def calculate_total_sales():
    total = 0

    for i in range(len(seats)):
        if seats[i] == 1:
            total += ticket_price

    return total

def cancel_seat(num):
    if num < 1 or num > len(seats):
        print('존재하지 않는 좌석입니다.')

    elif seats[num - 1] == 1:
        seats[num - 1] = 0
        print(f'{num}번 좌석 예매 취소 되었습니다.')
    else:
        print(f'{num}번 좌석은 예매 되어 있지 않습니다.')


# 입력 메뉴 구성
print('[1] 좌석 조회')
print('[2] 좌석 선택')
print('[3] 취소')
print('[0] 종료')

while True:
    menu_number = input('\n메뉴를 선택하세요 : ')

    if not menu_number.isdigit():
        print('메뉴 번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
        continue

    menu_number = int(menu_number)

    if menu_number == 1:
        print_seats()

    elif menu_number == 2:
        while True:
            seat_number = input(
                '좌석 번호를 입력하세요. 예매가 완료되면 [Enter] : '
            )

            if seat_number == '':
                break

            if not seat_number.isdigit():
                print('숫자를 입력해주세요.')
                continue

            reserve_seat(int(seat_number))

    elif menu_number == 3:
        while True:
            seat_number = input(
                '좌석 번호를 입력하세요. 예매가 취소가 완료되면 [Enter] : '
            )
            if seat_number == '':
                break

            if not seat_number.isdigit():
                print('숫자를 입력해주세요.')
                continue

            cancel_seat(int(seat_number))

    elif menu_number == 0:
        total = calculate_total_sales()

        print(f'총 매출액은 {total:,}원입니다.')
        print('종료되었습니다.')
        break

    else:
        print('잘못 입력하셨습니다.')

#%%
# 함수로 입력 받은 수가 짝수인지 홀수 인지 결과 출력
def odd_even(num):
    if num % 2 == 0:
        return '짝수'
    else:
        return '홀수'

print(odd_even(5))
print(odd_even(6))

#%%
# 입력으로 들어오는 수의 평균을 구해서 반환 후 출력 하기
num = list(map(int, input('숫자를 입력하세요.').split()))

def avg(num):
    return sum(num) / len(num)

print(f'{avg(num)}:.2f')


#%%
# 소수의 합 구하기
def solution(num):
    total = 0
    for i in range(2, num + 1):
        is_prime = True

        for e in range(2, i):
            if i % e == 0:
                is_prime = False
                break

        if is_prime:
            total += i

    return total

print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))

#%%
# 두번째 수 찾기
def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt == 0 :
                return i + 1
            else: cnt += 1
    return -1

ls = list(map(int, input("리스트 입력 : ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls, n))
#%%
#세자리수 정수 입력 받아 가장 큰 수 출력하기

a = b = c = 0
def num_split(input):
    global a, b, c
    a = input // 100
    b = (input % 100) // 10
    c = (input % 100) % 10

def compare_num():
    if a > b:
        if a > c: return a
        else: return c
    else:
        if b > c: return b
        else: return c

n = int(input())
num_split(n)
print(compare_num())
