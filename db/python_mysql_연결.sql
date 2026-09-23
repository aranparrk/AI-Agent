DROP DATABASE IF EXISTS mysqlDB;

CREATE DATABASE mysqlDB;

USE mysqlDB;

SELECT * FROM userTable;

-- 이미 존
CREATE TABLE userTable (
    id CHAR(10) PRIMARY KEY,
    pwd CHAR(15),
    name CHAR(20),
    email CHAR(20),
    addr CHAR(50)
)

-- 게시글 테이블
CREATE TABLE boardTable (
	board_no BIGINT PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(100) NOT NULL,
	contents TEXT NOT NULL,
	board_writer CHAR(10) NOT NULL,
	reg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (board_writer) REFERENCES userTable(id)
)

-- 댓글 테이블
CREATE TABLE commentTable (
	comment_no BIGINT PRIMARY KEY AUTO_INCREMENT,
	board_no BIGINT NOT NULL,
	comment_writer CHAR(10) NOT NULL,
	comment VARCHAR(500) NOT NULL,
	reg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (board_no) REFERENCES boardTable(board_no) ON DELETE CASCADE,
	FOREIGN KEY (comment_writer) REFERENCES userTable(id)
)

SHOW TABLES;

DESC boardTable;

DESC commentTable;

SELECT * FROM userTable WHERE id = 'aabb111'

SELECT * FROM boardTable where board_writer = 'aabb111'


SELECT a.board_no, a.title, b.name, a.reg_date 
FROM boardTable a 
JOIN userTable b
	ON a.board_writer = b.id 
ORDER BY a.board_no DESC

SELECT * FROM commentTable

DELETE FROM userTable WHERE id = 'ayj987';

SELECT a.board_no, a.title, a.contents, b.comment, b.comment_writer, b.reg_date 
FROM boardTable a 
LEFT JOIN commentTable b
	ON a.board_no = b.board_no
WHERE a.board_no = %s

commit;

SELECT * FROM commentTable WHERE comment_writer = 'aabb111'