CREATE DATABASE shop_db;

USE shop_db;

create table member (
	member_id CHAR(8) not null primary key,
	member_name CHAR(5) not null,
	member_addr CHAR(20)
);