-- ============================================================================= 
-- 적절한 데이터형을 사용해 테이블 생성하기 : member_ex1
-- mem_id : 고정된 문자열 8자리, PK
-- mem_name : 가변 문자열 10자리, NULL 허용 하지 않음
-- mem_number : 정수타입, NULL 허용 하지 않음
-- addr : 지역 표기 (서울, 경기 등), 고정된 문자열 2자리, NULL 허용 하지 않음
-- phone1 : 국번은 고정된 문자열 3자리
-- phone2 : 나머지 전화 번호, 고정된 문자열 8자리
-- height : SMALLINT
-- debut_date : 날짜형 데이터 사용
-- =============================================================================

CREATE TABLE member_ex1 (
	mem_id 		CHAR(8) PRIMARY KEY,
	mem_name 	VARCHAR(10) NOT NULL,
	mem_number 	INT NOT NULL,
	addr 		CHAR(2) NOT NULL,
	phone1 		CHAR(3),
	phone2		CHAR(8),
	height		SMALLINT,
	debut_date	DATE
);

INSERT INTO member_ex1 VALUES ('TWC', '트와이스', 9, '서울', '02', '12345678', 162, '2015-10-20');
INSERT INTO member_ex1 VALUES ('BLK', '블랙핑크', 4, '경기', '031', '23456789', 163, '2016-08-08');
INSERT INTO member_ex1 VALUES ('WMD', '여자아이들', 6, '경남', '055', '34567890', 165, '2018-05-02');
INSERT INTO member_ex1 VALUES ('OMY', '오마이걸', 7, '서울', '02', '45678901', 164, '2015-04-21');
INSERT INTO member_ex1 VALUES ('GRLS', '걸스데이', 4, '충북', '043', '56789012', 166, '2010-07-09');
INSERT INTO member_ex1 VALUES ('APN', '에이핑크', 6, '경기', '031', '67890123', 161, '2011-04-19');
INSERT INTO member_ex1 VALUES ('SPC', '우주소녀', 13, '서울', '02', '78901234', 162, '2016-02-25');
INSERT INTO member_ex1 VALUES ('MOM', '마마무', 4, '전남', '061', '89012345', 168, '2014-06-19');
INSERT INTO member_ex1 VALUES ('IVEX', 'IVE', 6, '서울', '02', '90123456', 167, '2021-12-01');
INSERT INTO member_ex1 VALUES ('NJS', '뉴진스', 5, '경기', '031', '01234567', 163, '2022-07-22');

select * from member_ex1;

-- =============================================================================
-- 실습문제
-- =============================================================================

-- 다음 조건에 맞는 product_info 테이블을 만드세요.
-- product_id : 최대 32767까지만 저장 (음수 불필요)
-- product_name : 최대 20글자
-- price : 최대 21억까지 저장 가능한 정수
-- stock : 재고 수량, 음수가 될 수 없고 0~255 사이만 저장

-- CRUD 해보기 : INSERT, SELECT, UPDATE, DELETE 

CREATE TABLE product_info (
	product_id SMALLINT UNSIGNED,
	product_name VARCHAR(20),
	price INT,
	stock TINYINT UNSIGNED
);

INSERT INTO product_info 
VALUES (0001, '아이패드', 35000, 5),
		(0002, '맥북', 1500000, 3),
		(0003, '에어팟', 432000, 12),
		(0004, '아이폰', 1188800, 8),
		(0005, '갤럭시탭', 880000, 2),
		(0006, '애플워치', 550000, 15);

SELECT * FROM product_info

UPDATE product_info
SET stock = 2
WHERE product_name = '아이폰';

DELETE FROM product_info
WHERE stock = 2;