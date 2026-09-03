-- ======================================================================================
-- 조인 : 정규화로 나누어져 있는 여러개의 테이블을 묶어서 원하는 정보를 가져 오는 것
-- 내부 조인 : 양쪽 테이블 모두에 데이터가 존재하는 경우만 결과 반환, 
-- 			   두 테이블의 공통된 키를 기준으로 데이터를 결합
-- 
-- SELECT 	   열목록
-- FROM   	   테이블1
-- 	INNER JOIN 테이블2
--	ON		   테이블1.열 = 테이블2.열
-- [WHERE 조건]
-- 
-- ======================================================================================

SELECT buy.mem_id, member.mem_name, buy.prod_name, member.addr, CONCAT(member.phone1, member.phone2) AS 연락처
FROM buy AS b
	INNER JOIN member AS m
	ON buy.mem_id = member.mem_id;

-- INNER JOIN, 별칭 부여, 동등 컬럼 연결
SELECT b.mem_id AS `아이디`, m.mem_name AS `이름`, b.prod_name AS `제품 이름`, m.addr AS `주소`, CONCAT(m.phone1, m.phone2) AS 연락처
FROM buy b
INNER JOIN member m
	ON b.mem_id = m.mem_id;

-- OURTER JOIN : 한쪽 테이블에만 데이터가 있어도 결과로 포함
SELECT m.mem_id, m.mem_name, b.prod_name, m.addr
FROM member m
LEFT JOIN buy b
	ON m.mem_id = b.mem_id
ORDER BY m.mem_id;

-- 실전예제 : 구매 이력이 없는 회원 찾기
SELECT DISTINCT m.mem_id, m.mem_name, m.addr
FROM member m
LEFT JOIN buy b
	ON m.mem_id = b.mem_id
WHERE b.prod_name IS NULL
ORDER BY m.mem_id;

-- =============================================================
-- 1번 문제 – 내부 조인 기본
-- 
-- 회원과 구매 테이블을 내부 조인하여
-- 회원 이름, 구매한 상품명, 연락처를 출력하세요.
-- 
-- 연락처는 CONCAT(phone1, phone2)로 출력하세요.
-- =============================================================

SELECT m.mem_name AS `회원 이름`, b.prod_name AS `구매한 상품명`, CONCAT(m.phone1, m.phone2) AS `연락처`
FROM member m
INNER JOIN buy b
	ON m.mem_id = b.mem_id;

-- =============================================================
-- 2번 문제 – 외부 조인 활용
-- 
-- 구매 이력이 없는 회원의 ID, 이름, 주소를 출력하세요.
-- 결과는 회원 ID 오름차순으로 정렬하세요.
-- =============================================================
SELECT m.mem_id AS `회원ID`, m.mem_name AS `이름`, m.addr AS `주소`
FROM member m
LEFT JOIN buy b
	ON m.mem_id = b.mem_id
WHERE b.prod_name IS NULL
ORDER BY m.mem_id;

-- =============================================================
-- 3번 문제 – 조인 + 집계
-- 
-- 각 회원이 구매한 상품 개수를 구하세요.
-- 회원 이름과 구매 횟수를 출력하고, 구매 수가 많은 순으로 정렬하세요.
-- =============================================================
SELECT m.mem_name AS `회원 이름`, COUNT(b.amount) AS `구매 횟수`
FROM member m
INNER JOIN buy b
	ON m.mem_id = b.mem_id 
GROUP BY m.mem_id
ORDER BY `구매 횟수` DESC;

-- =============================================================
-- 4번 문제 – 자체 조인(Self Join)
-- 
-- 걸그룹 멤버 테이블에서 멤버 이름과 그 리더의 이름을 출력하세요.
-- =============================================================

CREATE TABLE girlgroup_members (
  member_id    INT PRIMARY KEY,
  member_name  VARCHAR(20) NOT NULL,
  leader_id    INT,
  FOREIGN KEY (leader_id) REFERENCES girlgroup_members(member_id)
);

INSERT INTO girlgroup_members (member_id, member_name, leader_id) VALUES
(1, '아이린',   NULL),  -- 레드벨벳 리더
(2, '슬기',     1),
(3, '웬디',     1),
(4, '조이',     1),
(5, '예리',     1),
(6, '태연',     NULL),  -- 소녀시대 리더
(7, '윤아',     6),
(8, '써니',     6);

SELECT * FROM girlgroup_members

SELECT m.member_name AS `멤버 이름`, l.member_name AS `리더 이름` FROM girlgroup_members m
INNER JOIN girlgroup_members l
	ON l.member_id = m.leader_id;

-- =============================================================
-- 5번 문제 – 외부 조인 실전 (LEFT JOIN 종합)
-- 
-- 회원과 구매 테이블을 외부 조인하여
-- 회원 이름, 주소, 상품명, 구매금액(가격 × 수량) 출력
-- (구매 기록이 없는 회원도 포함하세요)
-- =============================================================
SELECT m.mem_name AS `회원 이름`, m.addr AS `주소`, b.prod_name AS `상품명`, (b.price * b.amount) AS `구매 금액`
FROM member m
LEFT JOIN buy b
	ON m.mem_id = b.mem_id;

-- =============================================================
-- 6번 문제 – RIGHT JOIN
-- 
-- buy 테이블을 기준으로 RIGHT JOIN을 사용해
-- 모든 회원의 이름과 구매한 상품명을 출력하세요 (구매 기록 없는 회원도 포함).
-- =============================================================
SELECT m.mem_name AS `회원 이름`, b.prod_name AS `상품명`
FROM buy b
RIGHT JOIN member m
	ON b.mem_id = m.mem_id;

-- =============================================================
-- 7번 문제 – FULL OUTER JOIN 흉내내기
-- 
-- member와 buy 두 테이블을 UNION을 사용해 FULL OUTER JOIN처럼
-- 회원 ID, 이름, 상품명을 출력하세요.
-- =============================================================
SELECT *
FROM member m
LEFT JOIN buy b
	ON m.mem_id = b.mem_id
UNION
SELECT *
FROM member m
RIGHT JOIN buy b
	ON m.mem_id = b.mem_id;

-- =============================================================
-- 8번 문제 – SELF JOIN 심화 (리더 본인 포함)
-- 
-- 걸그룹 멤버 테이블에서 모든 멤버의 이름과 리더 이름을 출력하되
-- 리더 본인은 리더 컬럼을 NULL로 출력되게 하세요.
-- =============================================================
SELECT l.member_name AS `멤버 이름`, m.member_name AS `리더 이름`
FROM girlgroup_members m
RIGHT JOIN girlgroup_members l
	ON m.member_id = l.leader_id;

-- =============================================================
-- 9번 문제 – 조인 + 집계 + 조건절
-- 
-- 100원 이상 구매한 회원만 대상으로
-- 회원 이름과 총 구매금액(가격×수량 합계)을 구해 출력하고, 금액이 높은 순으로 정렬하세요.
-- =============================================================
SELECT m.mem_name AS `회원 이름`, SUM(b.price * b.amount) AS `총 구매금액`
FROM member m
INNER JOIN buy b
	ON m.mem_id = b.mem_id
GROUP BY m.mem_id
HAVING SUM(b.price * b.amount) > 100
ORDER BY SUM(b.price * b.amount) DESC;

-- =============================================================
-- 10번 문제 – 종합 (자체 조인 + 집계)
-- 
-- 각 리더별로 소속 멤버 수(본인 제외)를 구하세요.
-- 리더 이름과 소속 멤버 수를 출력하고, 멤버 수가 많은 순으로 정렬하세요.
-- =============================================================
SELECT l.member_name AS `리더 이름`, COUNT(m.member_id) AS `멤버 수`
FROM girlgroup_members l
INNER JOIN girlgroup_members m
	ON l.member_id = m.leader_id
GROUP BY l.member_id, l.member_name
ORDER BY `멤버 수` DESC;