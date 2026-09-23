import pymysql

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="12341234", database="mysqlDB", charset="utf8")
    return conn

def create_user_table(conn):
    cur = conn.cursor()
    # 2. 기존 테이블 삭제 및 생성
    cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE userTable (
            id CHAR(10) PRIMARY KEY,
            pwd CHAR(15),
            name CHAR(20),
            email CHAR(20),
            addr CHAR(50)
        )
    """)
    conn.commit()
    conn.close()

# 3. 초기 데이터 삽입
def insert_user(conn):
    cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구'),
        ('liz1234', '12345678', '리즈', 'liz@gmail.com', '서울시 강남구')
    ]

    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

    # 4. 커밋 및 연결 종료
    conn.commit()
    conn.close()

# 신규 회원 추가
def new_user_insert(conn):
    cur = conn.cursor()

    id = input('아이디 : ')
    if id == 'exit':
        return 'exit'
    pwd = input('패스워드 : ')
    name = input('이름 : ')
    mail = input('메일 : ')
    addr = input('주소 : ')
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
    except Exception as e:
        print(f'오류 발생 : {e}')

    conn.commit()
    conn.close()

# 회원 수정
def update_user(conn):
    cur = conn.cursor()
    id = input('ID : ')
    pwd = input('PASSWORD : ')
    name = input('NAME : ')
    email = input('EMAIL : ')
    addr = input('ADDR : ')
    cur.execute('UPDATE userTable SET pwd=%s, name=%s, email=%s, addr=%s WHERE id=%s', (pwd, name, email, addr, id))
    if cur.rowcount > 0:
        print('수정 완료!!')
    else:
        print('해당 ID는 존재 하지 않습니다.')
    conn.commit()
    conn.close()


# 회원 삭제
def delete_user(conn):
    cur = conn.cursor()
    id = input('삭제할 사용자 ID : ')
    cur.execute('DELETE FROM userTable WHERE id=%s', (id,))
    if cur.rowcount > 0:
        print('삭제 성공!')
    else:
        print('그런 ID는 없습니다...')

    conn.commit()
    conn.close()

# 회원 조회
def search_user(conn):
    cur = conn.cursor()
    id = input('조회할 회원 ID : ')
    cur.execute('SELECT * FROM userTable WHERE id=%s', (id,))
    row = cur.fetchone()

    if row:
        print("ID     비밀번호    이름     이메일     주소")
        print("------------------------------------------")
        print(f'{row[0]:10}   {row[1]:12}   {row[2]:10}   {row[3]:15}   {row[4]:15}')
    else:
        print('해당 ID는 존재하지 않습니다.')

    conn.commit()
    conn.close()


# 사용자 전체 조회
def select_all_user(conn):
    cur = conn.cursor()

    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()
    print("ID     비밀번호    이름     이메일     주소")
    print("------------------------------------------")
    for row in rows:
        print(f'{row[0]:10}   {row[1]:12}   {row[2]:10}   {row[3]:15}   {row[4]:15}')

    conn.commit()
    conn.close()


# 메뉴 출력
def print_menu():
    print('\n===== 사용자 관리 메뉴 =====')
    print('1. 사용자 추가')
    print('2. 사용자 수정')
    print('3. 사용자 삭제')
    print('4. 사용자 조회')
    print('5. 사용자 전체 조회')
    print('0. 종료')
    print('==========================')


def main():
    conn = get_connection() # DB 연결
    create_user_table(conn) # 테이블 생성
    conn = get_connection() # DB 연결
    insert_user(conn)       # 초기 회원 정보 삽입

    while True:
        conn = get_connection()
        print_menu()
        choice = input('선택: ')

        if choice == '1':
            conn = get_connection()
            new_user_insert(conn)
        elif choice == '2':
            conn = get_connection()
            update_user(conn)
        elif choice == '3':
            conn = get_connection()
            delete_user(conn)
        elif choice == '4':
            conn = get_connection()
            search_user(conn)
        elif choice == '5':
            conn = get_connection()
            select_all_user(conn)
        elif choice == '0':
            print('종료합니다.')
            break
        else:
            print('잘못 입력 하셨습니다. 다시 입력 해주세요.')


if __name__ == '__main__':
    main()