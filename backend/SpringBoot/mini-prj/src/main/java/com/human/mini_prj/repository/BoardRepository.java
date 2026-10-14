package com.human.mini_prj.repository;

import com.human.mini_prj.entity.Board;
import org.springframework.data.domain.*;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BoardRepository extends JpaRepository<Board, Long> {
    List<Board> findAllByOrderByRegDateDesc();

    // 제목 & 내용으로 검색
    Page<Board> findByTitleContainingOrContentContaining(String title, String content, Pageable pageable);

    // 제목으로 검색
    Page<Board> findByTitleContaining(String title, Pageable pageable);

    // 내용으로 검색
    Page<Board> findByContentContaining(String content, Pageable pageable);

    // 작성자로 검색
    Page<Board> findByMemberNameContaining(String memberName, Pageable pageable);

    // 내가 작성한 글 보기
    Page<Board> findByMemberEmail(String memberEmail, Pageable pageable);
}
