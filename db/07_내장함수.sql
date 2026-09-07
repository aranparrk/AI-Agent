-- MySQL 내장 함수 : MySQL이 기본적으로 제공하는 함수

-- CONCAT(a, b, c, ‥) --> 문자열 합치기
SELECT CONCAT('곰돌이', '님', '환영합니다.') AS `문자열 합치기`;

SELECT mem_name, CONCAT(phone1, phone2) AS `전화번호` FROM member;

-- LENGTH --> 문자 길이 구하기
SELECT LENGTH('안녕'); -- 바이트 6, 한글표기 방법 때문
SELECT CHAR_LENGTH('안녕');

SELECT LENGTH('AB');
SELECT CHAR_LENGTH('AB');

-- SUBSTRING(문자열, 시작위치, 크기) --> 부분 문자열 추출
SELECT SUBSTRING('20260904', 1, 4); -- 년
SELECT SUBSTRING('20260904', 5, 2); -- 월
SELECT SUBSTRING('20260904', 7, 2); -- 일

SELECT SUBSTRING('20260904', -3, 5);

-- REPLACE(str, from, to) --> 문자열 치환
SELECT REPLACE('자바 파이썬 자바스크립트 리액트', '자바', 'JAVA');

SELECT REPLACE('자바 파이썬 자바스크립트 리액트', '자바', '');

-- TRIM() --> 앞/뒤 공백 제거
SELECT TRIM('      안녕하세요.    만나서 반갑습니다.      ');

-- UPPER() / LOWER --> 대/소문자
SELECT UPPER('korea');
SELECT LOWER('JAPAN');

-- LPAD() / RPAD() --> 특정 문자 채우기
SELECT LPAD('1', 5, '-');
SELECT LPAD('12', 5, '-');
SELECT LPAD('123', 5, '-');

SELECT RPAD('010222-1', 13, '*');

SELECT RPAD('7', 3, '*');

SELECT RPAD(
    SUBSTRING(CONCAT(phone1, phone2), 1, CHAR_LENGTH(CONCAT(phone1, phone2)) - 3),
    CHAR_LENGTH(CONCAT(phone1, phone2)),
    '*' 
) AS `전화번호 마스킹`
FROM member;

-- ====================================================
-- 실습문제
-- ====================================================

-- 문제 1 : member 테이블에서 이름과 함께, 전화번호를 하이픈 없이 하나로 합쳐서 출력하세요. (컬럼명 : 전화번호)
SELECT mem_name AS `이름`, CONCAT(phone1, phone2) AS `전화번호` FROM member;

-- 문제 2 : member 테이블에서 이름의 글자 수(CHAR_LENGTH)와 바이트 수(LENGTH)를 함께 출력하세요.
SELECT CHAR_LENGTH(mem_name) AS `글자 수`, LENGTH(mem_name) AS `바이트 수` FROM member;

-- 문제 3 : member 테이블에서 debut_date(예 : '2015-10-19')에서 연도 4자리만 SUBSTRING으로 잘라 출력하세요.
SELECT SUBSTRING(debut_date, 1, 4) AS `데뷔년도` FROM member;

-- 문제 4 : buy 테이블에서 상품 이름(prod_name) 중 '청바지'를 'JEANS'로 바꿔서 출력하세요.
SELECT REPLACE(prod_name, '청바지', 'JEANS') AS `상품 이름` FROM buy;

-- 문제 5 : 이름 앞뒤에 공백이 섞인 문자열 ' 블랙핑크 '을 TRIM으로 정리해서 출력하세요.
SELECT TRIM(' 블랙핑크 ') AS `공백제거`;

-- 문제 6 : member 테이블에서 그룹 이름을 전부 대문자 영어처럼 보이도록(실습용) UPPER, LOWER을 각각 적용해 출력해보세요. (한글은 변화 없음을 확인하는 목적)
SELECT UPPER(mem_name) AS `대문자`, LOWER(mem_name) AS `소문자` FROM member;

-- 문제 7 : member 테이블에서 mem_id를 왼쪽에 '*' 문자로 채워서 총 10자리로 맞춰 출력하세요. (예 : 'TWC' -> '*******TWC')
SELECT LPAD(mem_id, 10, '*') AS `LPAD()` FROM member;

-- 문제 8 : member 테이블에서 전화번호 뒷자리(phone2)의 마지막 4자리만 남기고 앞부분을 '*'로 마스킹해서 출력하세요. (예 : '11111111' -> '****1111')
SELECT LPAD(SUBSTRING(phone2, 5, 4), 8, '*') AS `마스킹` FROM member;

-- 문제 9 : buy 테이블에서 상품 이름 앞 두 글자만 잘라서 출력하세요, (컬럼명: 상품약칭)
SELECT SUBSTRING(prod_name, 1, 2) FROM buy;

-- 문제 10 : member 테이블에서 이름과 지역(addr)을 CONCAT으로 '이름(지역)' 형태의 문자열로 합쳐서 출력하세요. (예: '트와이스(서울)')
SELECT CONCAT(mem_name, '(', addr, ')') AS `CONCAT()` FROM member;





-- 숫자함수
SELECT ROUND(3.141592, 2); -- 세 번째 자리를 반올림

SELECT CEIL(3.01); -- 소숫점 자리를 올림

SELECT FLOOR(3.01); -- 소숫점 자리를 내림

SELECT TRUNCATE(3.141592, 2);  -- 3.14

SELECT MOD(10, 3);

SELECT ABS(-3);

-- =========================================================

-- 날짜 / 시간 함수
SELECT NOW(); -- 현재 시간과 날짜
SELECT CURDATE();
SELECT YEAR('2025-06-01');
SELECT YEAR('2026/06/01');
SELECT YEAR('2024년05월01일');
SELECT YEAR('2024_05_01');

-- 날짜 차이 구하기
SELECT mem_name, DATEDIFF(NOW(), debut_date) AS `데뷔일 이후 경과날` FROM member;

-- 날짜 형식 출력하기
SELECT DATE_FORMAT(debut_date, '%Y년%m월%d일 (%W)') AS `데뷔일`FROM member;

SELECT DATE_FORMAT(CURDATE(), '%Y년%m월%d일 (%W)');

-- NULL 처리 함수 :IFNULL (NULL인지 아닌지 체크)
SELECT mem_name, IFNULL(phone1, '번호 없음') AS `연락처`
FROM member;

-- ================================================
-- 실습문제
-- ================================================

-- 문제1 : member 테이블에서 이름과 함께 전화번호가 없는 경우 '연락처 미등록'이라고 출력하세요.
SELECT mem_name, IFNULL(phone1, '연락처 미등록') AS `연락처` FROM member;

-- 문제2 : product 테이블에서 상품 가격에 부가세 10%를 더한 뒤 정수로 반올림하여 출력하세요.
SELECT prod_name, ROUND(price * 1.1) AS `가격` FROM buy;


-- 문제3 : 오늘 날짜를 '2026년 08월 27일' 형식으로 출력하세요.
SELECT DATE_FORMAT(CURDATE(), '%Y년%m월%d일');

-- 문제4: member 테이블에서 이름과 이름의 글자 수(공백 포함, 문자 개수 기준)를 함께 출력하세요.
SELECT mem_name, CHAR_LENGTH(mem_name) AS `글자 수` FROM member;

-- 문제5: member 테이블에서 이름을 모두 대문자(영문 가정 시)로 변환하고, 앞뒤 공백을 제거하여 출력하세요.
SELECT UPPER(TRIM(mem_name)) AS `이름` FROM member;

-- 문제6: member 테이블에서 전화번호 중 앞자리(phone1)의 하이픈을 제거한 값을 출력하세요.
SELECT REPLACE(phone1, '-', '') AS `phone1` FROM member;

-- 문제7: 회원번호(mem_no)를 항상 5자리로 만들고, 남는 자리는 앞에 '0'을 채워서 출력하세요. (예: 7 → '00007')
SELECT LPAD(mem_id, 5, '0') FROM member;

-- 문제8: buy 테이블에서 상품 가격을 100원 단위로 내림하여 출력하세요.
SELECT FLOOR(price / 100) * 100 FROM buy;

-- 문제9: product 테이블에서 재고 수량(stock)을 3으로 나눈 나머지를 출력하고, 나머지가 0인 상품(즉, 3으로 나누어 떨어지는 상품)만 조회하세요.
SELECT product_name, MOD(stock, 3) FROM product_info WHERE MOD(stock, 3) = 0;

-- 문제10: member 테이블에서 데뷔일(debut_date) 기준으로 몇 년째인지(만 나이 계산과 유사하게) 정수로 출력하세요. (힌트: DATEDIFF와 YEAR를 조합하거나, TIMESTAMPDIFF를 사용해도 됩니다)
SELECT CONCAT(TIMESTAMPDIFF(YEAR, debut_date, CURDATE()), '년') AS `데뷔년수` FROM member;

-- 문제11: member 테이블에서 데뷔일로부터 100일 후가 되는 날짜를 '2026-08-27' 형식으로 출력하세요.
SELECT DATE_ADD(debut_date, INTERVAL 100 DAY) FROM member;

-- 문제12: member 테이블에서 전화번호(phone1, phone2)가 둘 다 NULL인 경우 '번호없음', phone1만 있는 경우 phone1만, 둘 다 있는 경우 합쳐서 출력하세요. (힌트: CONCAT, IFNULL)
SELECT IFNULL(CONCAT(phone1, IFNULL(phone2, '')), '번호없음') FROM member;

-- 문제13: product 테이블에서 상품명과 가격을 "상품명 : 10,000원" 형식의 문자열 한 컬럼으로 합쳐서 출력하세요. (가격은 반올림 없이 정수 부분만 사용, 힌트: CONCAT과 TRUNCATE 또는 FORMAT 활용 가능)
SELECT CONCAT(product_name, ' : ', FORMAT(TRUNCATE(price, 0), 0), '원') FROM product_info;
