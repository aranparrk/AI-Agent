CREATE shop_db;

USE shop_db;

CREATE TABLE member -- 회원 테이블
(
  mem_id      CHAR(8) NOT NULL PRIMARY KEY, 	-- 회원 아이디(PK)
  mem_name    VARCHAR(10) NOT NULL,         	-- 이름
  mem_number  INT NOT NULL,                 	-- 인원수
  addr        CHAR(2) NOT NULL,             	-- 지역(예: 서울, 경기)
  phone1      CHAR(3),                      	-- 국번(02, 031 등)
  phone2      CHAR(8),                      	-- 전화번호 뒷자리
  height      SMALLINT,                     	-- 평균 키
  debut_date  DATE                          	-- 데뷔 일자
);


CREATE TABLE buy -- 구매 테이블
(
  num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
  mem_id      CHAR(8) NOT NULL,                        	-- 회원 아이디(FK)
  prod_name   CHAR(6) NOT NULL,                        	-- 제품 이름
  group_name  CHAR(4),                                 		-- 분류
  price       INT NOT NULL,                            	-- 가격
  amount      SMALLINT NOT NULL,                       	-- 수량
  FOREIGN KEY (mem_id) REFERENCES member(mem_id)       	-- 회원 테이블 참조
);


INSERT INTO member
VALUES
('TWC', '트와이스', 9, '서울', '02', '11111111', 167, '2015.10.19'),
('WMN', '여자친구', 6, '경기', '031', '33333333', 166, '2015.01.15'),
('OMY', '오마이걸', 7, '서울', NULL, NULL, 160, '2015.04.21'),
('GRL', '소녀시대', 8, '서울', '02', '44444444', 168, '2007.08.02'),
('ITZ', '잇지', 5, '경남', NULL, NULL, 167, '2019.02.12'),
('RED', '레드벨벳', 4, '경북', '054', '55555555', 161, '2014.08.01'),
('APN', '에이핑크', 6, '경기', '031', '77777777', 164, '2011.02.10'),
('SPC', '우주소녀', 13, '서울', '02', '88888888', 162, '2016.02.25'),
('ESP', '에스파', 4, '전남', '061', '99999999', 165, '2019.06.19'),
('BLK', '블랙핑크', 4, '경남', '055', '22222222', 163, '2016.08.08');

INSERT INTO buy
VALUES
(NULL, 'BLK', '지갑', NULL, 30, 2),
(NULL, 'BLK', '맥북프로', '디지털', 1000, 1),
(NULL, 'APN', '아이폰', '디지털', 200, 1),
(NULL, 'BLK', '청바지', '패션', 50, 3),
(NULL, 'GRL', 'SQL', '서적', 15, 5),
(NULL, 'APN', 'JAVA', '서적', 15, 2),
(NULL, 'GRL', 'Vue', '서적', 15, 2),
(NULL, 'APN', '청바지', '패션', 50, 1),
(NULL, 'APN', '리액트', '서적', 15, 1);

-- 테이블의 모든 데이터 조회

SELECT * FROM member;

SELECT * FROM buy;

-- 특정 열만 조회 : mem_name, addr
SELECT mem_name, addr FROM member;

-- 이름, 주소, 전화번호, 키, 데뷔일자
SELECT mem_name, addr, CONCAT(phone1, phone2), height, debut_date FROM member;

-- 
SELECT mem_id, prod_name FROM buy;
