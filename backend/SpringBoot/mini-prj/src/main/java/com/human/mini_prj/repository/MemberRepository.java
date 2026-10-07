package com.human.mini_prj.repository;

import com.human.mini_prj.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {
    // 기본적인 CRUD는 상속을 통해서 만들어졌고, 이를 구현하는 구현체는 별도의 하이버네이트가 SQL문으로 변경 해줌
    Optional<Member> findByEmail(String email); // SQL : SELECT * FROM member WHERE email = ?
    boolean existsByEmail(String email); // SQL : SELECT COUNT(*) FROM member WHERE email = ?
    Optional<Member> findByEmailAndPwd(String email, String password); // SQL : SELECT * FROM MEMBER WHERE EMAIL = ? AND PWD = ?
}
