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


SELECT b.mem_id AS `아이디`, m.mem_name AS `이름`, b.prod_name AS `제품 이름`, m.addr AS `주소`, CONCAT(m.phone1, m.phone2) AS 연락처
FROM buy b
INNER JOIN member m
	ON b.mem_id = m.mem_id;