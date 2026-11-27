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

-- JWT 인증을 도입하게 되어 맴버 테이블에 회원권한 추가
ALTER TABLE member
ADD COLUMN authority VARCHAR(20) NOT NULL DEFAULT 'ROLE_USER';

-- JWT Refresh Token 저장 및 관리를 위한 테이블 생성
-- refresh_token_id (PK)
-- member_id (FK)
-- token
-- expires_at
CREATE TABLE refresh_token (
    refresh_token_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    member_id BIGINT NOT NULL UNIQUE,
    token VARCHAR(512) NOT NULL,
    expires_at DATETIME(6) NOT NULL,

    CONSTRAINT fk_refresh_token_member
    FOREIGN KEY (member_id)
    REFERENCES member(member_id)
);

