-- 뷰(View) : 뷰는 하나 이상의 테이블을 조합한 가상의 테이블입니다.
-- 복잡한 JOIN / 서브쿼리를 반복 작성하지 않아도 됨
-- 특정 열만 노출시켜 보안을 강화할 수 있음 (예 : 비밀번호 열 제)
-- 주 쓰는 쿼리를 하나의 이름으로 재사용

CREATE VIEW view_member_buy AS
SELECT b.mem_id, m.mem_name, b.prod_name, b.price, b.amount
FROM buy b
INNER JOIN member m
	ON b.mem_id = m.mem_id;

SELECT * FROM view_member_buy;

-- ============================================
-- 실습문제
-- ============================================

-- 문제 1 :buy 테이블과 member 테이블을 조인해서, 회원 이름과 구매한 상품명, 금액을 보여주는 뷰 veiw_buy_detail을 만드세요.

CREATE VIEW view_buy_detail AS
SELECT m.mem_name, b.prod_name, b.price
FROM member m
JOIN buy b
	ON m.mem_id = b.mem_id;

SELECT * FROM view_buy_detail;

-- 문제 2: member 테이블의 addr 열에 인덱스를 생성하고, EXPLAIN으로 지역 조회 시 인덱스가 사용되는지 확인하세요.

CREATE INDEX idx_mem_addr ON member(addr);
EXPLAIN SELECT * FROM member WHERE addr = '서울';