import pymysql

# 1. DB 연결
conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                       password="12341234", db="mysqlDB", charset="utf8")
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

# 3. 초기 데이터 삽입
users = [
    ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
    ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
    ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
    ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
    ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구')
]

for user in users:
    cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

# 4. 커밋 및 연결 종료
conn.commit()
conn.close()