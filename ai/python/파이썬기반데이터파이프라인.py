# 1. 파일 읽기
try:
    with open('order.txt', 'r', encoding='utf-8') as file:
        total = 0
        for line in file:
            try:
                # 2. 텍스트 클렌징
                # 줄 전체의 양 끝 공백/줄바꿈 제거 후 쉼표로 나누기
                data = line.strip().split(',')

                # 각 항목의 앞뒤 공백 제거
                data[0] = data[0].strip()
                data[1] = data[1].strip()
                # '원' 제거
                data[2] = data[2].strip().replace('원', '')

                # 문자열 -> 정수 형변환
                data[1] = int(data[1])
                data[2] = int(data[2])

            # 숫자로 바꿀 수 없는 값이 섞여 있을 때 예외 처리
            except ValueError:
                print('숫자로 변환할 수 없습니다.')
                continue

            # 3. 이상치 제거
            if data[1] < 0 or data[2] > 10000 or data[2] < 0:
                continue

            # 4. 매출 계산
            total += data[1] * data[2]

        print(f'총매출 {total:,}원')
# 파일이 없을 때 예외 처리
except FileNotFoundError:
    print('order.txt 파일을 찾을 수 없습니다.')

