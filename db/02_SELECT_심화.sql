SELECT mem_id, mem_name, debut_date
FROM member
ORDER BY debut_date DESC;

-- 키가 164이상이고 데뷔일자 기준 내림 차순 정렬 
SELECT mem_id, mem_name, debut_date
FROM member
WHERE height >= 164
ORDER BY debut_date DESC;

-- 키가 164이상이고 데뷔일자 기준 내림 차순, 그리고 이름기준으로 오름차순 정렬
SELECT * FROM member 
WHERE height >= 164
ORDER BY debut_date DESC, mem_name;

-- 키가 164이상이고 데뷔일자 기준 내림 차순, 상위 3개만 출력
SELECT * FROM member
WHERE height >= 164
ORDER BY debut_date DESC
LIMIT 3;

-- 중복 제거 : DISTINCT, 결과에서 중복된 행을 제거함
SELECT addr FROM member;

SELECT DISTINCT addr FROM member;

-- 그룹화 및 집계함수 : GROUP BY + 집계 함수
SELECT COUNT(*) FROM member; -- NULL 포함
SELECT COUNT(phone1) FROM member; -- NULL 제외

-- 멤버 전체의 키 평균 구하기
SELECT AVG(height) AS 평균키 FROM member;

-- 멤버 전체에서 가장 큰 키 구하기
SELECT MAX(height) AS 최대키 FROM member;

-- 멤버 전체에서 가장 작은 키 구하기
SELECT MIN(height) AS 최저키 FROM member; 

-- 키가 가장 큰 그룹의 이름
SELECT * FROM member;

SELECT mem_name, height
FROM member
ORDER BY height DESC
LIMIT 1;

-- 키가 가장 작은 그룹의 이름
SELECT mem_name, height
FROM member
ORDER BY height
LIMIT 1;

-- 전체 회원의 총 구매 개수 
SELECT SUM(amount) FROM buy;

-- 회원별 총 구매 개수
SELECT mem_id, SUM(amount) FROM buy
GROUP BY mem_id;

-- 회원별 총 구매 금액
SELECT mem_id AS `회원 아이디`, SUM(price * amount) AS `총 구매 금액` FROM buy
GROUP BY mem_id;

-- 전체 평균 구매 개수
SELECT AVG(amount) AS `평균 구매 개수` FROM buy;

-- 회원별 평균 구매 개수
SELECT mem_id AS `회원 아이디`, AVG(amount) AS `평균 구매 개수` FROM buy
GROUP BY mem_id;

-- GROUP BY 다중 열 지정하기
SELECT mem_id, prod_name, SUM(amount) AS `상품별 구매개수` FROM buy
GROUP BY mem_id, prod_name;

-- 회원별 총구매 금액을 구하고, 구매 금액이 1000원을 초과하는 것만 출력하기
SELECT mem_id, SUM(PRICE * AMOUNT) AS `total_price` FROM buy
GROUP BY mem_id
HAVING total_price > 1000;

---------------------------------------------------------------------------
-- 실습문제
---------------------------------------------------------------------------

-- 문제1 : 키(height)가 165 이상인 회원을 debut_date 내림차순으로 정렬하여 5명만 출력하세요.
SELECT * FROM member
WHERE height >= 165
ORDER BY debut_date DESC
LIMIT 5;

-- 문제2 : 지역(addr)의 중복 없는 고유값 목록을 출력하세요.
SELECT DISTINCT addr FROM member;
 
-- 문제3 : 구매 테이블에서 회원별 평균 구매 개수가 3 이상인 회원만 출력하고, 평균값 기준으로 내림차순 정렬하세요.
SELECT mem_id, AVG(amount) FROM buy
GROUP BY mem_id
HAVING AVG(amount) >= 3
ORDER BY AVG(amount) DESC;
 
-- 문제4 : 회원별 총 구매 금액을 계산하고, 1000원 이상인 회원만 출력하세요.
SELECT mem_id, SUM(price * amount) FROM buy
GROUP BY mem_id
HAVING SUM(price * amount) >= 1000;
 
-- 문제5 : 회원 테이블에서 mem_id와 mem_name을 조회하되, 이름이 '에'으로 시작하는 회원만 오름차순으로 정렬하여 출력하세요.
SELECT mem_id, mem_name FROM member
WHERE mem_name LIKE '에%'
ORDER BY mem_name;

-- 문제6 : 구매 테이블에서 회원별, 상품별 구매 개수를 구하고, 구매 개수가 2개 이상인 경우만 출력하세요.
SELECT mem_id, SUM(amount) FROM buy
GROUP BY mem_id
HAVING SUM(amount) >= 2;