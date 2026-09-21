import pymysql

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="12341234", db="mysqlDB", charset="utf8")
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

def main():
    conn = get_connection()
    create_user_table(conn)
    conn = get_connection()
    insert_user(conn)

    while True:
        conn = get_connection()
        rst = new_user_insert(conn)
        if rst == 'exit': break



if __name__ == '__main__':
    main()