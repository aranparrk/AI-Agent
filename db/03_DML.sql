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

SELECT * FROM test_info1;

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

INSERT INTO test_info3 VALUES (NULL, '원이', '서울 강동구', '여', 22);
INSERT INTO test_info3 VALUES (NULL, '미나미', '서울 강서구', '여', 21);
INSERT INTO test_info3 VALUES (NULL, '리브', '서울 강남구', '여', 21);
INSERT INTO test_info3 VALUES (NULL, '메이', '서울 강동구', '여', 19);
INSERT INTO test_info3 VALUES (NULL, '제나', '서울 용산구', '여', 19);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('권지용', '경기 수원시', '남', 40);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('동영배', '경기 평택시', '남', 41);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('강대성', '경기 화성시', '남', 38);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('박지훈', '경기 이천시', '남', 26);
INSERT INTO test_info3 (user_name, addr, gender, age) VALUES ('최우식', '경기 양주시', '남', 38);

SELECT * FROM test_info3;

-- 수정 UPDATE
UPDATE test_info3
SET user_name = '장원영'
WHERE user_name = '박지훈';

UPDATE test_info3 
SET addr = '경기도 수원시', age = 18
WHERE user_name = '리브';

-- 이름이 '우식'인 회원의 나이를 30으로 수정하세요.
UPDATE test_info3
SET age = 30
WHERE user_name = '최우식';

SELECT * FROM test_info3 WHERE user_name = '최우식';

-- 나이가 20세 미만인 회원의 주소를 '주소 미상'으로 일괄 수정하세요.
UPDATE test_info3
SET addr = '주소 미상'
WHERE age < 20;

SELECT * FROM test_info3 WHERE age < 20;

-- 성별이 '여'인 회원의 나이를 1씩 증가시키세요.
UPDATE test_info3
SET age = age + 1
WHERE gender = '여';

SELECT * FROM test_info3 WHERE gender = '여';

-- test_id가 3번인 회원의 이름과 주소를 동시에 '지은', '대전시 유성구'로 수정하세요.
UPDATE test_info3
SET user_name = '지은', addr = '대전시 유성구'
WHERE user_id = 13;

SELECT * FROM test_info3 WHERE user_id = 3;

-- 주소에 '서울'이 포함된 회원의 성별을 모두 '여'로 수정하세요.
UPDATE test_info3
SET gender = '여'
WHERE addr LIKE '%서울%';

SELECT * FROM test_info3 WHERE addr LIKE '%서울%';

-- 삭제 DELETE
DELETE FROM test_info3;


-- test_id가 15번인 회원을 삭제하세요.
DELETE FROM test_info3
WHERE user_id = 15;

SELECT * FROM test_info3 WHERE user_id = 15;

-- 나이가 20세 미만인 회원을 모두 삭제하세요.
DELETE FROM test_info3
WHERE age < 20;

SELECT * FROM test_info3 WHERE age < 20;

-- 이름이 '메이'인 회원을 삭제하세요.
DELETE FROM test_info3
WHERE user_name = '메이';

SELECT * FROM test_info3 WHERE user_name = '메이';

-- 성별이 '남'이면서 나이가 22세 이상인 회원을 삭제하세요.
DELETE FROM test_info3
WHERE gender = '남' AND age >= 22;

SELECT * FROM test_info3 WHERE gender = '남' AND age >= 22;

-- 주소에 '강서구'가 포함된 회원을 모두 삭제하세요.
DELETE FROM test_info3
WHERE addr LIKE '%강서구%';

SELECT * FROM test_info3 WHERE addr LIKE '%강서구%';

