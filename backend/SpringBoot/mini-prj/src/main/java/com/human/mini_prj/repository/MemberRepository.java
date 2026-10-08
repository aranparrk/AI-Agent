package com.human.mini_prj.repository;

import com.human.mini_prj.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {
    // 기본적인 CRUD는 상속을 통해서 만들어졌고, 이를 구현하는 구현체는 별도의 하이버네이트가 SQL문으로 변경 해줌
    Optional<Member> findByEmail(String email); // SQL : SELECT * FROM member WHERE email = ?
    boolean existsByEmail(String email); // SQL : SELECT COUNT(*) FROM member WHERE email = ?
    Optional<Member> findByEmailAndPwd(String email, String password); // SQL : SELECT * FROM MEMBER WHERE EMAIL = ? AND PWD = ?

    // 1. 이름이 정확히 일치하는 회원 목록 조회
    List<Member> findByName(String name);

    // 2. 이름에 특정 글자가 포함된 회원 조회
    List<Member> findByNameContaining(String name);

    // 3. 특정 도메인(예: @gmail.com)으로 끝나는 이메일을 가진 회원 조회
    List<Member> findByEmailEndingWith(String email);

    // 4. 이름 또는 이메일이 일치하는 회원 조회
    List<Member> findByNameOrEmail(String name, String email);

    // 5. 특정 일시 이후에 가입한 회원 조회
    List<Member> findByRegDateAfter(LocalDateTime regDate);

    // 6. 두 일시 사이에 가입한 회원 조회
    List<Member> findByRegDateBetween(LocalDateTime startDate, LocalDateTime endDate);

    // 7. 전체 회원을 가입일 최신순으로 조회
    List<Member> findAllByOrderByRegDateDesc();

    // 8. 가장 최근에 가입한 회원 3명만 조회
    List<Member> findTop3ByOrderByRegDateDesc();

    // 9. 대소문자 구분 없이 이름에 키워드가 포함된 회원을 이름 오름차순으로 조회
    List<Member> findByNameContainingIgnoreCaseOrderByNameAsc(String name);

    // 10. 이메일로 회원 삭제
    long deleteByEmail(String email);
}
