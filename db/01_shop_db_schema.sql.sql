CREATE DATABASE shop_db;

USE shop_db;

CREATE TABLE member (
	member_id CHAR(8) not null primary key,
	member_name CHAR(5) not null,
	member_addr CHAR(20)
);

CREATE TABLE product (
	product_name CHAR(4) NOT NULL PRIMARY KEY,
	cost INT NOT NULL,
	make_date DATE,
	company CHAR(5),
	amount INT NOT NULL	
);

-- 아이브(IVE) 멤버
INSERT INTO member (member_id, member_name, member_addr) 
VALUES ('M003', '장원영', '서울 성동구'),
		('M004', '안유진', '서울 서초구'),
		('M005', '레이', '서울 용산구'),
		('M006', '리즈', '경기 성남시'),
		('M007', '가을', '서울 종로구'),
		('M008', '이서', '경기 고양시');
		

-- 르세라핌(LE SSERAFIM) 멤버 
INSERT INTO member (member_id, member_name, member_addr)
VALUES ('M009', '사쿠라', '서울 강동구'),
		('M010', '채원', '서울 송파구'),
		('M011', '윤진', '경기 수원시'),
		('M012', '카즈하', '서울 마포구'),
		('M013', '은채', '경기 부천시');

-- 상품
INSERT INTO product (product_name, cost, make_date, company, amount)
VALUES ('아이폰', 1550000, '2025-09-20', '애플', 30),
		('갤럭시', 1350000, '2025-03-14', '삼성', 45),
		('아이패드', 899000, '2025-05-01', '애플', 25),
		('닌텐도', 350000, '2024-10-08', '닌텐', 60),
		('플스5', 678000, '2024-11-15', '소니', 20),
		('에어팟', 359000, '2025-02-10', '애플', 100),
		('노트북', 1450000, '2025-01-25', 'LG전', 15),
		('모니터', 320000, '2025-03-30', '삼성', 40),
		('스피커', 89000, '2025-04-18', '보스', 70),
		('충전기', 25000, '2025-05-05', '애플', 200);

SELECT * FROM member;

SELECT * FROM product;
