CREATE DATABASE shop_db;

USE shop_db;

CREATE TABLE member (
	member_id CHAR(8) not null primary key,
	member_name CHAR(5) not null,
	member_addr CHAR(20)
);

CREATE TABLE product (
	product_name CHAR(4) NOT NULL PRIMARY KEY,
	cost INT NOT NULL,
	make_date DATE,
	company CHAR(5),
	amount INT NOT NULL	
);
