CREATE DATABASE emp_db;

USE emp_db;

-- 부서 테이블
CREATE TABLE dept (
	deptno 		INT 		PRIMARY KEY,			-- 부서번호
	dname 		VARCHAR(20) NOT NULL,				-- 부서이름
	loc 		VARCHAR(50)							-- 부서위치
);

-- 사원 테이블
CREATE TABLE emp (
	empno 		INT 		PRIMARY KEY,			-- 사원번호
	ename 		VARCHAR(20) NOT NULL,				-- 사원명 
	job 		VARCHAR(20) NOT NULL,				-- 직무
	mgr 		INT,								-- 상사번호
	hiredate 	DATE 		NOT NULL,				-- 입사일
	sal 		INT 		NOT NULL,				-- 급여
	comm 		INT,								-- 커미션
	deptno 		INT 		NOT NULL,				-- 부서번호
	FOREIGN KEY (deptno) REFERENCES dept(deptno)
);

-- 급여등급 테이블
CREATE TABLE salgrade (
	grade 		INT			PRIMARY KEY,			-- 급여등급
	losal 		INT			NOT NULL,				-- 최소급여
	hisal 		INT			NOT NULL				-- 최대급
);

-- 데이터 삽입
INSERT INTO dept 
VALUES 	(100, '개발팀', '수원'),
		(200, '재경팀', '잠실'),
		(300, '기획팀', '천안'),
		(400, '영업팀', '부산'),
		(500, '인사팀', '여수'),
		(600, '관리팀', '전주');

INSERT INTO emp
VALUES 	(999, '김민준', '백엔드개발자', 800, '2025-01-31', 1000, 10, 100),
		(998, '이서연', '프론트개발자', 800, '2025-01-31', 1000, 10, 100),
		(865, '박지훈', '인사담당자', NULL, '2019-08-24', 3000, 300, 500),
		(992, '최유진', '영업사원', 824, '2023-04-03', 1500, 110, 400),
		(824, '정현우', '영업팀장', NULL, '2010-09-16', 5000, 500, 500),
		(996, '한지민', '서비스기획자', 944, '2024-02-11', 1300, 20, 300),
		(887, '오세훈', '회계담당자', NULL, '2020-05-02', 2000, 200, 200),
		(855, '강도윤', '관리팀장', NULL, '2015-07-06', 4000, 200, 600);

INSERT INTO salgrade
VALUES 	(1, 0, 1000),
		(2, 1001, 2000),
		(3, 2001, 3000),
		(4, 3001, 4000),
		(5, 4001, 5000);

-- 다양한 조회 및 정렬 결과 확인을 위해 테스트 데이터 추가
INSERT INTO emp
VALUES 	(990, '문지호', '데이터엔지니어', 888, '2022-03-14', 2200, 100, 100),
		(989, '배수민', '인사사원', 865, '2021-11-01', 2500, 150, 500),
  	  	(988, '차은우', '기획사원', 996, '2023-07-18', 2800, 120, 300),
    	(987, '임서준', '영업사원', 824, '2024-05-09', 2300, 300, 400);

-- 문제 1. 급여가 2000을 초과하는 사원의 사원명, 급여, 부서이름 조회하세요.
SELECT e.ename, e.sal, d.dname 
FROM emp e
JOIN dept d
	ON e.deptno = d.deptno
WHERE e.sal > 2000;

ename|sal |dname|
-----+----+-----+
정현우 |5000|인사팀|
강도윤 |4000|관리팀|
박지훈 |3000|인사팀|
임서준 |2300|영업팀|
차은우 |2800|기획팀|
배수민 |2500|인사팀|
문지호 |2200|개발팀|

-- 문제 2. 급여가 1000이상 3000이하인 사원의 사원명, 급여, 급여등급을 조회하세요.
SELECT e.ename, e.sal, s.grade
FROM emp e
JOIN salgrade s
	ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.sal BETWEEN 1000 AND 3000;

ename|sal |grade|
-----+----+-----+
김민준 |1000|    1|
이서연 |1000|    1|
한지민 |1300|    2|
최유진 |1500|    2|
오세훈 |2000|    2|
문지호 |2200|    3|
배수민 |2500|    3|
차은우 |2800|    3|
임서준 |2300|    3|
박지훈 |3000|    3|

-- 문제 3. 입사일이 빠른 순으로 사원명, 입사일, 부서이름을 출력하세요.
SELECT e.ename, e.hiredate, d.dname
FROM emp e
JOIN dept d
	ON e.deptno = d.deptno 
ORDER BY e.hiredate;

ename|hiredate  |dname|
-----+----------+-----+
정현우 |2010-09-16|인사팀 |
강도윤 |2015-07-06|관리팀 |
박지훈 |2019-08-24|인사팀 |
오세훈 |2020-05-02|재경팀 |
배수민 |2021-11-01|인사팀 |
문지호 |2022-03-14|개발팀 |
최유진 |2023-04-03|영업팀 |
차은우 |2023-07-18|기획팀 |
한지민 |2024-02-11|기획팀 |
임서준 |2024-05-09|영업팀 |
이서연 |2025-01-31|개발팀 |
김민준 |2025-01-31|개발팀 |

-- 문제 4. 급여등급이 3이상인 사원만 사원명, 부서이름, 급여, 급여등급을 급여기준 내림차순 정렬하세요.
SELECT e.ename, d.dname, e.sal, s.grade
FROM emp e
JOIN salgrade s
	ON e.sal BETWEEN s.losal AND s.hisal
JOIN dept d
	ON e.deptno = d.deptno
WHERE s.grade >= 3
ORDER BY e.sal DESC;

ename|dname|sal |grade|
-----+-----+----+-----+
정현우 |인사팀|5000|    5|
강도윤 |관리팀|4000|    4|
박지훈 |인사팀|3000|    3|
차은우 |기획팀|2800|    3|
배수민 |인사팀|2500|    3|
임서준 |영업팀|2300|    3|
문지호 |개발팀|2200|    3|

-- 문제 5.각 부서 별로 평균 급여보다 높은 사원만 사원명, 부서이름, 급여, 평균급여를 부서이름 오름차순, 급여 내림차순으로 정렬하세요.
SELECT e.ename, d.dname, e.sal, a.avg_sal
FROM emp e
JOIN dept d
	ON e.deptno = d.deptno 
JOIN (
		SELECT deptno, avg(sal) AS `avg_sal`
		FROM emp
		GROUP BY deptno
	 ) a
	ON e.deptno = a.deptno
WHERE a.avg_sal < e.sal
ORDER BY d.dname, e.sal DESC;

ename|dname|sal |avg_sal  |
-----+-----+----+---------+
문지호 |개발팀|2200|1400.0000|
차은우 |기획팀|2800|2050.0000|
임서준 |영업팀|2300|1900.0000|
정현우 |인사팀|5000|3500.0000|