-- =========================================================
-- DML (Data Manipulation Language) : 데이터 조작
-- 새로 가입한 회원을 테이블에 추가 할 때 INSERT
-- 회원의 주소나 연락처가 변경되어 정보를 수정 할 때 UPDATE
-- 회원이 탈퇴해서 회원을 삭제 할 때 DELETE
-- =========================================================

-- TABLE 생성 (DDL)
CREATE TABLE test_info1 (
	test_id 	INT,
	test_name 	CHAR(5),
	test_age 	INT
);

-- 데이터 삽입 (DML)
INSERT INTO test_info1 (test_id, test_name) VALUES (1, '장원영'); -- 속성을 선택해서 넣는 경우
INSERT INTO test_info1 VALUES (2, '안유진', 23); -- 모든 속성을 넣어야 함

SELECT * FROM test_info1

-- 8개의 데이터를 추가
INSERT INTO test_info1 VALUES (3, '리즈', 23);
INSERT INTO test_info1 VALUES (4, '가을', 24);
INSERT INTO test_info1 VALUES (5, '이서', 18);
INSERT INTO test_info1 (test_id, test_name) VALUES (6, '남규리');
INSERT INTO test_info1 (test_id, test_name) VALUES (7, '이보람');
INSERT INTO test_info1 (test_id, test_name) VALUES (8, '김연지');

-- 자동 증가 열 : AUTO_INCREMENT
CREATE TABLE test_info2 (
	test_id 	INT AUTO_INCREMENT PRIMARY KEY,
	test_name 	CHAR(5),
	test_age 	INT
);

INSERT INTO test_info2 VALUES (NULL, '원이', 20);
INSERT INTO test_info2 (test_name, test_age) VALUES ('리브', 20);
INSERT INTO test_info2 VALUES (NULL, '메이', 19);
INSERT INTO test_info2 VALUES (NULL, '미나미', 19);
INSERT INTO test_info2 VALUES (NULL, '제나', 18);
INSERT INTO test_info2 (test_name, test_age) VALUES ('박지훈', 24);
INSERT INTO test_info2 (test_name, test_age) VALUES ('장동윤', 18);
INSERT INTO test_info2 (test_name, test_age) VALUES ('최우식', 20);

SELECT * FROM test_info2;

-- test_info3
-- 아이디(INT, PK, AUTO_INCREMENT), 이름(5), 주소(20), 성별(2), 나이(INT)
-- 데이터 10개 추가 하기
CREATE TABLE test_info3 (
	user_id 	INT AUTO_INCREMENT PRIMARY KEY,
	user_name 	CHAR(5),
	addr 		CHAR(20),
	gender 		CHAR(2),
	age 		INT	
);

INSERT INTO test_info3 VALUES (NULL, '원이', '서울 강동구', '여자', 22);
INSERT INTO test_info3 VALUES (NULL, '미나미', '서울 강서구', '여자', 21);
INSERT INTO test_info3 VALUES (NULL, '리브', '서울 강남구', '여자', 21);
INSERT INTO test_info3 VALUES (NULL, '메이', '서울 강동구', '여자', 19);
INSERT INTO test_info3 VALUES (NULL, '제나', '서울 용산구', '여자', 19);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('권지용', '경기 수원시', '남자', 40);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('동영배', '경기 평택시', '남자', 41);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('강대성', '경기 화성시', '남자', 38);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('박지훈', '경기 이천시', '남자', 26);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('최우식', '경기 양주시', '남자', 38);

SELECT * FROM test_info3;
