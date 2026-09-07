-- 집합 연산자 : 두 개 이상의 SELECT 결과를 위아래로 쳐서 하나의 결과로 만드는 연산자
SELECT mem_name, addr FROM member WHERE addr = '서울'
UNION
SELECT mem_name, addr FROM member WHERE addr = '경기';


SELECT mem_name, addr FROM member WHERE addr = '서울'
UNION ALL
SELECT mem_name, addr FROM member WHERE addr = '경기';

-- 문제 1 : 키가 165이상인 회원과 지역이 '경기'인 회원을 UNION으로 합쳐서 중복없이 출력하세요.
SELECT * FROM member WHERE height >= 165
UNION
SELECT * FROM member WHERE addr = '경기';

-- 문제 2 : 위 문제와 동일한 조건이지만, 중복을 제거하지 않고 모두 출력하세요.
SELECT * FROM member WHERE height >= 165
UNION ALL
SELECT * FROM member WHERE addr = '경기';
