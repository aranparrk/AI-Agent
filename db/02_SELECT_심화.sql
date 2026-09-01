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