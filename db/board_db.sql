CREATE DATABASE board_db;

USE board_db;

-- ===============================
-- 논리적 데이터 모델링
-- ===============================

/* 회원 (member) 엔터티
 * 회원 아이디      PK
 * 이메일
 * 비밀번호
 * 이름
 * 닉네임
 * 가입일
 */

/* 게시글 (post) 엔터티
 * 게시글 아이디    PK
 * 회원 아이디      FK
 * 제목
 * 내용
 * 작성일자
 */

/* 댓글 (comment) 엔터티
 * 댓글 아이디      PK
 * 게시글 아이디    FK
 * 회원 아이디      FK
 * 작성시간
 * 내용
 */


-- ===============================
-- 물리적 데이터 모델링
-- ===============================

-- ===============================
-- DDL (Data Definition Language)
-- ===============================

-- [테이블 생성]==================================================

-- 회원 (member) 테이블
CREATE TABLE member (
    member_id      BIGINT AUTO_INCREMENT PRIMARY KEY,
    email          VARCHAR(100) NOT NULL UNIQUE,
    pwd            VARCHAR(255) NOT NULL,
    member_name    VARCHAR(50) NOT NULL,
    register_date  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 게시글 (post) 테이블
CREATE TABLE post (
    post_id        BIGINT AUTO_INCREMENT PRIMARY KEY,
    member_id      BIGINT NOT NULL,
    title          VARCHAR(50) NOT NULL,
    contents       TEXT NOT NULL,
    write_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member(member_id)
);

-- 댓글 (comment) 테이블
CREATE TABLE comment (
    comment_id     BIGINT AUTO_INCREMENT PRIMARY KEY,
    post_id        BIGINT NOT NULL,
    member_id      BIGINT NOT NULL,
    write_date     DATETIME DEFAULT CURRENT_TIMESTAMP,
    contents       TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (member_id) REFERENCES member(member_id)
);
-- ===============================================================

-- [테이블 수정]==================================================
ALTER TABLE member ADD nickname VARCHAR(50) NOT NULL UNIQUE;

ALTER TABLE post MODIFY title VARCHAR(100) NOT NULL;
-- ===============================================================

-- [테이블 삭제]==================================================
DROP TABLE comment;

DROP TABLE post;

DROP TABLE member;
-- ===============================================================




-- =================================
-- DML (Data Manipulation Language)
-- =================================

-- [데이터 삽입]==================================================

SELECT * FROM member;

SELECT * FROM post;

SELECT * FROM comment;

INSERT INTO member (email, pwd, member_name, nickname) 
VALUES ('ab123@naver.com', '1234', '민달팽', '노롤로'), 
('ab124@naver.com', 'password1', '김민지', '김까까'),
('conne@google.com', 'password2', '김민자', '김끼끼'),
('wkkenw@nate.com', 'password3', '박민종', '퉁퉁이'),
('wkejfw@naver.com', 'password4', '이덕자', '소화기'),
('aas@google.com', 'password5', '문하영', '김수아'),
('wwee@daum.net', 'password6', '조인', '아이유'),
('efwe56464@nate.com', 'password7', '라랄', '한가인'),
('fwe2313@naver.com', 'password8', '룰루', '김미경'),
('qewfq321@naver.com', 'password9', '키키', '김꼬꼬');

INSERT INTO post (member_id, title, contents) 
VALUES (1, '제목1', '반갑습니다'),
(1, '제목2', '고맙습니다'),
(2, '제목3', '배고파요'),
(5, '제목4', '룰루 랄라'),
(5, '제목5', '룰루 신나'),
(5, '제목6', '참치김밥'),
(6, '제목7', '참치김치찌개'),
(7, '제목8', '김밥'),
(7, '제목9', '배불러요'),
(8, '제목10', '안녕하세요');

INSERT INTO comment (post_id, member_id, contents) 
VALUES (2, 5, '반갑습니다'),
(2, 6, '즐거운 하루 보내세요'),
(2, 1, '기분 좋아요'),
(3, 2, '멋진 글이에요'),
(5, 2, '굿이에요'),
(5, 3, '재밌어요'),
(6, 5, '김밥 맛있겠다'),
(6, 9, '저도 먹을래요'),
(7, 10, '랄라라'),
(8, 2, '신난다');
-- ===============================================================


-- [데이터 수정]==================================================
UPDATE member
SET member_name = '김세련'
WHERE member_id = 3;

SELECT * FROM member;

member_id|email             |pwd      |member_name|register_date      |nickname|
---------+------------------+---------+-----------+-------------------+--------+
        1|ab123@naver.com   |1234     |민달팽     |2026-09-03 17:03:32|노롤로  |
        2|ab124@naver.com   |password1|김민지     |2026-09-03 17:03:32|김까까  |
        3|conne@google.com  |password2|김세련     |2026-09-03 17:03:32|김끼끼  |
        4|wkkenw@nate.com   |password3|박민종     |2026-09-03 17:03:32|퉁퉁이  |
        5|wkejfw@naver.com  |password4|이덕자     |2026-09-03 17:03:32|소화기  |
        6|aas@google.com    |password5|문하영     |2026-09-03 17:03:32|김수아  |
        7|wwee@daum.net     |password6|조인       |2026-09-03 17:03:32|아이유  |
        8|efwe56464@nate.com|password7|라랄       |2026-09-03 17:03:32|한가인  |
        9|fwe2313@naver.com |password8|룰루       |2026-09-03 17:03:32|김미경  |
       10|qewfq321@naver.com|password9|키키       |2026-09-03 17:03:32|김꼬꼬  |
-- ===============================================================


-- [데이터 삭제]==================================================
DELETE FROM comment
WHERE comment_id = 3;

SELECT * FROM comment;

comment_id|post_id|member_id|write_date         |contents   |
----------+-------+---------+-------------------+-----------+
         1|      2|        5|2026-09-03 17:03:34|반갑습니다      |
         2|      2|        6|2026-09-03 17:03:34|즐거운 하루 보내세요|
         4|      3|        2|2026-09-03 17:03:34|멋진 글이에요    |
         5|      5|        2|2026-09-03 17:03:34|굿이에요       |
         6|      5|        3|2026-09-03 17:03:34|재밌어요       |
         7|      6|        5|2026-09-03 17:03:34|김밥 맛있겠다    |
         8|      6|        9|2026-09-03 17:03:34|저도 먹을래요    |
         9|      7|       10|2026-09-03 17:03:34|랄라라        |
        10|      8|        2|2026-09-03 17:03:34|신난다        |
-- ===============================================================

-- =================================
-- DQL (Data Query Language)
-- =================================

-- [SELECT와 FROM절]===============================================

-- member 테이블 조회
SELECT * FROM member;

member_id|email             |pwd      |member_name|register_date      |nickname|
---------+------------------+---------+-----------+-------------------+--------+
        1|ab123@naver.com   |1234     |민달팽        |2026-09-03 16:06:58|노롤로     |
        2|ab124@naver.com   |password1|김민지        |2026-09-03 16:06:58|김까까     |
        3|conne@google.com  |password2|김세련        |2026-09-03 16:06:58|김끼끼     |
        4|wkkenw@nate.com   |password3|박민종        |2026-09-03 16:06:58|퉁퉁이     |
        5|wkejfw@naver.com  |password4|이덕자        |2026-09-03 16:06:58|소화기     |
        6|aas@google.com    |password5|문하영        |2026-09-03 16:06:58|김수아     |
        7|wwee@daum.net     |password6|조인         |2026-09-03 16:06:58|아이유     |
        8|efwe56464@nate.com|password7|라랄         |2026-09-03 16:06:58|한가인     |
        9|fwe2313@naver.com |password8|룰루         |2026-09-03 16:06:58|김미경     |
       10|qewfq321@naver.com|password9|키키         |2026-09-03 16:06:58|김꼬꼬     |

-- post 테이블 조회
SELECT * FROM post;

post_id|member_id|title|contents|write_date         |
-------+---------+-----+--------+-------------------+
      1|        1|제목1  |반갑습니다   |2026-09-03 17:03:33|
      2|        1|제목2  |고맙습니다   |2026-09-03 17:03:33|
      3|        2|제목3  |배고파요    |2026-09-03 17:03:33|
      4|        5|제목4  |룰루 랄라   |2026-09-03 17:03:33|
      5|        5|제목5  |룰루 신나   |2026-09-03 17:03:33|
      6|        5|제목6  |참치김밥    |2026-09-03 17:03:33|
      7|        6|제목7  |참치김치찌개  |2026-09-03 17:03:33|
      8|        7|제목8  |김밥      |2026-09-03 17:03:33|
      9|        7|제목9  |배불러요    |2026-09-03 17:03:33|
     10|        8|제목10 |안녕하세요   |2026-09-03 17:03:33|

-- comment 테이블 조회
SELECT * FROM comment;

comment_id|post_id|member_id|write_date         |contents   |
----------+-------+---------+-------------------+-----------+
         1|      2|        5|2026-09-03 17:03:34|반갑습니다      |
         2|      2|        6|2026-09-03 17:03:34|즐거운 하루 보내세요|
         4|      3|        2|2026-09-03 17:03:34|멋진 글이에요    |
         5|      5|        2|2026-09-03 17:03:34|굿이에요       |
         6|      5|        3|2026-09-03 17:03:34|재밌어요       |
         7|      6|        5|2026-09-03 17:03:34|김밥 맛있겠다    |
         8|      6|        9|2026-09-03 17:03:34|저도 먹을래요    |
         9|      7|       10|2026-09-03 17:03:34|랄라라        |
        10|      8|        2|2026-09-03 17:03:34|신난다        |
-- ===============================================================


-- [WHERE 절]=====================================================

-- 김씨 조회
SELECT * FROM member
WHERE member_name LIKE '김%';

member_id|email           |pwd      |member_name|register_date      |nickname|
---------+----------------+---------+-----------+-------------------+--------+
        2|ab124@naver.com |password1|김민지     |2026-09-03 16:06:58|김까까  |
        3|conne@google.com|password2|김세련     |2026-09-03 16:06:58|김끼끼  |
-- ===============================================================


-- [GROUP BY 절]=================================================

-- 멤버 별 게시글 수
SELECT member_id, COUNT(*) FROM post
GROUP BY member_id;

member_id|COUNT(*)|
---------+--------+
        1|       2|
        2|       1|
        5|       3|
        6|       1|
        7|       2|
        8|       1|
-- ===============================================================


-- [HAVING절]=====================================================

-- 게시글을 2개 이상 쓴 데이터 조회
SELECT member_id, COUNT(*) FROM post
GROUP BY member_id
HAVING COUNT(*) > 2; 

member_id|COUNT(*)|
---------+--------+
        5|       3|
-- ===============================================================


-- [ORDER BY 절]=================================================
        
SELECT member_id, COUNT(*) FROM post
GROUP BY member_id
ORDER BY COUNT(*) DESC;

member_id|COUNT(*)|
---------+--------+
        5|       3|
        1|       2|
        7|       2|
        2|       1|
        6|       1|
        8|       1|
-- ===============================================================
        

-- [LIMIT절]======================================================

SELECT * FROM comment
LIMIT 5;
        
comment_id|post_id|member_id|write_date         |contents   |
----------+-------+---------+-------------------+-----------+
         1|      2|        5|2026-09-03 17:03:34|반갑습니다      |
         2|      2|        6|2026-09-03 17:03:34|즐거운 하루 보내세요|
         4|      3|        2|2026-09-03 17:03:34|멋진 글이에요    |
         5|      5|        2|2026-09-03 17:03:34|굿이에요       |
         6|      5|        3|2026-09-03 17:03:34|재밌어요       |
        
-- ===============================================================


-- [집계 함수 (Aggregate Functions)]==============================
         
SELECT 
	COUNT(*) AS `total_comment`, 
	AVG(LENGTH(contents)) AS `avg_content_length`,
	MAX(write_date),  
	MIN(write_date)
FROM comment;

total_comment|avg_content_length|MAX(write_date)    |MIN(write_date)    |
-------------+------------------+-------------------+-------------------+
            9|           15.8889|2026-09-03 17:03:34|2026-09-03 17:03:34|

-- ===============================================================

            
-- [JOIN절 (조인)]================================================
            
-- INNER JOIN

SELECT p.title, m.member_name 
FROM member m
INNER JOIN post p
	ON m.member_id = p.member_id;

title|member_name|
-----+-----------+
제목1  |민달팽   |
제목2  |민달팽   |
제목3  |김민지   |
제목4  |이덕자   |
제목5  |이덕자   |
제목6  |이덕자   |
제목7  |문하영   |
제목8  |조인     |
제목9  |조인     |
제목10 |라랄     |


-- LEFT JOIN
SELECT p.title, m.member_name 
FROM member m
LEFT JOIN post p
	ON m.member_id = p.member_id;

title |member_name|
------+-----------+
제목1 |민달팽     |
제목2 |민달팽     |
제목3 |김민지     |
      |김세련     |
      |박민종     |
제목4 |이덕자     |
제목5 |이덕자     |
제목6 |이덕자     |
제목7 |문하영     |
제목8 |조인       |
제목9 |조인       |
제목10|라랄       |
      |룰루       |
      |키키       |
            

-- [서브쿼리]=====================================================

SELECT * FROM post
WHERE member_id IN (SELECT member_id FROM member WHERE member_name LIKE '김%')

post_id|member_id|title|contents|write_date         |
-------+---------+-----+--------+-------------------+
      3|        2|제목3|배고파요|2026-09-03 17:03:33|
      
-- ===============================================================
      
-- [회원별 활동 분석]=============================================
      
SELECT m.member_name, 
       COUNT(DISTINCT b.post_id) AS post_count,
       COUNT(DISTINCT c.comment_id) AS comment_count
FROM member m
LEFT JOIN post b ON m.member_id = b.member_id
LEFT JOIN comment c ON m.member_id = c.member_id
GROUP BY m.member_id
ORDER BY post_count DESC, comment_count DESC;

member_name|post_count|comment_count|
-----------+----------+-------------+
이덕자     |         3|            2|
민달팽     |         2|            0|
조인       |         2|            0|
김민지     |         1|            3|
문하영     |         1|            1|
라랄       |         1|            0|
김세련     |         0|            1|
룰루       |         0|            1|
키키       |         0|            1|
박민종     |         0|            0|
      
-- ===============================================================


-- [인기 게시글 찾기]=============================================

SELECT p.title, COUNT(c.comment_id) AS comment_count
FROM post p
LEFT JOIN comment c ON p.post_id = c.post_id
GROUP BY p.post_id
ORDER BY comment_count DESC
LIMIT 1;

title|comment_count|
-----+-------------+
제목2|            2|
-- ===============================================================

-- [특정 키워드 검색]=============================================
SELECT p.title, c.contents
FROM post p
INNER JOIN comment c ON p.post_id = c.post_id
WHERE p.contents LIKE '%김밥%' OR c.contents LIKE '%김밥%';

title|contents      |
-----+--------------+
제목6|김밥 맛있겠다 |
제목6|저도 먹을래요 |
제목8|신난다        |
-- ===============================================================

