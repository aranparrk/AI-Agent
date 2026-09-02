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

SELECT * FROM test_info2;

