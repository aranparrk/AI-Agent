CREATE TABLE test_member (
	id 		CHAR(8) NOT NULL,
	name 	VARCHAR(10) NOT NULL,
	height  TINYINT UNSIGNED
);

ALTER TABLE test_member
ADD CONSTRAINT
PRIMARY KEY (id);

DESC test_member;

-- 외래키 제약 조건
CREATE TABLE test_buy (
	num 		INT AUTO_INCREMENT PRIMARY KEY,
	mem_id 		CHAR(8) NOT NULL,
	prod_name 	CHAR(8) NOT NULL,
	FOREIGN KEY (mem_id) REFERENCES test_member(id)
);

DESC test_buy;

-- ===========================================================================================
-- 실습 문제 1 : NOT NULL, DEFAULT
-- 
-- 회원의 정보를 저장할 수 있는 user_profile 테이블을 생성하세요. 다음 조건을 만족해야 합니다.
-- 
-- - user_id: 기본키
-- - username: 반드시 입력되어야 함 (NULL 불가)
-- - nation: 기본값은 ‘KOREA’로 설정되며, 생략 시 자동 입력됨
-- ===========================================================================================
CREATE TABLE user_profiled (
	user_id 	INT PRIMARY KEY,
	username 	VARCHAR(5) NOT NULL,
	nation 		VARCHAR(5) DEFAULT 'KOREA'
);

-- ===========================================================================================
-- 실습 문제 2 : UNIQUE, CHECK
-- 
-- 학생의 정보를 저장하는 student 테이블을 생성하세요. 조건은 다음과 같습니다.
-- 
-- - student_id: 기본키
-- - email: 중복되면 안 됨 (고유 이메일)
-- - age: 18세 이상만 입력 가능해야 함
-- ===========================================================================================
CREATE TABLE student (
	student_id 	INT PRIMARY KEY,
	email		VARCHAR(20) UNIQUE,
	age			INT CHECK (age >= 18)
);

-- ===========================================================================================
-- 실습 문제 3 : FOREIGN KEY와 참조 무결성
-- 
-- 회사 부서(department)와 직원(employee) 정보를 저장하는 두 테이블을 생성하세요.
-- 
-- - department: dept_id를 기본키로 사용
-- - employee: emp_id를 기본키로 사용하며, dept_id는 반드시 department 테이블에 존재하는 값만 가능해야 함
-- ===========================================================================================
CREATE TABLE department (
	dept_id INT PRIMARY KEY
);

CREATE TABLE employee (
	emp_id INT PRIMARY KEY,
	FOREING KEY (emp_id) REFERENCES department(dept_id)
);

-- ===========================================================================================
-- 실습 문제 4 : ON DELETE CASCADE
-- 
-- 회원이 탈퇴하면 그 회원의 주문도 함께 삭제되도록 설정된 member - orders 테이블을 작성하세요.
-- 
-- - member: mem_id를 기본키로
-- - orders: order_id는 자동 증가, mem_id는 member의 외래키이며, 삭제 시 연쇄 삭제됨
-- ===========================================================================================
CREATE TABLE member (
	mem_id INT PRIMARY KEY
);

CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	mem_id INT,
	FOREIGN KEY (mem_id) REFERENCES member(mem_id) ON DELETE CASCADE
);

-- ===========================================================================================
-- 실습 문제 5 : 복합키, CHECK, UNIQUE
-- 
-- 수강 신청 테이블 enroll을 만드세요. 조건은 다음과 같습니다.
-- 
-- - student_id + course_id 조합이 기본키 (복합키)
-- - grade는 A, B, C, D, F 중 하나만 허용
-- - 동일 학생은 동일한 성적으로 여러 과목을 신청할 수 없음
-- ===========================================================================================\
CREATE TABLE enroll (
    student_id INT,
    course_id INT,
    grade CHAR(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F')),
    PRIMARY KEY (student_id, course_id),
    UNIQUE (student_id, grade)
);