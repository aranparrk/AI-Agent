--------------------------------------------------------------------------------
-- 1. 정렬 : ORDER BY / LIMIT
--------------------------------------------------------------------------------

-- 데뷔일자 기준 내림차순 정렬
SELECT
    mem_id,
    mem_name,
    debut_date
FROM member
ORDER BY debut_date DESC;


-- 키가 164 이상이고 데뷔일자 기준 내림차순 정렬
SELECT
    mem_id,
    mem_name,
    debut_date
FROM member
WHERE height >= 164
ORDER BY debut_date DESC;


-- 키가 164 이상이고
-- 데뷔일자 기준 내림차순, 이름 기준 오름차순 정렬
SELECT *
FROM member
WHERE height >= 164
ORDER BY debut_date DESC, mem_name;


-- 키가 164 이상이고 데뷔일자 기준 내림차순,
-- 상위 3개만 출력
SELECT *
FROM member
WHERE height >= 164
ORDER BY debut_date DESC
LIMIT 3;


--------------------------------------------------------------------------------
-- 2. 중복 제거 : DISTINCT
--------------------------------------------------------------------------------

-- 주소 전체 조회
SELECT addr
FROM member;


-- 중복된 주소 제거
SELECT DISTINCT addr
FROM member;


--------------------------------------------------------------------------------
-- 3. 집계 함수 : COUNT / AVG / MAX / MIN / SUM
--------------------------------------------------------------------------------

-- 전체 회원 수 : NULL 포함
SELECT COUNT(*)
FROM member;


-- phone1 값이 있는 회원 수 : NULL 제외
SELECT COUNT(phone1)
FROM member;


-- 전체 회원의 평균 키
SELECT AVG(height) AS `평균 키`
FROM member;


-- 전체 회원 중 가장 큰 키
SELECT MAX(height) AS `최대 키`
FROM member;


-- 전체 회원 중 가장 작은 키
SELECT MIN(height) AS `최소 키`
FROM member;


-- 키가 가장 큰 회원
SELECT
    mem_name,
    height
FROM member
ORDER BY height DESC
LIMIT 1;


-- 키가 가장 작은 회원
SELECT
    mem_name,
    height
FROM member
ORDER BY height
LIMIT 1;


-- 전체 구매 개수
SELECT SUM(amount) AS `총 구매 개수`
FROM buy;


-- 전체 평균 구매 개수
SELECT AVG(amount) AS `평균 구매 개수`
FROM buy;


--------------------------------------------------------------------------------
-- 4. 그룹화 : GROUP BY
--------------------------------------------------------------------------------

-- 회원별 총 구매 개수
SELECT
    mem_id,
    SUM(amount) AS `총 구매 개수`
FROM buy
GROUP BY mem_id;


-- 회원별 총 구매 금액
SELECT
    mem_id AS `회원 아이디`,
    SUM(price * amount) AS `총 구매 금액`
FROM buy
GROUP BY mem_id;


-- 회원별 평균 구매 개수
SELECT
    mem_id AS `회원 아이디`,
    AVG(amount) AS `평균 구매 개수`
FROM buy
GROUP BY mem_id;


-- 회원별 + 상품별 구매 개수
SELECT
    mem_id,
    prod_name,
    SUM(amount) AS `상품별 구매 개수`
FROM buy
GROUP BY mem_id, prod_name;


--------------------------------------------------------------------------------
-- 5. 그룹 조건 : HAVING
--------------------------------------------------------------------------------

-- 회원별 총 구매 금액을 구하고,
-- 총 구매 금액이 1000원을 초과하는 회원만 조회
SELECT
    mem_id,
    SUM(price * amount) AS total_price
FROM buy
GROUP BY mem_id
HAVING total_price > 1000;


--------------------------------------------------------------------------------
-- 6. 실습 문제
--------------------------------------------------------------------------------

-- 문제 1
-- 키(height)가 165 이상인 회원을
-- debut_date 내림차순으로 정렬하여 5명만 출력
SELECT *
FROM member
WHERE height >= 165
ORDER BY debut_date DESC
LIMIT 5;


-- 문제 2
-- 지역(addr)의 중복 없는 고유값 목록 출력
SELECT DISTINCT addr
FROM member;


-- 문제 3
-- 회원별 평균 구매 개수가 3 이상인 회원만 출력하고,
-- 평균값 기준 내림차순 정렬
SELECT
    mem_id,
    AVG(amount) AS avg_amount
FROM buy
GROUP BY mem_id
HAVING avg_amount >= 3
ORDER BY avg_amount DESC;


-- 문제 4
-- 회원별 총 구매 금액을 계산하고,
-- 1000원 이상인 회원만 출력
SELECT
    mem_id,
    SUM(price * amount) AS total_price
FROM buy
GROUP BY mem_id
HAVING total_price >= 1000;


-- 문제 5
-- mem_id와 mem_name을 조회하되,
-- 이름이 '에'로 시작하는 회원만 이름 기준 오름차순 정렬
SELECT
    mem_id,
    mem_name
FROM member
WHERE mem_name LIKE '에%'
ORDER BY mem_name;


-- 문제 6
-- 회원별, 상품별 구매 개수를 구하고,
-- 구매 개수가 2개 이상인 경우만 출력
SELECT
    mem_id,
    prod_name,
    SUM(amount) AS total_amount
FROM buy
GROUP BY mem_id, prod_name
HAVING total_amount >= 2;


-- 전체 회원 수와
-- addr이 NULL이 아닌 회원 수 조회
SELECT
    COUNT(*) AS `전체 회원 수`,
    COUNT(addr) AS `주소가 있는 회원 수`
FROM member;


-- 상품별 총 판매 금액을 구하고,
-- 금액이 큰 순서로 상위 3개 상품 출력
SELECT
    prod_name,
    SUM(price * amount) AS total_price
FROM buy
GROUP BY prod_name
ORDER BY total_price DESC
LIMIT 3;


-- 키(height)가 4번째로 큰 회원부터 2명 출력
SELECT *
FROM member
ORDER BY height DESC
LIMIT 3, 2;


-- 회원별로 서로 다른 상품을 몇 종류 구매했는지 조회
SELECT
    mem_id,
    COUNT(DISTINCT prod_name) AS `구매 상품 종류 수`
FROM buy
GROUP BY mem_id;


-- 상품별 평균 가격을 구하고,
-- 평균 가격이 50원을 초과하는 상품만 조회
SELECT
    prod_name,
    AVG(price) AS `평균 가격`
FROM buy
GROUP BY prod_name
HAVING `평균 가격` > 50;


--------------------------------------------------------------------------------
-- 7. 서브쿼리
-- 하나의 SQL문 안에 포함된 또 다른 SELECT문
-- 괄호로 감싸서 사용
-- WHERE / FROM / SELECT 절 등에 사용할 수 있음
--------------------------------------------------------------------------------

-- 평균 키보다 큰 회원 조회
SELECT
    mem_name,
    height
FROM member
WHERE height > (
    SELECT AVG(height)
    FROM member
);


-- 평균 구매 가격보다 비싼 구매 내역 조회
SELECT *
FROM buy
WHERE price > (
    SELECT AVG(price)
    FROM buy
);


-- 평균 키보다 작은 회원 조회
SELECT
    mem_name,
    height
FROM member
WHERE height < (
    SELECT AVG(height)
    FROM member
);


-- 가장 최근 데뷔한 회원보다 먼저 데뷔한 회원 조회
SELECT *
FROM member
WHERE debut_date < (
    SELECT MAX(debut_date)
    FROM member
)
ORDER BY debut_date;


-- 최소 구매 가격과 같은 구매 내역 조회
SELECT *
FROM buy
WHERE price = (
    SELECT MIN(price)
    FROM buy
);


-- 평균 구매 개수보다 많이 산 구매 내역 조회
SELECT *
FROM buy
WHERE amount > (
    SELECT AVG(amount)
    FROM buy
);