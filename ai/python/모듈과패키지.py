# 모듈 : 파이썬의 파일
# 패키지 : 폴더 또는 디렉토리

def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password

if __name__ == '__main__':
    print(add(1, 2))

    print(sub(200, 100))

    url = input('url:')
    print(password(url))